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
  // Diagramas largos: o tema reduz o SVG à largura da coluna, e rótulos de diagramas largos ficam
  // ilegíveis no celular. A largura natural é medida sem acessar o SVG (shadow DOM fechado): com a
  // altura na largura atual e numa largura de teste, obtém-se a proporção e a largura natural. Se os
  // rótulos (LABEL_PX no tamanho natural) ficariam abaixo de TRIGGER_PX, o diagrama ganha largura
  // mínima para rótulos de MIN_LABEL_PX numa região com rolagem horizontal, rotulada e alcançável pelo
  // teclado. Diagramas que cabem, ou quase, não mudam.
  var LABEL_PX = 14, TRIGGER_PX = 9, MIN_LABEL_PX = 11, PROBE_PX = 4000;
  function fitDiagram(host) {
    var figure = host.closest("figure.saa-diagram");
    if (!figure || host.tagName !== "DIV") return true;  // <pre class="mermaid">: ainda não renderizado
    var wrap = host.parentElement.classList.contains("saa-diagram__scroll") ? host.parentElement : null;
    var position = wrap ? wrap.scrollLeft : 0;
    host.style.minWidth = "";
    var box = host.getBoundingClientRect();
    if (box.height < 20 || box.width < 1) return false;
    host.style.width = PROBE_PX + "px";
    var probe = host.getBoundingClientRect().height;
    host.style.width = "";
    var natural = probe > box.height + 1 ? Math.min(PROBE_PX, box.width * probe / box.height) : box.width;
    var needed = Math.ceil(natural * MIN_LABEL_PX / LABEL_PX);
    if (box.width * LABEL_PX / natural < TRIGGER_PX) {
      if (!wrap) {
        wrap = document.createElement("div");
        wrap.className = "saa-diagram__scroll";
        host.parentNode.insertBefore(wrap, host);
        wrap.appendChild(host);
      }
      var caption = figure.querySelector("figcaption");
      wrap.setAttribute("tabindex", "0");
      wrap.setAttribute("role", "region");
      wrap.setAttribute("aria-label", "Diagrama com rolagem horizontal" +
        (caption ? ": " + caption.textContent.replace(/\s+/g, " ").trim().slice(0, 160) : ""));
      host.style.minWidth = needed + "px";
      wrap.scrollLeft = position;  // remedir não devolve o leitor ao início
      figure.classList.add("saa-diagram--scroll");
    } else if (wrap) {
      ["tabindex", "role", "aria-label"].forEach(function (a) { wrap.removeAttribute(a); });
      figure.classList.remove("saa-diagram--scroll");
    }
    return true;
  }
  function fitDiagrams(force) {
    document.querySelectorAll("figure.saa-diagram .mermaid").forEach(function (host) {
      if (!force && host.getAttribute("data-saa-fitted")) return;
      if (fitDiagram(host) && host.tagName === "DIV") host.setAttribute("data-saa-fitted", "1");
    });
  }
  // O Mermaid é carregado (CDN) e desenhado de forma assíncrona, às vezes depois de vários segundos em
  // rede lenta: cada figura é observada até o diagrama ser desenhado (o <pre> vira <div>).
  var observer = typeof MutationObserver !== "undefined" ? new MutationObserver(function () {
    if (!document.querySelector("figure.saa-diagram .mermaid:not([data-saa-fitted])")) {
      observer.disconnect();
      return;
    }
    requestAnimationFrame(function () { fitDiagrams(false); });
  }) : null;
  function watchDiagrams() {
    if (observer) {
      observer.disconnect();
      document.querySelectorAll("figure.saa-diagram").forEach(function (figure) {
        observer.observe(figure, { childList: true, subtree: true });
      });
    }
    [300, 1000, 2500, 5000].forEach(function (delay) { setTimeout(function () { fitDiagrams(false); }, delay); });
  }
  // Só mudanças de largura: no celular, a altura muda quando a barra do navegador recolhe ou o teclado abre.
  var resizeTimer = null, lastWidth = window.innerWidth;
  window.addEventListener("resize", function () {
    if (window.innerWidth === lastWidth) return;
    lastWidth = window.innerWidth;
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () { fitDiagrams(true); }, 200);
  });

  if (typeof window.document$ !== "undefined" && window.document$.subscribe) {
    // navegação instantânea do tema; segunda passagem para elementos montados depois (anotações)
    window.document$.subscribe(function () { enhance(); setTimeout(enhance, 400); watchDiagrams(); });
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { enhance(); watchDiagrams(); });
  } else {
    enhance();
    watchDiagrams();
  }
})();
