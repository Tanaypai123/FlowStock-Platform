# FlowStock — Database Schema & Data Dictionary

The FlowStock database is hosted on **Supabase PostgreSQL** and comprises 14 core normalized tables.

---

## 1. Entity-Relationship Overview

```
auth.users (Supabase Managed)
  ├── 1:1  profiles (role, display_name)
  ├── 1:1  business_profile (admin_id, business_name, business_code)
  └── M:M  user_businesses <──> business_profile

business_profile
  ├── 1:N  inventory_items (name, stage, quantity, low_stock_alert, unit_price)
  ├── 1:N  orders (customer_id, driver_id, status, delivery_otp, otp_verified)
  ├── 1:N  deliveries (order_id, driver_id, status)
  ├── 1:N  api_logs (method, endpoint, status_code, response_time_ms)
  └── M:M  driver_business_links <──> drivers

orders
  ├── 1:N  order_line_items (inventory_item_id, item_name, quantity, unit_price)
  └── 1:1  deliveries

drivers
  ├── 1:N  driver_sessions (token, expires_at)
  └── M:M  driver_business_links

profiles (Customer)
  ├── 1:N  orders (as customer)
  ├── 1:N  complaints (order_id, message, issue_type, image_urls, status)
  └── 1:N  customer_addresses (label, region, address, is_default)
```

---

## 2. Table Specifications

### 1. `profiles`
- `id` (uuid, PK, FK to auth.users ON DELETE CASCADE)
- `role` (text, CHECK IN ('admin', 'customer', 'driver', 'super_admin'))
- `display_name` (text, nullable)
- `updated_at` (timestamptz, DEFAULT now())

### 2. `business_profile`
- `id` (uuid, PK, DEFAULT gen_random_uuid())
- `admin_id` (uuid, UNIQUE, FK to auth.users)
- `business_name` (text, NOT NULL)
- `owner_name` (text, NOT NULL)
- `phone` (text, NOT NULL)
- `email` (text, nullable)
- `address`, `warehouse_location` (text, nullable)
- `business_type` (text, Retail/Wholesale/Distributor/Manufacturer)
- `gst_number` (text, nullable)
- `logo_url` (text, nullable)
- `brand_color` (text, DEFAULT '#6366f1')
- `updates_phone` (text, NOT NULL — receives WhatsApp alerts)
- `business_code` (text, UNIQUE, alphanumeric join code)
- `created_at`, `updated_at` (timestamptz)

### 3. `user_businesses`
- `id` (uuid, PK)
- `user_id` (uuid, FK to auth.users ON DELETE CASCADE)
- `business_id` (uuid, FK to business_profile ON DELETE CASCADE)
- `role` (text, CHECK IN ('admin', 'customer', 'driver'))
- `join_source` (text, e.g. 'code', 'invite', 'admin_created')
- `created_at` (timestamptz)
- UNIQUE constraint: `(user_id, business_id)`

### 4. `inventory_items`
- `id` (uuid, PK)
- `business_id` (uuid, FK to business_profile ON DELETE CASCADE)
- `admin_id` (uuid, FK to profiles)
- `name` (text, NOT NULL)
- `stage` (text, 'raw', 'processing', 'packaged', 'ready', 'draft', 'archived')
- `quantity` (numeric, DEFAULT 0, CHECK >= 0)
- `low_stock_alert` (numeric, DEFAULT 0)
- `unit_price` (numeric, nullable)
- `unit` (text, nullable, e.g. "kg", "box")
- `description` (text, nullable)
- `image_url` (text, nullable)
- `image_urls` (text[], DEFAULT '{}')
- `updated_at` (timestamptz)

