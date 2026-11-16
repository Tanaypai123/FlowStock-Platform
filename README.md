# FlowStock — B2B Inventory Management & Logistics SaaS Platform

<p align="center">
  <img src="./LOGO.png" alt="FlowStock Logo" width="220" />
</p>

<p align="center">
  <strong>Streamlining inventory operations, order fulfillment, transportation workflows, and multi-tenant business operations.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Node.js-v22.x-green.svg" alt="Node Version" />
  <img src="https://img.shields.io/badge/React-19.x-blue.svg" alt="React Version" />
  <img src="https://img.shields.io/badge/Vite-6.x-646CFF.svg" alt="Vite Version" />
  <img src="https://img.shields.io/badge/Database-Supabase%20PostgreSQL-3ECF8E.svg" alt="Supabase" />
  <img src="https://img.shields.io/badge/License-Academic%20Project-orange.svg" alt="License" />
</p>

---

## 1. Project Overview

**FlowStock** is a comprehensive, production-grade B2B multi-tenant SaaS platform built to solve inventory management, multi-stop delivery logistics, order lifecycles, and business operations for modern enterprises and supply chains.

The platform provides isolated per-business operational workspaces with dedicated portals tailored for four distinct user personas:
1. **Admin Portal:** Comprehensive inventory cataloging, order processing, driver fleet management, automated dispatching, and revenue analytics.
2. **Customer Portal:** Product browsing, multi-item shopping carts, order tracking with real-time status progression, delivery address book, and dispute filing.
3. **Driver Portal:** Active delivery queue, single-click 3-tier route optimization (Google Maps Directions, OpenRouteService, heuristic fallback), OTP-based handover verification, and history logs.
4. **Developer / Super Admin Portal:** Cross-tenant platform KPIs, business health monitoring, slow query & API telemetry, and an integrated bug tracking console.

---

## 2. Key Capabilities & Features

### Multi-Tenancy & Tenant Isolation
- **Per-Tenant Scoping:** Every user belongs to one or more businesses via relational mappings (`user_businesses`).
- **Anti-Spoofing Perimeter:** HTTP requests enforce `x-business-id` validation at the Express middleware layer (`resolveBusinessId`), preventing cross-tenant data leakage.
- **Unique Join Codes:** Businesses onboard clients and staff seamlessly via shareable alphanumeric codes (`/join/:business_code`).

### Smart Order Lifecycle & Inventory Synchronization
- **State Machine:** Deterministic lifecycle: `pending` → `confirmed` → `dispatched` → `out_for_delivery` → `delivered` (or `cancelled`/`rejected`).
- **Stock Guard:** Stock is deducted automatically upon confirmation (`stock_deducted` flag guarantees double-deduction prevention).
- **Automated Messaging:** Dynamic WhatsApp dispatch updates dispatched via Twilio integration upon status transitions.

### 3-Tier Driver Route Optimization
- **Tier 1:** Google Maps Directions API for real-time traffic-aware multi-stop routing.
- **Tier 2:** OpenRouteService API fallback when Google quotas or limits are reached.
- **Tier 3:** High-efficiency nearest-neighbour geometric heuristic guaranteeing uninterrupted offline operation.

### Delivery Verification & Fraud Prevention
- **OTP Handoff:** Secure 4-digit one-time passcode generated per order; driver verifies customer OTP upon arrival to close the delivery loop.
- **Proof of Cancellation:** Supports image proof uploads to Supabase Storage if an order is cancelled or disputed in transit.

### Integrated Bug & Health Telemetry
- **In-App Bug Modal:** `BugReportModal` captures contextual screenshots, device information, viewport dimensions, and page URLs.
- **API Performance Logging:** `apiLogger` asynchronously measures latency, error rates, and throughput by endpoint without blocking client responses.

---

## 3. Technology Stack

