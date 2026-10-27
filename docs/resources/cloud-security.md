---
title: Cloud security
description: Documentação oficial de segurança da AWS, Microsoft Azure e Google Cloud e a Security Guidance da Cloud Security Alliance, com versão e conceitos.
---

# Cloud security

Documentos de provedores refletem o portfólio de cada provedor; a Security Guidance da CSA oferece o eixo neutro. A comparação entre eles está na [nota sobre fundações cloud](notes/cloud-foundations.md).

<!-- cloud:start -->

## Cloud Security

### Creating a trail for an organization — AWS CloudTrail User Guide

`AWS-CLOUDTRAIL-ORG-TRAIL` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

Página lida em 2026-10-23: criada pela conta de gerenciamento ou administrador delegado; contas-membro veem mas não alteram nem excluem; logs em bucket central organizado por conta.

Módulos: M09, M11, M15 · Leitura: Consulta (prioridade 2).

### What is AWS Config?

`AWS-CONFIG` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)

Página lida em 2026-10-23.

Módulos: M09, M11 · Leitura: Consulta (prioridade 3).

### What is AWS Control Tower?

`AWS-CONTROL-TOWER` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)

Página lida em 2026-10-23: orquestra Organizations, Service Catalog e IAM Identity Center; landing zone como ambiente multi-conta baseado em boas práticas; controles preventivos, detectivos e proativos; categorias mandatory, strongly recommended e elective; Account Factory.

Módulos: M09 · Leitura: Consulta (prioridade 3).

### Building a Data Perimeter on AWS

`AWS-DATA-PERIMETER` · AWS · Whitepaper, 13/06/2023 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html)

Introdução lida em 2026-10-23: o acesso só deve ser permitido se a identidade for confiável, o recurso for confiável e a rede for esperada. As seções sobre políticas e chaves de condição não foram lidas.

Módulos: M09, M13 · Leitura: Aprofundada (prioridade 3).

### Disaster Recovery of Workloads on AWS: Recovery in the Cloud

`AWS-DR-WHITEPAPER` · AWS · Whitepaper online (AWS Well-Architected); data de revisão não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

Seção 'Disaster recovery options in the cloud' lida em 2026-10-23: caracterização qualitativa de RPO e RTO das quatro estratégias; replicação contínua pode não proteger contra corrupção ou exclusão maliciosa, exigindo backups pontuais ou versionamento; a recuperação de corrupção sempre tem RPO maior que zero.

Módulos: M03, M09, M12 · Leitura: Consulta (prioridade 2).

### What is Amazon GuardDuty?

`AWS-GUARDDUTY` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

Página lida em 2026-10-23: fontes fundamentais (eventos de gerenciamento do CloudTrail, VPC flow logs, DNS); planos de proteção (AI, S3, EKS, Runtime Monitoring, Malware Protection, RDS, Lambda); gestão multi-conta via Organizations.

Módulos: M09, M15 · Leitura: Consulta (prioridade 3).

### What is Amazon Inspector?

`AWS-INSPECTOR` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)

Página lida em 2026-10-23: descoberta e varredura contínua; ajuste da pontuação CVSS do NVD ao ambiente (por exemplo, sem caminho de rede para a internet).

Módulos: M09, M14 · Leitura: Consulta (prioridade 3).

### About the migration strategies (7 Rs) — AWS Prescriptive Guidance, Large migration guide

`AWS-MIGRATION-7RS` · AWS · Documentação online · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html)

Página lida em 2026-10-23: definições e casos de uso das sete estratégias; recomendação de modernizar depois da migração em grandes migrações; retire inclui reduzir riscos de componentes sem suporte.

Módulos: M08, M09, M11 · Leitura: Consulta (prioridade 3).

### Resource control policies (RCPs) — AWS Organizations User Guide

`AWS-ORG-RCP` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html)

Página lida em 2026-10-23: RCPs nunca concedem permissões; afetam principais de dentro e de fora da organização, inclusive root; não afetam a conta de gerenciamento, service-linked roles nem chaves KMS gerenciadas pela AWS; lista limitada de serviços (S3, STS, KMS, SQS, Secrets Manager, entre outros); AWS recomenda testar antes de anexar à raiz.

Módulos: M09 · Leitura: Consulta (prioridade 3).

