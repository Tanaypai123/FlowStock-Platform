# FlowStock — Consolidated Semester Project Report

**Project Title:** FlowStock — Multi-Tenant B2B Inventory Management & Logistics SaaS Platform  
**Academic Institution:** Swami Keshvanand Institute of Technology, Management & Gramothan, Jaipur (SKIT)  
**Department:** Department of Computer Science & Engineering  
**Academic Period:** August 2026 – November 2026 (Semester VII)  
**Engineering Team:** Tanay Sharma, Sara Dingra, Vijay Kumar Soni  

---

## 1. Executive Summary

Modern wholesale distributors, regional supply chain hubs, and B2B manufacturers in India face significant operational hurdles when relying on disconnected tools for inventory management, order lifecycles, and fleet dispatching. Traditional enterprise software solutions are either cost-prohibitive, lack native multi-tenancy, or fail to account for local logistics realities (such as unstructured address formats, phone-based field driver workflows, and WhatsApp communication channels).

**FlowStock** was engineered to solve this challenge through a multi-tenant, cloud-native Software-as-a-Service (SaaS) architecture. Over a 13-week structured development cycle, the team designed, implemented, tested, and hardened a production-ready monorepo platform comprising:
- An isolated multi-tenant data architecture serving four user roles (Admin, Customer, Driver, Super Admin).
- A unified single-page application built on React 19, Vite, and Tailwind CSS.
- A high-throughput Node.js ESM REST API server utilizing Supabase PostgreSQL and Supabase Storage.
- Intelligent multi-stop logistics route optimization with three-tier fallback capabilities.
- Automated customer notification pipelines integrated with Twilio WhatsApp API.
- End-to-end delivery fraud prevention with 4-digit OTP customer handovers.

---

## 2. Project Architecture & System Overview

```
                                      ┌────────────────────────┐
                                      │   DNS / CLIENT (SPA)   │
                                      │ React 19 + Tailwind CSS │
                                      └───────────┬────────────┘
                                                  │ HTTPS / REST (x-business-id)
                                                  ▼
                                      ┌────────────────────────┐
                                      │   EXPRESS REST SERVER  │
                                      │ 11 Modules / Middleware│
                                      └───────────┬────────────┘
                                                  │
                 ┌────────────────────────────────┼──────────────────────────────┐
                 │                                │                              │
                 ▼                                ▼                              ▼
    ┌──────────────────────────┐     ┌─────────────────────────┐    ┌─────────────────────────┐
    │   SUPABASE POSTGRESQL    │     │    SUPABASE STORAGE     │    │   EXTERNAL CLOUD APIS   │
    │  - 14 Normalized Tables  │     │  - business-logos       │    │  - Twilio WhatsApp      │
    │  - Row Level Security    │     │  - product-images       │    │  - Google Maps Direct.  │
    │  - 34 Migration Scripts  │     │  - complaint-images     │    │  - OpenRouteService     │
    │  - Cascade Constraints   │     │  - bug-screenshots     │    │  - PDFKit Engine        │
    └──────────────────────────┘     └─────────────────────────┘    └─────────────────────────┘
```

---

## 3. 13-Week Semester Development Roadmap

The development trajectory adhered to structured incremental sprints across the semester:

```
AUG 14      AUG 22      AUG 29      SEP 04      SEP 11      SEP 18      SEP 25
  W1          W2          W3          W4          W5          W6          W7
  │           │           │           │           │           │           │
  ▼           ▼           ▼           ▼           ▼           ▼           ▼
Monorepo     OAuth       Multi-     Inventory   Customer      Order      Driver
Foundations & Supabase   Tenancy    Catalog &   Storefront  Lifecycle   Phone Auth
& Schema     JWT Auth    Schemas    Stages      & Cart      Engine      & Sessions
─────────────────────────────────────────────────────────────────────────────────
OCT 02      OCT 16      OCT 23      OCT 30      NOV 05      NOV 12
  W8          W9          W10         W11         W12         W13
  │           │           │           │           │           │
  ▼           ▼           ▼           ▼           ▼           ▼
Delivery    3-Tier      Disputes    PDFKit      System      Customer Boost,
OTP Hand-   Route Opt.  & Photo     Invoices &  Telemetry   CI/CD Pipeline &
over & Deduct & WhatsApp  Proof      Dev Console & Bug Modal Final Audit
```

---

## 4. Consolidated Contribution Breakdown

Individual contribution percentages across the semester reflect domain ownership and technical responsibilities:

| Team Member | Domain Specialization | Overall Share | Key Milestone Deliverables |
|---|---|:---:|---|
| **Tanay Sharma** | Full Stack Lead & Backend Systems | **39.2%** | Express REST server, JWT/Driver authentication, 3-tier route optimizer, Twilio WhatsApp integration, PDFKit engine. |
| **Vijay Kumar Soni** | Frontend Architect & Database Specialist | **33.1%** | React 19 SPA routing, operational dashboards, Recharts analytics, 14 database tables, 34 SQL migrations. |
| **Sara Dingra** | UI/UX Designer & Quality Assurance Lead | **27.7%** | Visual design system, responsive UI across all 4 portals, comprehensive QA test matrices, BugReportModal system. |

---

## 5. Security & Multi-Tenancy Architecture

1. **Cryptographic JWT & Token Auth:** Google OAuth JWTs are validated via `supabaseAnon.auth.getUser()`. Driver sessions use 64-character crypto-random tokens with 30-day expiries.
2. **Tenant Isolation:** Multi-tenancy is enforced at the database level (`user_businesses`) and validated at the Express middleware layer (`resolveBusinessId`). Requests cannot read or modify data outside their active tenant.
3. **Role-Based Guards:** `requireAdmin` checks `profiles.role = 'admin'`; `superAdminOnly` prevents role enumeration by returning uniform `403 Forbidden` responses.
4. **Environment Isolation:** Secrets, service-role keys, and tokens are isolated in local `.env` files protected by strict `.gitignore` rules.

---

## 6. Project Verification & Academic Sign-off

The FlowStock monorepo has undergone full static code analysis, dependency validation, client bundling via Vite, and end-to-end integration tests.

**Approved by:**

```
____________________________            ____________________________
Tanay Sharma                            Sara Dingra
(Full Stack Lead)                       (UI/UX & QA Lead)

____________________________            ____________________________
Vijay Kumar Soni                        Project Mentor / Guide
(Frontend & DB Specialist)              Department of CSE, SKIT
```
