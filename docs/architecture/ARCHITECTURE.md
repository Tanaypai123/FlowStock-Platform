# FlowStock — Architecture & System Design

## 1. System Overview

FlowStock is a multi-tenant B2B inventory management and logistics SaaS platform designed for Indian small and medium-sized enterprises (SMEs) and wholesale distributors.

```
+-----------------------------------------------------------------------------------+
|                                  CLIENT TIER                                      |
|  React 19 SPA (Vite) + Tailwind CSS + Recharts + React Router DOM v7               |
|  - Admin Portal       (/admin/*)                                                  |
|  - Customer Portal    (/customer/*)                                               |
|  - Driver Portal      (/driver/*)                                                 |
|  - Developer Console  (/dev/*)                                                    |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          | HTTPS / REST JSON API
                                          | Authorization: Bearer <token>
                                          | x-business-id: <uuid>
                                          v
+-----------------------------------------------------------------------------------+
|                                  SERVER TIER                                      |
|  Node.js 22+ (ESM) + Express.js 4.x                                               |
|  Middleware:                                                                      |
|    - CORS & JSON parsing                                                          |
|    - requireAuth (Supabase JWT via anon key)                                      |
|    - requireDriverAuth (Driver session token)                                     |
|    - requireAdmin (profiles.role check)                                           |
|    - superAdminOnly (super_admin role check)                                      |
|    - resolveBusinessId (Anti-spoofing tenant perimeter)                           |
|    - apiLogger (Asynchronous telemetry to api_logs)                               |
|  Routes:                                                                          |
|    - /api/admin, /api/orders, /api/customer, /api/driver, /api/inventory,         |
|      /api/business, /api/complaints, /api/bugs, /api/dev                          |
+---------------------+-------------------+-------------------+---------------------+
                      |                   |                   |
                      v                   v                   v
+---------------------+   +---------------+---+   +-----------+---------+
|      DATABASE       |   |   STORAGE         |   | THIRD-PARTY CLOUD   |
| Supabase PostgreSQL |   | Supabase Storage  |   | Twilio WhatsApp     |
| 14 tables, RLS,     |   | business-logos    |   | Google Maps API     |
| 34 migrations       |   | product-images    |   | OpenRouteService    |
|                     |   | complaint-images  |   | PDFKit Invoice      |
|                     |   | bug-screenshots   |   |                     |
+---------------------+   +-------------------+   +---------------------+
```

---

## 2. Security & Request Lifecycle

1. **Authentication Token Parsing:**
   - **Google OAuth JWT:** Validated via `supabaseAnon.auth.getUser(token)`.
   - **Driver Session Token:** Validated against `driver_sessions` table with 30-day expiration check.
2. **Tenant Scoping (`resolveBusinessId`):**
   - Extracts `x-business-id` header.
   - Verifies user's active membership in `user_businesses` (or `driver_business_links`).
   - If user is not authorized for the requested business, returns `403 Forbidden` with zero data leakage.
3. **Admin & Developer Authorization:**
   - `requireAdmin`: Checks `profiles.role = 'admin'`.
   - `superAdminOnly`: Checks `profiles.role = 'super_admin'`. Unauthenticated or unauthorized queries receive an identical `403 Access denied` response to prevent role discovery.
4. **Execution & Auditing:**
   - Database operations execute using `supabaseAdmin` (bypassing RLS for verified server logic).
   - `apiLogger` writes endpoint telemetry to `api_logs` asynchronously on response finish.