### Service control policies (SCPs) — AWS Organizations User Guide

`AWS-ORG-SCP` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

Página lida em 2026-10-23: SCPs definem o máximo de permissões e não concedem permissões; não afetam a conta de gerenciamento nem service-linked roles; permissões efetivas são a interseção entre SCPs, RCPs e políticas de identidade e de recurso.

Módulos: M09 · Leitura: Consulta (prioridade 2).

### What is AWS Security Hub CSPM?

`AWS-SECURITY-HUB-CSPM` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)

Página lida em 2026-10-23: padrões e controles; maioria dos controles depende do AWS Config; formato ASFF; recebe achados de GuardDuty, Inspector e Macie.

Módulos: M09, M11 · Leitura: Consulta (prioridade 3).

### AWS Security Hub now generally available with near real-time analytics and risk prioritization

`AWS-SECURITY-HUB-GA-2025` · AWS News Blog · 02/12/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://aws.amazon.com/blogs/aws/aws-security-hub-now-generally-available-with-near-real-time-analytics-and-risk-prioritization/)

Post lido em 2026-10-23: correlaciona GuardDuty, Inspector, Macie e Security Hub CSPM; exposições em tempo quase real; aba de caminho de ataque potencial; achados em OCSF.

Módulos: M09, M11, M14 · Leitura: Consulta (prioridade 3).

### What is Amazon Security Lake?

`AWS-SECURITY-LAKE` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html)

Página lida em 2026-10-23: dados ficam em buckets S3 da conta do cliente; fontes nativas (CloudTrail, EKS audit, Route 53 Resolver query logs, Security Hub CSPM, VPC Flow Logs, WAF); fontes personalizadas; regiões de consolidação (rollup) para requisitos de residência.

Módulos: M09, M11, M15 · Leitura: Consulta (prioridade 3).

### Security Pillar — AWS Well-Architected Framework

`AWS-SECURITY-PILLAR` · AWS · 6 de novembro de 2024 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

**Conceitos:** Shared Responsibility Model; Sete áreas: Security foundations, Identity and access management, Detection, Infrastructure protection, Data protection, Incident response, Application security.

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Área | Security foundations | M09 | **Lido** |
| Área | Identity and access management | M09 | **Lido** |
| Área | Detection | M09 | **Lido** |
| Área | Infrastructure protection | M09 | **Lido** |
| Área | Data protection | M09 | **Lido** |
| Área | Incident response | M09 | **Lido** |
| Área | Application security | M09 | **Lido** |

Whitepaper datado de 06/11/2024; as sete áreas de boas práticas conferidas na página 'Definition' (sec-def) do framework.

Módulos: M09, M11, M16 · Leitura: Essencial (prioridade 1).

### Shared Responsibility Model

`AWS-SHARED-RESPONSIBILITY` · AWS · Página online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://aws.amazon.com/compliance/shared-responsibility-model/)

Página lida em 2026-10-23: AWS protege a infraestrutura (hardware, software, rede, instalações); a responsabilidade do cliente depende dos serviços escolhidos; EC2 exige gestão do sistema convidado; em serviços abstraídos (S3, DynamoDB) o cliente gerencia dados, cifragem, classificação e permissões; controles herdados (físicos), compartilhados (patch, configuração, treinamento) e específicos do cliente (proteção de serviços e comunicações, zoneamento).

Módulos: M09, M11 · Leitura: Essencial (prioridade 1).

### AWS Security Reference Architecture (AWS SRA)

`AWS-SRA` · AWS · Setembro de 2023 — documento vivo · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Architecture | AWS SRA — contas e OUs (Org Management; Security OU: Security Tooling e Log Archive; Infrastructure OU: Network e Shared Services; Workloads OU: Application) | M09, M11 | **Lido** |
| Security Tooling account | Serviços administrados por delegação a partir da conta Security Tooling | M09 | **Lido** |

Publicado em setembro de 2023; documento vivo com histórico de revisões. Em 2026-10-23 foram lidas a página de boas-vindas (referência a adaptar, documento vivo), a de arquitetura e a da conta Security Tooling (administrador delegado de CloudTrail, Security Hub e Security Hub CSPM, GuardDuty, Config, Macie, Access Analyzer, Inspector, Detective, Firewall Manager, Audit Manager; exceções: Security Lake na Log Archive e IAM Identity Center na Shared Services).

