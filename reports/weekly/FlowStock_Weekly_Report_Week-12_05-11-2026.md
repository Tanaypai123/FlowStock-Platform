# FlowStock — Weekly Progress Report (Week 12)

**Reporting Date:** 05/11/2026  
**Reporting Period:** 31/10/2026 to 05/11/2026  
**Project:** FlowStock (B2B Inventory Management & Logistics SaaS Platform)  
**Phase:** System Health Telemetry & In-App Bug Reporting Subsystem  
**Status:** Completed & Verified  

---

## 1. Development Objectives

- Build non-blocking API telemetry middleware (apiLogger) logging status codes, latency, and endpoints
- Create embedded BugReportModal capturing device info, viewport, URL, and screenshots
- Develop System Health dashboard in Dev Console monitoring slow endpoints and error rates
- Build Bug Reports management console with severity tagging and resolution notes

## 2. Key Features Implemented

- Fire-and-forget apiLogger Express middleware recording request latency into api_logs table
- Universal BugReportModal accessible across all four portals with base64 screenshot upload
- System Health dashboard visualizing API response times, error rates, and 24-hour slow query logs
- Bug tracking management console with super_admin_note internal field

## 3. Module Progress Breakdown

- **Frontend Progress:** Built BugReportModal.jsx component embedded in layouts, SystemHealth.jsx telemetry console, and BugReports.jsx manager.
- **Backend Progress:** Engineered apiLogger.js (hooked to res.on("finish")), bugs.js route module, and authenticateAny multi-token parser.
- **Database Progress:** Authored bug_reports.sql migration creating bug_reports table with severity ENUMs and JSONB device metadata.
- **API Development:** Mounted POST /api/bugs/report, POST /api/bugs/upload-screenshot, and GET /api/dev/system/* telemetry endpoints.
- **UI/UX Improvements:** Designed unintrusive floating bug report trigger button, severity radio chips, and real-time system health status dials.
- **Testing & Bug Fixes:** Verified apiLogger does not delay HTTP response times, tested screenshot base64 decoding and storage permissions.

## 4. Challenges Encountered & Resolutions

Ensuring API telemetry logging never causes response latency or crashes the server even if database connection is congested.

## 5. Individual Contribution Breakdown

| Team Member | Role | Contribution (%) | Primary Deliverables & Focus Area |
|---|---|:---:|---|
| **Sara Dingra** | UI/UX Designer & QA Specialist | **45%** | Designed BugReportModal.jsx, device metadata capture UX, BugReports console, conducted QA on error states. |
| **Vijay Kumar Soni** | Frontend Architect & Database Specialist | **30%** | Authored bug_reports.sql migration, built SystemHealth.jsx dashboard and telemetry metric charts. |
| **Tanay Sharma** | Full Stack Lead & Backend Systems Engineer | **25%** | Engineered non-blocking apiLogger middleware, bugs.js REST controllers, and screenshot upload pipeline. |

> **Note:** Weekly contribution percentages are evaluated based on actual source deliverables, architectural ownership, and task complexity. Total = 100%.

## 6. Next Week Objectives

- Implement Customer Boost marketing module
- Configure automated weekly progress reporting via GitHub Actions
- Finalize system documentation and perform end-to-end verification

---
*Report compiled for academic evaluation & repository development history.*