### 5. `orders`
- `id` (uuid, PK)
- `business_id` (uuid, FK to business_profile ON DELETE CASCADE)
- `customer_id` (uuid, FK to profiles)
- `driver_id` (uuid, nullable, FK to drivers)
- `status` (text, 'pending', 'confirmed', 'dispatched', 'out_for_delivery', 'delivered', 'rejected', 'cancelled')
- `region` (text)
- `final_total` (numeric, nullable)
- `discount_amount` (numeric, nullable)
- `guest_customer_name` (text, nullable)
- `delivery_otp` (text, 4-digit code)
- `otp_verified` (boolean, DEFAULT false)
- `stock_deducted` (boolean, DEFAULT false)
- Timestamps: `confirmed_at`, `dispatched_at`, `out_for_delivery_at`, `delivered_at`, `cancelled_at`

### 6. `order_line_items`
- `id` (uuid, PK)
- `order_id` (uuid, FK to orders ON DELETE CASCADE)
- `inventory_item_id` (uuid, nullable)
- `item_name` (text, snapshot at order time)
- `quantity` (numeric, NOT NULL, CHECK > 0)
- `unit_price` (numeric, NOT NULL, CHECK >= 0)

### 7. `drivers`
- `id` (uuid, PK)
- `phone` (text, UNIQUE, NOT NULL)
- `password_hash` (text, NOT NULL, scrypt/bcrypt format)
- `name` (text, nullable)
- `vehicle_details` (text, nullable)
- `license_number` (text, nullable)
- `is_profile_complete` (boolean, DEFAULT false)
- `is_active` (boolean, DEFAULT true)

### 8. `driver_sessions`
- `id` (uuid, PK)
- `driver_id` (uuid, FK to drivers ON DELETE CASCADE)
- `token` (text, UNIQUE, 64-char crypto-hex)
- `expires_at` (timestamptz, now() + 30 days)

### 9. `driver_business_links`
- `id` (uuid, PK)
- `driver_id` (uuid, FK to drivers ON DELETE CASCADE)
- `business_id` (uuid, FK to business_profile ON DELETE CASCADE)
- UNIQUE constraint: `(driver_id, business_id)`

### 10. `deliveries`
- `id` (uuid, PK)
- `order_id` (uuid, FK to orders)
- `driver_id` (uuid, FK to drivers)
- `business_id` (uuid, FK to business_profile)
- `status` (text, 'pending', 'active', 'completed', 'failed')
- `delivered_at` (timestamptz, nullable)

### 11. `complaints`
- `id` (uuid, PK)
- `customer_id` (uuid, FK to profiles)
- `business_id` (uuid, nullable)
- `order_id` (uuid, nullable)
- `message` (text, NOT NULL, CHECK length >= 10)
- `issue_type`, `product_name` (text, nullable)
- `image_urls` (text[], nullable)
- `status` (text, CHECK IN ('open', 'in_review', 'resolved'))
- `admin_comment`, `resolution_message` (text, nullable)
- `resolved_at` (timestamptz, nullable)

### 12. `customer_addresses`
- `id` (uuid, PK)
- `customer_id` (uuid, FK to profiles)
- `label` (text, "Home", "Warehouse", "Shop")
- `region` (text)
- `address` (text)
- `pincode` (text, nullable)
- `is_default` (boolean, DEFAULT false)

### 13. `bug_reports`
- `id` (uuid, PK)
- `title`, `category`, `severity` (text, NOT NULL)
- `description` (text, NOT NULL)
- `image_urls` (text[], DEFAULT '{}')
- `device_info` (jsonb, browser, viewport, platform)
- `page_url` (text)
- `reported_by_type` (text, 'admin', 'customer', 'driver')
- `reported_by_id` (uuid, verified server-side)
- `status` (text, 'open', 'in_review', 'resolved', 'wont_fix')
- `super_admin_note` (text, internal only)

### 14. `api_logs`
- `id` (uuid, PK)
- `method`, `endpoint` (text)
- `status_code` (int)
- `response_time_ms` (int)
- `business_id` (uuid, nullable)
- `error_message` (text, nullable)
- `created_at` (timestamptz, DEFAULT now())

---

## 3. SQL Migrations

The database lifecycle is tracked across 34 sequential migrations in [`supabase/sql/`](../../supabase/sql/).
