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
> Users sign up and log in with an email address and password. The browser talks only to the BFF. Nginx is the only public path to FastAPI and exposes `/api/v1/*` only. The BFF calls `/auth/*` over a trusted internal connection. FastAPI turns every accepted credential into one Principal (`user_id`, `role`). Business routes authorise from that Principal and do not depend on whether the caller used a UI session or a PAT.
>
> **Database**
>
> - [x] User table: UUID id, unique email, password hash, name, role (`user` | `admin`)
> - [ ] PAT table: token hash, user id, expiry, revoked_at, created_at
> - [ ] Alembic migration off the bootstrap users stub
>
> **Keycloak**
>
> - [ ] Setup Keycloak as the IdP
> 
> **Backend —** `/auth/`* **(not routed by Nginx)**
>
> - [x] Password hashing
> - [x] User service (create, read, update, delete)
> - [x] Bootstrap admin email (config); every other signup is a basic user
> - [x] Conflict and unauthorized errors
> - [ ] BFF service credential; `/auth/*` rejects any other caller
> - [ ] Move user creation off `POST /api/v1/users` to `POST /auth/signup`
> - [ ] `POST /auth/login` validates email and password, then returns an internal user JWT
>
> **Backend —** `/api/v1/`* **(Nginx only)**
>
> - [ ] Principal dependency: internal user JWT or PAT → `user_id` and `role`; return 401 when missing, invalid, expired, or revoked
> - [ ] Require authentication on every `/api/v1` route, including health and readiness
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
> - [ ] BFF session cookie: login stores the internal user JWT; logout clears the session
> - [ ] BFF calls `/auth/*` with the service credential
> - [ ] BFF sends the internal user JWT as Bearer on `/api/v1/*`
> - [ ] Signup page
> - [ ] Login page
> - [ ] Home page: “Welcome, {name}”
> - [ ] PAT create and revoke in the UI

