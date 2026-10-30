---
name: linkedin-posts
description: Rédiger un post LinkedIn complet en français à partir d’un thème, en créant soi-même l’accroche puis le corps avec les consignes de Louis et sa voix personnelle.
---

# Posts LinkedIn complets

Utilise ce skill quand Louis donne un thème et veut un post LinkedIn publiable. Il n’a pas besoin de fournir une accroche : tu la crées, puis tu rédiges le post complet. S’il demande une idée depuis sa base ou signale qu’il est en panne d’idées, consulte d’abord son espace LinkedIn via le skill `linkedin-ideas`.

## Processus

1. Repère le thème, le lecteur visé, les faits et les éléments de preuve que Louis a fournis. N’invente ni expérience, ni client, ni statistique, ni résultat personnel.
2. Rédige une accroche selon les principes de `linkedin-hooks` : texte seul, valeur déjà claire, et une raison concrète de lire la suite. Si le skill est disponible, applique-le; sinon, suis la même règle décrite ici.
3. Rédige le post complet en prenant cette accroche comme les deux premières lignes. Ne demande pas à Louis de fournir l’accroche et ne la remplace pas par une autre au milieu du post.
4. Rédige le corps conformément au prompt de référence [post-generation-prompt.md](references/post-generation-prompt.md). Le texte de ce prompt est conservé tel qu’il a été donné. La seule adaptation opérationnelle est que l’accroche est générée par toi à partir du thème, au lieu d’être fournie par l’utilisateur; toutes les autres consignes de rédaction restent applicables.
5. Pour les mots, le ton et la formulation, applique `louis-linkedin-voice` si disponible. Cela adapte la voix sans changer les contraintes du prompt de corps.

## Idées de la base Ruff

Quand Louis fournit une idée précise, travaille à partir de son brief. Quand il demande de choisir dans sa base ou cherche une idée parce qu’il est en panne, utilise `linkedin-ideas` pour consulter https://ruff-saas-admin.vercel.app/linkedin avant de rédiger. Si la page est protégée, demande-lui de se connecter lui-même. Ne dis pas que tu as utilisé la base sans l’avoir effectivement consultée. N’ajoute pas automatiquement le brouillon à la base ou au calendrier.

## Contraintes de sortie

- Le post complet, accroche comprise, est directement publiable.
- Utilise uniquement du texte : aucun emoji, hashtag, gras, italique ou soulignement.
- Respecte les retours à la ligne et les listes demandés dans le prompt de référence.
- Mets chaque post demandé dans son propre bloc de code.
- Ne mets aucun texte, titre, explication ou note en dehors des blocs de code.
- Si plusieurs variantes sont demandées, chaque bloc contient un post complet avec sa propre accroche.
- Si le thème ne contient pas assez de faits pour une histoire ou un résultat précis, reste honnête et écris autour de l’idée disponible. Ne remplis pas les trous avec des détails inventés.
