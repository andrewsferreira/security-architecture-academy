---
title: Referência de componentes
description: Catálogo renderizado dos componentes de documentação suportados pelo portal, com a sintaxe de cada um — referência para autores, não uma aula.
---

# Referência de componentes

!!! info "Página de referência — não é uma aula"

    Esta página demonstra os componentes **efetivamente suportados** pelo portal e mostra a sintaxe para copiar. Os textos são exemplos neutros; o conteúdo educacional oficial está somente nos módulos publicados.

## Admonitions

!!! note "Nota"

    Informação complementar ao texto principal.

!!! tip "Recomendação"

    Prefira políticas de acesso baseadas em atributos quando os papéis começarem a se multiplicar.

!!! warning "Equívoco comum"

    Segmentação de rede não substitui autenticação entre serviços.

!!! danger "Ambiente isolado"

    Execute laboratórios apenas em ambientes próprios, criados para estudo.

!!! example "Cenário"

    A *Contoso Pagamentos* opera um data center próprio e workloads em dois provedores de cloud.

!!! abstract "Resumo"

    Um parágrafo que sintetiza a seção.

!!! question "Pergunta de reflexão"

    Em que ponto da arquitetura a decisão de acesso deveria ser tomada?

```markdown
!!! warning "Equívoco comum"

    Segmentação de rede não substitui autenticação entre serviços.
```

## Seções recolhíveis

??? note "Aprofundamento (clique para expandir)"

    Conteúdo opcional que não interrompe a leitura principal.

???+ tip "Aberta por padrão"

    Use `???+` para começar expandida.

```markdown
??? note "Aprofundamento"

    Conteúdo opcional.
```

## Tabs

=== "Conceito"

    Explicação neutra em relação a fornecedores.

=== "Exemplo A"

    Implementação ilustrativa no provedor A.

=== "Exemplo B"

    Implementação ilustrativa no provedor B.

```markdown
=== "Conceito"

    Texto da aba.

=== "Exemplo A"

    Texto da aba.
```

Abas com o mesmo rótulo são sincronizadas entre blocos da página (`content.tabs.link`).

## Blocos de código

Realce de sintaxe, botão de cópia e título:

```yaml title="policy.example.yaml"
# Exemplo fictício de política de acesso
policy:
  name: admin-console-access
  subjects: [group:platform-admins]
  conditions:
    mfa: required
    device_compliant: true
  effect: allow
```

### Anotações de código

```yaml
access_review:
  frequency: quarterly # (1)!
  scope: privileged-accounts # (2)!
```

1.  A periodicidade deve ser proporcional ao risco do acesso revisado.
2.  Contas privilegiadas são o escopo mínimo; outros escopos podem ser adicionados.

````markdown
```yaml
access_review:
  frequency: quarterly # (1)!
```

1.  Texto da anotação.
````

### Código em linha e teclas

Use `zensical serve` e interrompa com ++ctrl+c++. Destaques: ==texto marcado==, ^^inserido^^, ~~removido~~.

## Tabelas

| Controle | Objetivo | Tipo |
|:---|:---|:---|
| MFA para acesso administrativo | Reduzir o impacto de credenciais comprometidas | Preventivo |
| Registro de sessões privilegiadas | Permitir investigação e responsabilização | Detectivo |
| Revisão periódica de acessos | Remover privilégios desnecessários | Corretivo |

## Checklists

- [x] Requisitos de negócio identificados
- [x] Trust boundaries mapeados
- [ ] Threat model revisado
- [ ] Decisão registrada em ADR

```markdown
- [x] Item concluído
- [ ] Item pendente
```

## Listas de definição

Trust boundary
:   Ponto em que dados ou execução passam entre componentes com níveis de confiança diferentes.

Control
:   Medida que modifica um risco.

## Notas de rodapé

A arquitetura de referência de Zero Trust descreve componentes lógicos, não produtos[^zt].

[^zt]: NIST. *SP 800-207: Zero Trust Architecture*. 2020.

```markdown
Texto com referência[^id].

[^id]: Fonte da referência.
```

## Tooltips e siglas

Siglas definidas em `includes/abbreviations.md` ganham tooltip automaticamente: IAM, PEP, PDP, MFA, SIEM.

Links também podem ter tooltip: [Modelo de conteúdo](content-model.md "Status, front matter e critérios de publicação").

## Referências cruzadas

- Para uma página: [Design System](design-system.md)
- Para uma seção: [critérios de publicação](content-model.md#criterios-de-publicacao)

Use sempre caminhos relativos para arquivos `.md` — o build valida os links.

## Ícones

:lucide-shield-check: :lucide-fingerprint: :lucide-network: :lucide-cloud: :lucide-database: :lucide-radar:

```markdown
:lucide-shield-check:
```

## Cards e grid

<div class="grid cards" markdown>

-   :lucide-fingerprint:{ .lg .saa-card-icon } **Identidade**

    ---

    Card com ícone, título e descrição curta.

-   :lucide-network:{ .lg .saa-card-icon } **Rede**

    ---

    Cards de um mesmo grid têm textos de tamanho semelhante.

-   :lucide-database:{ .lg .saa-card-icon } **Dados**

    ---

    Um card, uma ideia.

</div>

## Blocos comparativos

<div class="grid" markdown>

<div class="card" markdown>

**Abordagem A — perímetro**

- Confiança baseada na localização de rede
- Controles concentrados na borda
- Movimento lateral facilitado após o acesso inicial

</div>

<div class="card" markdown>

**Abordagem B — Zero Trust**

- Confiança avaliada a cada solicitação
- Controles próximos aos recursos
- Movimento lateral limitado por políticas

</div>

</div>

## Status e nível

<span class="saa-level">Fundamentals</span> <span class="saa-status saa-status--draft">Draft</span> <span class="saa-status saa-status--published">Published</span>

## Diagramas

```mermaid
--8<-- "assets/diagrams/layered-security.mmd"
```

Padrões completos em [Padrões de diagramas](diagrams.md).

## Imagens com legenda

<figure markdown>

![Ilustração conceitual de zonas de confiança on-premises e cloud](../assets/images/hero-architecture-light.svg#only-light){ width="420" }
![Ilustração conceitual de zonas de confiança on-premises e cloud](../assets/images/hero-architecture-dark.svg#only-dark){ width="420" }

<figcaption>Figura — Variantes clara e escura com <code>#only-light</code> e <code>#only-dark</code>.</figcaption>
</figure>

```markdown
<figure markdown>

![Texto alternativo descritivo](../assets/images/arquivo-light.svg#only-light)
![Texto alternativo descritivo](../assets/images/arquivo-dark.svg#only-dark)

<figcaption>Figura 1 — Legenda.</figcaption>
</figure>
```
