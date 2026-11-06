"""Os pré-requisitos das aulas escritas estão contidos nos pré-requisitos do módulo.

Para módulos fora de Fundamentals (R1 e R2), todo módulo citado nos pré-requisitos
de uma aula deve estar no fecho transitivo dos pré-requisitos do módulo, ou fazer
parte de Fundamentals, que o Professional pressupõe concluído.
"""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = yaml.safe_load((ROOT / "curriculum/manifest.yml").read_text(encoding="utf-8"))


def _fundamentals() -> set[str]:
    mods: set[str] = set()
    for rel in MANIFEST["releases"]:
        if str(rel["id"]) in {"R1", "R2"}:
            mods.update(str(m) for m in rel.get("modules") or [])
    return mods


def _closure(prereqs: dict[str, set[str]], module: str) -> set[str]:
    seen: set[str] = set()
    stack = list(prereqs.get(module, ()))
    while stack:
        item = stack.pop()
        if item not in seen:
            seen.add(item)
            stack.extend(prereqs.get(item, ()))
    return seen


def test_lesson_prerequisites_within_module_prerequisites():
    fundamentals = _fundamentals()
    prereqs = {str(m["id"]): {str(p) for p in m.get("prerequisites") or []} for m in MANIFEST["modules"]}
    problems = []
    for module in MANIFEST["modules"]:
        mid = str(module["id"])
        if mid in fundamentals or not module.get("path"):
            continue
        folder = (ROOT / "docs" / module["path"]).parent
        allowed = _closure(prereqs, mid) | fundamentals | {mid}
        for lesson in module.get("lessons") or []:
            if not lesson.get("file"):
                continue
            text = (folder / lesson["file"]).read_text(encoding="utf-8")
            front = yaml.safe_load(text.split("---")[1])
            for pre in front.get("prerequisites") or []:
                pm = str(pre).split("-")[0]
                if pm not in allowed:
                    problems.append(f"{lesson['id']} → {pre} (módulo {pm} fora dos pré-requisitos de {mid})")
    assert not problems, "Pré-requisitos de aula fora do módulo:\n" + "\n".join(problems)
