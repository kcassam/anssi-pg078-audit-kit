#!/usr/bin/env python3
"""Score de conformité ANSSI-PG-078 à partir d'un JSON de verdicts.

Usage :
    python3 score.py verdicts.json

Entrée (sortie « Verdicts » du prompt d'audit) :
    {"R1": {"statut": "conforme"}, "R2": {"statut": "partiel"}, ...}
  ou {"R1": "conforme", "R2": "partiel", ...}

Barème : conforme=100, partiel=50, non conforme=0, en cours=0.
« N/A » exclu (non applicable) ; « à évaluer » exclu du score mais compté dans la couverture.
Voir referentiel/scoring.md pour la méthode complète.
"""
import json
import sys
import unicodedata


def norm(s):
    """Minuscule, sans accents, espaces normalisés (robuste aux variantes)."""
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return " ".join(s.lower().split())


POINTS = {"conforme": 100.0, "partiel": 50.0, "non conforme": 0.0, "en cours": 0.0}
POINTS_PROJETE = dict(POINTS, **{"en cours": 100.0})  # chantiers « en cours » aboutis
NA = {"n/a", "na"}
A_EVALUER = {"a evaluer"}

# Poids par criticité : 3 = critique, 2 = important, 1 = normal
WEIGHTS = {
    "R1": 2, "R2": 2, "R3": 1, "R4": 1, "R5": 2, "R6": 2, "R7": 1, "R8": 1,
    "R9": 2, "R10": 3, "R11": 3, "R12": 2, "R13": 3, "R14": 2, "R15": 2,
    "R16": 1, "R17": 1, "R18": 2, "R19": 2, "R20": 2, "R21": 2, "R22": 1,
    "R23": 2, "R24": 1, "R25": 1, "R26": 2, "R27": 3, "R28": 3, "R29": 3,
    "R29-": 3, "R30": 2, "R31": 1, "R32": 1, "R33": 1, "R34": 1, "R35": 1,
    "R36": 1, "R37": 1, "R38": 1, "R39": 1, "R40": 1, "R41": 1, "R42": 1,
}

CATEGORIES = [
    ("MFA / facteurs forts", ["R1", "R2"]),
    ("Cycle de vie", ["R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11",
                      "R12", "R13", "R14", "R15", "R16", "R17", "R18", "R19"]),
    ("Politique de mot de passe", ["R20", "R21", "R22", "R23", "R24", "R25", "R26", "R27"]),
    ("Stockage", ["R28", "R29", "R29-"]),
    ("Recouvrement & coffre-fort", ["R30", "R31"]),
    ("Règles utilisateur", ["R32", "R33", "R34", "R35", "R36", "R37", "R38"]),
    ("Possession & inhérent", ["R39", "R40", "R41", "R42"]),
]


def statut_of(v):
    return (v.get("statut") or v.get("status") or "") if isinstance(v, dict) else v


def compute(verdicts, points):
    """verdicts : {reco: statut_normalisé}. Retourne les métriques de score."""
    nf = df = nw = dw = 0.0
    n_eval = n_ae = 0
    for r, st in verdicts.items():
        if st in NA:
            continue                      # non applicable : hors calcul
        if st in A_EVALUER:
            n_ae += 1                      # applicable mais non évalué
            continue
        if st not in points:
            continue                      # statut inconnu : ignoré
        w = WEIGHTS.get(r, 1)
        p = points[st]
        nf += p
        df += 1
        nw += w * p
        dw += w
        n_eval += 1
    applicable = n_eval + n_ae
    return {
        "plat": round(nf / df) if df else None,
        "pondere": round(nw / dw) if dw else None,
        "evaluees": n_eval,
        "applicables": applicable,
        "couverture": round(100 * n_eval / applicable) if applicable else None,
    }


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 score.py verdicts.json")
    with open(sys.argv[1], encoding="utf-8") as fh:
        raw = json.load(fh)
    verdicts = {k: norm(statut_of(v)) for k, v in raw.items()}

    cur = compute(verdicts, POINTS)
    proj = compute(verdicts, POINTS_PROJETE)

    print(f"Score plat     : {cur['plat']}/100")
    print(f"Score pondéré  : {cur['pondere']}/100")
    print(f"Couverture     : {cur['couverture']}% "
          f"({cur['evaluees']}/{cur['applicables']} recos applicables évaluées)")
    if (proj["plat"], proj["pondere"]) != (cur["plat"], cur["pondere"]):
        print(f"Score projeté  : plat {proj['plat']} / pondéré {proj['pondere']} "
              f"(si les « en cours » aboutissent)")
    print("\nPar catégorie (score plat) :")
    for name, recos in CATEGORIES:
        sub = {r: verdicts[r] for r in recos if r in verdicts}
        m = compute(sub, POINTS)
        val = f"{m['plat']:>3}/100" if m["plat"] is not None else "  —  "
        print(f"  {name:<28} {val}  ({m['evaluees']} éval.)")


if __name__ == "__main__":
    main()
