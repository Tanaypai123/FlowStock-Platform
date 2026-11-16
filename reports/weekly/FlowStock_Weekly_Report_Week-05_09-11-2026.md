# FlowStock — Weekly Progress Report (Week 05)

**Reporting Date:** 09/11/2026  
**Reporting Period:** 05/09/2026 to 11/09/2026  
**Project:** FlowStock (B2B Inventory Management & Logistics SaaS Platform)  
**Phase:** Customer Storefront, Cart Management & Address System  
**Status:** Completed & Verified  

---

## 1. Development Objectives

- Develop responsive customer shopping storefront displaying products filtered by business
- Implement interactive slide-over shopping cart with real-time price calculations
- Build customer address book supporting default addresses and regional tagging
- Ensure seamless mobile UX for B2B wholesale buyers

## 2. Key Features Implemented

- Customer product catalog with search, price displays, and stock availability
- Slide-over shopping cart supporting quantity increment/decrement and item removal
- Customer address management: multiple saved delivery locations with region tags
- Business branding customization reflected dynamically in customer header

## 3. Module Progress Breakdown

- **Frontend Progress:** Built customer Home.jsx storefront, slide-over cart drawer, and customer Profile.jsx with address management cards.
- **Backend Progress:** Implemented /api/customer/products (filtering ready stage items) and /api/customer/addresses CRUD endpoints.
- **Database Progress:** Authored customer_profile_addresses.sql migration creating customer_addresses table with is_default flags.
- **API Development:** Mounted customer API router: GET /api/customer/products, GET /api/customer/business-info, and addresses endpoints.
- **UI/UX Improvements:** Engineered high-converting B2B storefront UI, responsive product grid, mobile floating cart button, and clean address cards.
- **Testing & Bug Fixes:** Tested cart persistence across browser page refreshes, address validation, and wholesale order total calculations.

## 4. Challenges Encountered & Resolutions

Preventing customers from adding items to cart exceeding available inventory stock in real-time.

## 5. Individual Contribution Breakdown

| Team Member | Role | Contribution (%) | Primary Deliverables & Focus Area |
|---|---|:---:|---|
| **Sara Dingra** | UI/UX Designer & QA Specialist | **40%** | Crafted customer storefront layout, slide-out cart drawer, mobile buyer experience, and address cards. |
| **Vijay Kumar Soni** | Frontend Architect & Database Specialist | **35%** | Authored customer_profile_addresses.sql, built address state management and shopping cart state store. |
| **Tanay Sharma** | Full Stack Lead & Backend Systems Engineer | **25%** | Implemented /api/customer/products and customer address API controllers with tenant verification. |

> **Note:** Weekly contribution percentages are evaluated based on actual source deliverables, architectural ownership, and task complexity. Total = 100%.

## 6. Next Week Objectives

- Implement order placement and order_line_items creation
- Develop order lifecycle state machine
- Build Admin order management dashboard

---
*Report compiled for academic evaluation & repository development history.*
