#!/usr/bin/env python3
"""seclab — mecanismos de segurança na prática (Laboratório 01).

Ferramenta educacional da Security Architecture Academy, somente biblioteca padrão.
Quatro experimentos, cada um ligado a uma propriedade de segurança do Módulo 01:

  integrity  — manifesto SHA-256 de uma pasta e detecção de alteração (integridade)
  hmac       — hash simples versus HMAC: quem pode recalcular? (autenticidade)
  passwords  — senhas sem sal versus scrypt com sal (confidencialidade de credenciais)
  authz      — autenticação não é autorização: decisão por papel e por objeto

Uso:
    python seclab.py integrity build data/docs manifest.json
    python seclab.py integrity verify data/docs manifest.json
    python seclab.py hmac demo
    python seclab.py passwords demo
    python seclab.py authz demo

Dados sintéticos. Não use estes exemplos como implementação de produção.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import secrets
import sys
import time
from dataclasses import dataclass
from pathlib import Path

# ---------------------------------------------------------------------------
# 1. Integridade: manifesto de hashes
# ---------------------------------------------------------------------------


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(folder: Path) -> dict[str, str]:
    return {str(p.relative_to(folder)).replace("\\", "/"): sha256_file(p)
            for p in sorted(folder.rglob("*")) if p.is_file()}


def verify_manifest(folder: Path, manifest: dict[str, str]) -> dict[str, list[str]]:
    current = build_manifest(folder)
    return {
        "alterados": sorted(k for k in manifest if k in current and current[k] != manifest[k]),
        "removidos": sorted(k for k in manifest if k not in current),
        "novos": sorted(k for k in current if k not in manifest),
    }


# ---------------------------------------------------------------------------
# 2. Autenticidade: hash simples versus HMAC
# ---------------------------------------------------------------------------


def plain_tag(message: bytes) -> str:
    return hashlib.sha256(message).hexdigest()


def hmac_tag(key: bytes, message: bytes) -> str:
    return hmac.new(key, message, hashlib.sha256).hexdigest()


def hmac_verify(key: bytes, message: bytes, tag: str) -> bool:
    return hmac.compare_digest(hmac_tag(key, message), tag)


# ---------------------------------------------------------------------------
# 3. Armazenamento de senhas
# ---------------------------------------------------------------------------

SCRYPT = {"n": 2**14, "r": 8, "p": 1}  # parâmetros didáticos; ajuste à capacidade real em produção


def unsalted_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def scrypt_hash(password: str, salt: bytes | None = None) -> str:
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.scrypt(password.encode(), salt=salt, dklen=32, **SCRYPT)
    return f"scrypt${SCRYPT['n']}${SCRYPT['r']}${SCRYPT['p']}${salt.hex()}${digest.hex()}"


def scrypt_verify(password: str, stored: str) -> bool:
    _, n, r, p, salt_hex, digest_hex = stored.split("$")
    digest = hashlib.scrypt(password.encode(), salt=bytes.fromhex(salt_hex), dklen=32,
                            n=int(n), r=int(r), p=int(p))
    return hmac.compare_digest(digest.hex(), digest_hex)


def precomputed_table(wordlist: list[str]) -> dict[str, str]:
    """Tabela hash→senha calculada uma única vez e reutilizável contra qualquer base sem sal."""
    return {unsalted_hash(w): w for w in wordlist}


def guesses_per_second(fn, sample: list[str]) -> float:
    start = time.perf_counter()
    for w in sample:
        fn(w)
    elapsed = time.perf_counter() - start
    return len(sample) / elapsed if elapsed > 0 else float("inf")


# ---------------------------------------------------------------------------
# 4. Autorização: papel e objeto
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class User:
    login: str
    roles: frozenset[str]
    approval_limit: int
    cost_center: str


@dataclass(frozen=True)
class Payment:
    pid: str
    amount: int
    cost_center: str
    created_by: str


def authorize_role_only(user: User, action: str) -> bool:
    """Modelo ingênuo: basta ter o papel."""
    return action == "approve" and "approver" in user.roles


def authorize(user: User, action: str, payment: Payment) -> tuple[bool, str]:
    """Decisão por papel, atributos do objeto e separação de funções."""
    if action != "approve":
        return False, "ação desconhecida"
    if "approver" not in user.roles:
        return False, "sem papel de aprovador"
    if payment.created_by == user.login:
        return False, "separação de funções: quem cria não aprova"
    if payment.cost_center != user.cost_center:
        return False, "pagamento de outro centro de custo"
    if payment.amount > user.approval_limit:
        return False, "acima do limite de aprovação"
    return True, "permitido"


# ---------------------------------------------------------------------------
# Demonstrações
# ---------------------------------------------------------------------------

DATA = Path(__file__).resolve().parent / "data"


def demo_hmac() -> None:
    message = b'{"pedido": 1042, "valor": 1500, "conta": "0001-9"}'
    tampered = b'{"pedido": 1042, "valor": 1500, "conta": "6666-6"}'
    key = secrets.token_bytes(32)
    print("Mensagem original :", message.decode())
    print("Mensagem alterada :", tampered.decode())
    print("\nCom hash simples, o atacante altera a mensagem e recalcula o hash:")
    print("  hash enviado confere?", plain_tag(tampered) == plain_tag(tampered), "— a verificação não detecta nada")
    print("\nCom HMAC, recalcular exige a chave, que o atacante não tem:")
    forged = plain_tag(tampered)
    print("  tag forjada aceita?", hmac_verify(key, tampered, forged))
    print("  tag legítima da original aceita?", hmac_verify(key, message, hmac_tag(key, message)))


def demo_passwords() -> None:
    users = json.loads((DATA / "users.json").read_text(encoding="utf-8"))
    wordlist = (DATA / "wordlist.txt").read_text(encoding="utf-8").split()
    unsalted = {u: unsalted_hash(p) for u, p in users.items()}
    salted = {u: scrypt_hash(p) for u, p in users.items()}
    table = precomputed_table(wordlist)
    print("Base SEM sal (SHA-256):")
    for u, h in unsalted.items():
        print(f"  {u:8} {h[:16]}…  →  {'RECUPERADA: ' + table[h] if h in table else 'não está na tabela'}")
    same = [u for u in unsalted if list(unsalted.values()).count(unsalted[u]) > 1]
    print("  usuários com hashes idênticos (mesma senha):", ", ".join(sorted(same)) or "nenhum")
    print("\nBase COM sal (scrypt): a tabela pré-calculada não serve, e hashes de senhas iguais diferem:")
    for u, h in salted.items():
        print(f"  {u:8} …{h[-16:]}  →  {'RECUPERADA' if h in table else 'tabela inútil'}")
    fast = guesses_per_second(unsalted_hash, wordlist * 50)
    slow = guesses_per_second(lambda w: scrypt_hash(w, b"0" * 16), wordlist[:5])
    print(f"\nCusto por tentativa neste computador: SHA-256 ≈ {fast:,.0f}/s · scrypt ≈ {slow:,.1f}/s")
    print("Lição: sal impede tabelas pré-calculadas; função lenta encarece cada tentativa; senhas fracas continuam fracas.")


def demo_authz() -> None:
    maria = User("maria", frozenset({"approver"}), 100_000, "CC-LOG")
    joao = User("joao", frozenset({"approver"}), 1_000_000, "CC-FIN")
    payments = [
        Payment("P-1", 50_000, "CC-LOG", "ana"),
        Payment("P-2", 500_000, "CC-LOG", "ana"),
        Payment("P-3", 20_000, "CC-FIN", "ana"),
        Payment("P-4", 30_000, "CC-LOG", "maria"),
    ]
    print(f"{'pagamento':10} {'usuário':8} {'só papel':9} {'papel + objeto':40}")
    for user in (maria, joao):
        for p in payments:
            ok, why = authorize(user, "approve", p)
            print(f"{p.pid:10} {user.login:8} {str(authorize_role_only(user, 'approve')):9} {str(ok):6} {why}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    integ = sub.add_parser("integrity")
    integ.add_argument("mode", choices=["build", "verify"])
    integ.add_argument("folder")
    integ.add_argument("manifest")
    for name in ("hmac", "passwords", "authz"):
        sub.add_parser(name).add_argument("mode", choices=["demo"])
    args = parser.parse_args(argv)

    if args.cmd == "integrity":
        folder, manifest_path = Path(args.folder), Path(args.manifest)
        if args.mode == "build":
            manifest = build_manifest(folder)
            manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"{len(manifest)} arquivo(s) registrados em {manifest_path}")
            return 0
        result = verify_manifest(folder, json.loads(manifest_path.read_text(encoding="utf-8")))
        for kind, items in result.items():
            for item in items:
                print(f"{kind.upper():9} {item}")
        changed = any(result.values())
        print("Integridade:", "VIOLADA" if changed else "preservada")
        return 1 if changed else 0
    {"hmac": demo_hmac, "passwords": demo_passwords, "authz": demo_authz}[args.cmd]()
    return 0


if __name__ == "__main__":
    sys.exit(main())
