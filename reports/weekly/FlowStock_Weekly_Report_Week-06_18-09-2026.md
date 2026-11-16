# FlowStock — Weekly Progress Report (Week 06)

**Reporting Date:** 18/09/2026  
**Reporting Period:** 12/09/2026 to 18/09/2026  
**Project:** FlowStock (B2B Inventory Management & Logistics SaaS Platform)  
**Phase:** Order Processing Engine & Order Lifecycle State Machine  
**Status:** Completed & Verified  

---

## 1. Development Objectives

- Implement transactional order placement with order_line_items snapshots
- Architect order state machine: pending -> confirmed -> dispatched -> out_for_delivery -> delivered
- Build Admin Orders dashboard for status updates, rejection, and guest order handling
- Create Customer order tracking page displaying historical and active orders

## 2. Key Features Implemented

- Transactional order placement capturing item price and name at order time
- Deterministic order status progression with cancellation rules
- Admin Orders management console with filter tabs and quick action buttons
- Customer order history view with step-by-step progress tracking bar

## 3. Module Progress Breakdown

- **Frontend Progress:** Built Admin Orders.jsx with status tabs, customer detail drawers, and Customer Orders.jsx with tracking timeline.
- **Backend Progress:** Engineered orders.js route module (2100+ lines), status timestamp tracking, and validation rules for transitions.
- **Database Progress:** Authored orders.sql, orders_status_timestamps.sql, and orders_pricing_discount.sql migrations.
- **API Development:** Created POST /api/customer/orders, GET /api/orders, PUT /api/orders/:id/status, and PUT /api/customer/orders/:id/cancel.
- **UI/UX Improvements:** Designed order tracking stepper component, status badges, and streamlined order review modal for admins.
- **Testing & Bug Fixes:** Tested order state transition edge cases: attempting cancellation on already dispatched orders, empty order handling.

## 4. Challenges Encountered & Resolutions

Ensuring line item prices remain immutable even if the underlying product price changes in the inventory catalog.

## 5. Individual Contribution Breakdown

| Team Member | Role | Contribution (%) | Primary Deliverables & Focus Area |
|---|---|:---:|---|
| **Tanay Sharma** | Full Stack Lead & Backend Systems Engineer | **50%** | Engineered transactional order creation, status transition state machine, and Express orders router. |
| **Vijay Kumar Soni** | Frontend Architect & Database Specialist | **30%** | Designed orders relational schema, authored migrations, built Admin Orders table and filter tabs. |
| **Sara Dingra** | UI/UX Designer & QA Specialist | **20%** | Designed order tracking visual stepper, tested order placement flows, validated mobile status views. |

> **Note:** Weekly contribution percentages are evaluated based on actual source deliverables, architectural ownership, and task complexity. Total = 100%.

## 6. Next Week Objectives

- Design driver authentication system (phone + password)
- Implement driver session token architecture
- Build Admin driver fleet management interface

---
*Report compiled for academic evaluation & repository development history.*
