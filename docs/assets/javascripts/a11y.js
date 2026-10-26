// Ajustes de acessibilidade (WCAG 2.1 AA) sobre a marcação gerada pelo tema.
// Verificados com axe-core; ver docs/internal/design-system.md#acessibilidade.
(function () {
  function enhance() {
    // Checklists: cada caixa de seleção recebe como rótulo o texto do próprio item.
    document.querySelectorAll(".md-typeset .task-list-item input[type=checkbox]").forEach(function (box) {
      if (box.hasAttribute("aria-label")) return;
      var item = box.closest("li");
      var text = item ? item.textContent.replace(/\s+/g, " ").trim() : "";
      box.setAttribute("aria-label", text.slice(0, 200) || "Item da lista de verificação");
    });
    // Marcadores de anotação de código: o tema os cria sem texto acessível.
    document.querySelectorAll(".md-annotation__index").forEach(function (link) {
      if (link.hasAttribute("aria-label")) return;
      var marker = link.querySelector("[data-md-annotation-id]");
      var id = marker ? marker.getAttribute("data-md-annotation-id") : "";
      link.setAttribute("aria-label", "Anotação " + id);
    });
    // Tabelas largas: a região com rolagem horizontal precisa ser alcançável pelo teclado.
    document.querySelectorAll(".md-typeset__scrollwrap").forEach(function (wrap) {
      if (wrap.hasAttribute("tabindex") || wrap.scrollWidth <= wrap.clientWidth) return;
      wrap.setAttribute("tabindex", "0");
      wrap.setAttribute("role", "region");
      wrap.setAttribute("aria-label", "Tabela com rolagem horizontal");
    });
  }
  if (typeof window.document$ !== "undefined" && window.document$.subscribe) {
    // navegação instantânea do tema; segunda passagem para elementos montados depois (anotações)
    window.document$.subscribe(function () { enhance(); setTimeout(enhance, 400); });
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enhance);
  } else {
    enhance();
  }
})();
