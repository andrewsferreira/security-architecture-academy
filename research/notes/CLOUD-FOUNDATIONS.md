# Fundações de segurança em cloud — AWS, Azure e Google Cloud

**Referências:** `AWS-SECURITY-PILLAR`, `AWS-SRA`, `AZURE-WAF-SECURITY`, `AZURE-WAF-SECURITY-CHECKLIST`, `MS-MCRA`, `GCP-ENTERPRISE-FOUNDATIONS`, `GCP-WAF-SECURITY`, `CSA-GUIDANCE-V5` · Nota de leitura original e comparativa · Revisão de 2026-10-23

## Identificação

| Referência | Documento | Versão conferida |
|:---|:---|:---|
| `AWS-SECURITY-PILLAR` | AWS Well-Architected — Security Pillar | Whitepaper de 06/11/2024 |
| `AZURE-WAF-SECURITY` | Azure Well-Architected — Security pillar | ms.date 14/07/2025 |
| `AZURE-WAF-SECURITY-CHECKLIST` | Security design review checklist | ms.date 14/11/2023 |
| `GCP-ENTERPRISE-FOUNDATIONS` | Enterprise foundations blueprint (antes *security foundations blueprint*) | Data não exibida; conteúdo conferido na versão Markdown oficial |
| `CSA-GUIDANCE-V5` | Security Guidance v5 | 15/07/2024, atualizada em 26/08/2025 |

## Relevância

Os três provedores publicam orientações com formas diferentes — **áreas** de boas práticas (AWS), **princípios e checklist** (Azure) e **blueprint implantável** (Google Cloud). Compará-las ensina ao arquiteto o que é comum (e, portanto, conceitual ou lógico) e o que é específico (físico). A Security Guidance da CSA oferece o eixo neutro de provedor.

## Comparação estrutural

| Tema | AWS — áreas do Security Pillar | Azure — checklist | Google Cloud — blueprint | CSA v5 — domínios |
|:---|:---|:---|:---|:---|
| Fundação e governança | Security foundations | SE:01 baseline | Organização e hierarquia por ambiente; políticas como código | Cloud Governance; Organization Management |
| Identidade | Identity and access management | SE:05 IAM | Grupos sincronizados do IdP via Cloud Identity, por função | Identity and Access Management |
| Rede e segmentação | Infrastructure protection | SE:04 segmentação; SE:06 tráfego | Shared VPC, caminhos privados, internet bloqueada por padrão | Infrastructure and Networking |
| Dados | Data protection | SE:03 classificação; SE:07 criptografia; SE:09 segredos | Projetos centrais para Secret Manager e Cloud KMS | Data Security |
| Detecção | Detection | SE:10 monitoramento | Security Command Center; log sinks agregados | Security Monitoring |
| Resposta | Incident response | SE:12 resposta a incidentes | Integração com o SOC existente | Incident Response and Resilience |
| Aplicações | Application security | SE:02 SDL; SE:08 hardening; SE:11 testes | Pipeline de CI/CD com validação antes da implantação | Application Security; Cloud Workload Security |

## Conceitos fundamentais

**O que é comum é decisão lógica.** Todos os documentos convergem em: hierarquia de recursos que separa ambientes, identidade centralizada no IdP corporativo, segmentação com caminhos privados, logs agregados fora do alcance de quem opera o workload, guardrails preventivos e detecção central. Essas são as decisões que a Academy trata na visão lógica.

**Guardrails preventivos e detectivos.** O blueprint do Google Cloud explicita a dupla: políticas de organização bloqueiam configurações de alto risco *antes* de existirem; detecção central identifica o que escapar. A mesma dupla aparece com outros nomes nos demais provedores.

**Infraestrutura como código como controle.** No blueprint, a fundação é implantada por Terraform em modelo GitOps e as mudanças passam por pipeline com contas de serviço privilegiadas — a mudança de infraestrutura vira um fluxo revisável, como no Laboratório 02.

## Ambientes híbridos

Os documentos tratam conectividade com on-premises de forma diferente, mas todos assumem identidade sincronizada a partir do diretório corporativo e caminhos privados até o datacenter. Em uma arquitetura híbrida, o arquiteto define **uma** política lógica e verifica se cada realização física a atende.

## Arquitetura empresarial

Para uma organização multicloud, a comparação acima é o ponto de partida de um *padrão corporativo de landing zone*: requisitos lógicos comuns, com anexos por provedor.

## Trade-offs

- Documentos de provedores refletem o portfólio do provedor; não são neutros.
- Blueprints implantáveis geram custo e pressupõem maturidade de engenharia que nem toda organização tem.
- Datas diferem bastante (checklist do Azure de 2023; pilar AWS de 2024); conferir a versão antes de citar detalhes.

## Aplicação educacional

- **M09–M11:** tabela comparativa acima como exercício — o estudante preenche a coluna de um quarto ambiente (on-premises).
- **M11:** padrão corporativo de landing zone multicloud com anexos por provedor.
- **M16:** discussão sobre adotar referências de provedor integralmente *versus* proporcionalmente (já introduzida em M02-L05).

## Referências

- AWS. *Security Pillar — AWS Well-Architected Framework*. 06/11/2024. <https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html>; áreas em <https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-def.md>. Consultado em 2026-10-23.
- Microsoft. *Azure Well-Architected Framework — Security*. <https://learn.microsoft.com/en-us/azure/well-architected/security/> e checklist <https://learn.microsoft.com/en-us/azure/well-architected/security/checklist>. Consultado em 2026-10-23.
- Google Cloud. *Enterprise foundations blueprint*. <https://docs.cloud.google.com/architecture/blueprints/security-foundations>. Consultado em 2026-10-23.
- Cloud Security Alliance. *Security Guidance v5*. <https://cloudsecurityalliance.org/artifacts/security-guidance-v5>. Consultado em 2026-10-23.
