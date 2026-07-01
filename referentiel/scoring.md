# Scoring de conformité ANSSI-PG-078

Un indicateur **0–100** par produit : `0` = toutes les recommandations évaluées sont KO ; `100` = toutes OK.

## Barème (statut → points)

| Statut | Points |
|---|--:|
| conforme | 100 |
| partiel | 50 |
| non conforme | 0 |
| en cours | 0 (compte 100 dans le *score projeté*) |
| N/A | exclu (non applicable) |
| à évaluer | exclu du score, compté dans la *couverture* |

## Formules

- **Score plat** = moyenne des points des recommandations **évaluées** (ni `N/A` ni `à évaluer`).
- **Score pondéré** = Σ(poids × points) ÷ Σ(poids) sur les recommandations évaluées.
- **Couverture** = évaluées ÷ applicables (applicables = tout sauf `N/A`). Un score à faible couverture est *provisoire*.
- **Score projeté** = le même calcul en passant les `en cours` à `conforme` (montre la trajectoire).

Pourquoi exclure `N/A` et `à évaluer` : les compter comme 0 pénaliserait à tort, comme 100 gonflerait le
score. On les sort du calcul et on publie la **couverture** à côté pour signaler ce qui reste à évaluer.

## Pondération par criticité

| Poids | Niveau | Recommandations |
|--:|---|---|
| ×3 | critique | R10, R11, R13, R27, R28, R29, R29- |
| ×2 | important | R1, R2, R5, R6, R9, R12, R14, R15, R18, R19, R20, R21, R23, R26, R30 |
| ×1 | normal | R3, R4, R7, R8, R16, R17, R22, R24, R25, R31, R32→R42 |

La pondération reflète l'impact d'une défaillance (un trou sur le hashage R29 ou l'anti-bruteforce R10
pèse plus qu'un sur R25). Elle est **ajustable** dans `scripts/score.py`.

## Sous-scores par catégorie

Le script affiche aussi un score plat par catégorie — MFA, Cycle de vie, Politique de mot de passe,
Stockage, Recouvrement & coffre-fort, Règles utilisateur, Possession & inhérent — pour voir *où* ça pèche.

## Calcul (déterministe)

Le calcul est fait par script (pas d'arithmétique laissée au LLM), à partir du JSON de verdicts produit
par le prompt d'audit :

```text
python3 scripts/score.py verdicts.json
```

Un exemple (fictif) est fourni : `scripts/exemple-verdicts.json`.

## Avertissement

Indicateur de **pilotage interne**, pas une cotation officielle ANSSI (le guide ne définit pas de score).
