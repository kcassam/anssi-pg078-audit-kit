# ANSSI-PG-078 audit kit — Authentication & passwords

[🇫🇷 Français](README.md) · **🇬🇧 English**

A **reusable kit** to audit an application against the French ANSSI **PG-078** guidelines
(*"Recommendations for multi-factor authentication and passwords"*, v2.0, Oct. 2021),
**recommendation by recommendation (R1 → R42 + R29-)**, by **reading the source code**, then to record
the result in a **per-product tracking table**.

Designed to be driven by an LLM (e.g. **Claude Code**, via the provided `/audit-anssi` command) or used
by hand.

> Note: the reference framework (ANSSI-PG-078) is French; the grid and prompts are written in French.
> This English README explains how to use the kit.

## ⚠️ Golden rule — confidentiality

**This repository only contains the generic method.** The *result* of an audit is sensitive: it
describes potentially **exploitable** weaknesses. **Never publish** audit reports, secrets,
`file:line` references, product/team names or internal repository URLs. Keep your results private.

## Contents

| File | Purpose |
|---|---|
| `referentiel/anssi-pg078-grille.md` | The 43-recommendation grid: title, category, **what to look for in the code**, scoring cues (in French). |
| `prompts/audit-agent.md` | Reusable, self-contained audit prompt to feed an LLM (in French). |
| `prompts/hints-par-stack.md` | Where authentication lives per tech stack (Java, Node, Python, JSP, SPA…). |
| `templates/tableau-suivi.md` | Tracking-table template (Markdown). |
| `templates/tableau-confluence.html` | HTML/ADF version (status lozenges) for Confluence. |
| `.claude/commands/audit-anssi.md` | Claude Code `/audit-anssi` command. |

## Status legend

| Lozenge | Status | Meaning |
|---|---|---|
| ✅ | conforme | fully applied in production |
| 🟡 | partiel | partially applied (add a comment) |
| ❌ | non conforme | not applied / bypassed |
| 🔵 | en cours | remediation in progress |
| ⬜ | N/A | not applicable to the product (justify briefly) |
| ❓ | à évaluer | undetermined: organizational, infrastructure, or delegated to a third party not visible in the code |

**Expected cell format**: *status + short comment (and/or ticket link)*, ideally with `file:line` evidence.

## Usage

### With Claude Code
1. Copy `.claude/commands/audit-anssi.md` into your project (`.claude/commands/`) or into `~/.claude/commands/`.
2. Run `/audit-anssi <repo-path-or-name>`.
3. Review the output, fill in the tracking table.

### With any LLM / by hand
Provide `prompts/audit-agent.md` (replacing the `{{PRODUIT}}` / `{{CHEMIN}}` placeholders), relying on
`referentiel/anssi-pg078-grille.md` and `prompts/hints-par-stack.md`.

## Method (summary)

1. **Locate** all authentication code (login, password hashing, sessions/JWT, reset, anti-bruteforce,
   password policy, MFA, TLS/cookie config).
2. **Score each recommendation** based on what is *actually* in the code, with `file:line` evidence. Be
   honest: use `à évaluer` when something is organizational/infrastructure/delegated and not visible —
   do not guess.
3. **Record** the result in the tracking table (one product per column).

Rule for "do not …" recommendations (R8 no SMS, R22 no max length, R24 no forced expiry): the **absence**
of the forbidden behavior = **conforme**.

## ANSSI sources

- Official page: <https://cyber.gouv.fr/publications/recommandations-relatives-lauthentification-multifacteur-et-aux-mots-de-passe>
- PDF: <https://cyber.gouv.fr/sites/default/files/2021/10/anssi-guide-authentification_multifacteur_et_mots_de_passe.pdf>
- Full list **R1 → R42 and R29-**: pages 43-44 of the PDF.

## Disclaimer

This grid is an **audit aid**, not an official conformity statement. Final scoring is the responsibility
of the CISO / auditor. The "recommendation → technical cue" mapping reflects an operational reading of
the guide.

## Contributing

Contributions welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md). In short: **generic content only** —
never real audit data, secrets, or internal names.

## License

Code: **MIT**. Documentation: **CC BY 4.0**. © 2026 Karim Cassam Chenaï - Cegape. See `LICENSE`.