| Domain | Technology | Version | Purpose |
|---|---|---|---|
| **Frontend SPA** | React | 19.x | Component-based reactive UI |
| **Routing** | React Router DOM | 7.x | Client-side declarative routing |
| **Styling & CSS** | Tailwind CSS & PostCSS | 3.4.x | Responsive design system |
| **Analytics Charts** | Recharts | 3.x | Operations & KPI visualisations |
| **Frontend Build** | Vite | 6.x | Fast ESM module bundling |
| **Backend Runtime** | Node.js | >=20.x | High-throughput ESM runtime |
| **Server Framework** | Express | 4.21.x | Modular REST API routing |
| **Database & Auth** | Supabase (PostgreSQL) | 2.x SDK | Relational storage & OAuth Auth |
| **PDF Generation** | PDFKit & ReportLab | Latest | Invoices & Form-3 progress reports |
| **Messaging API** | Twilio | 5.x SDK | Automated WhatsApp order alerts |
| **Mapping & Routing** | Google Maps / ORS | Cloud APIs | Multi-stop fleet route optimization |

---

## 4. Architecture Overview

```
                               ┌──────────────────────────────────────────────────────────┐
                               │                    FLOWSTOCK CLIENT                      │
                               │        React 19 SPA (Vite) + Tailwind CSS                │
                               ├──────────────┬──────────────┬──────────────┬─────────────┤
                               │ Admin Portal │ Customer Hub │ Driver PWA   │ Dev Console │
                               └──────┬───────┴──────┬───────┴──────┬───────┴──────┬──────┘
                                      │              │              │              │
                                      └──────────────┴──────┬───────┴──────────────┘
                                                            │ HTTP / JSON API (Bearer Token + x-business-id)
                                                            ▼
                               ┌──────────────────────────────────────────────────────────┐
                               │                 EXPRESS REST API SERVER                  │
                               │              Node.js 22+ (ESM Architecture)              │
                               ├──────────────────────────────────────────────────────────┤
                               │ Middleware: requireAuth | requireAdmin | requireDriverAuth│
                               │             superAdminOnly | resolveBusinessId | apiLogger│
                               ├──────────────────────────────────────────────────────────┤
                               │ Routes: /api/admin | /api/orders | /api/customer         │
                               │         /api/driver | /api/inventory | /api/dev          │
                               └──────────────┬─────────────────────────────┬─────────────┘
                                              │                             │
                     ┌────────────────────────┴────────┐           ┌────────┴──────────────┐
                     ▼                                 ▼           ▼                       ▼
      ┌─────────────────────────────┐   ┌────────────────────┐ ┌───────────────┐ ┌────────────────┐
      │     SUPABASE POSTGRESQL     │   │  SUPABASE STORAGE  │ │  TWILIO API   │ │ GOOGLE MAPS /  │
      │   14 Normalized Tables      │   │  - business-logos  │ │  WhatsApp     │ │ OPENROUTESRV   │
      │   Row Level Security (RLS)  │   │  - product-images  │ │  Dispatch     │ │ Fleet Route    │
      │   34 Migration Scripts      │   │  - bug-screenshots │ │  Alerts       │ │ Optimization   │
      └─────────────────────────────┘   └────────────────────┘ └───────────────┘ └────────────────┘
```

---

## 5. Repository Structure

```
FlowStock/
├── .github/
│   └── workflows/
│       └── weekly-progress-report.yml     # Automated weekly Form-3 reporting workflow
├── client/                                # React 19 Frontend application
│   ├── src/
│   │   ├── components/                    # Modal dialogs, route guards, error boundaries
│   │   ├── context/                       # AuthContext, DriverContext
│   │   ├── layouts/                       # Admin, Customer, Driver, Dev layouts
│   │   ├── lib/                           # adminApi, customerApi, driverApi, devApi
│   │   └── pages/                         # Multi-portal page views
│   └── package.json
├── server/                                # Express.js backend API
│   ├── src/
│   │   ├── middleware/                    # Auth, RBAC, business isolation, logging
│   │   ├── routes/                        # 11 REST route modules
│   │   └── services/                      # WhatsApp notification & inventory services
│   └── package.json
├── shared/                                # @flowstock/shared contracts package
│   ├── src/                               # TypeScript types, constants & schemas
│   └── package.json
├── supabase/
│   └── sql/                               # 34 incremental SQL database migrations
├── docs/                                  # Technical & system documentation
│   ├── architecture/                      # Architecture blueprints & flow diagrams
│   ├── database/                          # ER diagrams & schema specifications
│   └── project/                           # Project charters & milestone trackers
├── reports/                               # Form-3 weekly and consolidated reports
│   ├── weekly/                            # 13 weekly progress reports (PDF + Markdown)
│   └── consolidated/                      # Consolidated evaluation & contribution dashboard
├── scripts/
│   └── generate_report.py                 # Academic Form-3 PDF & Markdown report engine
├── FlowStock_System_Documentation.md      # Comprehensive 800+ line technical reference
├── CONTRIBUTORS.md                        # Team roles & verified contribution matrix
├── CONTRIBUTING.md                        # Engineering & development standards
├── TEAM.md                                # Team charter and governance model
├── .env.example                           # Safe environment configuration template
├── .gitignore                             # Secret-safe Git ignore configuration
└── package.json                           # Root monorepo workspace configuration
```

