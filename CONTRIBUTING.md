# Contributing to FlowStock

Thank you for contributing to **FlowStock: B2B Inventory Management & Logistics SaaS Platform**. To ensure code quality, security, and consistent collaboration across all team members, please adhere to the following development guidelines.

---

## 1. Code of Conduct & Standards

- **Conventional Commits:** Write clear, meaningful commit messages using standardized prefixes:
  - `feat:` A new feature or capability
  - `fix:` A bug fix
  - `refactor:` Code restructuring without functional changes
  - `docs:` Documentation updates or weekly reports
  - `test:` Adding or updating tests
  - `style:` Formatting, whitespace, or visual styling
  - `chore:` Maintenance, dependency updates, or build configuration
  - `perf:` Performance improvements
- **No Artificially Inflated Commits:** Commits must represent genuine, logical units of work.
- **Commit Authorship:** Author attribution must reflect real individual contribution.

---

## 2. Environment & Secret Management

- **NEVER commit sensitive credentials:**
  - `.env`, `.env.production`, `.env.local`
  - Database service-role keys, JWT secrets, passwords, private keys (`.pem`, `.key`)
- **Use `.env.example`** to document required environment variables with dummy/placeholder values.
- Verify `.gitignore` before every commit.

---

## 3. Monorepo Architecture

FlowStock is organized as an npm workspaces monorepo:

```
FlowStock/
├── client/     # React 19 + Vite + Tailwind CSS SPA
├── server/     # Node.js 24 + Express ESM API server
├── shared/     # @flowstock/shared (TypeScript types & constants)
├── supabase/   # SQL migrations and schema definitions
├── docs/       # Architecture, database, and project documentation
├── reports/    # Automated weekly and consolidated progress reports
└── scripts/    # Automation and reporting utilities
```

### Development Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Fill in local or development Supabase & service keys
   ```

3. **Build shared packages:**
   ```bash
   npm run build --workspace shared
   ```

4. **Launch development environment:**
   ```bash
   npm run dev
   # Concurrently starts client (Vite on 5173) and server (Express on 8000)
   ```

---

## 4. Code Style & Review Guidelines

### Backend Guidelines
- Use Express 4.x ESM modules (`import`/`export`).
- Always route authentication through appropriate middleware (`requireAuth`, `requireAdmin`, `requireDriverAuth`, `superAdminOnly`).
- Ensure all business-scoped routes resolve and validate `x-business-id` to prevent multi-tenant data leakage.
- Return standardized API responses:
  - Success: `{ "success": true, "data": ... }`
  - Error: `{ "success": false, "error": "message" }`
  - List: `{ "success": true, "data": [...], "count": N }`

### Frontend Guidelines
- Use React 19 functional components and hooks.
- Handle loading, error, and empty states explicitly.
- Protect client routes with `ProtectedRoute`, `SuperAdminRoute`, or `DriverProtectedRoute`.
- Ensure mobile responsiveness across phones, tablets, and desktops using Tailwind CSS.

### Database Guidelines
- Never alter existing historical migration files in `supabase/sql/`. Add new numbered/dated SQL migrations for schema modifications.
- Ensure foreign keys include proper cascade behaviors (`ON DELETE CASCADE` or `ON DELETE SET NULL`).
- Maintain Row Level Security (RLS) policies where applicable.

---

## 5. Reporting & Quality Assurance

- Weekly progress reporting is automated through `.github/workflows/weekly-progress-report.yml` and `scripts/generate_report.py`.
- Form-3 weekly PDF reports and markdown logs are stored in `reports/weekly/`.
- Consolidated milestone evaluations are stored in `reports/consolidated/`.