Módulos: M02, M09, M11 · Leitura: Consulta (prioridade 3).

### Free digital training: Security (AWS Skill Builder)

`AWS-TRAINING-SECURITY` · AWS · Página viva — data de atualização não exibida · Gratuito com cadastro · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://training.resources.awscloud.com/get-certified-security-specialty/free-digital-training-security)

Cinco cursos gratuitos listados.

Módulos: M09 · Leitura: Consulta (prioridade 3).

### Control access to VPC endpoints using endpoint policies — AWS PrivateLink

`AWS-VPC-ENDPOINT-POLICIES` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html)

Página lida em 2026-10-23: política baseada em recurso que controla quais principais usam o endpoint; não substitui políticas de identidade ou de recurso; política padrão concede acesso total.

Módulos: M09 · Leitura: Consulta (prioridade 3).

### Infrastructure security in Amazon VPC — Amazon VPC User Guide

`AWS-VPC-INFRA-SECURITY` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)

Página lida em 2026-10-23: security groups no nível da instância, só regras de permissão, avaliação de todas as regras, stateful; NACLs no nível da sub-rede, permissão e negação, avaliação em ordem, stateless; security groups como mecanismo principal; PrivateLink para acessar serviços por IPs privados.

Módulos: M09 · Leitura: Consulta (prioridade 2).

### AWS Well-Architected Framework — Security Pillar (design principles)

`AWS-WA-SECURITY-DESIGN` · AWS · Página viva — data de atualização não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html)

Página lida em 2026-10-23: sete princípios — identidade forte, rastreabilidade, segurança em todas as camadas, automação de boas práticas, proteção de dados em trânsito e em repouso, manter pessoas longe dos dados, preparação para eventos de segurança. Data de atualização não exibida.

Módulos: M02, M09, M11 · Leitura: Consulta (prioridade 3).

### Azure Architecture Center — Security

`AZURE-ARCH-SECURITY` · Microsoft · Leitura online gratuita · redistribuição: não verificada · **Indisponível** · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/architecture/security/)

URL indicada no prompt de pesquisa; fora da lista de acesso do ambiente de verificação em 2026-10-23. Não citar até conferir.

Módulos: M10, M11 · Leitura: Consulta (prioridade 3).

### What is an Azure landing zone? — Cloud Adoption Framework

`AZURE-LANDING-ZONE` · Microsoft · Atualizado em 01/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

Página lida em 2026-10-23: arquitetura para governar, proteger e escalar ambiente multi-assinatura; uma platform landing zone por tenant Entra na maioria dos casos; workload landing zones com assinaturas por ambiente; políticas herdadas pela hierarquia; aceleradores de IaC; centralizar só o que traz benefício claro.

Módulos: M10 · Leitura: Essencial (prioridade 1).

### Azure landing zone design areas — Cloud Adoption Framework

`AZURE-LZ-DESIGN-AREAS` · Microsoft · Atualizado em 19/12/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-areas)

Página lida em 2026-10-23.

Módulos: M10 · Leitura: Consulta (prioridade 3).

### Management groups — Azure landing zone design area (resource organization)

`AZURE-LZ-MANAGEMENT-GROUPS` · Microsoft · Atualizado em 19/12/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-management-groups)

Página lida em 2026-10-23: intermediate root; Platform (Identity, Management, Connectivity, Security); Landing zones (Corp, Online, Local); Sandboxes; Decommissioned; hierarquia rasa (três a quatro níveis); não criar management groups por ambiente nem por região; não dar RBAC a times de workload em escopo de management group; management group padrão para novas assinaturas; limitar políticas na raiz.

Módulos: M10, M16 · Leitura: Consulta (prioridade 2).

### Azure Policy definitions effect basics

`AZURE-POLICY-EFFECTS` · Microsoft · Atualizado em 04/03/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics)

Página lida em 2026-10-23: efeitos addToNetworkGroup, append, audit, auditIfNotExists, deny, denyAction, deployIfNotExists, disabled, manual, modify, mutate; ordem: disabled, append e modify, deny, audit, manual, auditIfNotExists, denyAction; auditIfNotExists e deployIfNotExists avaliados após a requisição.

