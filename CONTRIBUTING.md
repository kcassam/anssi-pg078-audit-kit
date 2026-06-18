# Contribuer

Merci de votre intérêt ! Ce kit vise à rester une **méthode générique et réutilisable** d'audit de
conformité ANSSI-PG-078 (authentification & mots de passe). Toute amélioration est bienvenue.

## ⚠️ Règle d'or — à lire avant toute contribution

**Ne jamais inclure de données confidentielles.** Aucune contribution ne doit contenir :
- un **résultat d'audit réel**, une faille concrète d'un système identifiable ;
- un **secret**, mot de passe, clé, jeton ;
- une référence `fichier:ligne` pointant un dépôt réel privé ;
- un **nom** de produit, d'équipe, de personne, ou une **URL de dépôt interne**.

Les exemples doivent être **entièrement fictifs**. Toute PR contenant ce type de donnée sera refusée.

## Comment contribuer

1. Ouvrez une **issue** pour discuter de l'ajout/correction (nouvelle techno, précision sur une reco,
   correction de cotation, traduction…).
2. Proposez une **pull request** ciblée, avec un message clair. La documentation est rédigée en
   **français** (le README a une version EN).

## Contributions bienvenues

- **Grille** (`referentiel/anssi-pg078-grille.md`) : précisions « quoi chercher dans le code », repères de cotation, références ANSSI.
- **Indices par stack** (`prompts/hints-par-stack.md`) : nouvelles technos, librairies, anti-patterns.
- **Prompt / commande** (`prompts/audit-agent.md`, `.claude/commands/audit-anssi.md`).
- **Modèles** (`templates/`) : autres formats de tableau (CSV, autre wiki…).
- **Traductions** (anglais des autres fichiers, autres langues).

## Style

- Markdown, français par défaut.
- Rester aligné sur le guide **ANSSI-PG-078** : citer la recommandation concernée (R#).
- Garder le kit léger : « fichiers + prompts », sans dépendance lourde.
- Toute cotation proposée doit être **justifiable** par le texte du guide.

## Licence des contributions

En contribuant, vous acceptez que votre contribution soit publiée sous les licences du dépôt :
**MIT** (code) et **CC BY 4.0** (documentation).

---

**EN** — Contributions welcome (docs are in French; the README has an English version). **Never include
confidential or real audit data, secrets, `file:line` references to real systems, or internal
product/team/person names** — examples must be fully fictional. By contributing, you agree your work is
published under the repository's **MIT** (code) and **CC BY 4.0** (documentation) licenses.
