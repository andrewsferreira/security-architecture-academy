---
title: Guia editorial
description: Padrões de escrita, terminologia, código, diagramas, tabelas, referências e avisos obrigatórios para todo conteúdo da Security Architecture Academy.
---

# Guia editorial

Referência obrigatória para qualquer conteúdo educacional do projeto. Revisores usam este guia como critério objetivo de aprovação.

## Idioma e tom

- **Português brasileiro** claro, direto e impessoal. Prefira a voz ativa: *"O PEP intercepta a solicitação"*, não *"A solicitação é interceptada pelo PEP"*.
- Frases curtas; um conceito por parágrafo.
- Escreva para profissionais: explique o porquê, não apenas o quê. Evite simplificações que se tornem incorretas.
- Sem jargão de marketing (*"revolucionário"*, *"definitivo"*, *"bala de prata"*) e sem alarmismo.
- Sem emojis em conteúdo técnico.

## Terminologia

- **Termos técnicos consolidados ficam em inglês**, com explicação em português na primeira ocorrência da página:
  > *Trust boundary* (fronteira de confiança) é o ponto em que dados ou execução passam entre componentes com níveis de confiança diferentes.
- Depois da primeira ocorrência, use apenas o termo em inglês, em texto normal (sem itálico).
- **Siglas:** por extenso na primeira ocorrência — *Policy Enforcement Point (PEP)* — e adicionadas a `includes/abbreviations.md`, que gera tooltip em todo o portal.
- Consistência acima de preferência pessoal: se o glossário define *threat modeling*, não use *modelagem de ameaças* em outra aula.

| Use | Evite |
|:---|:---|
| controle de segurança | medida, proteção (como sinônimos soltos) |
| identidade | usuário (quando incluir identidades de máquina) |
| trust boundary | perímetro (exceto quando for de fato um perímetro de rede) |
| vulnerabilidade / ameaça / risco | uso intercambiável dos três |

## Tipos de afirmação

Toda afirmação normativa ou de boa prática deve deixar claro **de onde vem**:

| Tipo | Como sinalizar | Exemplo |
|:---|:---|:---|
| Requisito normativo | Citar norma, seção e versão | *"A ISO/IEC 27001:2022 exige… (cláusula 6.1.2)"* |
| Boa prática reconhecida | Citar a fonte | *"O NIST SP 800-207 recomenda…"* |
| Prática comum de mercado | Declarar como tal | *"É comum que organizações…"* |
| Opinião ou recomendação do autor | Declarar explicitamente | *"Na visão desta formação…"* |

Afirmações sem fundamento técnico verificável não são publicadas.

## Estrutura das páginas

