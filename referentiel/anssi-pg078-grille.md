# Grille d'audit ANSSI-PG-078 (R1 → R42 + R29-)

Pour chaque recommandation : l'**intitulé**, la **catégorie**, **quoi chercher dans le code**, et les
**repères de cotation**. Référentiel : ANSSI-PG-078 v2.0 (oct. 2021), pages 43-44.

## Vocabulaire de cotation

`conforme` · `partiel` · `non conforme` · `en cours` · `N/A` · `à évaluer`

- **à évaluer** = indéterminable depuis le code : organisationnel, infra/reverse-proxy, ou **délégué à
  un IdP/SSO/LDAP externe** non visible. Soyez honnête, ne devinez pas.
- Recommandations « ne pas … » (R8, R22, R24) : **absence** du comportement interdit = **conforme**.
- Toujours citer la preuve `fichier:ligne` pour une cotation autre que `à évaluer`.

## La grille

| R# | Recommandation | Catégorie | Quoi chercher dans le code | Repères de cotation |
|---|---|---|---|---|
| R1 | Privilégier l'authentification multifacteur | MFA | 2ᵉ facteur : TOTP/HOTP, OTP e-mail, WebAuthn/FIDO2, app mobile ; ou IdP imposant le MFA | MFA dispo/activable = conforme ; optionnel/partiel = partiel ; mono-facteur MDP = non conforme |
| R2 | Privilégier des moyens d'authentification forts | MFA | Facteurs forts (certificat, FIDO2, app) vs simple MDP | facteur fort = conforme ; MDP seul = non conforme |
| R3 | Conduire une analyse de risque | Analyse de risque | — (organisationnel) | à évaluer |
| R4 | Créer les facteurs dans un environnement maîtrisé | Cycle de vie – Création | Mode de création des comptes/MDP initiaux (admin vs auto-inscription publique) | provisioning maîtrisé = conforme |
| R5 | Générer l'aléa avec un RNG robuste | Cycle de vie – Création | CSPRNG (`SecureRandom` Java, `secrets`/`os.urandom` Python, `crypto.randomBytes` Node) vs `Random`/`Math.random` pour OTP, tokens, sels | CSPRNG partout = conforme ; RNG non sûr = non conforme |
| R6 | Remettre les facteurs via des canaux sécurisés | Cycle de vie – Création | Remise du secret initial : pas en clair, pas prévisible, pas mutualisé | secret en clair/prévisible = non conforme |
| R7 | Processus de renouvellement des facteurs | Cycle de vie – Renouvellement | Flux de changement de MDP / renouvellement de facteur | présent = conforme |
| R8 | Ne pas utiliser le SMS comme canal de réception | Cycle de vie – Transmission | Usage du SMS comme canal d'un facteur | absence de SMS = conforme |
| R9 | Conserver les historiques d'utilisation | Cycle de vie – Transmission | Journalisation des auth (succès/échec), dernière connexion, audit | journalisation complète = conforme |
| R10 | Limiter dans le temps le nb de tentatives | Cycle de vie – Transmission | Anti-bruteforce : verrouillage, compteur d'échecs, throttling/rate-limit, captcha | mécanisme actif = conforme ; aucun = non conforme |
| R11 | Authentifier via un canal sécurisé | Cycle de vie – Transmission | HTTPS imposé, cookies `Secure`/`HttpOnly`/`SameSite`, HSTS, TLS ingress | souvent infra → à évaluer si non visible |
| R12 | Limiter la durée de validité d'une session | Cycle de vie – Transmission | Timeout de session / TTL du JWT | timeout défini et raisonnable = conforme |
| R13 | Protéger les données d'auth stockées | Cycle de vie – Transmission | Hashage des MDP (cf R28/R29) + protection des secrets (clés, tokens en clair/en dur ?) | hashage fort + secrets externalisés = conforme |
| R14 | Ne pas divulguer d'info sur l'échec | Cycle de vie – Transmission | Message de login générique (ne révèle pas l'existence du compte), y compris au reset | message générique = conforme |
| R15 | Définir un délai d'expiration des facteurs | Cycle de vie – Transmission | TTL des tokens (reset, OTP, JWT, session) ; usage unique du token de reset | TTL définis = conforme |
| R16 | Définir une politique d'utilisation des facteurs | Cycle de vie – Transmission | — (organisationnel) | à évaluer |
| R17 | Sensibiliser les utilisateurs | Cycle de vie – Transmission | — (organisationnel) | à évaluer / N/A |
| R18 | Processus de révocation des facteurs | Cycle de vie – Révocation | Désactivation de compte, logout invalidant la session, révocation de token/JWT | révocation possible = conforme |
| R19 | Délais adaptés de prise en compte des révocations | Cycle de vie – Révocation | Invalidation immédiate des sessions/tokens (JWT auto-portés = non révocables sans denylist) | invalidation immédiate = conforme |
| R20 | Politique de sécurité des mots de passe | Mot de passe – Politique | Validateur/politique **côté serveur** (pas seulement client) | politique serveur = conforme ; client seulement = partiel/non conforme |
| R21 | Imposer une longueur minimale | Mot de passe – Longueur | Longueur min **côté serveur** (viser ≥ 12 sans MFA) | min serveur suffisant = conforme |
| R22 | Ne pas imposer de longueur maximale | Mot de passe – Longueur | Bornage max (`maxlength`, regex `{x,y}`, troncature) | aucune borne < 64 = conforme |
| R23 | Règles de complexité | Mot de passe – Complexité | Règles de complexité **côté serveur** | complexité serveur = conforme |
| R24 | Pas d'expiration par défaut (comptes non sensibles) | Mot de passe – Expiration | Expiration périodique forcée (déconseillée par l'ANSSI hors compromission) | absence d'expiration forcée = conforme |
| R25 | Expiration des MDP des comptes à privilèges (1-3 ans) | Mot de passe – Expiration | Expiration définie pour comptes admin/privilégiés | expiration 1-3 ans = conforme |
| R26 | Révocation immédiate si compromission | Mot de passe – Expiration | Capacité à forcer un reset / révoquer un MDP | forçage possible = conforme |
| R27 | Contrôler la robustesse à la création | Mot de passe – Robustesse | Blocklist/dictionnaire, zxcvbn, HIBP, MDP communs — **bloquant côté serveur** | contrôle serveur = conforme ; client seulement = partiel |
| R28 | Sel aléatoire ≥ 128 bits, par compte | Stockage | Sel aléatoire par compte (bcrypt/scrypt/argon2/pbkdf2 l'intègrent) | sel ≥ 128 bits/compte = conforme ; pas de sel = non conforme |
| R29 | Dérivation memory-hard (Argon2 / scrypt) | Stockage | Algo de hashage réel | Argon2/scrypt = conforme ; bcrypt/PBKDF2 = partiel (cf R29-) ; SHA/MD5 nu ou chiffrement réversible = non conforme |
| R29- | À défaut, PBKDF2 | Stockage | PBKDF2 avec nb d'itérations suffisant (≥ reco OWASP) | PBKDF2 bien dimensionné = conforme ; sinon N/A si Argon2/scrypt déjà utilisé |
| R30 | Proposer une méthode de recouvrement d'accès | Recouvrement | Flux « mot de passe oublié » / réinitialisation | présent = conforme |
| R31 | Mettre à disposition un coffre-fort de MDP | Coffre-fort | Coffre-fort fourni aux utilisateurs | souvent N/A |
| R32 | [Utilisateur] Mots de passe robustes | Utilisateurs | N/A sauf indicateur de force fourni par l'appli | N/A par défaut |
| R33 | [Utilisateur] Un MDP différent par service | Utilisateurs | côté utilisateur | N/A |
| R34 | [Utilisateur] Utiliser un coffre-fort | Utilisateurs | côté utilisateur | N/A |
| R35 | [Utilisateur] Protéger ses MDP | Utilisateurs | côté utilisateur | N/A |
| R36 | [Utilisateur] MDP robuste pour la messagerie | Utilisateurs | côté utilisateur | N/A |
| R37 | [Utilisateur] Pas d'information personnelle | Utilisateurs | Contrôle applicatif interdisant login/e-mail/nom dans le MDP | N/A sauf contrôle applicatif |
| R38 | [Utilisateur] Changer les MDP par défaut | Utilisateurs | L'appli force-t-elle le changement du MDP initial à la 1ʳᵉ connexion ? | N/A sauf si forçage présent/attendu |
| R39 | Facteur de possession qualifié/certifié | Facteur de possession | Token matériel/carte à composant certifié | souvent N/A |
| R40 | Facteur inhérent pas en mono-facteur | Facteur inhérent | Biométrie | N/A si pas de biométrie |
| R41 | Facteur inhérent + facteur fort en MFA | Facteur inhérent | Biométrie | N/A si pas de biométrie |
| R42 | Enrôlement biométrie en personne | Facteur inhérent | Biométrie | N/A si pas de biométrie |

> Note R29/R29- : l'ANSSI privilégie une fonction **memory-hard** (Argon2id, scrypt) pour R29, et accepte
> **PBKDF2** comme repli (R29-). En pratique : Argon2id/scrypt → R29 conforme ; PBKDF2 bien dimensionné →
> R29 *partiel* + R29- *conforme* ; bcrypt → R29 *partiel* ; MD5/SHA nu ou chiffrement réversible → non conforme.