Módulos: M10 · Leitura: Consulta (prioridade 3).

### What is Azure Resource Graph?

`AZURE-RESOURCE-GRAPH` · Microsoft · Atualizado em 19/08/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/governance/resource-graph/overview)

Página lida em 2026-10-23.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### Arquitetura de segurança no Azure — introdução (pt-BR)

`AZURE-SECURITY-ARCH-PTBR` · Microsoft · Leitura online gratuita · redistribuição: não verificada · **Pendente** · [abrir fonte oficial](https://learn.microsoft.com/pt-br/azure/architecture/security/security-get-started)

URL fornecida no currículo; não aberta no ambiente de verificação.

Módulos: M10 · Leitura: Consulta (prioridade 3).

### Azure Well-Architected Framework pillars

`AZURE-WAF-PILLARS` · Microsoft · Atualizado em 22/01/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/azure/well-architected/pillars)

Atualizado em 22/01/2025.

Módulos: M10 · Leitura: Consulta (prioridade 3).

### Azure Well-Architected Framework — Security pillar

`AZURE-WAF-SECURITY` · Microsoft · ms.date 14/07/2025 (metadado de atualização 19/03/2026) · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/well-architected/security/)

**Conceitos:** Princípios: Plan your security readiness; Design to protect confidentiality; integrity; availability; Sustain and evolve your security posture.

Página lida em 2026-10-23 (ms.date 14/07/2025, atualizada em 19/03/2026): cinco princípios — plan your security readiness; design to protect confidentiality; design to protect integrity; design to protect availability; sustain and evolve your security posture.

Módulos: M10, M11, M16 · Leitura: Essencial (prioridade 1).

### Azure Well-Architected — Security design review checklist

`AZURE-WAF-SECURITY-CHECKLIST` · Microsoft · ms.date 14/11/2023 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/well-architected/security/checklist)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| SE:01 | Establish a security baseline | — | **Lido** |
| SE:02 | Align secure development lifecycle (SDL) | — | **Lido** |
| SE:03 | Classify and label data | — | **Lido** |
| SE:04 | Create intentional segmentation and perimeters | — | **Lido** |
| SE:05 | Implement strict identity and access management (IAM) | — | **Lido** |
| SE:06 | Isolate, filter, and control network traffic | — | **Lido** |
| SE:07 | Encrypt data with modern standards | — | **Lido** |
| SE:08 | Harden all workload components | — | **Lido** |
| SE:09 | Protect application secrets | — | **Lido** |
| SE:10 | Implement a holistic monitoring strategy | — | **Lido** |
| SE:11 | Establish a comprehensive testing regimen | — | **Lido** |
| SE:12 | Define and test incident response procedures | — | **Lido** |

Doze recomendações SE:01–SE:12 conferidas.

Módulos: M10, M11, M16 · Leitura: Exercícios (prioridade 2).

### Security Guidance for Critical Areas of Focus in Cloud Computing v5

`CSA-GUIDANCE-V5` · Cloud Security Alliance · v5 (15/07/2024; atualizado em 26/08/2025) · Gratuito com cadastro · redistribuição: restrita · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://cloudsecurityalliance.org/artifacts/security-guidance-v5)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Domínio 1 | Cloud Computing Concepts and Architectures | — | Localizado |
| Domínio 2 | Cloud Governance | — | Localizado |
| Domínio 3 | Risk, Audit, and Compliance | — | Localizado |
| Domínio 4 | Organization Management | — | Localizado |
| Domínio 5 | Identity and Access Management | — | Localizado |
| Domínio 6 | Security Monitoring | — | Localizado |
| Domínio 7 | Infrastructure and Networking | — | Localizado |
| Domínio 8 | Cloud Workload Security | — | Localizado |
| Domínio 9 | Data Security | — | Localizado |
| Domínio 10 | Application Security | — | Localizado |
| Domínio 11 | Incident Response and Resilience | — | Localizado |
| Domínio 12 | Related Technologies and Strategies | — | Localizado |

Página conferida: 12 domínios (numeração pela ordem da lista), opções de Login e Create Account para download; rodapé 'All rights reserved'. Condições exatas de download não exibidas.

