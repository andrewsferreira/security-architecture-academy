---
id: M01-L04
title: "Aula 04 — Criptografia aplicada: simétrica, assimétrica, hashing e assinaturas"
public_title: "Módulo 1 — Aula 04 — Criptografia aplicada: simétrica, assimétrica, hashing e assinaturas"
description: O que cada primitiva criptográfica garante — e o que não garante —, como elas se combinam em esquemas híbridos, os erros de uso mais comuns e o que muda com a criptografia pós-quântica.
domain: security-foundations
tier: fundamental
status: published
prerequisites: [M01-L01]
objectives:
  - Diferenciar criptografia simétrica, assimétrica, hash, MAC e assinatura digital quanto às propriedades que garantem.
  - Explicar por que esquemas reais combinam primitivas (criptografia híbrida).
  - Identificar erros de uso frequentes em arquiteturas.
  - Situar a transição para algoritmos pós-quânticos e o conceito de agilidade criptográfica.
minutes: 75
sources: [BOOK-ANDERSON-SE3, NIST-SP800-57-PT1-R5, NIST-FIPS-203, NIST-IR-8547]
further_reading: [RFC-9846]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M01
---

# Aula 04 — Criptografia aplicada: simétrica, assimétrica, hashing e assinaturas { #criptografia-aplicada-simetrica-assimetrica-hashing-e-assinaturas }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 1 · Nível 0</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min · ID técnico: M01-L04</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Arquitetos não precisam projetar algoritmos — e não devem. Precisam saber **qual primitiva resolve qual problema**, como elas se combinam e onde os sistemas reais costumam errar. Quase sempre, a criptografia falha não pela matemática, mas pelo uso: chaves no código, cifragem sem integridade, hashes rápidos para senhas. Esta aula organiza esse conhecimento e situa a mudança mais importante da área: a transição para algoritmos resistentes a computadores quânticos.

