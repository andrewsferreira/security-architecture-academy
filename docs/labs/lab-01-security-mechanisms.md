---
id: LAB-01
title: "Laboratório 01 — Mecanismos de segurança na prática"
description: Laboratório local e gratuito com quatro experimentos curtos — integridade com hashes, autenticidade com HMAC, armazenamento de senhas com e sem sal e autorização por papel e por objeto — que tornam observáveis as propriedades e os mecanismos do Módulo 1.
domain: security-foundations
tier: fundamental
status: published
prerequisites: [M01-L01, M01-L02, M01-L04]
objectives:
  - Detectar alteração de arquivos com um manifesto de hashes e explicar o que ele não garante.
  - Demonstrar por que um hash simples não autentica uma mensagem e um HMAC sim.
  - Comparar armazenamento de senhas sem sal e com função lenta e sal.
  - Distinguir autenticação de autorização com decisões por objeto e separação de funções.
estimated_time: "1 h 30 min"
cost: "Sem custo — execução local"
tested: true
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
---

# Laboratório 01 — Mecanismos de segurança na prática

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Laboratório · LAB-01</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">1 h 30 min · sem custo</span>
</div>

## Resumo

!!! danger "Ambiente isolado e dados sintéticos"

    Todos os experimentos rodam no seu computador, sem rede, com usuários, senhas, documentos e pagamentos **sintéticos**, criados para o laboratório. As senhas de exemplo são propositalmente fracas e não pertencem a ninguém.