Módulos: M09, M10, M11 · Leitura: Aprofundada (prioridade 2).

### Google Cloud Architecture Center

`GCP-ARCH-CENTER` · Google Cloud · Página viva — data de atualização não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/architecture/)

Página conferida: categorias 'Security and compliance' e 'Hybrid and multicloud'; cards 'Landing zone design', 'Enterprise foundations blueprint' e 'Google Cloud Well-Architected Framework'. Data não exibida.

Módulos: M10, M11 · Leitura: Consulta (prioridade 3).

### Architecture fundamentals

`GCP-ARCH-FUNDAMENTALS` · Google Cloud · Leitura online gratuita · redistribuição: não verificada · **Pendente** · [abrir fonte oficial](https://docs.cloud.google.com/architecture/fundamentals)

Localizada por busca; conteúdo não aberto.

Módulos: M10 · Leitura: Consulta (prioridade 3).

### Cloud Audit Logs overview

`GCP-AUDIT-LOGS` · Google Cloud · Atualizado em 22/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/logging/docs/audit)

Página lida em 2026-10-23: Admin Activity e System Event sempre gravados, não desabilitáveis; Data Access desabilitado por padrão exceto BigQuery; Policy Denied gerado por padrão; entradas imutáveis.

Módulos: M10, M15 · Leitura: Consulta (prioridade 3).

### Cloud Asset Inventory overview

`GCP-CLOUD-ASSET-INVENTORY` · Google Cloud · Atualizado em 20/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)

Página lida em 2026-10-23: não projetado para consulta em tempo real; eventualmente consistente.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### Enterprise foundations blueprint (formerly security foundations blueprint)

`GCP-ENTERPRISE-FOUNDATIONS` · Google Cloud · Página viva — data de atualização não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/architecture/blueprints/security-foundations)

**Conceitos:** Organização e hierarquia de recursos por ambiente; Grupos sincronizados do IdP via Cloud Identity; Shared VPC e caminhos privados; Organization Policy e policy-as-code; Log sinks agregados; Implantação via Terraform e GitOps.

Conteúdo conferido na versão Markdown da página (security-foundations.md.txt). Repositório de referência: github.com/terraform-google-modules/terraform-example-foundation. Data de atualização não exibida. Visão geral relida em 2026-10-23: organização com pastas por ambiente; IaC em Terraform com GitOps e Cloud Build; restrições organizacionais contra configurações de alto risco; sinks agregados de logs; Security Command Center; Shared VPC sem tráfego de/para internet por padrão; Cloud Identity sincronizado com o IdP; projetos centrais para Secret Manager e Cloud KMS.

Módulos: M10, M11, M16 · Leitura: Essencial (prioridade 1).

### Introduction to the Organization Policy Service

`GCP-ORG-POLICY` · Google Cloud · Atualizado em 22/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)

Página lida em 2026-10-23: restrições gerenciadas, personalizadas e legadas; política por organização, pasta ou projeto, herdada pelos descendentes; modo dry-run com registro sem bloqueio; aplicação normalmente não retroativa; exemplos de localização de recursos, contas de serviço e compartilhamento restrito por domínio.

Módulos: M10 · Leitura: Consulta (prioridade 2).

### Resource hierarchy — Resource Manager

`GCP-RESOURCE-HIERARCHY` · Google Cloud · Atualizado em 22/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)

Página lida em 2026-10-23: organização como raiz associada a uma conta Google Workspace ou Cloud Identity; pastas como sub-organizações; projeto como entidade fundamental; políticas de permissão, negação e organizacionais herdadas.

Módulos: M10 · Leitura: Essencial (prioridade 2).

### Security Command Center overview

`GCP-SCC-OVERVIEW` · Google Cloud · Atualizado em 22/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)

Página lida em 2026-10-23: níveis Standard, Premium e Enterprise; Enterprise descontinuado, com encerramento previsto para 21/05/2027 e migração para Premium; ativação por projeto ou organização; conectores para AWS e Azure listados no nível Enterprise; exportação para BigQuery e Pub/Sub.

Módulos: M10, M11 · Leitura: Consulta (prioridade 3).

### Well-Architected Framework: Security, privacy, and compliance pillar

`GCP-WAF-SECURITY` · Google Cloud · Atualizado em 13/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/architecture/framework/security)