- Um único H1 por página, igual ao `title` do front matter.
- Hierarquia sem saltos: H2 → H3 → H4. Títulos objetivos, sem pontuação final.
- Abertura com 1–3 frases dizendo o que a página resolve.
- Seções longas terminam com um resumo ou com os pontos-chave.
- Use os [templates](content-model.md#templates-de-autoria) — eles já trazem a estrutura correta.

## Exemplos

- Cenários **corporativos e realistas**, mas **fictícios**: empresas como *Contoso Pagamentos* ou *Acme Logística*.
- Domínios, IPs e identificadores reservados para documentação:

| Tipo | Use |
|:---|:---|
| Domínios | `example.com`, `example.org`, `*.example` |
| IPv4 | `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` (RFC 5737) |
| IPv6 | `2001:db8::/32` (RFC 3849) |
| E-mails | `ana.silva@example.com` |
| Chaves e tokens | valores visivelmente falsos: `EXAMPLE-KEY-0000`, `eyJ...EXAMPLE` |

- **Proibido:** dados pessoais reais, credenciais reais (mesmo revogadas), nomes de clientes, informações internas de empregadores, IPs ou domínios reais de terceiros.

## Código

- Bloco sempre com linguagem declarada e, quando relevante, `title`.
- Código deve ser **executável ou explicitamente marcado como ilustrativo** (`!!! note "Trecho ilustrativo"`).
- Configurações devem refletir padrões seguros; quando um exemplo inseguro for didático, ele deve vir marcado com `!!! danger` e acompanhado da versão corrigida.
- Indicar versões de ferramentas quando a sintaxe depender delas.
- Comandos com efeitos destrutivos nunca aparecem sem aviso.

## Diagramas

- Use Mermaid a partir de `assets/diagrams/` — ver [Padrões de diagramas](diagrams.md).
- Todo diagrama precisa de propósito declarado no texto: *"O diagrama abaixo mostra…"*.
- Toda figura de conteúdo tem legenda e descrição acessível (`accDescr`).

## Checklists

- Use listas de tarefas (`- [ ]`) para verificações que o leitor executa.
- Cada item é verificável com sim/não: *"Todos os acessos administrativos exigem MFA"*, não *"Pensar em MFA"*.

## Tabelas

- Para comparar opções ou mapear relações (controle × framework). Não para texto corrido.
- Até 5 colunas, cabeçalho obrigatório, primeira coluna identifica a linha.

## Referências externas

Formato padrão ao final de cada página:

```markdown
## Referências

- NIST. *SP 800-207: Zero Trust Architecture*. 2020. <https://doi.org/10.6028/NIST.SP.800-207> — gratuito.
- ISO/IEC. *27001:2022 — Information security management systems*. 2022. — pago.
```

Regras:

- Autor/organização, título em itálico, versão ou ano, link e **gratuito/pago**.
- Preferir links permanentes (DOI, página oficial) a cópias de terceiros.
- Notas de rodapé (`[^1]`) para referências pontuais dentro do texto.
- Nunca reproduzir trechos extensos de normas pagas; parafrasear e citar.

## Notas técnicas e avisos

| Situação | Componente |
|:---|:---|
| Detalhe aprofundado, opcional | `??? note "Aprofundamento"` (recolhível) |
| Pegadinha conceitual comum | `!!! warning "Equívoco comum"` |
| Ação que pode causar dano | `!!! danger` com a consequência descrita |
| Exemplo de cenário | `!!! example` |

### Aviso de segurança obrigatório em laboratórios

Todo laboratório começa com:

```markdown
!!! danger "Ambiente isolado"

    Execute este laboratório apenas em ambiente próprio e isolado, criado para
    estudo. Nunca aplique os passos em sistemas de terceiros ou de produção.
```

## Versões de frameworks

- Informe a versão sempre que o conteúdo depender dela: *"CIS Controls v8.1"*, *"NIST CSF 2.0"*.
- Registre a data de consulta em `last_updated` no front matter.
- Ao surgir nova versão, a página recebe `!!! warning "Versão"` até ser revisada.

## Conteúdo desatualizado

- Conteúdo que perdeu validade recebe status `deprecated` no front matter e no manifesto, com `replaced_by` ou `deprecation_note`.
- A página exibe no topo:

```markdown
!!! warning "Conteúdo descontinuado"

    Esta página foi substituída por [Nova página](link). Mantida apenas para referência.
```

## Recursos pagos e gratuitos

- Recursos externos indicam explicitamente **gratuito**, **pago** ou **freemium**.
- Toda aula deve ser compreensível usando apenas recursos gratuitos; recursos pagos são complementares.
- Sem links de afiliado, cupons ou recomendações comerciais.

## Checklist do autor

- [ ] Front matter completo e `last_updated` atualizado
- [ ] Terminologia e siglas conforme este guia
- [ ] Afirmações normativas com fonte e versão
- [ ] Exemplos fictícios, sem dados ou credenciais reais
- [ ] Diagramas com `accTitle`, `accDescr` e legenda
- [ ] Seção de referências no formato padrão
- [ ] `make validate` sem erros
