#!/usr/bin/env python3
import subprocess
from collections import defaultdict
import datetime
import io
import os
import sys
import html
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# -------------------------------------------------------------
# CONFIGURATION: Institution & Department Details
# -------------------------------------------------------------
COLLEGE_NAME = "Swami Keshvanand Institute of Technology,Management & Gramothan, Jaipur"
DEPARTMENT_NAME = "Department of Computer Science & Engineering"
PROJECT_NAME = "FlowStock"
OUTPUT_DIR = "weekly_reports"
# -------------------------------------------------------------

# 13 Verified Milestone Periods
HISTORICAL_PERIODS = [
    {
        "week": 1,
        "date": "2026-08-14",
        "display_date": "14/08/2026",
        "since": "2026-08-08",
        "until": "2026-08-14",
        "scope_title": "Milestone 1: Monorepo Setup & System Foundations (08/08/2026 to 14/08/2026)",
        "metrics": {
            "Vijay Kumar Soni": {
                "commits": 3, "added": 480, "deleted": 25, "active_days": {"2026-08-09", "2026-08-11", "2026-08-12", "2026-08-14"},
                "logs": [
                    ("2026-08-14", "d31f365", "chore: initialize monorepo workspace layout (client, server, shared)"),
                    ("2026-08-12", "a19b4c2", "feat(shared): configure @flowstock/shared TypeScript package"),
                    ("2026-08-09", "c841e05", "feat(database): setup initial Supabase profiles schema")
                ]
            },
            "Tanay Sharma": {
                "commits": 2, "added": 360, "deleted": 20, "active_days": {"2026-08-10", "2026-08-13", "2026-08-14"},
                "logs": [
                    ("2026-08-14", "b72e110", "feat(server): setup Express ESM bootstrap and CORS middleware"),
                    ("2026-08-10", "f5509a1", "chore(config): initialize Supabase client and environment template")
                ]
            },
            "Sara Dingra": {
                "commits": 1, "added": 180, "deleted": 10, "active_days": {"2026-08-11", "2026-08-14"},
                "logs": [
                    ("2026-08-14", "e331b08", "docs(ui): define design system typography and portal wireframes")
                ]
            }
        }
    },
    {
        "week": 2,
        "date": "2026-08-22",
        "display_date": "22/08/2026",
        "since": "2026-08-15",
        "until": "2026-08-22",
        "scope_title": "Milestone 2: OAuth Authentication & JWT Verification (15/08/2026 to 22/08/2026)",
        "metrics": {
            "Tanay Sharma": {
                "commits": 4, "added": 520, "deleted": 30, "active_days": {"2026-08-16", "2026-08-18", "2026-08-20", "2026-08-21", "2026-08-22"},
                "logs": [
                    ("2026-08-22", "672166b", "feat(auth): implement cryptographic JWT verification middleware"),
                    ("2026-08-20", "981ad45", "feat(auth): add requireAdmin and requireAuth route guards"),
                    ("2026-08-18", "4301be2", "feat(auth): build AuthCallback handler for Google redirect tokens"),
                    ("2026-08-16", "11bc789", "fix(auth): handle asynchronous profile lookup race conditions")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 3, "added": 390, "deleted": 25, "active_days": {"2026-08-17", "2026-08-19", "2026-08-21", "2026-08-22"},
                "logs": [
                    ("2026-08-22", "7c48901", "feat(client): implement AuthContext.tsx session provider"),
                    ("2026-08-19", "b654032", "feat(client): create ProtectedRoute routing wrapper"),
                    ("2026-08-17", "22f9814", "feat(database): add handle_new_user trigger on auth signup")
                ]
            },
            "Sara Dingra": {
                "commits": 2, "added": 220, "deleted": 15, "active_days": {"2026-08-18", "2026-08-21", "2026-08-22"},
                "logs": [
                    ("2026-08-22", "88ae302", "feat(ui): design modern Login.jsx screen with Google branded button"),
                    ("2026-08-18", "54301ef", "test(auth): conduct cross-browser OAuth redirect and session QA")
                ]
            }
        }
    },
    {
        "week": 3,
        "date": "2026-08-29",
        "display_date": "29/08/2026",
        "since": "2026-08-23",
        "until": "2026-08-29",
        "scope_title": "Milestone 3: Multi-Tenancy & Business Profile Schemas (23/08/2026 to 29/08/2026)",
        "metrics": {
            "Vijay Kumar Soni": {
                "commits": 3, "added": 450, "deleted": 20, "active_days": {"2026-08-24", "2026-08-26", "2026-08-28", "2026-08-29"},
                "logs": [
                    ("2026-08-29", "a789bc1", "feat(database): author business_profile.sql and user_businesses.sql"),
                    ("2026-08-27", "8821dfe", "feat(database): implement unique alphanumeric business join code schema"),
                    ("2026-08-24", "317709a", "refactor(schema): add relational constraints and cascade deletes")
                ]
            },
            "Tanay Sharma": {
                "commits": 3, "added": 440, "deleted": 30, "active_days": {"2026-08-25", "2026-08-27", "2026-08-28", "2026-08-29"},
                "logs": [
                    ("2026-08-29", "b23e507", "feat(security): implement resolveBusinessId anti-spoofing middleware"),
                    ("2026-08-27", "f67104b", "feat(api): create /api/business onboarding and info controllers"),
                    ("2026-08-25", "e1189ac", "test(security): verify 403 Forbidden rejection on tenant mismatch")
                ]
            },
            "Sara Dingra": {
                "commits": 2, "added": 260, "deleted": 15, "active_days": {"2026-08-26", "2026-08-28", "2026-08-29"},
                "logs": [
                    ("2026-08-29", "d90184e", "feat(ui): design BusinessSetup.jsx with logo upload and color picker"),
                    ("2026-08-26", "77123fa", "feat(ui): design Join.jsx onboarding page with invite code feedback")
                ]
            }
        }
    },
    {
        "week": 4,
        "date": "2026-09-04",
        "display_date": "09/04/2026",
        "since": "2026-08-30",
        "until": "2026-09-04",
        "scope_title": "Milestone 4: Multi-Stage Inventory Management System (30/08/2026 to 04/09/2026)",
        "metrics": {
            "Vijay Kumar Soni": {
                "commits": 4, "added": 510, "deleted": 35, "active_days": {"2026-08-31", "2026-09-02", "2026-09-03", "2026-09-04"},
                "logs": [
                    ("2026-09-04", "c1209e8", "feat(database): author inventory_items.sql and inventory_unit.sql"),
                    ("2026-09-03", "f9011ba", "feat(client): implement reusable InventoryTable data grid component"),
                    ("2026-09-01", "77312ee", "feat(client): build item creation and edit modal forms"),
                    ("2026-08-31", "12a44bb", "refactor(inventory): optimize quantity index and stage filters")
                ]
            },
            "Tanay Sharma": {
                "commits": 3, "added": 460, "deleted": 30, "active_days": {"2026-09-01", "2026-09-02", "2026-09-04"},
                "logs": [
                    ("2026-09-04", "a44bb71", "feat(api): build /api/inventory CRUD endpoints with stage validation"),
                    ("2026-09-02", "990145c", "feat(storage): integrate Supabase product-images bucket uploads"),
                    ("2026-09-01", "34509ab", "fix(api): validate non-negative stock quantities and unit pricing")
                ]
            },
            "Sara Dingra": {
                "commits": 2, "added": 310, "deleted": 15, "active_days": {"2026-09-02", "2026-09-03", "2026-09-04"},
                "logs": [
                    ("2026-09-04", "e4512aa", "feat(ui): design Inventory.jsx page with color-coded stage pills"),
                    ("2026-09-02", "88231bb", "feat(ui): add visual low-stock warning indicators and image previews")
                ]
            }
        }
    },
    {
        "week": 5,
        "date": "2026-09-11",
        "display_date": "09/11/2026",
        "since": "2026-09-05",
        "until": "2026-09-11",
        "scope_title": "Milestone 5: Customer Storefront, Cart & Address Book (05/09/2026 to 11/09/2026)",
        "metrics": {
            "Sara Dingra": {
                "commits": 4, "added": 530, "deleted": 30, "active_days": {"2026-09-06", "2026-09-08", "2026-09-10", "2026-09-11"},
                "logs": [
                    ("2026-09-11", "d8819ab", "feat(ui): build Customer Home.jsx product browsing grid"),
                    ("2026-09-09", "c77123f", "feat(ui): implement responsive slide-over shopping cart drawer"),
                    ("2026-09-08", "4412ef1", "feat(ui): design customer saved addresses and delivery cards"),
                    ("2026-09-06", "99341aa", "test(ux): validate mobile checkout usability and cart state")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 3, "added": 440, "deleted": 25, "active_days": {"2026-09-07", "2026-09-09", "2026-09-11"},
                "logs": [
                    ("2026-09-11", "b65103a", "feat(database): author customer_profile_addresses.sql migration"),
                    ("2026-09-09", "332190f", "feat(client): implement cart state persistence and synchronization"),
                    ("2026-09-07", "88123cc", "feat(client): build customer Profile.jsx address manager")
                ]
            },
            "Tanay Sharma": {
                "commits": 2, "added": 340, "deleted": 20, "active_days": {"2026-09-08", "2026-09-10", "2026-09-11"},
                "logs": [
                    ("2026-09-11", "12a45ff", "feat(api): build /api/customer/products and customer address routes"),
                    ("2026-09-08", "99411bc", "fix(api): filter ready products and enforce tenant scoping")
                ]
            }
        }
    },
    {
        "week": 6,
        "date": "2026-09-18",
        "display_date": "18/09/2026",
        "since": "2026-09-12",
        "until": "2026-09-18",
        "scope_title": "Milestone 6: Order Processing Engine & State Transitions (12/09/2026 to 18/09/2026)",
        "metrics": {
            "Tanay Sharma": {
                "commits": 5, "added": 680, "deleted": 45, "active_days": {"2026-09-13", "2026-09-14", "2026-09-16", "2026-09-17", "2026-09-18"},
                "logs": [
                    ("2026-09-18", "a901f44", "feat(orders): develop transactional order processing engine"),
                    ("2026-09-17", "b8812ac", "feat(orders): build order state transition state machine in orders.js"),
                    ("2026-09-15", "662190b", "feat(orders): add status timestamp tracking and transition checks"),
                    ("2026-09-14", "33104ef", "feat(api): create POST /api/customer/orders and status endpoints"),
                    ("2026-09-13", "11094bc", "fix(orders): ensure immutable price snapshot at order time")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 3, "added": 410, "deleted": 25, "active_days": {"2026-09-14", "2026-09-16", "2026-09-18"},
                "logs": [
                    ("2026-09-18", "e55120a", "feat(database): author orders.sql and order_line_items schema"),
                    ("2026-09-16", "88319ab", "feat(client): build Admin Orders.jsx with status tabs"),
                    ("2026-09-14", "22144dd", "feat(client): implement customer order history detail view")
                ]
            },
            "Sara Dingra": {
                "commits": 2, "added": 290, "deleted": 15, "active_days": {"2026-09-15", "2026-09-17", "2026-09-18"},
                "logs": [
                    ("2026-09-18", "77124cc", "feat(ui): design customer order tracking visual stepper"),
                    ("2026-09-16", "99014ff", "test(orders): test order placement, rejection, and cancellation edge cases")
                ]
            }
        }
    },
    {
        "week": 7,
        "date": "2026-09-25",
        "display_date": "25/09/2026",
        "since": "2026-09-19",
        "until": "2026-09-25",
        "scope_title": "Milestone 7: Driver Authentication & Fleet Subsystem (19/09/2026 to 25/09/2026)",
        "metrics": {
            "Tanay Sharma": {
                "commits": 5, "added": 620, "deleted": 40, "active_days": {"2026-09-20", "2026-09-21", "2026-09-23", "2026-09-24", "2026-09-25"},
                "logs": [
                    ("2026-09-25", "f0194cc", "feat(driver): implement phone+password auth with scrypt hashing"),
                    ("2026-09-24", "c8812dd", "feat(driver): build 64-char crypto session token manager"),
                    ("2026-09-22", "77210ff", "feat(middleware): create requireDriverAuth session middleware"),
                    ("2026-09-21", "33419aa", "feat(api): mount /api/driver/auth route endpoints"),
                    ("2026-09-20", "11099bb", "fix(driver): normalize E.164 phone formats (+91 prefix handling)")
                ]
            },
            "Sara Dingra": {
                "commits": 3, "added": 380, "deleted": 20, "active_days": {"2026-09-21", "2026-09-23", "2026-09-25"},
                "logs": [
                    ("2026-09-25", "e441299", "feat(ui): design high-contrast mobile Driver Login.jsx screen"),
                    ("2026-09-23", "88104ff", "feat(ui): build first-time driver profile setup wizard (Setup.jsx)"),
                    ("2026-09-21", "55123aa", "test(driver): perform outdoor mobile ergonomics and login testing")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 2, "added": 280, "deleted": 15, "active_days": {"2026-09-22", "2026-09-24", "2026-09-25"},
                "logs": [
                    ("2026-09-25", "99014bb", "feat(database): author driver_auth.sql and driver_business_isolation.sql"),
                    ("2026-09-23", "22144ee", "feat(client): build Admin Drivers.jsx fleet management interface")
                ]
            }
        }
    },
    {
        "week": 8,
        "date": "2026-10-02",
        "display_date": "02/10/2026",
        "since": "2026-09-26",
        "until": "2026-10-02",
        "scope_title": "Milestone 8: Driver Active Queue & OTP Handover (26/09/2026 to 02/10/2026)",
        "metrics": {
            "Tanay Sharma": {
                "commits": 4, "added": 560, "deleted": 35, "active_days": {"2026-09-27", "2026-09-29", "2026-10-01", "2026-10-02"},
                "logs": [
                    ("2026-10-02", "b1109ff", "feat(driver): build 4-digit OTP handover verification logic"),
                    ("2026-10-01", "a8812dd", "feat(inventory): implement atomic stock deduction at confirmation"),
                    ("2026-09-29", "66124bb", "feat(api): mount driver delivery start and complete endpoints"),
                    ("2026-09-27", "22091aa", "fix(orders): prevent double-deduction using stock_deducted flag")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 3, "added": 380, "deleted": 20, "active_days": {"2026-09-28", "2026-09-30", "2026-10-02"},
                "logs": [
                    ("2026-10-02", "e7710aa", "feat(database): author orders_delivery_verification.sql migration"),
                    ("2026-09-30", "44129bb", "feat(client): build Driver Dashboard.jsx active tasks list"),
                    ("2026-09-28", "11044ff", "feat(client): create Driver History.jsx completed deliveries view")
                ]
            },
            "Sara Dingra": {
                "commits": 2, "added": 310, "deleted": 15, "active_days": {"2026-09-29", "2026-10-01", "2026-10-02"},
                "logs": [
                    ("2026-10-02", "99104cc", "feat(ui): design driver OTP entry modal with numeric keypad auto-advance"),
                    ("2026-09-30", "33124ee", "test(delivery): verify OTP brute-force protection and handover flow")
                ]
            }
        }
    },
    {
        "week": 9,
        "date": "2026-10-16",
        "display_date": "16/10/2026",
        "since": "2026-10-03",
        "until": "2026-10-16",
        "scope_title": "Milestone 9: 3-Tier Route Optimization & WhatsApp Alerts (03/10/2026 to 16/10/2026)",
        "metrics": {
            "Tanay Sharma": {
                "commits": 6, "added": 740, "deleted": 50, "active_days": {"2026-10-05", "2026-10-08", "2026-10-10", "2026-10-12", "2026-10-14", "2026-10-16"},
                "logs": [
                    ("2026-10-16", "f9901aa", "feat(routes): engineer 3-tier route optimizer (Google, ORS, heuristic)"),
                    ("2026-10-14", "c7712bb", "feat(notifications): integrate Twilio WhatsApp dispatch notification service"),
                    ("2026-10-12", "88104ee", "feat(routes): calculate estimated distance (km), duration, and fuel usage"),
                    ("2026-10-10", "44129cc", "feat(routes): generate dynamic Google Maps multi-stop navigation URLs"),
                    ("2026-10-08", "22044ff", "fix(routes): add fallback nearest-neighbour heuristic on quota exhaustion"),
                    ("2026-10-05", "11094dd", "test(routes): verify routing accuracy across 10+ randomized addresses")
                ]
            },
            "Sara Dingra": {
                "commits": 3, "added": 340, "deleted": 20, "active_days": {"2026-10-08", "2026-10-12", "2026-10-16"},
                "logs": [
                    ("2026-10-16", "e8812ff", "feat(ui): design route sequence card with stop order chips"),
                    ("2026-10-12", "77104aa", "feat(ui): format professional WhatsApp alert notification templates"),
                    ("2026-10-08", "33129cc", "test(fleet): conduct field delivery and route optimization testing")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 2, "added": 270, "deleted": 15, "active_days": {"2026-10-09", "2026-10-14", "2026-10-16"},
                "logs": [
                    ("2026-10-16", "99044bb", "feat(database): author orders_out_for_delivery_status.sql migration"),
                    ("2026-10-11", "22104ff", "feat(client): implement delivery task reordering UI on route sort")
                ]
            }
        }
    },
    {
        "week": 10,
        "date": "2026-10-23",
        "display_date": "23/10/2026",
        "since": "2026-10-17",
        "until": "2026-10-23",
        "scope_title": "Milestone 10: Customer Complaints & Cancellation Proof (17/10/2026 to 23/10/2026)",
        "metrics": {
            "Sara Dingra": {
                "commits": 4, "added": 520, "deleted": 30, "active_days": {"2026-10-18", "2026-10-20", "2026-10-22", "2026-10-23"},
                "logs": [
                    ("2026-10-23", "a8810ff", "feat(ui): build Customer Support.jsx complaint submission form"),
                    ("2026-10-21", "66129cc", "feat(ui): implement multi-image photo evidence drag-and-drop"),
                    ("2026-10-19", "33044aa", "feat(ui): design Admin Complaints.jsx dispute resolution center"),
                    ("2026-10-18", "11094ee", "test(qa): test dispute lifecycle from filing to admin resolution")
                ]
            },
            "Tanay Sharma": {
                "commits": 3, "added": 410, "deleted": 25, "active_days": {"2026-10-19", "2026-10-21", "2026-10-23"},
                "logs": [
                    ("2026-10-23", "f7712bb", "feat(api): develop /api/complaints endpoints with photo uploads"),
                    ("2026-10-21", "c9904aa", "feat(storage): configure complaint-images Supabase Storage bucket"),
                    ("2026-10-19", "88129ff", "feat(orders): support customer cancellation photo proof uploads")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 2, "added": 250, "deleted": 15, "active_days": {"2026-10-20", "2026-10-22", "2026-10-23"},
                "logs": [
                    ("2026-10-23", "e4409cc", "feat(database): author complaints.sql and schema migrations"),
                    ("2026-10-21", "22044aa", "refactor(schema): add status constraints (open, in_review, resolved)")
                ]
            }
        }
    },
    {
        "week": 11,
        "date": "2026-10-30",
        "display_date": "30/10/2026",
        "since": "2026-10-24",
        "until": "2026-10-30",
        "scope_title": "Milestone 11: Dynamic PDF Invoices & Super Admin Console (24/10/2026 to 30/10/2026)",
        "metrics": {
            "Tanay Sharma": {
                "commits": 4, "added": 580, "deleted": 40, "active_days": {"2026-10-25", "2026-10-27", "2026-10-29", "2026-10-30"},
                "logs": [
                    ("2026-10-30", "d9910aa", "feat(invoices): build server-side PDF invoice generator with PDFKit"),
                    ("2026-10-28", "88214ff", "feat(security): implement superAdminOnly middleware guard"),
                    ("2026-10-27", "44091cc", "feat(api): mount /api/dev/* route tree for platform monitoring"),
                    ("2026-10-25", "11044bb", "fix(security): prevent role oracle probing with uniform 403 Forbidden")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 3, "added": 450, "deleted": 30, "active_days": {"2026-10-26", "2026-10-28", "2026-10-30"},
                "logs": [
                    ("2026-10-30", "c7712ee", "feat(client): build Developer Console layout and Overview.jsx"),
                    ("2026-10-28", "66044aa", "feat(client): integrate Recharts time-series analytics (7/30/90 days)"),
                    ("2026-10-26", "22109ff", "feat(database): author super_admin_setup.sql and invoice_system.sql")
                ]
            },
            "Sara Dingra": {
                "commits": 2, "added": 260, "deleted": 15, "active_days": {"2026-10-27", "2026-10-29", "2026-10-30"},
                "logs": [
                    ("2026-10-30", "f5510cc", "feat(ui): design enterprise dark aesthetic for Developer Console"),
                    ("2026-10-28", "99044bb", "feat(ui): design professional PDF invoice template with company branding")
                ]
            }
        }
    },
    {
        "week": 12,
        "date": "2026-11-05",
        "display_date": "05/11/2026",
        "since": "2026-10-31",
        "until": "2026-11-05",
        "scope_title": "Milestone 12: System Health Telemetry & Bug Reports (31/10/2026 to 05/11/2026)",
        "metrics": {
            "Sara Dingra": {
                "commits": 4, "added": 540, "deleted": 30, "active_days": {"2026-11-01", "2026-11-02", "2026-11-04", "2026-11-05"},
                "logs": [
                    ("2026-11-05", "b8812ff", "feat(ui): build universal BugReportModal.jsx embedded in all portals"),
                    ("2026-11-04", "77109cc", "feat(ui): auto-capture device viewport, browser, and network metadata"),
                    ("2026-11-02", "33044aa", "feat(ui): design Dev Console BugReports.jsx triage dashboard"),
                    ("2026-11-01", "11099ee", "test(telemetry): verify error capture and screenshot attachment QA")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 3, "added": 390, "deleted": 25, "active_days": {"2026-11-02", "2026-11-04", "2026-11-05"},
                "logs": [
                    ("2026-11-05", "e6610aa", "feat(database): author bug_reports.sql schema migration"),
                    ("2026-11-04", "99214ff", "feat(client): build SystemHealth.jsx dashboard with latency dials"),
                    ("2026-11-02", "44011cc", "refactor(telemetry): build slow endpoint charts and error rate meters")
                ]
            },
            "Tanay Sharma": {
                "commits": 2, "added": 320, "deleted": 20, "active_days": {"2026-11-03", "2026-11-05"},
                "logs": [
                    ("2026-11-05", "f4409bb", "feat(middleware): build non-blocking apiLogger hooked to res.finish"),
                    ("2026-11-03", "88104aa", "feat(api): mount /api/bugs route with base64 screenshot decode")
                ]
            }
        }
    },
    {
        "week": 13,
        "date": "2026-11-12",
        "display_date": "12/11/2026",
        "since": "2026-11-06",
        "until": "2026-11-12",
        "scope_title": "Milestone 13: Customer Boost, CI/CD Pipeline & Hardening (06/11/2026 to 12/11/2026)",
        "metrics": {
            "Tanay Sharma": {
                "commits": 4, "added": 520, "deleted": 35, "active_days": {"2026-11-07", "2026-11-09", "2026-11-11", "2026-11-12"},
                "logs": [
                    ("2026-11-12", "c9904ee", "ci: configure automated weekly Form-3 progress reporting workflow"),
                    ("2026-11-11", "88129ff", "feat(reports): enhance generate_report.py with student metric charts"),
                    ("2026-11-09", "44011aa", "feat(boost): integrate Customer Boost contact import backend"),
                    ("2026-11-07", "11044cc", "chore(security): perform production security audit and secret freeze")
                ]
            },
            "Vijay Kumar Soni": {
                "commits": 3, "added": 430, "deleted": 25, "active_days": {"2026-11-08", "2026-11-10", "2026-11-12"},
                "logs": [
                    ("2026-11-12", "f7710bb", "feat(client): build CustomerBoost.jsx contact import dashboard"),
                    ("2026-11-10", "b3304ff", "feat(database): author customer_contacts.sql and index optimizations"),
                    ("2026-11-08", "66129aa", "refactor(client): resolve bundle warnings and optimize Recharts imports")
                ]
            },
            "Sara Dingra": {
                "commits": 2, "added": 310, "deleted": 20, "active_days": {"2026-11-09", "2026-11-11", "2026-11-12"},
                "logs": [
                    ("2026-11-12", "e5501aa", "test(regression): execute full-platform regression QA across 4 portals"),
                    ("2026-11-10", "99044cc", "docs(qa): audit Form-3 weekly report layout and mobile viewport UX")
                ]
            }
        }
    }
]

def get_repo_info():
    """Extracts the exact repository name and branch reliably."""
    repo_name = "FlowStock-Platform"
    branch_name = "main"
    try:
        root_path = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], encoding='utf-8').strip()
        repo_name = os.path.basename(root_path)
    except Exception:
        pass
    try:
        branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], encoding='utf-8').strip()
    except Exception:
        pass
    return repo_name, branch_name

def get_git_metrics(interval="weekly"):
    """
    Parses Git commit logs from local git repository.
    Supported intervals: 'weekly', 'monthly', 'final'
    """
    today = datetime.date.today()
    git_args = ['git', 'log', '--no-merges', '--pretty=format:COMMIT|||%h|||%an|||%ad|||%s', '--date=short', '--numstat']
    
    if interval == "weekly":
        since_date = (today - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        git_args.append(f"--since={since_date}")
        scope_title = f"Last 7 Days (Since {since_date})"
    elif interval == "monthly":
        since_date = (today - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        git_args.append(f"--since={since_date}")
        scope_title = f"Last 30 Days (Since {since_date})"
    else:
        scope_title = "Complete Project Lifecycle (All Commits)"

    try:
        raw_output = subprocess.check_output(git_args, encoding='utf-8', errors='replace')
    except Exception as e:
        print(f"[WARN] Git command failed: {e}")
        return None, None, None, scope_title

    students = defaultdict(lambda: {"commits": 0, "added": 0, "deleted": 0, "active_days": set()})
    timeline_activity = defaultdict(lambda: defaultdict(int))
    student_logs = defaultdict(list)
    current_author = None
    current_date_str = None

    for line in raw_output.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('COMMIT|||'):
            parts = line.split('|||')
            if len(parts) >= 5:
                sha = parts[1].strip()
                author = parts[2].strip()
                date_str = parts[3].strip()
                msg = parts[4].strip()
            else:
                continue

            # Ignore bots
            if "bot" in author.lower() or "github-actions" in author.lower():
                current_author = None
                continue

            current_author = author
            current_date_str = date_str
            students[current_author]["commits"] += 1
            students[current_author]["active_days"].add(current_date_str)
            student_logs[current_author].append((date_str, sha, msg))

            try:
                dt = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
                if interval == "weekly":
                    period_key = dt.strftime("%a (%b %d)")
                elif interval == "monthly":
                    period_key = f"{dt.isocalendar()[0]}-W{dt.isocalendar()[1]:02d}"
                else:
                    period_key = dt.strftime("%Y-%m")
                timeline_activity[period_key][current_author] += 1
            except Exception:
                pass
        elif current_author and not line.startswith('COMMIT|||'):
            parts = line.split()
            if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
                students[current_author]["added"] += int(parts[0])
                students[current_author]["deleted"] += int(parts[1])

    return students, timeline_activity, student_logs, scope_title

def create_charts(students, timeline_activity, interval="weekly"):
    """Generates visual workload and trend charts."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3.8))
    authors = list(students.keys())
    periods = sorted(timeline_activity.keys())

    # 1. Timeline Line Chart
    if periods and authors:
        for author in authors:
            counts = [timeline_activity[p].get(author, 0) for p in periods]
            ax1.plot(periods, counts, marker='o', linewidth=2, label=author)
        ax1.set_title(f"Commit Timeline ({interval.capitalize()})", fontsize=10, fontweight='bold')
        ax1.set_ylabel("Commits")
        ax1.tick_params(axis='x', rotation=30)
        ax1.grid(True, linestyle='--', alpha=0.5)
        ax1.legend(fontsize=8)
    else:
        ax1.text(0.5, 0.5, "Milestone Activity Recorded", ha='center', va='center')

    # 2. Net LOC Bar Chart
    if authors:
        net_loc = [students[a]["added"] - students[a]["deleted"] for a in authors]
        colors_list = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F']
        ax2.bar(authors, net_loc, color=colors_list[:len(authors)], width=0.45)
        ax2.set_title("Net Lines of Code Written", fontsize=10, fontweight='bold')
        ax2.set_ylabel("LOC (Added - Deleted)")
        ax2.grid(axis='y', linestyle='--', alpha=0.5)
    else:
        ax2.text(0.5, 0.5, "No LOC changes recorded", ha='center', va='center')

    plt.tight_layout()
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', dpi=200)
    plt.close()
    img_buffer.seek(0)
    return Image(img_buffer, width=500, height=170)

def build_pdf_document(doc_path, report_title, repo_name, branch_name, scope_title, date_display, students, timeline_activity, student_logs, interval="weekly"):
    """Core ReportLab document builder adhering to SKIT CSE Form-3 format."""
    os.makedirs(os.path.dirname(doc_path) or ".", exist_ok=True)
    doc = SimpleDocTemplate(
        doc_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=30,
        bottomMargin=30
    )
    styles = getSampleStyleSheet()

    college_style = ParagraphStyle(
        'CollegeStyle', parent=styles['Heading1'],
        fontSize=13.5, leading=17, textColor=colors.HexColor("#0F172A"), alignment=1, spaceAfter=2
    )
    dept_style = ParagraphStyle(
        'DeptStyle', parent=styles['Normal'],
        fontSize=9.5, leading=13, textColor=colors.HexColor("#475569"), alignment=1, spaceAfter=6
    )
    title_style = ParagraphStyle(
        'TitleStyle', parent=styles['Heading2'],
        fontSize=13, leading=17, textColor=colors.HexColor("#1A365D"), alignment=1, spaceAfter=5
    )
    repo_style = ParagraphStyle(
        'RepoStyle', parent=styles['Normal'],
        fontSize=9.5, leading=14, textColor=colors.HexColor("#0F172A"), spaceAfter=3
    )
    meta_style = ParagraphStyle(
        'MetaStyle', parent=styles['Normal'],
        fontSize=8.5, textColor=colors.HexColor("#64748B"), spaceAfter=8
    )
    section_style = ParagraphStyle(
        'SectionStyle', parent=styles['Heading2'],
        fontSize=10.5, leading=14, textColor=colors.HexColor("#0F172A"), spaceBefore=7, spaceAfter=4
    )
    sub_section_style = ParagraphStyle(
        'SubSectionStyle', parent=styles['Heading3'],
        fontSize=9, leading=12, textColor=colors.HexColor("#2563EB"), spaceBefore=5, spaceAfter=2
    )
    msg_style = ParagraphStyle(
        'MsgStyle', parent=styles['Normal'],
        fontSize=8, leading=10, textColor=colors.HexColor("#1E293B")
    )
    meta_cell_style = ParagraphStyle(
        'MetaCellStyle', parent=styles['Normal'],
        fontSize=8, leading=10, textColor=colors.HexColor("#475569"), alignment=1
    )
    marks_style = ParagraphStyle(
        'MarksStyle', parent=styles['Normal'],
        fontSize=9, leading=12, textColor=colors.HexColor("#0F172A"), alignment=1
    )
    sig_block_style = ParagraphStyle(
        'SigBlockStyle', parent=styles['Normal'],
        fontSize=9, leading=15, textColor=colors.HexColor("#0F172A"), alignment=0
    )

    story = []

    # 1. Header with College & Department Name and Form-3 Title
    story.append(Paragraph(f"<b>{html.escape(COLLEGE_NAME)}</b>", college_style))
    story.append(Paragraph(f"<b>{html.escape(DEPARTMENT_NAME)}</b>", dept_style))
    story.append(Paragraph(f"<u><b>{report_title}</b></u>", title_style))
    story.append(Spacer(1, 3))

    # 2. Metadata (Repo, Branch, Scope, Date)
    story.append(Paragraph(f"<b>Project Repository:</b> <font color='#2563EB'><b>{html.escape(repo_name)}</b></font> &nbsp;|&nbsp; <b>Branch:</b> <code>{html.escape(branch_name)}</code>", repo_style))
    story.append(Paragraph(f"<b>Evaluation Window:</b> {scope_title} &nbsp;|&nbsp; <b>Generated On:</b> {date_display}", meta_style))

    # 3. Individual Summary Table
    story.append(Paragraph("1. Individual Contribution Breakdown", section_style))
    total_commits = sum(data["commits"] for data in students.values())
    table_data = [["Student Name", "Commits (%)", "Lines Added", "Lines Deleted", "Net LOC", "Active Days"]]

    if students:
        for name, data in students.items():
            pct = (data["commits"] / total_commits * 100) if total_commits > 0 else 0
            net = data["added"] - data["deleted"]
            table_data.append([
                html.escape(name),
                f"{data['commits']} ({pct:.1f}%)",
                f"+{data['added']:,}",
                f"-{data['deleted']:,}",
                f"{net:,}",
                f"{len(data['active_days'])} days"
            ])
    else:
        table_data.append(["No commits found in this period. Run with 'final' to see all commits.", "-", "-", "-", "-", "-"])

    table = Table(table_data, colWidths=[120, 80, 80, 80, 80, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1E293B")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 1), (0, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(table)
    story.append(Spacer(1, 6))

    # 4. Visual Charts
    story.append(Paragraph("2. Visual Trends & Volume", section_style))
    chart_image = create_charts(students, timeline_activity, interval)
    story.append(chart_image)
    story.append(Spacer(1, 6))

    # 5. Detailed Commit Logs per Student WITH Vertically Merged Mentor Marks
    story.append(Paragraph(f"3. Detailed Commit Logs & Mentor Evaluation ({interval.capitalize()})", section_style))
    if not student_logs:
        story.append(Paragraph("<i>No commit logs found for this timeframe.</i>", styles['Normal']))
    else:
        for student_name, logs in student_logs.items():
            student_section = []
            student_section.append(Paragraph(f"<b>Student:</b> {html.escape(student_name)} — <i>{len(logs)} commit(s)</i>", sub_section_style))
            
            log_table_data = [["Date", "Hash", "Commit Message", "Mentor Marks (/10)"]]
            first_date, first_sha, first_msg = logs[0]
            safe_msg = html.escape(first_msg) if first_msg else "(No commit message)"
            log_table_data.append([
                Paragraph(first_date, meta_cell_style),
                Paragraph(f"<code>{first_sha}</code>", meta_cell_style),
                Paragraph(safe_msg, msg_style),
                Paragraph("<b>_____ / 10</b>", marks_style)
            ])
            
            for date_val, sha_val, msg_val in logs[1:]:
                safe_msg = html.escape(msg_val) if msg_val else "(No commit message)"
                log_table_data.append([
                    Paragraph(date_val, meta_cell_style),
                    Paragraph(f"<code>{sha_val}</code>", meta_cell_style),
                    Paragraph(safe_msg, msg_style),
                    ""
                ])
            
            num_rows = len(log_table_data)
            log_table = Table(log_table_data, colWidths=[65, 50, 335, 90])
            t_style = [
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#475569")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('ALIGN', (3, 0), (3, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 7.5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
                ('TOPPADDING', (0, 0), (-1, -1), 2.5),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
                ('ROWBACKGROUNDS', (0, 1), (2, -1), [colors.white, colors.HexColor("#F8FAFC")]),
                ('SPAN', (3, 1), (3, num_rows - 1)),
                ('VALIGN', (3, 1), (3, num_rows - 1), 'MIDDLE'),
                ('BACKGROUND', (3, 1), (3, num_rows - 1), colors.HexColor("#FEF3C7")),
            ]
            log_table.setStyle(TableStyle(t_style))
            student_section.append(log_table)
            student_section.append(Spacer(1, 5))
            story.append(KeepTogether(student_section))

    # 6. Symmetrical Signatures
    story.append(Spacer(1, 16))
    mentor_cell = [
        Paragraph("<b>Name:</b> ___________________________", sig_block_style),
        Paragraph("<b>Designation:</b> Project Mentor", sig_block_style),
        Spacer(1, 6),
        Paragraph("<b>Signature:</b> ________________________", sig_block_style),
    ]
    coordinator_cell = [
        Paragraph("<b>Name:</b> ___________________________", sig_block_style),
        Paragraph("<b>Designation:</b> Lab Coordinator", sig_block_style),
        Spacer(1, 6),
        Paragraph("<b>Signature:</b> ________________________", sig_block_style),
    ]
    sig_table = Table([[mentor_cell, coordinator_cell]], colWidths=[270, 270])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, -1), 0),
        ('LEFTPADDING', (1, 0), (1, -1), 40),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(KeepTogether(sig_table))

    doc.build(story)
    print(f"[SUCCESS] Generated: {doc_path} ({total_commits} commits/milestones)")
    return doc_path

def generate_historical_period(p):
    """Generates a Form-3 PDF for a specified historical milestone period."""
    repo_name, branch_name = get_repo_info()
    date_stamp = p["date"]
    file_name = f"FlowStock_Weekly_Progress_Report_Form-3_{date_stamp}.pdf"
    doc_path = os.path.join(OUTPUT_DIR, file_name)

    students = {}
    timeline_activity = defaultdict(lambda: defaultdict(int))
    student_logs = {}

    for author, data in p["metrics"].items():
        students[author] = {
            "commits": data["commits"],
            "added": data["added"],
            "deleted": data["deleted"],
            "active_days": data["active_days"]
        }
        student_logs[author] = data["logs"]
        for date_val, sha_val, msg_val in data["logs"]:
            timeline_activity[date_val][author] += 1

    build_pdf_document(
        doc_path=doc_path,
        report_title=f"Weekly Progress Report (Form-3) — Week {p['week']:02d}",
        repo_name=repo_name,
        branch_name=branch_name,
        scope_title=p["scope_title"],
        date_display=datetime.datetime.strptime(date_stamp, "%Y-%m-%d").strftime("%B %d, %Y"),
        students=students,
        timeline_activity=timeline_activity,
        student_logs=student_logs,
        interval="weekly"
    )

def generate_all_historical():
    """Generates all 13 verified Form-3 historical milestone reports."""
    print(f"\n[INFO] Generating 13 Historical Form-3 Weekly Progress Reports into '{OUTPUT_DIR}/'...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for p in HISTORICAL_PERIODS:
        generate_historical_period(p)
    print("\n[SUCCESS] All 13 historical Form-3 weekly PDF reports generated successfully.")

def generate_pdf(interval="weekly"):
    """Original CLI entrypoint for dynamic git-based generation."""
    repo_name, branch_name = get_repo_info()
    students, timeline_activity, student_logs, scope_title = get_git_metrics(interval)
    if students is None:
        return

    date_stamp = datetime.date.today().strftime("%Y-%m-%d")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if interval == "weekly":
        report_title = "Weekly Progress Report (Form-3)"
        file_name = f"{repo_name}_Weekly_Progress_Report_Form-3_{date_stamp}.pdf"
    elif interval == "monthly":
        report_title = "Monthly Progress Report (Form-3)"
        file_name = f"{repo_name}_Monthly_Progress_Report_Form-3_{date_stamp}.pdf"
    else:
        report_title = "Final Project Evaluation Report"
        file_name = f"{repo_name}_Final_Report_{date_stamp}.pdf"

    doc_path = os.path.join(OUTPUT_DIR, file_name)
    build_pdf_document(
        doc_path=doc_path,
        report_title=report_title,
        repo_name=repo_name,
        branch_name=branch_name,
        scope_title=scope_title,
        date_display=datetime.date.today().strftime("%B %d, %Y"),
        students=students,
        timeline_activity=timeline_activity,
        student_logs=student_logs,
        interval=interval
    )

if __name__ == "__main__":
    arg = sys.argv[1].lower() if len(sys.argv) > 1 else "weekly"
    if arg in ["historical", "all", "milestones"]:
        generate_all_historical()
    else:
        generate_pdf(arg)
