# Best Practices Guide
This document contains the best practices and rules to be followed throughout the development of Xenon.


----
## Python Coding Standards

1. Strict type hints to be used everywhere.
2. Prefer functions by default. Each function should have a single responsibility.
3. Use Pydantic models (or dataclasses where validation is unnecessary) to represent structured data.
4. Introduce classes only when something has state, identity, or owns a resource.
5. All configuration must be accessed through a single configuration module. Configuration may originate from YAML files, environment variables, or secret stores, but application code should never hardcode configuration values.
6. Follow PEP 8 conventions:
   - `snake_case` for variables and functions
   - `PascalCase` for classes
   - `UPPER_CASE` for constants
7. Use structured logging instead of `print()` statements.
8. Catch specific exceptions, log them appropriately, and avoid swallowing errors.
9. Every Function/Class must have a docstring explaining its purpose.
10. Use automated tooling: (`Ruff`) to enforce formatting, linting and type checking.


----
## TypeScript Coding Standards

1. Enable strict mode (`"strict": true`) and never disable type checking to silence errors.
2. Avoid `any`. Prefer `unknown` when the type is genuinely unknown.
3. Prefer `type` aliases by default. Use `interface` only when we expect declaration merging or extensibility.
4. Prefer functions by default. Introduce classes only when modelling stateful objects or abstractions.
5. Model our domain using explicit types instead of loosely typed objects.
6. Never duplicate type definitions. Reuse existing types through composition (`Pick`, `Omit`, `Partial`, `Record`, etc.).
7. Load all configuration through a central configuration module. Never hardcode configuration values.
8. Follow consistent naming conventions:
    - `camelCase` for variables/functions
    - `PascalCase` for types, interfaces, classes and React components
    - `UPPER_CASE` for constants
9. Prefer immutable data (`const`, `readonly`) unless mutation is required.
10. Use structured logging instead of `console.log()` for application logging.
11. Catch specific errors, provide meaningful messages, and avoid swallowing exceptions.
12. Use ESLint + Prettier to enforce formatting and code quality automatically.
13. Write JSDoc comments only for public APIs or non-obvious logic.
14. Never ignore Promise rejections. Always `await` asynchronous operations or explicitly handle them.


---
## REST API Design Best Practices
1. Model endpoints around resources (nouns), not actions (verbs).
2. Use the correct HTTP methods:
    - `GET` → Read
    - `POST` → Create
    - `PUT` → Replace
    - `PATCH` → Partial Update
    - `DELETE` → Delete
3. Use plural resource names.
4. Use path parameters only for resource identifiers. Use query parameters for filtering, sorting and pagination.
5. Always return consistent response schemas.
6. Use appropriate HTTP status codes.
7. Validate all request payloads before reaching business logic.
8. Return structured error responses with machine-readable error codes.
9. Never expose internal implementation details (database IDs, stack traces, SQL errors).
10. Make endpoints idempotent where HTTP semantics require it.
11. Support pagination for collection endpoints.
12. Version APIs explicitly (`/api/v1/...`) once they become public.


----
## Database Schema Design Best Practices

1. Design the data model before creating tables.
2. Model real-world entities, not application screens.
3. Use singular table names (`user`, `document`, `workspace`).
4. Use UUIDs as primary keys unless auto-increment IDs are explicitly justified.
5. Every table should have:
    - `id`
    - `created_at`
    - `updated_at`
6. Use foreign keys to enforce relationships.
7. Normalize data first. Denormalize only when performance requires it.
8. Avoid storing derived or duplicate data unless intentionally cached.
9. Use appropriate data types. Never store numbers, dates or booleans as strings.
10. Make nullable columns intentional.
11. Add constraints wherever possible (`NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`).
12. Create indexes based on query patterns, not assumptions.
13. Use junction tables for many-to-many relationships.
14. Store timestamps in UTC.
15. Every schema change must be applied through migrations.


----
## General Rules
1. Commit Message Format: **Conventional Commits Specification**

```shell
git commit -m "feat: Feature Details" -m "Here goes the Feature Description" 
```

```text
feat: Adds a brand new feature to the codebase

fix: Patches a bug or fixes an error

docs: Changes or additions to documentation files only

style: Formatting, missing semi-colons, or white-space changes

refactor: Code changes that neither fix a bug nor add a feature

chore: Updates to build tasks, package dependencies, or .gitignore
```