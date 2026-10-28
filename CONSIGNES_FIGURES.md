# Consignes de conversion des figures ASCII → SVG (LA VOIE DU NOMBRE)

Racine : `c:\Silvere\Encours\Developpement\Articles\livre_mathematiques\`
Sources : `v2\Volume_<N>\Chapitre_*.md` (Markdown + LaTeX `$...$`).
Le livre est compilé par Pandoc (md → Typst) puis Typst. Le fichier `.typ` final est à la racine, donc
les chemins d'image dans le Markdown doivent être relatifs à la racine : `figures/vol_<N>/...`.

## Objectif
Il ne doit RESTER AUCUN dessin en caractères (ASCII / box-drawing : `─ │ ┌ ▲ ► / \ ● ○ ■ ╲` etc.)
dans les chapitres de ton volume. Chaque bloc ``` ``` sans langage doit être traité.

## Règles par type de bloc
1. **Code Python** (def, import, while, print…) → garder, mais changer la clôture en ```` ```python ````.
2. **Figure / schéma / graphe / repère / courbe / arbre / tableau de variations / droite graduée /
   opération posée (addition, soustraction, multiplication en colonnes, division en potence) /
   diagramme de flux / grille de points / boîtes** → créer un **SVG** dédié et remplacer le bloc par :
   `![Légende précise et pédagogique](figures/vol_<N>/chNN_figK.svg){width=80%}`
   (largeur 50–95 % selon le contenu). Si le bloc est dans un encadré (lignes préfixées `> `),
   la ligne de remplacement doit aussi commencer par `> `.
3. **Simple tableau de données** (valeurs alignées en colonnes, sans dessin) → tableau Markdown pipe
   (`| a | b |` + ligne `|---|---|`), avec une ligne d'en-tête pertinente.
4. **Texte simplement mis en retrait** sans aucun dessin → texte normal ou formule `$$...$$`.
5. **HTML brut `<div ...><svg>...</svg></div>`** présent dans certains chapitres (Ch. 05, 09, 23, 32, 37, 52) :
   extraire le SVG dans un fichier `figures/vol_<N>/...svg` (le corriger si besoin) et remplacer le HTML par
   la syntaxe image Markdown. Plus aucun HTML ne doit rester.

## Exigences de qualité des SVG (impératif)
- **Fidélité** : la figure reproduit exactement le contenu du schéma d'origine (mêmes points, lettres,
  valeurs numériques, étiquettes, légendes) et le texte environnant du chapitre. Lis le paragraphe autour
  pour comprendre ce que la figure doit montrer. Pas de figure générique « approximative ».
- **Exactitude mathématique** : courbes calculées (génère les `path` par Python à partir de la vraie
  fonction : parabole, exp, ln, sin, 1/x…), proportions et angles corrects, triangles rectangles vraiment
  droits, divisions posées arithmétiquement justes (vérifie chaque calcul).
- Palette Oliver Byrne : bleu `#1d4ed8`, rouge `#b91c1c`, jaune/ambre `#d97706`, vert `#15803d`,
  encre `#0f172a`, gris `#64748b`, fonds clairs `#eff6ff` `#fef2f2` `#fffbeb` `#f0fdf4` `#f8fafc`.
- Police : `font-family="Liberation Sans, Arial, sans-serif"` ; maths en italique (`font-style="italic"`)
  pour les variables. Taille de texte ≥ 11 (dans un viewBox de largeur ~600).
- SVG autonome : `xmlns`, `viewBox`, `width`/`height`. Pas de `<foreignObject>`, pas de CSS `<style>`,
  pas d'images externes, pas de police web. Flèches : petits `<polygon>` (ou `<marker>` simple).
- XML valide : échapper `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;` dans les textes. Utiliser les caractères
  Unicode directement (π, θ, √, ², ≤, →, ∞, ⃗ évité : préférer une petite flèche dessinée au-dessus).
- Fond très clair arrondi, marges internes, rien ne déborde, pas de chevauchement de texte.

## Méthode recommandée
- Écrire un script reproductible `figures/gen_vol_<N>.py` qui génère tous les SVG du volume dans
  `figures/vol_<N>/` (fonctions utilitaires : axes, flèche, point, courbe échantillonnée, opération posée…).
- Puis remplacer les blocs dans les `.md` (script Python ou édition manuelle), en relisant chaque remplacement.
- **Vérification obligatoire** :
  a) parser chaque SVG avec `xml.etree.ElementTree` ;
  b) créer `figures/test_vol_<N>.typ` qui contient `#image("vol_<N>/xxx.svg", width: 80%)` pour tous les SVG,
     compiler avec Typst :
     `C:\Users\silve\AppData\Local\Microsoft\WinGet\Packages\Typst.Typst_Microsoft.Winget.Source_8wekyb3d8bbwe\typst-x86_64-pc-windows-msvc\typst.exe compile figures\test_vol_<N>.typ figures\test_vol_<N>.pdf`
     (aucune erreur tolérée) ; puis export PNG de quelques pages
     (`... compile --format png --ppi 80 figures\test_vol_<N>.typ figures\test_vol_<N>_{p}.png`) et
     **regarder les images** (read_file sur le PNG) pour contrôler visuellement la lisibilité et l'exactitude ;
  c) re-scanner les `.md` du volume : il ne doit plus y avoir de bloc ``` ``` sans langage ni caractère de dessin
     dans un bloc de code non-Python, ni de balise HTML.
- Python : `C:\Users\silve\AppData\Local\Programs\Python\Python314\python.exe` (attention, la console Windows
  est en cp1252 : écrire les sorties dans des fichiers en UTF-8 plutôt que les `print` avec caractères spéciaux,
  ou lancer avec `-X utf8`).

## Interdits
- Ne modifier QUE les fichiers de ton volume et ton dossier `figures/vol_<N>/` (+ ton script/test).
- Ne pas toucher au script de build, ni aux autres volumes, ni au contenu pédagogique (hors blocs dessin).
- Ne pas supprimer d'information : toute étiquette du schéma doit se retrouver dans la figure ou la légende.

## Compte rendu final (message au parent)
Nombre de blocs traités par type (SVG / tableau / python / texte), liste des fichiers SVG créés,
résultat des vérifications (compilation Typst OK, scan final propre), problèmes éventuels.
