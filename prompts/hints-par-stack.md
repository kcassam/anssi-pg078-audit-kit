# Où vit l'authentification, selon la techno

Indices génériques pour localiser vite le code d'auth et les points sensibles ANSSI-PG-078.
À adapter ; ce sont des points de départ de recherche, pas des règles absolues.

## Repères transverses (à grep partout)
- Hashage : `argon2`, `scrypt`, `bcrypt`, `pbkdf2`, `PBKDF2`, `MessageDigest`, `MD5`, `SHA-1/256/512`, `hashlib`, `passlib`, `password_hash`.
- RNG : `SecureRandom`, `secrets.`, `os.urandom`, `crypto.randomBytes` (bon) vs `java.util.Random`, `Math.random`, `random.` (mauvais pour un secret).
- Jetons/sessions : `jwt`, `jsonwebtoken`, `pyjwt`, `jose`, `session`, `cookie`, `Secure`, `HttpOnly`, `SameSite`.
- MFA : `otp`, `totp`, `hotp`, `webauthn`, `mfa`, `2fa`, `authenticator`, `speakeasy`, `otplib`.
- Anti-bruteforce : `rate`, `ratelimit`, `throttle`, `lockout`, `bruteforce`, `attempts`, `slowapi`, `express-rate-limit`.
- Secrets en dur : `password =`, `secret`, `api_key`, `BEGIN PRIVATE KEY`, `.env`, fichiers `*.env`, `template.env`, `application*.yml/properties`.

## Java — Spring / Spring Boot (Spring Security)
- Config : `SecurityFilterChain`/`WebSecurityConfigurerAdapter`, `application.yml/properties`.
- Hashage : `PasswordEncoder` (`BCryptPasswordEncoder`, `Argon2PasswordEncoder`, `Pbkdf2PasswordEncoder`, `DelegatingPasswordEncoder`).
- Entités `User`/`Role`, `UserDetailsService`, `AuthenticationProvider`. JWT : `jjwt`, `nimbus-jose-jwt`.

## Java — Grails (plugin Spring Security)
- `grails-app/conf/application.yml` + `application.groovy` (clés `grails.plugin.springsecurity.*`).
- Domaines `User`/`Role` ; encodeur via `grails.plugin.springsecurity.password.algorithm` ou un bean `passwordEncoder`.

## Java EE / JSP (servlets)
- `WebContent/WEB-INF/web.xml` : `<security-constraint>`, `<session-config>/<session-timeout>`, `<cookie-config>`, filtres.
- Login souvent dans une servlet ; hashage parfois « maison » (à vérifier : MD5/AES vs PBKDF2/bcrypt/argon2).
- SSO possible via PAC4J/CAS (`pac4j-*`, `cas-client`) → auth déléguée à un IdP (souvent « à évaluer »).

## Node.js / Express
- `package.json` (deps : `bcrypt`, `argon2`, `jsonwebtoken`, `express-rate-limit`, `helmet`, `passport`, `express-session`).
- Routes de login/auth, middleware ; stockage du JWT côté front (cookie `HttpOnly` vs `localStorage` = risque XSS) ; `cors`.

## Python — FastAPI / Flask / Django
- Deps : `passlib`, `argon2-cffi`, `bcrypt`, `pyjwt`/`python-jose`, `slowapi` (rate-limit).
- FastAPI : `OAuth2PasswordBearer`, dépendances d'auth, `SECRET_KEY` (en env ou en dur ?).
- Django : `AUTH_PASSWORD_VALIDATORS`, `PASSWORD_HASHERS` (Argon2/PBKDF2), `django.contrib.auth` (souvent bon par défaut).

## .NET / ASP.NET
- ASP.NET Identity (`PasswordHasher`, PBKDF2 par défaut), `Microsoft.AspNetCore.Authentication.*`, JWT bearer, Data Protection.

## PHP
- `password_hash()` / `password_verify()` (bcrypt/argon2 = bon) ; sessions PHP ; frameworks (Laravel `Hash`, Symfony Security).

## Frontends (SPA — Vue / React / Angular)
- Validation de MDP **côté client uniquement** = R20/R21/R23/R27 non garantis (contournables par appel API direct) → vérifier le **serveur**.
- Stockage du token : `localStorage`/`sessionStorage` (XSS) vs cookie `HttpOnly`/`Secure`.
- Indicateur de force (`zxcvbn`) = utile pour R27/R32, mais doit être **bloquant côté serveur** pour compter.

## Infra / déploiement (Kustomize, Helm, Terraform, nginx, ingress)
- TLS (R11) : ingress/reverse-proxy (`tls`, `websecure`, ALB HTTPS, redirection 80→443), HSTS.
- Secrets : à externaliser (ExternalSecret/Vault/SealedSecrets) — **jamais en clair** dans `*.env`/manifests committés.
