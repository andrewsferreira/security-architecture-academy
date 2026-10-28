"""Nomenclatura pública de módulos e aulas (scripts/naming.py e páginas geradas)."""

from __future__ import annotations

import copy
import json
import re
from pathlib import Path

import pytest

import render_curriculum as rc
from _common import DOCS, ROOT, load_manifest, read_front_matter
from naming import Naming, NamingError, lesson_label, module_id_for_name, module_name, modules_phrase

MANIFEST = load_manifest()
NAMING = Naming(MANIFEST)

# URLs publicadas na v0.1.0 (contrato: não podem mudar).
R1_LESSON_PATHS = [
    "modules/00-foundations/01-computing-os-virtualization.md",
    "modules/00-foundations/02-tcp-ip-networking.md",
    "modules/00-foundations/03-segmentation-connectivity.md",
    "modules/00-foundations/04-datacenter-high-availability.md",
    "modules/00-foundations/05-containers-apis-serverless.md",
    "modules/00-foundations/06-cloud-computing-models.md",
    "modules/00-foundations/07-reading-architecture-diagrams.md",
    "modules/01-security-fundamentals/01-security-properties.md",
    "modules/01-security-fundamentals/02-secure-design-principles.md",
    "modules/01-security-fundamentals/03-trust-boundaries-attack-surface.md",
    "modules/01-security-fundamentals/04-applied-cryptography.md",
    "modules/01-security-fundamentals/05-pki-tls-key-management.md",
    "modules/01-security-fundamentals/06-threat-vulnerability-risk.md",
    "modules/01-security-fundamentals/07-formal-security-models.md",
    "modules/02-security-architecture/01-security-architect-role.md",
    "modules/02-security-architecture/02-enterprise-solution-security-architecture.md",
    "modules/02-security-architecture/03-conceptual-logical-physical.md",
    "modules/02-security-architecture/04-principles-standards-baselines-exceptions.md",
    "modules/02-security-architecture/05-reference-architectures-blueprints.md",
    "modules/02-security-architecture/06-frameworks.md",
    "modules/02-security-architecture/07-business-driven-requirements.md",
    "modules/02-security-architecture/08-architecture-decision-records.md",
]


# --------------------------------------------------------------- regras básicas
@pytest.mark.parametrize("mid, name", [("M00", "Módulo Inicial"), ("M01", "Módulo 1"), ("M02", "Módulo 2"),
                                       ("M10", "Módulo 10"), ("M17", "Módulo 17")])
def test_module_names(mid, name):
    assert module_name(mid) == name
    assert module_id_for_name(name) == mid


@pytest.mark.parametrize("lid, reference", [
    ("M00-L01", "Módulo Inicial — Aula 01"), ("M00-L07", "Módulo Inicial — Aula 07"),
    ("M01-L01", "Módulo 1 — Aula 01"), ("M01-L07", "Módulo 1 — Aula 07"),
    ("M02-L01", "Módulo 2 — Aula 01"), ("M02-L08", "Módulo 2 — Aula 08"),
])
def test_lesson_references(lid, reference):
    assert NAMING.lesson(lid).reference == reference


def test_full_and_short_titles():
    lesson = NAMING.lesson("M00-L01")
    assert lesson.short_title == "Aula 01 — Computação, sistemas operacionais e virtualização"
    assert lesson.full_title == "Módulo Inicial — Aula 01 — Computação, sistemas operacionais e virtualização"
    assert NAMING.module_title("M01") == "Módulo 1 — Fundamentos de Segurança"


def test_numbering_restarts_and_follows_manifest_order():
    for mod in MANIFEST["modules"]:
        numbers = [NAMING.lesson(x["id"]).number for x in mod["lessons"]]
        assert numbers == list(range(1, len(mod["lessons"]) + 1)), mod["id"]
        labels = [NAMING.lesson(x["id"]).label for x in mod["lessons"]]
        assert len(set(labels)) == len(labels)
        assert all(re.fullmatch(r"Aula \d{2}", label) for label in labels)
        assert "Aula 00" not in labels