Página lida em 2026-10-23 (revisada em 13/10/2026): sete princípios — security by design; zero trust; shift-left security; preemptive cyber defense; use AI securely and responsibly; use AI for security; meet regulatory, compliance, and privacy needs. Oito áreas de foco: infraestrutura, IAM, dados, IA e ML, SecOps, aplicações, governança/risco/conformidade, logs e monitoramento.

Módulos: M02, M10 · Leitura: Consulta (prioridade 3).

### Cloud Native Security and Kubernetes (Overview of Cloud Native Security)

`K8S-SECURITY-OVERVIEW` · The Kubernetes Authors · Página viva — modificada em 02/05/2025 (versão em espanhol) · Leitura online gratuita · redistribuição: não verificada · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://kubernetes.io/docs/concepts/security/overview/)

**Conceitos:** Camadas Cloud, Cluster, Container e Code.

Conferida a versão em espanhol da página: segurança pensada em camadas (Cloud, Clusters, Containers, Code) e o aviso de que o modelo é uma sugestão, não um teste de política. Recomendações por camada não lidas. A documentação Kubernetes é licenciada pelos autores sob CC BY 4.0 segundo o rodapé do site — não conferido nesta revisão.

Módulos: M00, M12 · Leitura: Consulta (prioridade 3).

### What is Microsoft Defender for Cloud?

`MS-DEFENDER-FOR-CLOUD` · Microsoft · Atualizado em 10/08/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)

Página lida em 2026-10-23: Foundational CSPM gratuito com secure score e conexão multicloud; Defender CSPM pago com attack path analysis, cloud security explorer e data security posture; planos para servidores, storage, bancos, contêineres, App Service, Key Vault, Resource Manager, APIs; conectores agentless para AWS e GCP; Microsoft cloud security benchmark aplicado a Azure, AWS e GCP.

Módulos: M10, M11 · Leitura: Consulta (prioridade 2).

### Microsoft Cybersecurity Reference Architectures (MCRA)

`MS-MCRA` · Microsoft · Abril de 2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/security/adoption/mcra)

Versão de abril de 2025, em PowerPoint.

Módulos: M02, M07, M10, M11 · Leitura: Consulta (prioridade 3).

### Study guide for Exam SC-100: Microsoft Cybersecurity Architect

`MS-SC100-GUIDE` · Microsoft · Habilidades atualizadas em 21/09/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/certifications/resources/study-guides/SC-100)

Página lida em 2026-10-23 (atualizada em 21/09/2026; habilidades vigentes a partir de 21/10/2026): quatro grupos — práticas e prioridades (20–25%); operações de segurança, identidade e conformidade (25–30%); infraestrutura (25–30%); aplicações e dados (20–25%). A versão em português costuma ser atualizada cerca de oito semanas depois.

Módulos: M10, M11, M16 · Leitura: Consulta (prioridade 3).

### SC-100: Design solutions that align with security best practices and priorities (learning path)

`MS-SC100-PATH` · Microsoft · Leitura online gratuita · redistribuição: não verificada · **Pendente** · [abrir fonte oficial](https://learn.microsoft.com/en-us/training/paths/sc-100-design-solutions-best-practices-priorities/)

Localizada por busca; conteúdo não aberto.

Módulos: M02, M10 · Leitura: Consulta (prioridade 3).

### What is a cloud-native application protection platform (CNAPP)?

`MS-WHAT-IS-CNAPP` · Microsoft · Página Security 101; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.microsoft.com/en-us/security/business/security-101/what-is-cnapp)

Página lida em 2026-10-23. Texto de fornecedor; definições de mercado podem variar.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### SP 800-145 — The NIST Definition of Cloud Computing

`NIST-SP800-145` · NIST · Final (28/09/2011) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/145/final)

**Conceitos:** Cinco características essenciais; SaaS, PaaS e IaaS; Nuvem privada, comunitária, pública e híbrida.

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| §2 (p. 2–3) | The NIST Definition of Cloud Computing (características, modelos de serviço e de implantação) | M00 | **Lido** |

Página oficial e PDF conferidos: as cinco características (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service), os três modelos de serviço e os quatro de implantação estão na seção 2, pp. 2–3. Documento curto e ainda sem revisão.

