# FlowStock — Engineering Team Charter & Organization

## Institution & Department
- **Institution:** Swami Keshvanand Institute of Technology, Management & Gramothan, Jaipur (SKIT)
- **Department:** Department of Computer Science & Engineering
- **Project:** FlowStock — B2B Inventory Management & Logistics SaaS Platform
- **Academic Year:** 2026

---

## 1. Team Roster & Roles

```
                      ┌──────────────────────────────────────────────┐
                      │                 FLOWSTOCK                    │
                      │         Core Engineering Collective          │
                      └──────────────────────┬───────────────────────┘
                                             │
         ┌───────────────────────────────────┼───────────────────────────────────┐
         │                                   │                                   │
         ▼                                   ▼                                   ▼
┌──────────────────┐               ┌──────────────────┐               ┌──────────────────┐
│   Tanay Sharma   │               │   Sara Dingra    │               │ Vijay Kumar Soni │
│  Full Stack Lead │               │  UI/UX & QA Lead │               │ Frontend & DB    │
│  & Backend Eng.  │               │                  │               │ Specialist       │
└──────────────────┘               └──────────────────┘               └──────────────────┘
```

### Team Member 1: Tanay Sharma
- **Designation:** Full Stack Lead & Backend Systems Engineer
- **GitHub:** [@Tanaypai123](https://github.com/Tanaypai123)
- **Primary Domain:** Backend Architecture, REST API Design, Security & Integration
- **Key Responsibilities:**
  - Architecting the Node.js/Express ESM backend server.
  - Designing and implementing 11 route modules covering admin, orders, inventory, drivers, complaints, invoices, and developer console.
  - Implementing end-to-end authentication: Google OAuth with Supabase JWT validation and standalone custom Driver session management.
  - Designing multi-tenant security architecture with `resolveBusinessId` anti-spoofing middleware.
  - Integrating external third-party services: Twilio WhatsApp messaging, Google Maps Directions & OpenRouteService routing, and PDFKit server-side invoice generation.
  - Maintaining application deployment stability and CI/CD automation pipelines.

### Team Member 2: Sara Dingra
- **Designation:** UI/UX Designer & Quality Assurance Lead
- **Primary Domain:** Human-Computer Interaction, Design Systems, Functional & Integration Testing
- **Key Responsibilities:**
  - Establishing design principles, visual hierarchy, typography scales, and responsive design systems using Tailwind CSS.
  - Crafting user interfaces across all four platform personas: Admin, Customer, Driver, and Super Admin.
  - Performing comprehensive functional testing of business workflows: order placement, driver dispatch, OTP delivery verification, and dispute resolution.
  - Conducting end-to-end integration and regression testing for authentication flows, session lifecycles, and route guards.
  - Designing the embedded Bug Reporting system (`BugReportModal`) and managing defect triage, severity tagging, and regression tracking.
  - Ensuring accessibility, mobile touch compliance, and multi-device usability.

### Team Member 3: Vijay Kumar Soni
- **Designation:** Frontend Architect & Database Specialist
- **Primary Domain:** React Application Architecture, Dashboard Engineering, PostgreSQL Schema Design
- **Key Responsibilities:**
  - Designing the client single-page application (SPA) architecture with React 19, Vite, and React Router DOM v7.
  - Building modular, reusable React component systems and robust client layout structures.
  - Implementing data-rich interactive dashboards and Recharts analytical visualisations for Admin and Super Admin portals.
  - Designing the Supabase PostgreSQL relational schema across 14 tables, configuring foreign keys, indexes, and constraints.
  - Formulating and managing the 34 SQL migration scripts for database versioning and tenant isolation.
  - Establishing monorepo workspace configurations and maintaining the shared TypeScript library (`@flowstock/shared`).

---

## 2. Collaborative Workflow & Standards

1. **Architecture Alignment:** Major schema or API contract modifications require mutual cross-review between Tanay Sharma (Backend/API) and Vijay Kumar Soni (Frontend/Database).
2. **Design & QA Verification:** All new UI features and route modifications must pass UX review and QA sign-off by Sara Dingra prior to production deployment.
3. **Branching & Commits:** Development follows conventional commits (`feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `style:`, `chore:`, `perf:`).
4. **Security Priority:** Secrets, environment tokens, and service keys must never be committed. All database transactions must enforce multi-tenant isolation.
5. **Continuous Reporting:** Weekly development progress is tracked, analyzed, and committed to `reports/weekly/` using the automated progress reporting pipeline.