**Pré-requisitos:** [Propriedades de segurança](01-security-properties.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar criptografia simétrica, assimétrica, hash, MAC e assinatura digital quanto às propriedades que garantem.
- Explicar por que esquemas reais combinam primitivas (criptografia híbrida).
- Identificar erros de uso frequentes em arquiteturas.
- Situar a transição para algoritmos pós-quânticos e o conceito de agilidade criptográfica.

## Conceito

### Primitivas e propriedades

| Primitiva | O que faz | Garante | Não garante | Exemplos |
|:---|:---|:---|:---|:---|
| **Cifra simétrica** | Mesma chave cifra e decifra | Confidencialidade (e integridade, se autenticada) | Quem enviou, se a chave é compartilhada | AES-GCM, ChaCha20-Poly1305 |
| **Cifra assimétrica / troca de chaves** | Par de chaves: pública e privada | Confidencialidade para o dono da chave privada; acordo de chaves | Desempenho para grandes volumes | RSA, ECDH, ML-KEM |
| **Hash** | Resumo de tamanho fixo, unidirecional | Detecção de alteração **se o hash for protegido** | Autenticidade — qualquer um calcula | SHA-256, SHA-3 |
| **MAC** | Hash com chave secreta | Integridade e autenticidade entre quem tem a chave | Não repúdio (ambos têm a chave) | HMAC-SHA-256 |
| **Assinatura digital** | Assina com chave privada; verifica com a pública | Integridade, autenticidade de origem, base para não repúdio | Confidencialidade | ECDSA, Ed25519, RSA-PSS, ML-DSA |

Uma conclusão importante da tabela: **cifrar não garante integridade por si só**, e **hash não garante autenticidade**. Um arquivo publicado com seu hash no mesmo servidor não está protegido contra quem comprometer o servidor — o atacante troca os dois.

### O princípio de Kerckhoffs

A segurança de um sistema criptográfico deve depender apenas do segredo das **chaves**, não do segredo do algoritmo — a versão criptográfica do princípio de *open design* (Aula 02). Algoritmos públicos e amplamente analisados são mais confiáveis que algoritmos "proprietários". Na prática de arquitetura: **use bibliotecas e algoritmos padronizados; nunca criptografia caseira.**

## Fundamentos técnicos

### Simétrica: rápida, mas a chave é o problema

Cifras simétricas são rápidas e cifram grandes volumes. Modos **autenticados** (AEAD), como AES-GCM e ChaCha20-Poly1305, entregam confidencialidade e integridade juntas — e são a escolha padrão hoje. O problema é a **distribuição da chave**: as duas partes precisam conhecê-la, e qualquer uma pode cifrar ou decifrar.

### Assimétrica: resolve a distribuição, mas é lenta

Com um par de chaves, qualquer um pode cifrar para o dono da chave pública, e só ele decifra com a privada; e só o dono da chave privada consegue assinar, enquanto qualquer um verifica. Operações assimétricas são muito mais lentas, por isso são usadas para **trocar ou proteger chaves simétricas** e para **assinar resumos**, não para cifrar grandes volumes.

### Criptografia híbrida

Na prática, os esquemas combinam primitivas — é assim que funcionam TLS, e-mail cifrado e cifragem de arquivos.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m01-l04-hybrid-encryption.mmd"
```

<figcaption>Figura 1 — Envio de um arquivo cifrado e assinado com criptografia híbrida.</figcaption>
</figure>

A chave simétrica aleatória cifra o volume; a assimétrica protege essa chave; a assinatura sobre o hash prova origem e integridade. Cada primitiva cumpre o papel em que é boa.

### Senhas: um caso especial de hash

Senhas não devem ser cifradas (cifra é reversível) nem guardadas com hash rápido (SHA-256 permite bilhões de tentativas por segundo em hardware comum). Usa-se **função de derivação de chaves lenta e com salt** — como Argon2id, scrypt ou PBKDF2 com muitas iterações — para tornar ataques de força bruta caros.

### Chaves e cryptoperiods

A segurança depende de como as chaves são geradas, armazenadas, usadas, trocadas e destruídas. O NIST SP 800-57 Part 1 Rev. 5 trata o gerenciamento de chaves e o conceito de **cryptoperiod** — o tempo durante o qual uma chave pode ser usada. Esse tema é aprofundado na Aula 05 e no Módulo 13.

### Pós-quântica e agilidade criptográfica

Computadores quânticos suficientemente grandes quebrariam os algoritmos assimétricos usados hoje (RSA e curvas elípticas). Em agosto de 2024, o NIST publicou os primeiros padrões pós-quânticos: **FIPS 203** (ML-KEM, para encapsulamento de chaves), **FIPS 204** (assinatura baseada em reticulados) e **FIPS 205** (assinatura baseada em hash). Em novembro de 2024, publicou o rascunho do **NIST IR 8547**, que propõe a transição dos algoritmos vulneráveis — ainda um rascunho público, não uma norma final.

Duas consequências para arquitetos:

- **"Colete agora, decifre depois":** dados cifrados hoje com troca de chaves clássica podem ser gravados e decifrados no futuro. Dados com necessidade de confidencialidade de longo prazo justificam priorizar a transição.
- **Agilidade criptográfica:** sistemas devem permitir trocar algoritmos sem reescrever aplicações — o que exige saber **onde** a criptografia é usada (um inventário criptográfico) e centralizá-la em bibliotecas e serviços.

## Exemplo empresarial

!!! example "Aurora Pagamentos — o arquivo de conciliação"

    A Aurora recebe diariamente um arquivo de conciliação de um banco parceiro. O processo atual: o banco cifra o arquivo com uma senha combinada por e-mail há quatro anos e envia por SFTP.

    A revisão criptográfica encontrou três problemas:

    | Problema | Propriedade afetada | Correção |
    |:---|:---|:---|
    | A senha nunca foi trocada e circulou por e-mail | Confidencialidade | Troca de chaves com par assimétrico: o banco cifra para a chave pública da Aurora |
    | Nada prova que o arquivo veio do banco | Autenticidade e integridade | Assinatura do banco sobre o arquivo, verificada antes do processamento |
    | Algoritmo e chave estão fixos no código do processo | Agilidade | Biblioteca padrão e chaves em serviço de gestão de chaves |

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Algoritmos | Escolhidos por cada desenvolvedor | Lista corporativa de algoritmos e bibliotecas aprovados |
| Cifragem | Sem integridade (modos não autenticados) | AEAD por padrão |
| Senhas | Hash rápido ou cifra reversível | Função de derivação lenta com salt |
| Chaves | No código, em arquivos, por e-mail | Em KMS/HSM, com rotação e acesso por identidade |
| Evolução | Troca de algoritmo exige reescrever sistemas | Inventário criptográfico e agilidade |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | O que muda |
|:---|:---|
| **On-premises** | HSMs próprios ou servidores de chaves; maior esforço operacional. |
| **Cloud** | KMS gerenciado cifra serviços nativos com poucos cliques; a decisão é quem controla a chave (provedor, cliente, ou chave externa). |
| **Híbrido** | Políticas de algoritmos e de chaves precisam ser uniformes; dados que circulam entre ambientes não podem cair para o padrão mais fraco. |

## Como especificar e implementar

- "Somente algoritmos e bibliotecas da lista criptográfica corporativa são usados; cifragem usa modos autenticados."
- "Senhas são armazenadas com Argon2id ou equivalente aprovado."
- "Chaves não são armazenadas em código, repositórios ou configuração em claro; ficam em serviço de gestão de chaves."
- "Sistemas que protegem dados com necessidade de confidencialidade superior a 10 anos têm plano de transição pós-quântica."

## Trade-offs, limitações e antipadrões

- **Antipadrão — criptografia caseira** ou algoritmos obsoletos (MD5, SHA-1 para assinaturas, DES, RC4).
- **Antipadrão — "está cifrado, então está seguro"** com a chave no mesmo servidor dos dados.
- **Limitação:** criptografia protege dados, não decide quem deve acessá-los — isso é autorização.

## Como validar

- Inventariar onde há criptografia: protocolos, bibliotecas, algoritmos, chaves e quem as controla.
- Procurar segredos em repositórios de código e configurações.
- Verificar o armazenamento de senhas nas aplicações.
- Conferir se processos de recebimento de arquivos verificam assinaturas antes de processar.

## Como apresentar e justificar

- **Para engenharia:** "Vamos exigir assinatura do banco e trocar a senha compartilhada por chaves assimétricas; a biblioteca e as chaves passam a ser gerenciadas centralmente."
- **Para gestores:** "Hoje não conseguimos provar que o arquivo de conciliação veio do banco. Um atacante poderia inserir um arquivo falso. A mudança garante a origem e a integridade dos dados."

## Checklist de revisão arquitetural

- [ ] As primitivas usadas correspondem às propriedades exigidas.
- [ ] Algoritmos e bibliotecas são padronizados e atuais.
- [ ] A cifragem é autenticada.
- [ ] Senhas usam função de derivação lenta com salt.
- [ ] Chaves estão em KMS/HSM, com rotação e controle de acesso.
- [ ] Existe inventário criptográfico e plano de agilidade.

## Questões de compreensão

**1.** Por que um hash publicado no mesmo servidor do arquivo não garante que o arquivo é autêntico?

??? success "Resposta comentada"

    Porque quem comprometer o servidor pode trocar o arquivo e o hash juntos. O hash detecta alterações acidentais; para autenticidade, é preciso uma assinatura com chave privada que o atacante não tem.

**2.** Qual a diferença entre MAC e assinatura digital quanto ao não repúdio?

??? success "Resposta comentada"

    No MAC, as duas partes têm a mesma chave secreta, então qualquer uma poderia ter gerado o código — não há não repúdio entre elas. Na assinatura, só o dono da chave privada consegue assinar.

**3.** Por que dados cifrados hoje podem estar em risco por causa de computadores quânticos futuros?

??? success "Resposta comentada"

    Porque um atacante pode gravar o tráfego cifrado agora e decifrá-lo no futuro, quando houver computadores quânticos capazes de quebrar a troca de chaves clássica. Dados que precisam permanecer confidenciais por muitos anos são os mais afetados.

## Exercício de tomada de decisão

!!! question "Cenário: armazenar documentos de pacientes na Lumen"

    A Lumen vai armazenar laudos em PDF em um serviço de armazenamento de objetos. Propostas: (A) cifragem padrão do serviço, com chave gerenciada pelo provedor; (B) cifragem do serviço com chave gerenciada pela Lumen no KMS, com política de acesso à chave restrita à aplicação de laudos; (C) cifragem na aplicação antes do envio, com chaves por paciente em HSM próprio.

    Critérios: separação entre acesso aos dados e acesso às chaves, operação e recuperação, e custo.

??? success "Resolução de referência"

    | Critério | Peso | A — Chave do provedor | B — Chave da Lumen no KMS | C — Cifragem na aplicação com HSM |
    |:---|:---|:---|:---|:---|
    | Separação entre acesso aos dados e às chaves | 3 | 1 | 3 | 3 |
    | Operação e recuperação | 2 | 3 | 2 | 1 |
    | Custo | 1 | 3 | 2 | 1 |
    | **Total ponderado** | | **12** | **15** | **12** |

    **Recomendação: B.**

    - **A** protege contra roubo de mídia física, mas qualquer identidade com acesso ao armazenamento lê os laudos — a separação entre "acesso ao armazenamento" e "acesso à chave" não existe.
    - **B** cria uma segunda condição para ler os dados: ter permissão na chave, controlada pela Lumen e restrita à aplicação; permite auditar o uso da chave e revogá-la.
    - **C** oferece o maior isolamento, mas acrescenta complexidade alta (gestão de milhões de chaves, recuperação, busca) e custo de HSM que dificilmente se justifica para o porte da Lumen.

    O ponto central: **o valor da cifragem está em separar quem tem acesso aos dados de quem tem acesso às chaves**.

## Pontos-chave

- Cada primitiva garante propriedades específicas; cifrar não garante integridade, e hash não garante autenticidade.
- Esquemas reais são híbridos: simétrica para volume, assimétrica para chaves e assinaturas.
- Use algoritmos padronizados e modos autenticados; nunca criptografia caseira.
- Senhas exigem funções de derivação lentas com salt.
- FIPS 203, 204 e 205 (2024) iniciaram a era pós-quântica; agilidade criptográfica começa pelo inventário.

## Referências

### Fundamentação principal

- R. Anderson. *Security Engineering*, 3ª ed. Cap. 5 *Cryptography*. <https://www.cl.cam.ac.uk/archive/rja14/book.html> *(capítulo localizado pelo sumário)*.
- NIST. *SP 800-57 Part 1 Rev. 5 — Recommendation for Key Management: Part 1 – General*. 2020. <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final> — ciclo de vida e cryptoperiods de chaves. *(Página oficial conferida.)*
- NIST. *FIPS 203 — Module-Lattice-Based Key-Encapsulation Mechanism Standard*; *FIPS 204 — Module-Lattice-Based Digital Signature Standard*; *FIPS 205 — Stateless Hash-Based Digital Signature Standard*. 13/08/2024. <https://csrc.nist.gov/pubs/fips/203/final>
- NIST. *IR 8547 — Transition to Post-Quantum Cryptography Standards* (Initial Public Draft). 12/11/2024. <https://csrc.nist.gov/pubs/ir/8547/ipd> — proposta de transição; ainda não final.

### Leitura complementar

- E. Rescorla. *RFC 9846 — TLS 1.3*. IETF, 2026 — exemplo de protocolo que combina troca de chaves, cifragem autenticada e assinaturas.

### Aplicação prática

- Comece um inventário criptográfico com três colunas: onde a criptografia é usada, qual algoritmo e quem controla a chave.
- O [Laboratório 01](../../labs/lab-01-security-mechanisms.md) mostra na prática integridade com hashes, HMAC e armazenamento de senhas com e sem sal.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