def test_technical_ids_unchanged():
    ids = [x["id"] for mod in MANIFEST["modules"] for x in mod["lessons"]]
    assert all(re.fullmatch(r"M\d{2}-L\d{2}", i) for i in ids)
    assert [m["id"] for m in MANIFEST["modules"]] == [f"M{n:02d}" for n in range(18)]
    for mod in MANIFEST["modules"]:
        for lesson in mod["lessons"]:
            if lesson.get("file") and lesson["status"] != "planned":
                meta, _ = read_front_matter(DOCS / rc.unit_base(mod) / lesson["file"])
                assert meta["id"] == lesson["id"]
                assert meta["module"] == mod["id"]


def test_r1_urls_preserved():
    files = {f"{rc.unit_base(mod)}/{x['file']}" for mod in MANIFEST["modules"] for x in mod["lessons"] if x.get("file")}
    for path in R1_LESSON_PATHS:
        assert path in files and (DOCS / path).is_file(), path


def test_complement_is_not_a_module():
    with pytest.raises(NamingError):
        module_name("C01")
    assert "C01" not in NAMING.modules
    assert all(not lid.startswith("C") for lid in NAMING.lessons)


def test_modules_phrase():
    assert modules_phrase(["M00", "M01", "M02"]) == "Módulo Inicial, Módulo 1 e Módulo 2"
    assert modules_phrase([f"M{n:02d}" for n in range(3, 16)]) == "Módulos 3 a 15"
    assert modules_phrase(["M16", "M17"]) == "Módulos 16 e 17"


# ----------------------------------------------------------- entradas inválidas
@pytest.mark.parametrize("bad", ["M0", "M100", "m01", "L01", "C01", "", None, "M01-L01"])
def test_malformed_module_ids(bad):
    with pytest.raises(NamingError):
        module_name(bad)


@pytest.mark.parametrize("bad", [0, -1, 100, "1", True])
def test_malformed_lesson_numbers(bad):
    with pytest.raises(NamingError):
        lesson_label(bad)


def _manifest(lessons, mid="M02"):
    return {"modules": [{"id": mid, "title": "Teste", "lessons": lessons}]}


def test_conflicts_are_rejected():
    ok = {"id": "M02-L01", "title": "A"}
    with pytest.raises(NamingError, match="duplicada"):
        Naming(_manifest([ok, dict(ok, title="B")]))
    with pytest.raises(NamingError, match="pertence"):
        Naming(_manifest([{"id": "M03-L01", "title": "A"}]))
    with pytest.raises(NamingError, match="inválido"):
        Naming(_manifest([{"id": "M02-X1", "title": "A"}]))
    with pytest.raises(NamingError, match="repetido"):
        Naming(_manifest([ok, {"id": "M02-L02", "title": "A"}]))
    with pytest.raises(NamingError, match="sem título"):
        Naming(_manifest([{"id": "M02-L01", "title": ""}]))
    data = copy.deepcopy(MANIFEST)
    data["modules"].append(copy.deepcopy(data["modules"][0]))
    with pytest.raises(NamingError, match="duplicado"):
        Naming(data)


def test_missing_references_are_rejected():
    with pytest.raises(NamingError):
        NAMING.lesson("M02-L99")
    with pytest.raises(NamingError):
        NAMING.module_title("M18")
    with pytest.raises(NamingError):
        NAMING.by_reference("M02", 9)
    assert NAMING.by_reference("M02", 8).id == "M02-L08"
    with pytest.raises(NamingError):
        NAMING.lesson_range("M02-L04", "M02-L01")
    with pytest.raises(NamingError):
        module_id_for_name("Módulo 0")


# ------------------------------------------------------------ páginas geradas
def test_lesson_pages_use_public_names():
    for mod in MANIFEST["modules"]:
        for lesson in mod["lessons"]:
            if not (lesson.get("file") and lesson["status"] != "planned"):
                continue
            info = NAMING.lesson(lesson["id"])
            meta, body = read_front_matter(DOCS / rc.unit_base(mod) / lesson["file"])
            assert meta["title"] == info.short_title
            assert meta["public_title"] == info.full_title
            heading = re.search(r"^# (.+?)(?: \{ #([\w-]+) \})?$", body, re.M)
            assert heading.group(1) == info.short_title
            assert heading.group(2) == rc.slugify(info.title)  # âncora publicada na v0.1.0
            assert f'<span class="saa-level">{info.module_name} · ' in body
            assert f"ID técnico: {lesson['id']}</span>" in body


