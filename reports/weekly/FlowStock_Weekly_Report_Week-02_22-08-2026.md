# FlowStock — Weekly Progress Report (Week 02)

**Reporting Date:** 22/08/2026  
**Reporting Period:** 15/08/2026 to 22/08/2026  
**Project:** FlowStock (B2B Inventory Management & Logistics SaaS Platform)  
**Phase:** Authentication System, OAuth Integration & Role Guards  
**Status:** Completed & Verified  

---

## 1. Development Objectives

- Integrate Google OAuth authentication via Supabase Auth
- Implement JWT extraction and cryptographic signature validation in Express
- Create client-side ProtectedRoute wrappers and AuthContext provider
- Establish database trigger for automatic customer profile generation

## 2. Key Features Implemented

- Google OAuth login integration for Admins and Customers
- Express requireAuth and requireAdmin middleware validating Supabase JWTs
- Client AuthContext.tsx managing active user session state
- Database trigger handle_new_user automatically populating profiles table

## 3. Module Progress Breakdown

- **Frontend Progress:** Implemented AuthContext.tsx, ProtectedRoute.jsx component, and AuthCallback.jsx to process Google redirect tokens.
- **Backend Progress:** Engineered requireAuth.js and requireAdmin.js middleware utilizing supabaseAnon.auth.getUser(token) for strict cryptographic validation.
- **Database Progress:** Created profiles table with CHECK constraints on role (admin, customer, driver, super_admin); added handle_new_user trigger.
- **API Development:** Mounted /api/admin/users and token verification routes with Bearer token authentication.
- **UI/UX Improvements:** Designed modern Login.jsx page featuring Google sign-in branding, responsive card layout, and error notification toasts.
- **Testing & Bug Fixes:** Tested OAuth token lifecycle, expired session rejection, and verified client redirection based on user roles.

## 4. Challenges Encountered & Resolutions

Handling asynchronous profile lookup race conditions immediately following first-time Google OAuth redirects on the client.

## 5. Individual Contribution Breakdown

| Team Member | Role | Contribution (%) | Primary Deliverables & Focus Area |
|---|---|:---:|---|
| **Tanay Sharma** | Full Stack Lead & Backend Systems Engineer | **45%** | Engineered cryptographic JWT validation middleware, built AuthCallback routing logic, configured backend auth security. |
| **Vijay Kumar Soni** | Frontend Architect & Database Specialist | **35%** | Built AuthContext state manager, ProtectedRoute guard wrappers, and executed setup_profiles.sql migration. |
| **Sara Dingra** | UI/UX Designer & QA Specialist | **20%** | Designed Login.jsx UI, designed OAuth button components, conducted cross-browser authentication UX testing. |

> **Note:** Weekly contribution percentages are evaluated based on actual source deliverables, architectural ownership, and task complexity. Total = 100%.

## 6. Next Week Objectives

- Design multi-tenant business profile data model
- Implement business onboarding and join-by-code endpoints
- Create resolveBusinessId tenant isolation middleware

---
*Report compiled for academic evaluation & repository development history.*
