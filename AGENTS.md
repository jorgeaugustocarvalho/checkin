# Engineering & Architecture Guidelines

This repository follows Clean Architecture principles.

The AI reviewer (Codex) must enforce architectural boundaries and engineering quality standards described below.

---

# 1. Global Rules

## Scope Control
- Do NOT modify files outside the scope of the PR.
- Do NOT perform opportunistic refactors.
- Architectural changes require explicit justification in the PR description.

## Tests
- Any business logic change MUST include tests.
- New features MUST include at least one test covering the happy path.
- Bug fixes MUST include a regression test.
- If tests are not added, the PR must explain why.

## Security & Safety
- Never log secrets or PII.
- Handle exceptions explicitly.
- Do not expose internal stack traces in HTTP responses.

---

# 2. Architectural Boundaries (Strict Enforcement)

The project structure is:

app/
  domain/
  application/
  infrastructure/
  main.py

The AI reviewer must flag any violation of these boundaries.

---

## 2.1 Domain Layer (app/domain)

Purpose:
- Pure business rules.

Rules:
- MUST NOT import from infrastructure or web layers.
- MUST NOT depend on FastAPI, SQLAlchemy, or external frameworks.
- Entities must contain behavior, not just data.
- Repository definitions here are interfaces only.

Tests:
- Prefer pure unit tests.
- No framework dependencies.

Flag as violation if:
- ORM models appear in domain.
- HTTP objects appear in domain.
- Database session usage appears in domain.

---

## 2.2 Application Layer (app/application)

Purpose:
- Orchestrates use cases.
- Coordinates domain objects.

Rules:
- MUST depend only on domain.
- MUST NOT depend on infrastructure directly.
- Use explicit input/output objects (DTOs or dataclasses).
- One use case = one clear responsibility.

Flag as violation if:
- SQLAlchemy session appears here.
- FastAPI request/response objects appear here.

---

## 2.3 Infrastructure Layer (app/infrastructure)

Purpose:
- Implements domain interfaces.
- Contains ORM, database, and external integrations.

Rules:
- Repository implementations must implement domain interfaces.
- No business rules allowed.
- Conversion between ORM models and domain entities must be explicit.
- Schema changes require Alembic migration.

Flag as violation if:
- Business decisions appear in repository implementations.
- Domain logic is duplicated here.

---

## 2.4 Web Layer (app/infrastructure/web)

Purpose:
- HTTP concerns only.

Rules:
- Routes must call application use cases.
- No business logic inside routes.
- Map domain exceptions to proper HTTP responses.
- Validate input using schemas.

Flag as violation if:
- Complex logic appears inside route handlers.
- Direct database calls occur inside routes.

---

# 3. Pull Request Review Checklist

When reviewing a PR, the AI must verify:

- Is architecture respected?
- Are responsibilities properly separated?
- Are tests included and meaningful?
- Is error handling explicit?
- Is there risk of tight coupling?

If architectural violation is detected, clearly explain why and suggest correction.

---

# 4. Code Quality

- Prefer explicit over implicit behavior.
- Avoid unnecessary abstractions.
- Keep functions small and focused.
- Use clear naming aligned with business language.