"""Nomenclatura pública de módulos e aulas — fonte única das regras de apresentação.

Os identificadores técnicos (``M00``, ``M00-L01``…) continuam sendo a chave de dados,
dependências, testes, URLs e Research Library. Para o estudante, o portal mostra:

* módulo ``M00`` → "Módulo Inicial"; ``Mnn`` (nn ≥ 1) → "Módulo nn" sem zero à esquerda;
* aula → "Aula NN", com dois dígitos, numerada pela **ordem do manifesto** dentro do
  módulo (começa em 01 e reinicia a cada módulo — não é derivada do sufixo ``Lnn``);
* título completo de uma aula → "Módulo Inicial — Aula 01 — <título técnico>".

Complementos (``C01``…) mantêm a própria identidade e não recebem nome de módulo.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

MODULE_ID_RE = re.compile(r"^M(\d{2})$")
LESSON_ID_RE = re.compile(r"^(M\d{2})-L\d{2}$")
SEP = " — "


class NamingError(ValueError):
    """Entrada malformada, referência inexistente ou conflito de numeração."""


def module_name(module_id: str) -> str:
    """Nome público de um módulo: ``M00`` → "Módulo Inicial", ``M07`` → "Módulo 7"."""
    match = MODULE_ID_RE.match(str(module_id))
    if not match:
        raise NamingError(f"identificador de módulo inválido: {module_id!r} (esperado Mnn; complementos não são módulos)")
    number = int(match.group(1))
    return "Módulo Inicial" if number == 0 else f"Módulo {number}"


def lesson_label(number: int) -> str:
    """Rótulo da aula dentro do módulo: 1 → "Aula 01"."""
    if not isinstance(number, int) or isinstance(number, bool) or number < 1 or number > 99:
        raise NamingError(f"número de aula inválido: {number!r} (1 a 99)")
    return f"Aula {number:02d}"


@dataclass(frozen=True)
class Lesson:
    id: str
    module: str
    number: int
    title: str

    @property
    def label(self) -> str:
        """ "Aula 01" """
        return lesson_label(self.number)

    @property
    def module_name(self) -> str:
        """ "Módulo Inicial" """
        return module_name(self.module)

    @property
    def reference(self) -> str:
        """ "Módulo Inicial — Aula 01" — para citar a aula fora do contexto do módulo."""
        return f"{self.module_name}{SEP}{self.label}"

    @property
    def short_title(self) -> str:
        """ "Aula 01 — Computação…" — título da página e do menu, onde o módulo já é o contexto."""
        return f"{self.label}{SEP}{self.title}"

    @property
    def full_title(self) -> str:
        """ "Módulo Inicial — Aula 01 — Computação…" — busca, compartilhamento e títulos de janela."""
        return f"{self.reference}{SEP}{self.title}"


class Naming:
    """Numeração pública derivada de ``curriculum/manifest.yml``."""

    def __init__(self, manifest: dict[str, Any]):
        self.modules: dict[str, dict[str, Any]] = {}
        self.lessons: dict[str, Lesson] = {}
        for unit in manifest.get("modules") or []:
            mid = unit.get("id")
            module_name(mid)  # valida o formato
            if mid in self.modules:
                raise NamingError(f"módulo duplicado no manifesto: {mid}")
            self.modules[mid] = unit
            seen_titles: set[str] = set()
            for index, lesson in enumerate(unit.get("lessons") or [], start=1):
                lid = lesson.get("id")
                match = LESSON_ID_RE.match(str(lid))
                if not match:
                    raise NamingError(f"{mid}: identificador de aula inválido: {lid!r}")
                if match.group(1) != mid:
                    raise NamingError(f"{lid}: aula listada no módulo {mid}, mas o identificador pertence a {match.group(1)}")
                if lid in self.lessons:
                    raise NamingError(f"aula duplicada no manifesto: {lid}")
                title = str(lesson.get("title") or "").strip()
                if not title:
                    raise NamingError(f"{lid}: aula sem título")
                if title in seen_titles:
                    raise NamingError(f"{mid}: título de aula repetido no módulo: {title!r}")
                seen_titles.add(title)
                self.lessons[lid] = Lesson(lid, mid, index, title)

    # -- módulos -------------------------------------------------------------
    def module(self, module_id: str) -> dict[str, Any]:
        if module_id not in self.modules:
            raise NamingError(f"módulo inexistente no manifesto: {module_id!r}")
        return self.modules[module_id]

    def module_name(self, module_id: str) -> str:
        self.module(module_id)
        return module_name(module_id)

    def module_title(self, module_id: str) -> str:
        """ "Módulo Inicial — Fundamentos de Infraestrutura e Computação" """
        return f"{self.module_name(module_id)}{SEP}{self.module(module_id)['title']}"

    # -- aulas ---------------------------------------------------------------
    def lesson(self, lesson_id: str) -> Lesson:
        if lesson_id not in self.lessons:
            raise NamingError(f"aula inexistente no manifesto: {lesson_id!r}")
        return self.lessons[lesson_id]

    def module_lessons(self, module_id: str) -> list[Lesson]:
        self.module(module_id)
        return [lesson for lesson in self.lessons.values() if lesson.module == module_id]

    def by_reference(self, module_id: str, number: int) -> Lesson:
        """Aula a partir da identificação pública (módulo e número da aula)."""
        for lesson in self.module_lessons(module_id):
            if lesson.number == number:
                return lesson
        raise NamingError(f"{self.module_name(module_id)} não tem {lesson_label(number)}")

    def lesson_range(self, first_id: str, last_id: str) -> str:
        """ "Módulo 2 — Aulas 01 a 04" para um intervalo de aulas do mesmo módulo."""
        first, last = self.lesson(first_id), self.lesson(last_id)
        if first.module != last.module or first.number >= last.number:
            raise NamingError(f"intervalo de aulas inválido: {first_id} a {last_id}")
        return f"{first.module_name}{SEP}Aulas {first.number:02d} a {last.number:02d}"


def module_id_for_name(name: str) -> str:
    """Inverso de :func:`module_name` — usado pelas verificações de consistência."""
    if name == "Módulo Inicial":
        return "M00"
    match = re.fullmatch(r"Módulo (\d{1,2})", name)
    if not match or int(match.group(1)) == 0:
        raise NamingError(f"nome público de módulo inválido: {name!r}")
    return f"M{int(match.group(1)):02d}"


def modules_phrase(module_ids: list[str]) -> str:
    """Lista de módulos em linguagem natural.

    ``[M00, M01, M02]`` → "Módulo Inicial, Módulo 1 e Módulo 2";
    ``[M03 … M15]`` (contíguos) → "Módulos 3 a 15"; ``[M16, M17]`` → "Módulos 16 e 17".
    """
    if not module_ids:
        raise NamingError("lista de módulos vazia")
    numbers = []
    for mid in module_ids:
        module_name(mid)
        numbers.append(int(mid[1:]))
    if len(set(numbers)) != len(numbers):
        raise NamingError(f"módulo repetido na lista: {module_ids}")
    if len(numbers) == 1:
        return module_name(module_ids[0])
    if 0 not in numbers:
        contiguous = numbers == list(range(numbers[0], numbers[0] + len(numbers)))
        if contiguous and len(numbers) > 2:
            return f"Módulos {numbers[0]} a {numbers[-1]}"
        return "Módulos " + ", ".join(str(n) for n in numbers[:-1]) + f" e {numbers[-1]}"
    names = [module_name(mid) for mid in module_ids]
    return ", ".join(names[:-1]) + f" e {names[-1]}"
