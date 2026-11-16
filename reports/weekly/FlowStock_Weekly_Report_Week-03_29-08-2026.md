# FlowStock — Weekly Progress Report (Week 03)

**Reporting Date:** 29/08/2026  
**Reporting Period:** 23/08/2026 to 29/08/2026  
**Project:** FlowStock (B2B Inventory Management & Logistics SaaS Platform)  
**Phase:** Multi-Tenancy Architecture & Business Profile Management  
**Status:** Completed & Verified  

---

## 1. Development Objectives

- Implement multi-tenant business isolation schema in Supabase PostgreSQL
- Enable business onboarding with custom branding, warehouse location, and join code
- Build resolveBusinessId middleware for request-level tenant boundary enforcement
- Create Admin BusinessSetup UI for company profile and logo management

## 2. Key Features Implemented

- Multi-tenant relational schema: business_profile, user_businesses, and business_code
- resolveBusinessId middleware guaranteeing no cross-tenant query execution
- Unique alphanumeric business join code generator (/join/:code)
- Business profile creation and logo upload to Supabase Storage

## 3. Module Progress Breakdown

- **Frontend Progress:** Built BusinessSetup.jsx page with logo image uploader and brand color selection; built Join.jsx for business onboarding via code.
- **Backend Progress:** Created businessSetup.js route module, implemented x-business-id header resolution and anti-spoofing checks.
- **Database Progress:** Authored business_profile.sql, user_businesses.sql, and business_code.sql migrations; added unique constraints on (user_id, business_id).
- **API Development:** Added GET /api/business/info/:code, POST /api/business/setup, and PUT /api/admin/business-profile endpoints.
- **UI/UX Improvements:** Designed intuitive business onboarding wizard, company logo cropping preview, and visual feedback for invalid join codes.
- **Testing & Bug Fixes:** Executed security tests attempting cross-tenant access using modified x-business-id headers, verifying HTTP 403 Forbidden rejection.

## 4. Challenges Encountered & Resolutions

Preventing tenant ID enumeration and ensuring users belonging to multiple businesses can switch contexts smoothly.

## 5. Individual Contribution Breakdown

| Team Member | Role | Contribution (%) | Primary Deliverables & Focus Area |
|---|---|:---:|---|
| **Vijay Kumar Soni** | Frontend Architect & Database Specialist | **40%** | Designed business relational schema, authored business_profile.sql and user_businesses.sql migrations. |
| **Tanay Sharma** | Full Stack Lead & Backend Systems Engineer | **40%** | Developed resolveBusinessId anti-spoofing middleware and /api/business route controllers. |
| **Sara Dingra** | UI/UX Designer & QA Specialist | **20%** | Designed BusinessSetup.jsx and Join.jsx pages, validated branding color pickers and mobile layout. |

> **Note:** Weekly contribution percentages are evaluated based on actual source deliverables, architectural ownership, and task complexity. Total = 100%.

## 6. Next Week Objectives

- Implement full inventory CRUD management
- Support multi-stage inventory lifecycle (raw, processing, packaged, ready)
- Add image uploads to product-images storage bucket

---
*Report compiled for academic evaluation & repository development history.*