---

## 6. Getting Started

### Prerequisites
- **Node.js:** `>= 20.x` (Tested on Node 22+)
- **npm:** `>= 10.x`
- **Supabase Account:** Configured PostgreSQL database & Storage buckets
- **Python 3.x:** (Optional, for Form-3 progress report generation with `reportlab` & `matplotlib`)

### 1. Installation
Clone the repository and install dependencies across the monorepo workspaces:
```bash
git clone https://github.com/Tanaypai123/FlowStock-Platform.git
cd FlowStock-Platform
npm install
```

### 2. Environment Configuration
Copy the template configuration and supply your Supabase and service keys:
```bash
cp .env.example .env
```
Key configuration parameters:
- `SUPABASE_URL` & `SUPABASE_ANON_KEY`: Client & JWT verification credentials.
- `SUPABASE_SERVICE_ROLE_KEY`: Server-side administrative database transactions.
- `VITE_API_URL`: Backend endpoint (defaults to `http://localhost:8000`).
- `PORT`: Server listen port (default `8000`).

### 3. Build & Run
Compile the shared TypeScript package and run client and server concurrently:
```bash
# Build shared library
npm run build --workspace shared

# Run both Client and Server concurrently
npm run dev
```
- Client interface: `http://localhost:5173`
- Backend API server: `http://localhost:8000`

---

## 7. Weekly Progress Reporting Automation

FlowStock includes an automated academic evaluation pipeline configured for weekly submission (`Form-3`):
- **GitHub Action:** `.github/workflows/weekly-progress-report.yml` executes on schedule every Thursday at 18:29 UTC (11:59 PM IST) and on manual trigger (`workflow_dispatch`).
- **Reporting Engine:** `scripts/generate_report.py` analyzes repository commits, line additions/deletions, active days, and generates Form-3 PDF documents complete with mentor signature blocks.
- **Reports Archive:** All weekly reports are archived in [`reports/weekly/`](./reports/weekly/).
- **Consolidated Milestone Dashboard:** Full project metrics and contribution analytics are maintained in [`reports/consolidated/`](./reports/consolidated/).

---

## 8. Engineering Team & Core Responsibilities

FlowStock was developed through collaborative engineering by a dedicated team at the **Department of Computer Science & Engineering, Swami Keshvanand Institute of Technology, Management & Gramothan, Jaipur (SKIT)**.

| Team Member | Role | Primary Focus Areas |
|---|---|---|
| **Tanay Sharma**<br>([@Tanaypai123](https://github.com/Tanaypai123)) | Lead Full Stack & Backend Engineer | Backend Architecture, Express APIs, Supabase Auth & Driver Token Auth, RBAC Middleware, Twilio WhatsApp, Route Optimization, System Integration |
| **Sara Dingra** | UI/UX Designer & QA Specialist | Visual Design System, Tailwind UI, Mobile Ergonomics, Functional Testing, Integration QA, Bug Reporting System (`BugReportModal`), Usability |
| **Vijay Kumar Soni** | Frontend Architect & Database Engineer | React 19 Client SPA, Router Architecture, Dashboards (Admin, Customer, Driver, Dev), Supabase Database Schema (14 Tables), 34 SQL Migrations |

Detailed member responsibilities, contribution matrices, and team governance are documented in:
- [`CONTRIBUTORS.md`](./CONTRIBUTORS.md)
- [`TEAM.md`](./TEAM.md)
- [`CONTRIBUTING.md`](./CONTRIBUTING.md)

---

## 9. System Documentation

For in-depth architectural details, request lifecycles, database entity relationships, route permissions, and threat modeling, refer to [`FlowStock_System_Documentation.md`](./FlowStock_System_Documentation.md).
