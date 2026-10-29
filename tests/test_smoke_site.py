"""Smoke tests do site publicado: expectativas derivadas da árvore e regras de retentativa (sem rede)."""

from __future__ import annotations

import smoke_test_site as st
from _common import ROOT

BASE = "https://example.test/security-architecture-academy/"
CANON = "https://andrewsferreira.github.io/security-architecture-academy/"


def portal_page(canonical: str, extra: str = "") -> str:
    return (f'<html><head><meta name="generator" content="zensical-0.0.72">'
            f'<link rel="canonical" href="{canonical}"></head><body>{extra}</body></html>')


def runner(responses: dict[str, list[st.Response]], attempts: int = 3, deadline: float = 100.0):
    calls: list[str] = []
    sleeps: list[float] = []
    clock = [0.0]

    def fetch(url: str) -> st.Response:
        calls.append(url)
        queue = responses[url]
        return queue.pop(0) if len(queue) > 1 else queue[0]

    def sleep(seconds: float) -> None:
        sleeps.append(seconds)
        clock[0] += seconds

    return st.Runner(fetch, attempts, 5.0, deadline, 0.0, sleep, lambda: clock[0]), calls, sleeps


def test_expectations_come_from_navigation_and_manifest():
    exp = st.expectations(ROOT)
    assert exp["site_url"] == CANON
    for doc in ("index.md", "getting-started/index.md", "assessments/fundamentals-final.md",
                "assessments/level-1-integrative.md", "modules/04-threat-modeling/index.md"):
        assert doc in exp["core"], doc
    assert "internal/" in exp["forbidden"]
    assert "getting-started/local-development/" in exp["forbidden"]
    assert "modules/05-network-security/" in exp["forbidden"]
    assert not any(f.startswith("modules/0" + n) for f in exp["forbidden"] for n in "01234")


def test_page_url_follows_directory_urls():
    assert st.page_url(BASE, "index.md") == BASE
    assert st.page_url(BASE, "labs/index.md") == BASE + "labs/"
    assert st.page_url(BASE, "about/roadmap.md") == BASE + "about/roadmap/"


def test_valid_page_passes_and_error_page_with_200_fails():
    url = BASE + "labs/"
    ok = st.check_page(st.Response(200, url, portal_page(CANON + "labs/")), url, CANON + "labs/")
    assert ok.ok
    fake = st.check_page(st.Response(200, url, "<html><title>Página não encontrada</title></html>"), url)
    assert not fake.ok and not fake.transient
    other = st.check_page(st.Response(200, url, portal_page(CANON)), url, CANON + "labs/")
    assert not other.ok and "canonical" in other.detail


def test_redirect_is_reported_and_not_retried():
    url = BASE + "labs/"
    run, calls, _ = runner({url: [st.Response(301, BASE + "outro/", "")]})
    result = run.run(url, lambda r: st.check_page(r, url))
    assert not result.ok and "redirecionamento" in result.detail and len(calls) == 1


def test_propagation_is_retried_with_backoff_then_passes():
    url = BASE
    stale = st.Response(200, url, portal_page(CANON, "Publicado: v0.2.0"))
    fresh = st.Response(200, url, portal_page(CANON, "Publicado: v0.2.1 — Fundamentals"))
    run, calls, sleeps = runner({url: [st.Response(None, url, "", "timeout"), stale, fresh]})
    result = run.run(url, lambda r: st.check_version(r, url, "v0.2.1", CANON))
    assert result.ok and len(calls) == 3
    assert [s for s in sleeps if s] == [5.0, 10.0]


def test_retries_are_bounded_by_attempts_and_deadline():
    url = BASE + "labs/"
    run, calls, _ = runner({url: [st.Response(503, url, "")]}, attempts=4)
    result = run.run(url, lambda r: st.check_page(r, url))
    assert not result.ok and len(calls) == 4 and "4 tentativa" in result.detail
    run, calls, _ = runner({url: [st.Response(503, url, "")]}, attempts=10, deadline=12.0)
    run.run(url, lambda r: st.check_page(r, url))
    assert len(calls) == 2  # 5 s + 10 s ultrapassariam o prazo de 12 s


def test_version_does_not_match_a_longer_version():
    url = BASE
    body = portal_page(CANON, "v0.2.10")
    assert not st.check_version(st.Response(200, url, body), url, "v0.2.1", CANON).ok


def test_forbidden_address_must_return_404():
    url = BASE + "internal/"
    assert st.check_absent(st.Response(404, url, ""), url).ok
    soft = st.check_absent(st.Response(200, url, "<h1>404 — não encontrado</h1>"), url)
    assert not soft.ok
    run, calls, _ = runner({url: [st.Response(200, url, "conteúdo antigo em cache"), st.Response(404, url, "")]})
    assert run.run(url, lambda r: st.check_absent(r, url)).ok and len(calls) == 2


def test_sitemap_requires_navigation_pages_and_rejects_forbidden():
    pages = {CANON, CANON + "labs/"}
    xml = ('<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           + "".join(f"<url><loc>{u}</loc></url>" for u in sorted(pages)) + "</urlset>")
    url = BASE + "sitemap.xml"
    assert st.check_sitemap(st.Response(200, url, xml), url, pages, ["internal/"], CANON).ok
    missing = st.check_sitemap(st.Response(200, url, xml), url, pages | {CANON + "about/"}, [], CANON)
    assert not missing.ok and missing.transient
    leaked = xml.replace("</urlset>", f"<url><loc>{CANON}internal/</loc></url></urlset>")
    blocked = st.check_sitemap(st.Response(200, url, leaked), url, pages, ["internal/"], CANON)
    assert not blocked.ok and not blocked.transient


def test_checks_after_the_deadline_make_no_request():
    url = BASE + "labs/"
    run, calls, _ = runner({url: [st.Response(503, url, "")]}, attempts=3, deadline=0.0)
    result = run.run(url, lambda r: st.check_page(r, url))
    assert not result.ok and result.transient and "prazo" in result.detail and calls == []


def test_home_page_response_is_reused_for_asset_discovery():
    url = BASE
    page = st.Response(200, url, portal_page(CANON, '<link href="./assets/stylesheets/x.css">'))
    run, calls, _ = runner({url: [page]})
    run.run(url, lambda r: st.check_page(r, url, CANON))
    assert run.last[url] is page
