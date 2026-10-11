# Xenon Roadmap

This document serves as a RoadMap through the lifecycle of this project.

## Release Legend

### Major Release (v2.0)

- Breaking architectural changes
- Large feature sets

### Minor Release (v1.3)

- New backwards-compatible features

### Patch Release (v1.3.1)

- Bug fixes
- Performance improvements
- Documentation

## Product Roadmap

> *System Design*   
>
> Plan and Create Documentation. Includes:
>
> - ✅ Repository Structure
> - ✅ Finalise High Level Architecture
> - ✅ Finalise Coding Practices
> - ✅ Select and Finalise Tech Stack

---

> **v0.0.0**   
>
> *Project Bootstrap*   
>
> **Backend**
>
> - ✅ FastAPI project
> - ✅ Configuration system (Global YAML)
> - ✅ Logging Format
> - ✅ Exception handling + RFC 9457 API Error Details
> - ✅ Docstrings for all Files, Functions, Classes
> - ✅ Health endpoint (GET /health)
> - ✅ Dependency injection structure
>
> **Database**
>
> - ✅ PostgreSQL running
> - ✅ SQLAlchemy configured
> - ✅ Alembic configured
> - ✅ Initial migration working
> - ✅ Database connection established
>
> **Development**
>
> - ✅ Docker Compose
> - ✅ Ruff
> - ✅ mypy
> - ✅ GitHub Actions
>
> **Frontend**
>
> - ✅ NextJS project

---

> **v0.1.0**
>
> *User account management, authentication, and authorisation*
>
> Users authenticate through Keycloak using OpenID Connect. The browser talks only to the BFF. Nginx is the only public path to FastAPI and exposes `/api/v1/*` only. The BFF calls `/auth/*` over a trusted internal connection. FastAPI turns every accepted credential into one Principal (`user_id`, `role`). Business routes authorise from that Principal and do not depend on whether the caller used a UI session or a PAT.
>
> **Database**
>
> - [x] User table: UUID id, unique email, name, role, Keycloak subject
> - [ ] PAT table: token hash, user id, expiry, revoked_at, created_at
> - [x] Alembic migration off the bootstrap users stub
>
> **Keycloak / BFF**
>
> - [x] Configure Keycloak as the OIDC identity provider
> - [x] BFF login and signup flows use Keycloak
> - [x] BFF provisions users through `/auth/provision` using the service credential
> - [ ] Show the authenticated user's name on the home page
> 
> **Backend —** `/auth/`* **(not routed by Nginx)**
>
> - [x] User service (create, read, update, delete)
> - [x] Bootstrap admin email (config); every other signup is a basic user
> - [x] Conflict and unauthorized errors
> - [x] BFF service credential; `/auth/*` rejects any other caller
> - [x] Provision a Xenon user through internal `POST /auth/provision` after Keycloak sign-in
> - [ ] Define and implement the API credential handoff from the BFF to FastAPI (validated Keycloak access token or short-lived internal user JWT)
>
> **Backend —** `/api/v1/`* **(Nginx only)**
>
> - [ ] Principal dependency: validated API credential or PAT → `user_id` and `role`; return 401 when missing, invalid, expired, or revoked
> - [ ] Require authentication on business `/api/v1` routes; define health and readiness access separately for infrastructure checks
> - [ ] `GET`, `PATCH`, `DELETE /api/v1/users/me`, scoped to the authenticated user
> - [ ] `POST /api/v1/pats` issues a PAT once and stores only its hash
> - [ ] `DELETE /api/v1/pats/{id}` revokes a PAT owned by the authenticated user
>
> **Edge**
>
> - [ ] Nginx reverse proxy as the only public entry to FastAPI
> - [ ] Nginx proxies `/api/v1/*` and does not expose `/auth/*`
>
> **Frontend**
>
> - [ ] BFF session cookie: maintain the Keycloak-backed session and clear it on logout
> - [ ] BFF sends the selected API credential as Bearer on `/api/v1/*`
> - [x] Signup page
> - [x] Login page
> - [ ] PAT create and revoke in the UI