Módulos: M00, M09, M10, M11 · Leitura: Essencial (prioridade 1).

## Hybrid & Multicloud Architecture

### Encryption in transit in AWS Direct Connect

`AWS-DX-ENCRYPTION` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html)

Página lida em 2026-10-23.

Módulos: M09, M11 · Leitura: Consulta (prioridade 3).

### What is Route 53 VPC Resolver?

`AWS-ROUTE53-RESOLVER` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)

Página lida em 2026-10-23: o serviço passou a se chamar Route 53 VPC Resolver; endpoints de entrada recebem consultas da rede on-premises; endpoints de saída encaminham consultas para resolvedores on-premises; regras por domínio, compartilháveis entre contas.

Módulos: M09, M11 · Leitura: Consulta (prioridade 3).

### What is AWS Site-to-Site VPN?

`AWS-SITE-TO-SITE-VPN` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

Página lida em 2026-10-23: IPsec com IKEv2; dois túneis por conexão para alta disponibilidade; terminação em virtual private gateway (uma VPC) ou transit gateway; recomendação de CIDRs não sobrepostos.

Módulos: M09, M11 · Leitura: Consulta (prioridade 3).

### Azure Arc overview

`AZURE-ARC-OVERVIEW` · Microsoft · Atualizado em 26/08/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/azure-arc/overview)

Página lida em 2026-10-23: governança e gestão consistentes para recursos fora do Azure; Azure Policy, RBAC, tags e management groups; serviços como Defender for Cloud e Azure Monitor cobrados conforme o serviço.

Módulos: M10, M11 · Leitura: Consulta (prioridade 3).

### What is Azure DNS Private Resolver?

`AZURE-DNS-PRIVATE-RESOLVER` · Microsoft · Atualizado em 22/06/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview)

Página lida em 2026-10-23: inbound endpoint como destino do encaminhamento condicional on-premises; outbound endpoint com rulesets de até 1.000 regras; ordem de avaliação (servidores DNS personalizados, zonas privadas vinculadas, regras de encaminhamento; sufixo mais longo vence); exige ExpressRoute ou VPN para resolução híbrida.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### About encryption for Azure ExpressRoute

`AZURE-ER-ENCRYPTION` · Microsoft · Atualizado em 03/02/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-about-encryption)

Página lida em 2026-10-23: por padrão o tráfego não é cifrado; MACsec só no ExpressRoute Direct, desabilitado por padrão, com chave do cliente no Key Vault e sem fallback para tráfego em claro; IPsec fim a fim com VPN gateway sobre private peering; podem ser usados juntos.

Módulos: M11 · Leitura: Consulta (prioridade 2).

### What is Azure ExpressRoute?

`AZURE-EXPRESSROUTE` · Microsoft · Atualizado em 27/08/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

Página lida em 2026-10-23: não trafega pela internet pública; cada circuito tem duas conexões a dois roteadores de borda da Microsoft com BGP duplo; para máxima resiliência, dois circuitos em dois locais de peering; ExpressRoute Direct; Global Reach.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### Best practices for Cloud DNS

`GCP-CLOUD-DNS-BEST-PRACTICES` · Google Cloud · Atualizado em 20/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/dns/docs/best-practices)

Página lida em 2026-10-23: evitar compartilhar o mesmo domínio entre nuvem e on-premises (usar subdomínios distintos); zona de encaminhamento preferida a servidor alternativo; uma única VPC para encaminhamento de saída; consultas encaminhadas a partir de 35.199.192.0/19, que deve ser liberado e anunciado; peering de DNS unidirecional.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### Choosing a Network Connectivity product — Google Cloud

`GCP-CONNECTIVITY-CHOOSE` · Google Cloud · Atualizado em 13/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product)

Página lida em 2026-10-23: HA VPN com SLA de 99,99% ou 99,9% conforme topologia; Dedicated Interconnect de 10, 100 ou 400 Gbps; Partner Interconnect; Cross-Cloud Interconnect para AWS, Azure, OCI e Alibaba com duas conexões para o SLA; HA VPN sobre Cloud Interconnect para cifrar; com Partner Interconnect é preciso acrescentar IPsec.

Módulos: M11 · Leitura: Consulta (prioridade 3).

<!-- cloud:end -->
