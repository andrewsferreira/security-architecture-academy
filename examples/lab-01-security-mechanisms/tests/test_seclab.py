"""Testes do seclab (Laboratório 01). Executados no CI junto com os testes do projeto."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(LAB))

import seclab  # noqa: E402


def test_integrity_detects_change_removal_and_addition(tmp_path):
    folder = tmp_path / "docs"
    shutil.copytree(LAB / "data" / "docs", folder)
    manifest = tmp_path / "manifest.json"
    assert seclab.main(["integrity", "build", str(folder), str(manifest)]) == 0
    assert seclab.main(["integrity", "verify", str(folder), str(manifest)]) == 0
    (folder / "tabela-fretes.txt").write_text("Rota 01: R$ 0,10/km\n", encoding="utf-8")
    (folder / "politica-reembolso.txt").unlink()
    (folder / "novo.txt").write_text("x", encoding="utf-8")
    result = seclab.verify_manifest(folder, json.loads(manifest.read_text(encoding="utf-8")))
    assert result == {"alterados": ["tabela-fretes.txt"], "removidos": ["politica-reembolso.txt"], "novos": ["novo.txt"]}
    assert seclab.main(["integrity", "verify", str(folder), str(manifest)]) == 1


def test_hmac_requires_key():
    key, msg = b"k" * 32, b"pedido 1042"
    tag = seclab.hmac_tag(key, msg)
    assert seclab.hmac_verify(key, msg, tag)
    assert not seclab.hmac_verify(key, b"pedido 1043", tag)
    assert not seclab.hmac_verify(b"x" * 32, msg, tag)
    # hash simples pode ser recalculado por qualquer um
    assert seclab.plain_tag(b"pedido 1043") == seclab.plain_tag(b"pedido 1043")


def test_password_storage():
    stored = seclab.scrypt_hash("verao2026")
    assert seclab.scrypt_verify("verao2026", stored)
    assert not seclab.scrypt_verify("verao2027", stored)
    assert seclab.scrypt_hash("verao2026") != seclab.scrypt_hash("verao2026")  # sal diferente
    assert seclab.unsalted_hash("verao2026") == seclab.unsalted_hash("verao2026")
    table = seclab.precomputed_table(["123456", "verao2026"])
    assert table[seclab.unsalted_hash("verao2026")] == "verao2026"
    assert stored not in table


def test_authorization_by_object():
    maria = seclab.User("maria", frozenset({"approver"}), 100_000, "CC-LOG")
    ok = seclab.Payment("P-1", 50_000, "CC-LOG", "ana")
    too_big = seclab.Payment("P-2", 500_000, "CC-LOG", "ana")
    other_cc = seclab.Payment("P-3", 20_000, "CC-FIN", "ana")
    own = seclab.Payment("P-4", 30_000, "CC-LOG", "maria")
    assert seclab.authorize_role_only(maria, "approve") is True
    assert seclab.authorize(maria, "approve", ok) == (True, "permitido")
    assert seclab.authorize(maria, "approve", too_big)[0] is False
    assert seclab.authorize(maria, "approve", other_cc)[0] is False
    assert seclab.authorize(maria, "approve", own) == (False, "separação de funções: quem cria não aprova")
    reader = seclab.User("rui", frozenset({"reader"}), 10**9, "CC-LOG")
    assert seclab.authorize(reader, "approve", ok)[0] is False


def test_demos_run(capsys):
    for cmd in ("hmac", "authz", "passwords"):
        assert seclab.main([cmd, "demo"]) == 0
    out = capsys.readouterr().out
    assert "RECUPERADA: verao2026" in out
    assert "tabela inútil" in out
    assert "separação de funções" in out
