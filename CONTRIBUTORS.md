# FlowStock — Contributors

This document recognizes the core engineering team members who designed, built, tested, and maintain **FlowStock: B2B Inventory Management & Logistics SaaS Platform**.

---

## Core Engineering Team

### 1. Tanay Sharma
- **Role:** Lead Full Stack & Backend Engineer
- **GitHub Profile:** [@Tanaypai123](https://github.com/Tanaypai123)
- **Key Responsibilities & Contributions:**
  - **Full Stack Development:** End-to-end integration across client, server, and Supabase layers.
  - **Backend Architecture & APIs:** Designed and implemented Express.js REST API layer comprising 11 route modules (`admin.js`, `orders.js`, `driverRoutes.js`, `customerOrders.js`, `invoices.js`, `complaints.js`, etc.).
  - **Authentication & Security:** Implemented dual-auth infrastructure — Google OAuth JWT verification for Admins/Customers and secure token-based authentication (phone + bcrypt password + 30-day session tokens) for Drivers.
  - **Authorization Middleware:** Engineered RBAC middleware stack (`requireAuth`, `requireAdmin`, `requireDriverAuth`, `superAdminOnly`, `resolveBusinessId`).
  - **System-level Integrations:** Multi-carrier logistics route optimization (3-Tier: Google Maps Directions API, OpenRouteService fallback, and nearest-neighbour heuristic), Twilio WhatsApp automated dispatch alerts, and PDFKit dynamic invoice generation.
  - **Multi-Tenant Isolation:** Anti-spoofing header resolution ensuring strict tenant perimeter isolation.

---

### 2. Sara Dingra
- **Role:** UI/UX Designer & Quality Assurance Lead
- **Key Responsibilities & Contributions:**
  - **UI/UX Design & Prototyping:** Crafted design language, responsive typography, visual layout systems, brand themes, and dark/light accents for all 4 application portals.
  - **User Experience Optimization:** Streamlined complex inventory workflows, driver order claiming, OTP delivery handoffs, and customer multi-item shopping checkout flows.
  - **Frontend Design Support:** Authored intuitive user journeys, landing page presentation, feature comparison tables ("Traditional vs FlowStock"), and responsive mobile navigation.
  - **Quality Assurance & Testing:** Formulated comprehensive test matrices covering cross-browser rendering, mobile viewport ergonomics, role-based route guard validations, and token expiration lifecycles.
  - **Bug Identification & Tracking:** Spearheaded the integrated Bug Reporting subsystem (`BugReportModal`), standardizing metadata collection (browser, OS, viewport, network state, screenshots) to accelerate defect resolution.

---

### 3. Vijay Kumar Soni
- **Role:** Frontend Architect & Database Specialist
- **Key Responsibilities & Contributions:**
  - **Frontend Development:** Architected React 19 single-page application utilizing Vite and modern React Router DOM v7 client-side routing.
  - **React Component Engineering:** Developed modular component library, including protected routing wrappers (`ProtectedRoute`, `SuperAdminRoute`), modal dialogs, and reusable data tables.
  - **Dashboard Engineering:** Built specialized portals: Admin Operations Center, Customer Self-Service Storefront, Driver Task Console, and Developer System Health Monitor with Recharts analytics.
  - **Database Design & Architecture:** Engineered Supabase PostgreSQL relational schema across 14 normalized tables with Row Level Security (RLS) policies, cascade constraints, and custom triggers.
  - **Database Schema Planning & Evolution:** Planned and authored 34 incremental SQL migrations managing business codes, order state transitions, audit logging, and driver session indexing.
  - **Monorepo Structure:** Structured the monorepo workspaces (`client`, `server`, `shared`) and TypeScript shared contracts package (`@flowstock/shared`).

---

## Responsibility Matrix

| Functional Area | Tanay Sharma | Sara Dingra | Vijay Kumar Soni |
|---|:---:|:---:|:---:|
| Backend Architecture & Express APIs | **Primary** | — | Supporting |
| Auth & Security (JWT, Driver Auth, RBAC) | **Primary** | Testing | — |
| UI/UX Design & User Experience | — | **Primary** | Supporting |
| Frontend Engineering (React 19, Routing) | Supporting | — | **Primary** |
| Component Libraries & Dashboards | Supporting | UX Review | **Primary** |
| Database Schema & Migrations | Supporting | — | **Primary** |
| QA, Functional & Integration Testing | Supporting | **Primary** | Supporting |
| External Integrations (WhatsApp, Maps, PDF) | **Primary** | QA Verification | Supporting |
| Multi-Tenancy & Tenant Isolation | **Primary** | Testing | Architecture |
| Bug Tracking & Quality Assurance | Bug Resolution | **Primary (Triage & QA)** | Bug Resolution |
