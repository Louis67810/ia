---
name: linkedin-ideas
description: Consulter et gérer la base d’idées de posts LinkedIn de Louis sur son espace Ruff : rechercher, ajouter, planifier, décaler et supprimer des idées.
---

# Base d’idées LinkedIn de Louis

Espace à utiliser : https://ruff-saas-admin.vercel.app/linkedin
API dédiée présentée dans le panneau « API agent » de l’application : https://ruff-saas-admin.vercel.app/api/linkedin

La base Ruff est la source de vérité pour les idées, leurs catégories, leur statut et le calendrier. Elle est privée. L’interface et l’API nécessitent une connexion ou une clé dédiée.

## Accès et secrets

- Ne demande pas à Louis d’envoyer un mot de passe dans le chat et ne stocke jamais de mot de passe ni de clé API dans ce skill, dans les JSON d’idées ou dans un brouillon.
- Si la session du navigateur est déjà ouverte, utilise l’interface du site et vérifie chaque résultat.
- L’application propose une clé API dédiée avec deux portées : lecture seule ou lecture, ajout et planification. La création de clé élargit l’accès à cette base et doit être confirmée par Louis au moment de la création.
- Si une clé est nécessaire, utilise-la uniquement depuis un moyen de stockage secret approuvé et accessible à l’outil d’appel. Si aucun stockage sécurisé ou client HTTP authentifié n’est disponible, demande à Louis de se connecter dans la page et utilise l’interface; ne prétends pas que l’API est connectée.
- Si Vercel bloque une requête d’agent, ne contourne pas la protection. Le site mentionne un header de bypass géré dans les réglages Vercel; son ajout élargit l’accès et nécessite une autorisation explicite.

## API observée dans la documentation du site

Base : `https://ruff-saas-admin.vercel.app/api/linkedin`
Authentification annoncée : `Authorization: Bearer <clé dédiée>`

- Lire l’historique : `GET /posts?createdAfter=<date ISO>`.
- Lire le calendrier : `GET /posts?dateFrom=YYYY-MM-DD&dateTo=YYYY-MM-DD`.
- Ajouter une idée planifiée : `POST /posts` avec un objet comme `{"title":"Mon idée","date":"YYYY-MM-DD"}`. N’envoie que les champs dont le site documente le support ou que l’interface confirme.
- Déplacer une idée : `PATCH /posts/{id}` avec la nouvelle date, par exemple `{"date":"YYYY-MM-DD"}`.
- Suivre `nextCursor` jusqu’à la fin des résultats paginés.
- La documentation consultée indique que l’API ne publie pas automatiquement sur LinkedIn. Elle ne présente pas d’endpoint de suppression dans le résumé visible; pour supprimer, utilise l’interface si l’action y est disponible. Ne suppose pas qu’un endpoint DELETE existe.

Avant une action d’écriture, vérifie que l’idée ciblée et les champs demandés sont clairs. Après l’action, relis l’élément dans la base ou le calendrier pour confirmer le résultat. Ne modifie que ce que Louis a demandé.

## Quand consulter la base

- Si Louis est en panne d’idées ou demande à retrouver une idée, cherche d’abord dans la base. Résume les idées pertinentes avec leur catégorie, statut et date si visibles.
- S’il donne le thème lui-même, travaille à partir de ce brief; ne le remplace pas par une idée trouvée ailleurs.
- Pour une accroche ou un post basé sur une idée sauvegardée, récupère l’idée puis conserve son sens. Applique `louis-linkedin-voice` pour la formulation.
- Après rédaction, ne sauvegarde, ne planifie et ne publie pas automatiquement le brouillon. Attends une demande explicite.

## Actions dans l’interface

- **Ajouter** : saisis fidèlement l’idée dictée par Louis; n’invente pas de faits. Vérifie qu’elle apparaît dans la liste.
- **Planifier / décaler** : utilise la date et l’heure explicitement demandées. Si seule une période vague est donnée et que la date n’est pas déductible, demande le jour et l’heure. Vérifie ensuite le calendrier.
- **Modifier** : ne change que les champs demandés et relis les valeurs sauvegardées.
- **Supprimer** : identifie exactement l’idée. Si l’opération est définitive, demande confirmation juste avant de cliquer. Si elle est réversible, effectue la suppression demandée puis vérifie le statut.

Réponds brièvement avec l’action effectuée et les détails vérifiés. Si la connexion, la clé ou une fonction manque, décris précisément le blocage et ne prétends pas que la base a été modifiée.
