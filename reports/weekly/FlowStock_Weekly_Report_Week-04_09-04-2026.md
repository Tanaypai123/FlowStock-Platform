# FlowStock — Weekly Progress Report (Week 04)

**Reporting Date:** 09/04/2026  
**Reporting Period:** 30/08/2026 to 04/09/2026  
**Project:** FlowStock (B2B Inventory Management & Logistics SaaS Platform)  
**Phase:** Inventory Management System & Multi-Stage Tracking  
**Status:** Completed & Verified  

---

## 1. Development Objectives

- Build complete inventory item management with quantity tracking and low stock alerts
- Support B2B multi-stage inventory tracking: raw, processing, packaged, ready, draft, archived
- Implement product image upload to Supabase Storage product-images bucket
- Create interactive Admin Inventory data grid with search, filtering, and stage tabs

## 2. Key Features Implemented

- Full inventory CRUD operations scoped by business_id
- Multi-stage product categorization with badge indicators
- Low-stock threshold notifications and quantity adjustment controls
- Single and multiple product image upload integration

## 3. Module Progress Breakdown

- **Frontend Progress:** Created Inventory.jsx with real-time stage filtering, search bars, stock status badges, and item creation/edit modal dialogs.
- **Backend Progress:** Developed inventory.js route module with validation for numeric prices, non-negative quantities, and allowed stage ENUMs.
- **Database Progress:** Authored inventory_items.sql, inventory_unit.sql, and inventory_image.sql migrations with cascade deletions and stage indices.
- **API Development:** Created GET, POST, PUT, DELETE /api/inventory, and POST /api/inventory/upload-image.
- **UI/UX Improvements:** Designed clean tabular inventory UI with responsive horizontal scrolling, color-coded stage pills, and stock level progress meters.
- **Testing & Bug Fixes:** Conducted boundary testing on numeric inventory quantities, negative values prevention, and image mime-type validation.

## 4. Challenges Encountered & Resolutions

Handling multiple image uploads efficiently while maintaining optimistic UI updates on the client inventory table.

## 5. Individual Contribution Breakdown

| Team Member | Role | Contribution (%) | Primary Deliverables & Focus Area |
|---|---|:---:|---|
| **Vijay Kumar Soni** | Frontend Architect & Database Specialist | **40%** | Designed inventory database tables, authored migrations, built reusable inventory table components. |
| **Tanay Sharma** | Full Stack Lead & Backend Systems Engineer | **35%** | Built /api/inventory CRUD endpoints, image upload pipeline, and business scoping filters. |
| **Sara Dingra** | UI/UX Designer & QA Specialist | **25%** | Designed Inventory.jsx layout, stage color system, low-stock visual warnings, and item modal UX. |

> **Note:** Weekly contribution percentages are evaluated based on actual source deliverables, architectural ownership, and task complexity. Total = 100%.

## 6. Next Week Objectives

- Develop Customer shopping portal and product catalog
- Implement client-side shopping cart with multi-item aggregation
- Build customer delivery address management

---
*Report compiled for academic evaluation & repository development history.*
