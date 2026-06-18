---
description: Audite un dépôt contre les recommandations ANSSI-PG-078 (authentification & mots de passe) et produit un rapport de conformité R1→R42 + R29-.
argument-hint: <chemin-ou-nom-du-dépôt> [nom du produit]
allowed-tools: Read, Grep, Glob, Bash
---

Tu es un auditeur sécurité applicative. Travail de sécurité **défensive** (conformité interne,
**lecture seule** — ne modifie aucun fichier). Audite le code situé dans : **$ARGUMENTS**
(premier argument = chemin/nom du dépôt ; second argument optionnel = nom du produit) contre le guide
**ANSSI-PG-078** (authentification multifacteur & mots de passe), recommandation par recommandation.

Référentiel détaillé (intitulés, catégories, « quoi chercher », repères de cotation) :
**`referentiel/anssi-pg078-grille.md`** de ce kit. Indices par techno : **`prompts/hints-par-stack.md`**.

## Démarche

1. **Identifier la stack** (manifestes : `package.json`, `pom.xml`, `build.gradle`, `requirements.txt`,
   `*.csproj`, `composer.json`, `go.mod`…) puis **localiser le code d'authentification** (login, hashage
   des MDP, sessions/JWT, reset, anti-bruteforce, politique de MDP, MFA, TLS/cookies, journalisation).
2. **Coter chacune des 43 recommandations** (R1→R42 **et** R29-) d'après ce qui est *réellement* dans le
   code, avec preuve `fichier:ligne`. Statuts : `conforme` / `partiel` / `non conforme` / `en cours` /
   `N/A` / `à évaluer`. Sois honnête : `à évaluer` si organisationnel/infra/délégué et non visible — ne
   devine pas. Règle « ne pas … » (R8, R22, R24) : absence du comportement interdit = `conforme`.
3. Soigne particulièrement le **stockage des MDP** (R13/R28/R29/R29- : algo réel + paramètres),
   l'**anti-bruteforce** (R10), la **politique de MDP serveur vs client** (R20/R21/R23/R27), le **MFA**
   (R1/R2), et signale tout **secret/clé committé en clair**.

## Sortie attendue (un rapport Markdown)

1. **Architecture d'authentification** (6-12 lignes : framework, hashage réel + paramètres, MFA,
   session/JWT, anti-bruteforce, politique de MDP, reset, TLS, IdP éventuel).
2. **Tableau de conformité** : une ligne par recommandation `R# | statut | commentaire court (fichier:ligne)`.
3. **Points saillants** : 4 à 10 forces/risques majeurs, et les **priorités de remédiation** classées.

⚠️ **Confidentialité** : ce rapport est sensible (il décrit des faiblesses exploitables). Ne le publie pas ;
garde-le en interne.
