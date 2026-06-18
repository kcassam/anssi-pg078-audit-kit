# Kit d'audit ANSSI-PG-078 — Authentification & mots de passe

**🇫🇷 Français** · [🇬🇧 English](README.en.md)

[![Markdown lint](https://github.com/cegape/anssi-pg078-audit-kit/actions/workflows/markdown-lint.yml/badge.svg)](https://github.com/cegape/anssi-pg078-audit-kit/actions/workflows/markdown-lint.yml) ![Code: MIT](https://img.shields.io/badge/code-MIT-blue) ![Docs: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

Kit **réutilisable** pour auditer une application contre les recommandations ANSSI **PG-078**
(« Recommandations relatives à l'authentification multifacteur et aux mots de passe », v2.0, oct. 2021),
**recommandation par recommandation (R1 → R42 + R29-)**, par **lecture du code source**, puis pour
consigner le résultat dans un **tableau de suivi par produit**.

Pensé pour être piloté par un LLM (ex. **Claude Code**, via la commande `/audit-anssi` fournie) ou
utilisé à la main.

## ⚠️ Règle d'or — confidentialité

**Ce dépôt ne contient QUE la méthode générique.** Le *résultat* d'un audit est sensible : il décrit
des faiblesses potentiellement **exploitables**. **Ne jamais publier** les rapports d'audit, les
secrets, les références `fichier:ligne`, les noms de produits/équipes ni les URLs de dépôts internes.
Gardez vos résultats en interne (wiki privé, ticket, etc.).

## Contenu

| Fichier | Rôle |
|---|---|
| `referentiel/anssi-pg078-grille.md` | La grille des 43 recommandations : intitulé, catégorie, **quoi chercher dans le code**, repères de cotation. |
| `prompts/audit-agent.md` | Prompt d'audit réutilisable (auto-suffisant) à donner à un LLM. |
| `prompts/hints-par-stack.md` | Où vit l'authentification selon la techno (Java, Node, Python, JSP, SPA…). |
| `templates/tableau-suivi.md` | Modèle de tableau de suivi (markdown). |
| `templates/tableau-confluence.html` | Version HTML/ADF (pastilles de statut) pour Confluence. |
| `.claude/commands/audit-anssi.md` | Commande Claude Code `/audit-anssi`. |

## Légende des statuts

| Pastille | Statut | Sens |
|---|---|---|
| ✅ | conforme | règle pleinement appliquée en production |
| 🟡 | partiel | partiellement appliquée (préciser dans le commentaire) |
| ❌ | non conforme | non appliquée / contournée |
| 🔵 | en cours | chantier de mise en conformité en cours |
| ⬜ | N/A | non applicable au produit (justifier brièvement) |
| ❓ | à évaluer | indéterminé : organisationnel, infra, ou délégué à un tiers non visible |

**Format attendu dans une cellule** : *statut + commentaire court (et/ou lien ticket)*, avec si possible
la preuve `fichier:ligne`.

## Utilisation

### Avec Claude Code

1. Copier `.claude/commands/audit-anssi.md` dans votre projet (`.claude/commands/`) ou dans `~/.claude/commands/`.
2. Lancer `/audit-anssi <chemin-ou-nom-du-dépôt>`.
3. Relire la sortie, reporter dans le tableau de suivi.

### Avec n'importe quel LLM / à la main

Fournir `prompts/audit-agent.md` (en remplaçant les placeholders `{{PRODUIT}}` / `{{CHEMIN}}`), en
s'appuyant sur `referentiel/anssi-pg078-grille.md` et `prompts/hints-par-stack.md`.

## Méthode (résumé)

1. **Localiser** tout le code d'authentification (login, hashage des MDP, sessions/JWT, reset,
   anti-bruteforce, politique de MDP, MFA, config TLS/cookies).
2. **Coter chaque recommandation** d'après ce qui est *réellement* dans le code, avec preuve
   `fichier:ligne`. Honnêteté : `à évaluer` quand c'est organisationnel/infra/délégué et non visible —
   ne pas deviner.
3. **Reporter** dans le tableau de suivi (un produit par colonne).

Règle pour les recommandations « ne pas … » (R8 pas de SMS, R22 pas de longueur max, R24 pas
d'expiration forcée) : l'**absence** du comportement interdit = **conforme**.

## Sources ANSSI

- Page officielle : <https://cyber.gouv.fr/publications/recommandations-relatives-lauthentification-multifacteur-et-aux-mots-de-passe>
- PDF : <https://cyber.gouv.fr/sites/default/files/2021/10/anssi-guide-authentification_multifacteur_et_mots_de_passe.pdf>
- Liste exhaustive **R1 → R42 et R29-** : pages 43-44 du PDF.

## Avertissement

Cette grille est une **aide à l'audit**, pas un avis de conformité officiel. La cotation définitive
relève du RSSI / de l'auditeur. La correspondance « reco → indice technique » reflète une
interprétation opérationnelle du guide.

## Contribuer

Contributions bienvenues — voir [`CONTRIBUTING.md`](CONTRIBUTING.md). En bref : **que du générique**,
jamais de données d'audit réelles, de secrets ni de noms internes.

## Licence

Code : **MIT**. Documentation : **CC BY 4.0**. © 2026 Karim Cassam Chenaï - Cegape. Voir `LICENSE`.
