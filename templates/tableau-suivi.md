# Tableau de suivi de conformité ANSSI-PG-078 (modèle)

Un **produit par colonne**. Cellule = *statut + commentaire court* (et si possible `fichier:ligne` ou
lien ticket). Dupliquez/ajoutez des colonnes selon vos produits.

**Légende** : ✅ conforme · 🟡 partiel · ❌ non conforme · 🔵 en cours · ⬜ N/A · ❓ à évaluer

| R# | Recommandation | Catégorie | Produit A | Produit B |
|---|---|---|:--:|:--:|
| R1 | Privilégier le MFA | MFA | ❓ | ❓ |
| R2 | Moyens d'auth forts | MFA | ❓ | ❓ |
| R3 | Analyse de risque | Analyse de risque | ❓ | ❓ |
| R4 | Création en env. maîtrisé | Cycle de vie – Création | ❓ | ❓ |
| R5 | RNG robuste | Cycle de vie – Création | ❓ | ❓ |
| R6 | Remise par canaux sûrs | Cycle de vie – Création | ❓ | ❓ |
| R7 | Renouvellement des facteurs | Cycle de vie – Renouvellement | ❓ | ❓ |
| R8 | Pas de SMS | Cycle de vie – Transmission | ❓ | ❓ |
| R9 | Historiques d'utilisation | Cycle de vie – Transmission | ❓ | ❓ |
| R10 | Limiter les tentatives | Cycle de vie – Transmission | ❓ | ❓ |
| R11 | Canal sécurisé (TLS) | Cycle de vie – Transmission | ❓ | ❓ |
| R12 | Durée de session limitée | Cycle de vie – Transmission | ❓ | ❓ |
| R13 | Protéger les données d'auth | Cycle de vie – Transmission | ❓ | ❓ |
| R14 | Pas d'info sur l'échec | Cycle de vie – Transmission | ❓ | ❓ |
| R15 | Expiration des facteurs | Cycle de vie – Transmission | ❓ | ❓ |
| R16 | Politique d'utilisation | Cycle de vie – Transmission | ❓ | ❓ |
| R17 | Sensibilisation | Cycle de vie – Transmission | ❓ | ❓ |
| R18 | Révocation des facteurs | Cycle de vie – Révocation | ❓ | ❓ |
| R19 | Délais de révocation | Cycle de vie – Révocation | ❓ | ❓ |
| R20 | Politique de mots de passe | Mot de passe – Politique | ❓ | ❓ |
| R21 | Longueur minimale | Mot de passe – Longueur | ❓ | ❓ |
| R22 | Pas de longueur maximale | Mot de passe – Longueur | ❓ | ❓ |
| R23 | Règles de complexité | Mot de passe – Complexité | ❓ | ❓ |
| R24 | Pas d'expiration par défaut | Mot de passe – Expiration | ❓ | ❓ |
| R25 | Expiration comptes à privilèges | Mot de passe – Expiration | ❓ | ❓ |
| R26 | Révocation si compromission | Mot de passe – Expiration | ❓ | ❓ |
| R27 | Contrôle de robustesse | Mot de passe – Robustesse | ❓ | ❓ |
| R28 | Sel aléatoire ≥ 128 bits | Stockage | ❓ | ❓ |
| R29 | Dérivation memory-hard (Argon2/scrypt) | Stockage | ❓ | ❓ |
| R29- | À défaut PBKDF2 | Stockage | ❓ | ❓ |
| R30 | Recouvrement d'accès | Recouvrement | ❓ | ❓ |
| R31 | Coffre-fort de mots de passe | Coffre-fort | ❓ | ❓ |
| R32 | [Utilisateur] Mots de passe robustes | Utilisateurs | ❓ | ❓ |
| R33 | [Utilisateur] Un MDP par service | Utilisateurs | ❓ | ❓ |
| R34 | [Utilisateur] Coffre-fort | Utilisateurs | ❓ | ❓ |
| R35 | [Utilisateur] Protéger ses MDP | Utilisateurs | ❓ | ❓ |
| R36 | [Utilisateur] MDP robuste messagerie | Utilisateurs | ❓ | ❓ |
| R37 | [Utilisateur] Pas d'info personnelle | Utilisateurs | ❓ | ❓ |
| R38 | [Utilisateur] Changer les MDP par défaut | Utilisateurs | ❓ | ❓ |
| R39 | Possession qualifié/certifié | Facteur de possession | ❓ | ❓ |
| R40 | Inhérent pas en mono-facteur | Facteur inhérent | ❓ | ❓ |
| R41 | Inhérent + facteur fort en MFA | Facteur inhérent | ❓ | ❓ |
| R42 | Enrôlement biométrie en personne | Facteur inhérent | ❓ | ❓ |