| Item | Valor |
|:---|:---|
| Tempo estimado | 1 h 30 min |
| Custo | Nenhum — Python, somente biblioteca padrão |
| Status de teste | **Executado e testado** em 2026-10-23 e novamente em 2026-10-27: os quatro experimentos foram executados em diretório limpo; a ferramenta é verificada por testes automatizados no CI |
| Arquivos | [`examples/lab-01-security-mechanisms/`](https://github.com/andrewsferreira/security-architecture-academy/tree/main/examples/lab-01-security-mechanisms) |

O Módulo 1 apresentou propriedades — integridade, autenticidade, confidencialidade, autorização — e os mecanismos que as realizam. Aqui você vai **ver** cada mecanismo funcionar e, principalmente, ver **o que ele não garante**. Cada experimento leva 15 a 20 minutos.

## Objetivo

- Detectar alteração de arquivos com um manifesto de hashes e explicar o que ele não garante.
- Demonstrar por que um hash simples não autentica uma mensagem e um HMAC sim.
- Comparar armazenamento de senhas sem sal e com função lenta e sal.
- Distinguir autenticação de autorização com decisões por objeto e separação de funções.

## Cenário empresarial

A Meridiana Distribuidora está revisando controles básicos antes de uma auditoria: documentos de política precisam ter integridade verificável; mensagens de pedidos trocadas com um parceiro precisam ser autênticas; o sistema legado de reembolsos guarda senhas com SHA-256 sem sal; e o novo fluxo de aprovação de pagamentos verifica apenas se o usuário "é aprovador". Você vai demonstrar à equipe, com dados sintéticos, por que cada ponto importa.

## Requisitos

| Item | Versão | Observação |
|:---|:---|:---|
| Python | 3.11 ou superior | Gratuito; nenhuma biblioteca externa |
| Terminal | Qualquer | — |

## Arquitetura inicial

| Experimento | Propriedade (Módulo 1 — Aula 01) | Mecanismo | Aula de apoio |
|:---|:---|:---|:---|
| `integrity` | Integridade | Hash SHA-256 por arquivo, em um manifesto | [Módulo 1 — Aula 04](../modules/01-security-fundamentals/04-applied-cryptography.md) |
| `hmac` | Autenticidade de mensagem | HMAC-SHA256 com chave secreta | Módulo 1 — Aula 04 |
| `passwords` | Confidencialidade de credenciais | scrypt com sal versus SHA-256 sem sal | Módulo 1 — Aula 04 |
| `authz` | Autorização e separação de funções | Decisão por papel, atributos do objeto e criador | [Módulo 1 — Aula 01](../modules/01-security-fundamentals/01-security-properties.md) e [Módulo 1 — Aula 02](../modules/01-security-fundamentals/02-secure-design-principles.md) |

## Passo a passo

### 1. Preparar o ambiente

```bash
git clone https://github.com/andrewsferreira/security-architecture-academy.git
cd security-architecture-academy/examples/lab-01-security-mechanisms
python3 seclab.py --help
```

### 2. Integridade com manifesto de hashes

```bash
python3 seclab.py integrity build data/docs manifest.json
python3 seclab.py integrity verify data/docs manifest.json
```

**Resultado esperado:** "Integridade: preservada". Agora altere uma linha de `data/docs/tabela-fretes.txt` e verifique de novo.

**Resultado esperado:** `ALTERADOS tabela-fretes.txt` e "Integridade: VIOLADA" (código de saída `1`).

!!! question "Pare e pense"

    Quem alterou o arquivo também poderia gerar um novo `manifest.json`. O que é preciso para que o manifesto seja confiável? (Dica: onde ele fica guardado e quem pode alterá-lo — ou como ele seria assinado.)

### 3. Hash simples versus HMAC

```bash
python3 seclab.py hmac demo
```

**Resultado esperado:** com hash simples, a mensagem alterada "confere", porque o atacante recalcula o hash; com HMAC, a tag forjada é rejeitada e a legítima é aceita.

### 4. Armazenamento de senhas

```bash
python3 seclab.py passwords demo
```

**Resultado esperado:**

- Na base **sem sal**, três das quatro senhas são recuperadas por uma tabela pré-calculada, e dois usuários aparecem com o **mesmo hash** (mesma senha).
- Na base **com scrypt e sal**, a tabela é inútil e hashes de senhas iguais são diferentes.
- O custo por tentativa cai de centenas de milhares a milhões por segundo (SHA-256) para dezenas por segundo (scrypt) — os números exatos dependem do seu computador. Em 2026-10-27, numa execução de referência, foram cerca de 0,6 a 1 milhão por segundo com SHA-256 e cerca de 16 a 23 por segundo com scrypt.

!!! question "Pare e pense"

    A senha da usuária "ana" continua fraca com scrypt. O que o sal e a função lenta resolvem, e o que só uma política de senhas (ou MFA) resolve?

### 5. Autenticação não é autorização

```bash
python3 seclab.py authz demo
```

**Resultado esperado:** o modelo "só papel" permite todas as aprovações; o modelo "papel + objeto" nega pagamentos acima do limite, de outro centro de custo e criados pelo próprio aprovador.

## Critérios de validação

- [ ] Você provocou e detectou uma alteração de integridade.
- [ ] Você explicou por que o hash simples não autentica e o HMAC sim.
- [ ] Você descreveu o que o sal e a função lenta resolvem — e o que não resolvem.
- [ ] Você identificou as três razões de negação no modelo "papel + objeto".

## Evidências esperadas

| Evidência | Conteúdo |
|:---|:---|
| Saídas dos quatro experimentos | Copiadas para um documento próprio |
| Respostas às perguntas "Pare e pense" | Documento próprio |
| Respostas às perguntas arquiteturais | Documento próprio |

## Perguntas arquiteturais

1. Em que tipo de sistema um manifesto de hashes é suficiente, e em que tipo você precisaria de assinatura digital (Módulo 1 — Aula 05)?
2. O parceiro e a Meridiana compartilham a chave do HMAC. O HMAC oferece **não repúdio**? Por quê?
3. O sistema legado não pode ser alterado nos próximos seis meses. Que controles compensatórios você propõe para a base de senhas sem sal?
4. A regra "quem cria não aprova" é um exemplo de qual princípio de design seguro (Módulo 1 — Aula 02)?
5. Onde, em uma arquitetura real, deveria ficar a decisão de autorização por objeto — no front-end, na API ou no banco? Justifique.

## Explicação do resultado

??? success "O que este laboratório demonstra"

    **Hash detecta alteração, mas não diz quem alterou.** O manifesto só é confiável se estiver protegido contra quem pode alterar os arquivos — guardado em outro lugar, com outro controle de acesso, ou assinado.

    **Integridade de mensagem exige segredo ou assinatura.** Qualquer um recalcula um SHA-256; um HMAC exige a chave. Mas, como as duas partes conhecem a chave, o HMAC não prova **qual** delas gerou a mensagem — não há não repúdio. Para isso, assinatura digital com chave privada sob controle exclusivo do autor.

    **Sal e função lenta tratam ataques diferentes.** O sal impede tabelas pré-calculadas e esconde senhas repetidas; a função lenta encarece cada tentativa. Nenhum dos dois torna forte uma senha fraca: isso é papel de política de senhas, listas de senhas proibidas e MFA.

    **Ter o papel não basta.** A maioria das falhas de autorização em aplicações acontece porque se verifica a **função** do usuário e não o **objeto** — exatamente a diferença entre os dois modelos. Separação de funções e limites por valor são regras de negócio que precisam estar na decisão de autorização, no servidor.

## Desmontagem

```bash
rm -f manifest.json
git checkout -- data/docs   # desfaz a alteração feita no passo 2
```

## Referências

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020 — Cap. 3 *Psychology and Usability* e Cap. 5 *Cryptography* (capítulos localizados pelo sumário; leitura recomendada). Livro comercial.
- IETF. *RFC 2104 — HMAC: Keyed-Hashing for Message Authentication*. 1997. <https://www.rfc-editor.org/rfc/rfc2104> — gratuito.
- IETF. *RFC 7914 — The scrypt Password-Based Key Derivation Function*. 2016. <https://www.rfc-editor.org/rfc/rfc7914> — gratuito.
- Python Software Foundation. *hashlib*, *hmac* e *secrets*. <https://docs.python.org/3/library/hashlib.html> — gratuito.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última execução de teste | 2026-10-27 — `pytest examples/lab-01-security-mechanisms` (5 testes) e execução dos passos 2 a 5 em diretório limpo (Linux, Python 3.13). |
