-- =============================================================================
-- Portfolio app: PostgreSQL DDL + optional RLS (Supabase SQL Editor)
-- =============================================================================
--
-- Preferred: create ALL Django tables (auth, admin, portfolio, sessions, …)
-- with Django, then use this file only if you need RLS for PostgREST/anon:
--
--   cd backend
--   python manage.py migrate
--
-- If you run the CREATE TABLE section below on an empty database WITHOUT
-- running `migrate`, Django will be out of sync. Use one approach, not both
-- for the same tables.
--
-- Mixed approach that works:
--   1) Run `migrate` first (creates portfolio_* + django_migrations rows).
--   2) Then run only the RLS section here (enable RLS + policies).
--
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 1) Final `portfolio_*` table definitions (PostgreSQL / Supabase)
--    Matches Django models after migration portfolio/0003.
-- -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS portfolio_education (
    id BIGSERIAL PRIMARY KEY,
    institution VARCHAR(100) NOT NULL,
    degree VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS portfolio_experience (
    id BIGSERIAL PRIMARY KEY,
    role VARCHAR(100) NOT NULL,
    company VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS portfolio_skill (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Django uses quoted mixed-case column names for these fields:
CREATE TABLE IF NOT EXISTS portfolio_project (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    technologies VARCHAR(200) NOT NULL,
    "Live_link" VARCHAR(200) NULL,
    "Github_link" VARCHAR(200) NULL,
    image VARCHAR(100) NULL
);

CREATE TABLE IF NOT EXISTS portfolio_certification (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    organization VARCHAR(100) NOT NULL,
    issue_date DATE NOT NULL,
    description TEXT NOT NULL,
    credential_url VARCHAR(200) NULL,
    logo VARCHAR(100) NULL
);

-- -----------------------------------------------------------------------------
-- 2) Optional Row Level Security (Supabase PostgREST / anon / authenticated)
--
-- Django’s DB user (often the `postgres` role) typically BYPASSES RLS, so
-- your API server keeps working. These policies matter if the browser calls
-- Supabase REST or Realtime on these tables with the anon key.
--
-- Uncomment and run AFTER tables exist (usually AFTER migrate).
-- -----------------------------------------------------------------------------

ALTER TABLE portfolio_project ENABLE ROW LEVEL SECURITY;
ALTER TABLE portfolio_education ENABLE ROW LEVEL SECURITY;
ALTER TABLE portfolio_experience ENABLE ROW LEVEL SECURITY;
ALTER TABLE portfolio_skill ENABLE ROW LEVEL SECURITY;
ALTER TABLE portfolio_certification ENABLE ROW LEVEL SECURITY;

-- Public read (adjust if you want auth-only reads)
CREATE POLICY "portfolio_project_select_public"
  ON portfolio_project FOR SELECT TO anon, authenticated
  USING (true);

CREATE POLICY "portfolio_education_select_public"
  ON portfolio_education FOR SELECT TO anon, authenticated
  USING (true);

CREATE POLICY "portfolio_experience_select_public"
  ON portfolio_experience FOR SELECT TO anon, authenticated
  USING (true);

CREATE POLICY "portfolio_skill_select_public"
  ON portfolio_skill FOR SELECT TO anon, authenticated
  USING (true);

CREATE POLICY "portfolio_certification_select_public"
  ON portfolio_certification FOR SELECT TO anon, authenticated
  USING (true);

-- No INSERT/UPDATE/DELETE for anon (writes only via Django / service role)
-- (Omit policies for those operations = denied for anon when RLS is on.)
