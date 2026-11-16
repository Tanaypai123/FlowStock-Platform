# FlowStock — Weekly Progress Report (Week 10)

**Reporting Date:** 23/10/2026  
**Reporting Period:** 17/10/2026 to 23/10/2026  
**Project:** FlowStock (B2B Inventory Management & Logistics SaaS Platform)  
**Phase:** Customer Disputes, Complaints & Proof of Cancellation  
**Status:** Completed & Verified  

---

## 1. Development Objectives

- Build customer complaint filing module with photo evidence upload
- Create Admin complaint triage and resolution console
- Implement customer cancellation proof storage in Supabase Storage
- Provide dispute status tracking (open, in_review, resolved)

## 2. Key Features Implemented

- Customer complaint submission with issue categorization and minimum length validation
- Multiple photo uploads to Supabase complaint-images storage bucket
- Admin Complaints management console with resolution messaging and status updates
- Proof of order cancellation upload support preventing fraudulent cancellation claims

## 3. Module Progress Breakdown

- **Frontend Progress:** Built customer Support.jsx complaint form with drag-and-drop image upload; built Admin Complaints.jsx resolution center.
- **Backend Progress:** Developed complaints.js route module with role-based access (POST: customer, GET/PUT: admin) and photo storage handlers.
- **Database Progress:** Authored complaints.sql, complaints_v2.sql, complaints_v3.sql, and orders_customer_cancel_proof.sql migrations.
- **API Development:** Mounted /api/complaints endpoints: POST /api/complaints, GET /api/complaints/mine, and PUT /api/complaints/:id/resolve.
- **UI/UX Improvements:** Designed intuitive customer dispute submission form, image thumbnail previews, and Admin resolution comment modal.
- **Testing & Bug Fixes:** Tested file upload size limits (20MB Express cap), image MIME filtering, and customer dispute resolution workflows.

## 4. Challenges Encountered & Resolutions

Handling image compression and non-blocking uploads when customers upload multi-megabyte mobile photos on cellular networks.

## 5. Individual Contribution Breakdown

| Team Member | Role | Contribution (%) | Primary Deliverables & Focus Area |
|---|---|:---:|---|
| **Sara Dingra** | UI/UX Designer & QA Specialist | **45%** | Designed Support.jsx and Complaints.jsx interfaces, drag-and-drop file uploader, executed dispute QA. |
| **Tanay Sharma** | Full Stack Lead & Backend Systems Engineer | **35%** | Built complaints.js REST controllers, Supabase Storage integration, cancellation proof pipeline. |
| **Vijay Kumar Soni** | Frontend Architect & Database Specialist | **20%** | Authored complaints.sql and schema migrations, configured database foreign keys and status ENUMs. |

> **Note:** Weekly contribution percentages are evaluated based on actual source deliverables, architectural ownership, and task complexity. Total = 100%.

## 6. Next Week Objectives

- Implement dynamic PDF invoice generation via PDFKit
- Build Super Admin / Developer monitoring console
- Create platform-wide analytics dashboards

---
*Report compiled for academic evaluation & repository development history.*
