# 🚀 AWS Solutions Architect Portfolio

> **8 hands-on AWS projects** — from static website hosting to multi-region disaster recovery.  
> Built to demonstrate real-world cloud architecture skills for financial services & FinTech.

[![AWS](https://img.shields.io/badge/AWS-Solutions_Architect-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![ICAN](https://img.shields.io/badge/ICAN-Chartered_Accountant-003366?style=for-the-badge)](https://www.ican.org.ng/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 👋 About Me

I'm **Iyiola Olubankole** — a finance professional (ICAN finalist) transitioning into cloud architecture. I sit at the intersection of **finance and technology**, building cloud solutions that solve real problems for financial services organizations.

**Why this portfolio exists:**  
I believe the best way to learn AWS is to build. Each project here was architected, deployed, broken, fixed, and documented — not just studied from a textbook.

---

## 📊 Projects Overview

| # | Project | Difficulty | Key Services | Status |
|---|---------|-----------|--------------|--------|
| 1 | [Static Website Hosting](#project-1-static-website-hosting-with-cicd) | ⭐ | S3, CloudFront, Route 53, CodePipeline | ✅ |
| 2 | [Infrastructure as Code](#project-2-infrastructure-as-code) | ⭐⭐ | CloudFormation, VPC, EC2 | 🔲 |
| 3 | [Serverless REST API](#project-3-serverless-rest-api) | ⭐⭐ | API Gateway, Lambda, DynamoDB, Cognito | 🔲 |
| 4 | [Event-Driven Pipeline](#project-4-event-driven-image-processing) | ⭐⭐⭐ | S3, SQS, Lambda, SNS | 🔲 |
| 5 | [Highly Available Web App](#project-5-highly-available-web-application) | ⭐⭐⭐ | EC2, ALB, ASG, RDS Multi-AZ | 🔲 |
| 6 | [Data Lake & Analytics](#project-6-data-lake--analytics-platform) | ⭐⭐⭐⭐ | S3, Glue, Athena, QuickSight | 🔲 |
| 7 | [Microservices (ECS/EKS)](#project-7-microservices-on-ecseks) | ⭐⭐⭐⭐ | ECS Fargate, ECR, Cloud Map | 🔲 |
| 8 | [Multi-Region DR](#project-8-multi-region-disaster-recovery) | ⭐⭐⭐⭐⭐ | Route 53, S3 CRR, RDS Replicas | 🔲 |

> 🔲 = Not started | 🔨 = In progress | ✅ = Completed

---

## 🏗️ Project Details

### Project 1: Static Website Hosting with CI/CD
**Architecture:** GitHub → CodePipeline → S3 → CloudFront → Route 53 → Users

📁 [`/project-01-static-website`](./project-01-static-website)

**What I built:** A static website hosted on S3 with CloudFront CDN, custom domain via Route 53, HTTPS via ACM, and automated deployments via CodePipeline.

**Finance analogy:** CI/CD is the "continuous audit" of software — catching errors in real-time vs. year-end audits.

---

### Project 2: Infrastructure as Code
**Architecture:** CloudFormation Template → Stack → VPC + Subnets + EC2 + Gateways

📁 [`/project-02-infrastructure-as-code`](./project-02-infrastructure-as-code)

**What I built:** A complete VPC with public/private subnets, NAT Gateway, Internet Gateway, Security Groups, and EC2 — all defined in CloudFormation YAML.

**Finance analogy:** IaC is double-entry bookkeeping for cloud — every resource declared (debited), every deletion tracked (credited).

---

### Project 3: Serverless REST API
**Architecture:** Client → API Gateway → Lambda → DynamoDB | Cognito Auth

📁 [`/project-03-serverless-api`](./project-03-serverless-api)

**What I built:** A fully serverless CRUD API with authentication, monitoring, and distributed tracing. Zero servers to manage.

**Finance analogy:** Lambda is variable costing — you only pay per invocation. EC2 is fixed costing — you pay regardless of usage.

---

### Project 4: Event-Driven Image Processing
**Architecture:** Upload → S3 → SQS → Lambda → S3 (processed) + DynamoDB + SNS

📁 [`/project-04-event-driven-pipeline`](./project-04-event-driven-pipeline)

**What I built:** A decoupled image processing pipeline with buffering (SQS), error handling (DLQ), notifications (SNS), and lifecycle management (Glacier archival).

**Finance analogy:** Dead Letter Queues are like suspense accounts — holding failed transactions until they can be investigated and resolved.

---

### Project 5: Highly Available Web Application
**Architecture:** Route 53 → WAF → ALB (Multi-AZ) → ASG → RDS Multi-AZ + ElastiCache

📁 [`/project-05-ha-web-app`](./project-05-ha-web-app)

**What I built:** A production-grade, multi-AZ web application with auto-scaling, database replication, caching, and security (WAF).

**Finance analogy:** Auto Scaling matches costs to revenue cycles — just like CVP analysis aligns spending with activity levels.

---

### Project 6: Data Lake & Analytics Platform
**Architecture:** Sources → S3 (Raw) → Glue ETL → S3 (Curated) → Athena → QuickSight

📁 [`/project-06-data-lake`](./project-06-data-lake)

**What I built:** A complete data lake with the medallion pattern (raw/staged/curated), automated schema discovery, serverless SQL queries, and BI dashboards.

**Finance analogy:** Glue ETL is like financial statement preparation — raw transactions are transformed through trial balance into meaningful financial reports.

---

### Project 7: Microservices on ECS/EKS
**Architecture:** Route 53 → ALB (path-based) → ECS Fargate Services → Databases

📁 [`/project-07-microservices`](./project-07-microservices)

**What I built:** Three containerized microservices with independent scaling, CI/CD, service discovery, and observability.

**Finance analogy:** Each microservice is a profit center — owning its own data, budget, and P&L. Independence with accountability.

---

### Project 8: Multi-Region Disaster Recovery
**Architecture:** Route 53 (Failover) → Primary (us-east-1) ↔ Secondary (eu-west-1)

📁 [`/project-08-multi-region-dr`](./project-08-multi-region-dr)

**What I built:** A multi-region architecture with S3 Cross-Region Replication, RDS Read Replicas, DynamoDB Global Tables, and automated failover.

**Finance analogy:** DR is like portfolio diversification — never put all your infrastructure in one region, just as you never put all investments in one asset class.

---

## 🛠️ Technologies & Services Used

### Compute
`EC2` `Lambda` `ECS Fargate` `EKS`

### Storage
`S3` `S3 Glacier` `EBS`

### Database
`RDS (PostgreSQL)` `DynamoDB` `ElastiCache (Redis)`

### Networking
`VPC` `Route 53` `CloudFront` `ALB/NLB` `API Gateway`

### Security
`IAM` `Cognito` `WAF` `ACM` `Security Groups` `NACLs`

### DevOps & Monitoring
`CloudFormation` `CodePipeline` `CloudWatch` `X-Ray`

### Analytics
`Glue ETL` `Athena` `QuickSight` `Kinesis`

### Integration
`SQS` `SNS` `EventBridge`

---

## 🎓 Certifications

| Certification | Status |
|--------------|--------|
| AWS Cloud Practitioner | ✅ Passed |
| AWS Solutions Architect Associate | 📖 Preparing (retake) |
| ICAN (Chartered Accountant) | 📖 Final stage |

---

## 💡 What Makes This Portfolio Different

Most cloud portfolios follow tutorials step-by-step. This one is different:

1. **Finance context** — Each project connects to real accounting/finance concepts (ICAN syllabus)
2. **Triple-pass approach** — Console → CLI → IaC for every project
3. **Break-and-fix documented** — I intentionally broke things to understand failure modes
4. **Architecture decisions explained** — Not just *what* I built, but *why* I chose this approach
5. **Cost-aware** — Every project includes cost analysis and optimization considerations

---

## 📬 Connect With Me

- 🔗 [LinkedIn](https://linkedin.com/in/YOUR-LINKEDIN)
- 📧 bankytuase@gmail.com
- 🌐 [Portfolio Website](#) *(Project 1 — coming soon)*

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ☁️ and 📊 — where cloud architecture meets financial expertise.*
