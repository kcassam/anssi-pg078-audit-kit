# Prompt d'audit ANSSI-PG-078 (réutilisable)

Donnez ce prompt à un LLM en remplaçant `{{PRODUIT}}` et `{{CHEMIN}}`. Il est auto-suffisant (la grille
est incluse). Voir aussi `../prompts/hints-par-stack.md` pour des indices selon la techno.

---

Tu es un auditeur sécurité applicative. Travail de sécurité **défensive** (conformité interne, lecture
seule — **ne modifie aucun fichier**). Évalue la conformité du produit **{{PRODUIT}}** (code dans
`{{CHEMIN}}`) au guide **ANSSI-PG-078** (authentification multifacteur & mots de passe), recommandation
par recommandation.

## Méthode

1. **Localise** tout le code d'authentification : login, gestion des comptes/rôles, **hashage des mots
   de passe**, sessions/JWT, reset de MDP, anti-bruteforce, politique de MDP, MFA/OTP, config TLS/cookies,
   journalisation. Sers-toi de grep/glob puis lis les fichiers clés.
2. Pour **chaque** recommandation ci-dessous, donne un statut fondé **uniquement** sur ce que tu as
   réellement vu dans le code/config. Cite la preuve `fichier:ligne`. N'invente rien.

## Statuts

`conforme` / `partiel` / `non conforme` / `en cours` / `N/A` / `à évaluer`.

- `à évaluer` = indéterminable ici (organisationnel, infra/reverse-proxy, ou délégué à un IdP/SSO/LDAP
  externe non visible) — sois honnête.
- Règle « ne pas … » (R8, R22, R24) : absence du comportement interdit = `conforme`.

## Recommandations à évaluer (R1 → R42 ET R29-) — [quoi chercher]

- R1 [MFA] 2ᵉ facteur (TOTP/OTP/WebAuthn) ou IdP imposant MFA ; mono-facteur = non conforme.
- R2 [Auth fort] facteurs forts vs simple MDP.
- R3 [Analyse de risque] organisationnel → à évaluer.
- R4 [Création env. maîtrisé] création des comptes/MDP initiaux.
- R5 [RNG robuste] CSPRNG (SecureRandom / secrets / os.urandom / crypto.randomBytes) vs Random/Math.random.
- R6 [Remise canaux sûrs] secret initial pas en clair/prévisible/mutualisé.
- R7 [Renouvellement] changement/renouvellement de MDP.
- R8 [Pas de SMS] absence = conforme.
- R9 [Historiques] journalisation auth succès/échec, audit.
- R10 [Limiter tentatives] verrouillage/compteur/throttling/captcha.
- R11 [Canal sûr/TLS] HTTPS imposé, cookies Secure/HttpOnly/SameSite, HSTS (infra → à évaluer si non visible).
- R12 [Durée session] timeout de session / TTL JWT.
- R13 [Protéger données stockées] hashage MDP (R28/R29) + secrets externalisés (pas en dur).
- R14 [Pas d'info échec] message de login générique.
- R15 [Expiration facteurs] TTL tokens (reset/OTP/JWT/session) + usage unique du token de reset.
- R16 [Politique d'utilisation] organisationnel → à évaluer.
- R17 [Sensibilisation] organisationnel → à évaluer/N/A.
- R18 [Révocation] désactivation compte, logout invalidant la session, révocation token.
- R19 [Délais révocation] invalidation immédiate (JWT auto-portés non révocables sans denylist).
- R20 [Politique MDP] validateur côté serveur (pas seulement client).
- R21 [Longueur min] longueur minimale côté serveur (viser ≥ 12 sans MFA).
- R22 [Pas de longueur max] absence de borne < 64 = conforme.
- R23 [Complexité] règles de complexité côté serveur.
- R24 [Pas d'expiration par défaut] absence d'expiration forcée = conforme.
- R25 [Expiration privilèges 1-3 ans] pour comptes admin.
- R26 [Révocation immédiate compromission] forcer reset/révoquer.
- R27 [Robustesse création] blocklist/dictionnaire/zxcvbn/HIBP bloquant côté serveur.
- R28 [Sel ≥128 bits/compte] sel aléatoire par compte (bcrypt/argon2/scrypt/pbkdf2 l'intègrent).
- R29 [Memory-hard] Argon2/scrypt = conforme ; bcrypt/PBKDF2 = partiel ; MD5/SHA nu ou chiffrement réversible = non conforme. Précise l'algo RÉEL + paramètres.
- R29- [PBKDF2 à défaut] PBKDF2 itérations suffisantes = conforme ; N/A si Argon2/scrypt déjà utilisé.
- R30 [Recouvrement] flux « mot de passe oublié ».
- R31 [Coffre-fort] souvent N/A.
- R32–R36 [Utilisateur] N/A sauf guidage applicatif (ex. indicateur de force).
- R37 [Utilisateur – pas d'info perso] N/A sauf contrôle applicatif (interdit login/e-mail/nom dans le MDP).
- R38 [Utilisateur – changer MDP défaut] N/A sauf si l'appli force le changement du MDP initial.
- R39 [Possession certifié] souvent N/A.
- R40–R42 [Inhérent/biométrie] N/A si pas de biométrie.

## Format de sortie (exact)

### Architecture d'authentification

<6-12 lignes : framework, où vit l'auth, algo de hashage RÉEL + paramètres, MFA, session/JWT (secret en env ou en dur ? expiration ? stockage côté client ?), anti-bruteforce, politique de MDP (serveur vs client), reset, TLS/cookies, IdP éventuel.>

### Verdicts

```json
{"R1":{"statut":"…","preuve":"fichier:ligne","commentaire":"…"}, "…": {…}, "R29-":{…}, "…": {…}, "R42":{…}}
```

(inclure les **43 clés** R1..R42 + R29- ; `commentaire` ≤ 160 caractères, factuel ; `preuve` = `fichier:ligne` ou `—`)

### Points saillants

- 4 à 10 forces/risques majeurs, chacun avec `fichier:ligne`. Signale tout **secret/clé committé en clair**.

CONTRAINTE : lecture seule, ne modifie aucun fichier.
