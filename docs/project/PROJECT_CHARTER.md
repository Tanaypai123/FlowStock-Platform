# FlowStock — Project Charter & Technical Specification

**Project Title:** FlowStock — Multi-Tenant B2B Inventory Management & Logistics SaaS  
**Institution:** Swami Keshvanand Institute of Technology, Management & Gramothan, Jaipur (SKIT)  
**Academic Department:** Department of Computer Science & Engineering  
**Project Lead:** Tanay Sharma  
**Team Members:** Tanay Sharma, Sara Dingra, Vijay Kumar Soni  

---

## 1. Problem Statement

Wholesale supply chains, local distribution hubs, and B2B manufacturers face challenges coordinating stock movement, order dispatching, and field delivery verification. Existing software solutions either:
1. Lack native multi-tenancy, requiring dedicated server deployments per business.
2. Rely on complex enterprise interfaces unsuitable for field delivery drivers on mobile devices.
3. Lack integrated logistics route optimization, causing high fuel costs and delayed deliveries.
4. Have no dispute verification mechanisms, leading to fraudulent delivery claims and order cancellations.

---

## 2. Project Goals & Objectives

1. **Multi-Tenant SaaS Foundation:** Build a multi-tenant cloud architecture where multiple independent businesses operate securely without data leakage.
2. **Deterministic Order Processing:** Automate order lifecycles from customer shopping cart to dispatch, transit, and delivery.
3. **Logistics Optimization:** Provide multi-stop route optimization using Google Maps Directions API and OpenRouteService with an offline fallback heuristic.
4. **Fraud-Resistant Deliveries:** Guarantee delivery authenticity through customer-provided 4-digit OTP passcodes.
5. **Real-Time Customer Alerts:** Deliver automated WhatsApp notifications via Twilio API upon status changes.
6. **Platform Monitoring:** Build a Developer / Super Admin console tracking cross-tenant KPIs, slow API queries, and bug reports.

---

## 3. User Personas & Permissions

| Persona | Access Route | Authentication Method | Core Capabilities |
|---|---|---|---|
| **Admin** | `/admin/*` | Google OAuth (JWT) | Inventory CRUD, driver fleet management, order processing, sales analytics, company branding. |
| **Customer** | `/customer/*` | Google OAuth (JWT) | Product browsing, shopping cart, order tracking, address book, complaint filing. |
| **Driver** | `/driver/*` | Phone + Password (Token) | Active deliveries queue, 3-tier route optimization, OTP verification, completion logs. |
| **Super Admin** | `/dev/*` | Google OAuth (`super_admin` role) | System health, API latency charts, cross-tenant revenue KPIs, bug report management. |

---

## 4. Academic Evaluation Milestones

The project was executed across 13 weeks adhering to academic Form-3 reporting requirements:
- **Weeks 1–3:** Inception, Monorepo Setup, Auth & Multi-Tenancy
- **Weeks 4–6:** Inventory Cataloging, Customer Storefront & Order State Engine
- **Weeks 7–9:** Driver Fleet System, OTP Verification & 3-Tier Route Optimization
- **Weeks 10–13:** Dispute Handling, PDF Invoices, Telemetry & Production Hardening