def test_module_indexes_and_navigation():
    config = (ROOT / "zensical.toml").read_text(encoding="utf-8")
    for mod in MANIFEST["modules"]:
        if not mod.get("path") or mod["status"] in ("planned", "draft"):
            continue
        meta, body = read_front_matter(DOCS / mod["path"])
        title = NAMING.module_title(mod["id"])
        assert meta["title"] == title and f"\n# {title} {{ #" in "\n" + body
        block = body.split("<!-- lessons:start -->", 1)[1].split("<!-- lessons:end -->", 1)[0]
        labels = re.findall(r"^\| \[?(Aula \d{2})", block, re.M)
        assert labels == [NAMING.lesson(x["id"]).label for x in mod["lessons"]]
        assert f'{{ "{title}" = [' in config


def test_last_lessons_point_to_next_steps():
    m00 = (DOCS / "modules/00-foundations/07-reading-architecture-diagrams.md").read_text(encoding="utf-8")
    assert "avaliação do Módulo Inicial".lower() in m00.lower() and "Módulo 1 — Fundamentos de Segurança" in m00
    m02 = (DOCS / "modules/02-security-architecture/08-architecture-decision-records.md").read_text(encoding="utf-8")
    assert "fundamentals-final.md" in m02 and "case-a-meridiana" in m02


def test_generators_are_idempotent():
    first = {str(p): c for p, c in rc.targets()}
    second = {str(p): c for p, c in rc.targets()}
    assert first == second
    for path, content in first.items():
        assert Path(path).read_text(encoding="utf-8") == content, f"{path} desatualizado — execute make curriculum"


# -------------------------------------------------- texto voltado ao estudante
PROTECT_RE = re.compile(r"(<!-- (?P<blk>[a-z-]+):start -->.*?<!-- (?P=blk):end -->)|(`[^`\n]+`)|(\]\([^)\s]*\))"
                        r"|(<[^>\n]+>)|(https?://\S+)", re.S)
ID_RE = re.compile(r"\bM\d{2}(?:-L\d{2})?\b(?!-)")


def student_pages():
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if not rel.startswith(("docs/internal/", "docs/resources/")):
            yield path
    for name in ("README.md", "GETTING-STARTED.md", "ROADMAP.md"):
        yield ROOT / name


def test_no_bare_technical_ids_in_student_text():
    """IDs técnicos aparecem só como metadado (código inline, front matter, ID técnico); o texto usa nomes públicos."""
    offenders = []
    for path in student_pages():
        text = path.read_text(encoding="utf-8")
        if text.startswith("---\n"):
            text = text[text.index("\n---", 4) + 4:]
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = PROTECT_RE.sub("", text)
        text = re.sub(r"ID técnico: M\d{2}(?:-L\d{2})?", "", text)
        found = ID_RE.findall(text)
        if found:
            offenders.append(f"{path.relative_to(ROOT)}: {sorted(set(found))[:5]}")
    assert not offenders, "\n".join(offenders)


def test_public_lesson_references_exist():
    """Toda menção "Módulo X — Aula NN" aponta para uma aula que existe no manifesto."""
    pattern = re.compile(r"(Módulo (?:Inicial|\d{1,2})) — Aulas? (\d{2})(?:(?:, | e | a )(\d{2}))*")
    for path in student_pages():
        for match in pattern.finditer(path.read_text(encoding="utf-8")):
            mid = module_id_for_name(match.group(1))
            for number in re.findall(r"\d{2}", match.group(0).split("—", 1)[1]):
                NAMING.by_reference(mid, int(number))


def test_built_site_titles_if_present():
    """Com o site compilado (zensical build), a busca e as abas mostram os nomes públicos."""
    search = ROOT / "site" / "search.json"
    if not search.is_file():
        pytest.skip("site não compilado")
    items = {i["location"]: i for i in json.loads(search.read_text(encoding="utf-8"))["items"]}
    for path in R1_LESSON_PATHS:
        url = path[:-3] + "/"
        assert url in items, url
        assert re.match(r"Aula \d{2} — ", items[url]["title"])
        html = (ROOT / "site" / url / "index.html").read_text(encoding="utf-8")
        assert re.search(r"<title>Módulo (Inicial|\d) — Aula \d{2} — ", html)
        lid = next(x["id"] for m in MANIFEST["modules"] for x in m["lessons"] if x.get("file") and path.endswith(x["file"]))
        assert f'<h1 id="{rc.slugify(NAMING.lesson(lid).title)}"' in html  # âncora da v0.1.0
