"""Remplace le texte du post dans la page de copie (post-spreak-copier.html) sans toucher au reste.

Usage : python maj_page_copie.py <post.txt> [<titre de la page>]
Le post est un texte classique : une ligne vide entre deux blocs, pas de lignes vides dans un bloc.
Le bouton "Copier pour LinkedIn" de la page met lui-même le caractère invisible sur les lignes vides.
"""
import html
import re
import sys
from pathlib import Path

PAGE = Path(__file__).with_name("post-spreak-copier.html")

post = Path(sys.argv[1]).read_text(encoding="utf-8").rstrip("\n")
page = PAGE.read_text(encoding="utf-8")

page, n = re.subn(
    r'(<textarea id="post" readonly>).*?(</textarea>)',
    lambda m: m.group(1) + html.escape(post, quote=False) + m.group(2),
    page,
    count=1,
    flags=re.S,
)
if n != 1:
    sys.exit("textarea introuvable dans la page")

if len(sys.argv) > 2:
    titre = html.escape(sys.argv[2], quote=False)
    page = re.sub(r"<h1>.*?</h1>", lambda m: f"<h1>{titre}</h1>", page, count=1, flags=re.S)

PAGE.write_text(page, encoding="utf-8")
print("page mise à jour")
