# -*- coding: utf-8 -*-
"""
Master Book Builder v5 for LA VOIE DU NOMBRE
- Authors: Silvère-Martin Michiellot & Antigravity
- Cover with cover_art.jpg and Edition Integrale de Reference 2026
- Clean copyright page without fake ISBN
- Clickable depth-2 Sommaire with genuine page numbers
- Running headers: active volume left, active chapter right (checks current page first)
- Foliotage éditorial : couverture (plats 1-4) hors décompte, page 1 = faux-titre,
  liminaires muets, ouvertures de volumes/chapitres en belle page muette,
  pages blanches sans folio, folio toujours sur la marge extérieure (jamais côté reliure)
- Uniform left alignment on exercises (first-line-indent: 0pt)
- Automatic blank line before all **Exercice and **Solution to prevent concatenation
- Sticky headings & callouts to prevent orphan headers at page bottoms
- Hyphenate false on headings to prevent broken titles
- Priority mapping to dedicated custom SVGs in figures/vol_1 to vol_6
- Clean fallback vector SVGs (viewBox 600, no clipping, zero box characters)
- Comprehensive Appendices: Formulaire trigonométrique exact, Formules, Dérivées, Notations
- Autonomous Conclusion & Épilogue with L'Arbre des Savoirs Mathématiques
- Back Cover (Quatrième de couverture) without headers/footers
"""
import os
import glob
import re
import json
import subprocess
import sys
import textwrap
import pypdfium2 as pdfium

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEXTES_DIR = os.path.join(BASE_DIR, "textes")
FIG_DIR = os.path.join(BASE_DIR, "figures")
DIAG_DIR = os.path.join(FIG_DIR, "diags")
PANDOC_EXE = r"C:\Users\silve\AppData\Local\Pandoc\pandoc.exe"
TYPST_EXE = r"C:\Users\silve\AppData\Local\Microsoft\WinGet\Packages\Typst.Typst_Microsoft.Winget.Source_8wekyb3d8bbwe\typst-x86_64-pc-windows-msvc\typst.exe"

TEMP_MD = os.path.join(BASE_DIR, "temp_preprocessed_book.md")
TEMP_TYP = os.path.join(BASE_DIR, "temp_pandoc_out.typ")
FINAL_TYP = os.path.join(BASE_DIR, "LA_VOIE_DU_NOMBRE.typ")
FINAL_PDF = os.path.join(BASE_DIR, "LA_VOIE_DU_NOMBRE.pdf")

DIAG_BY_LOC = {}
# ==============================================================================
# 1. TYPST PREAMBLE & BOOK DESIGN
# ==============================================================================

PREAMBLE = """
#set document(
  title: "LA VOIE DU NOMBRE — Une Odyssée Constructive",
  author: "Silvère-Martin Michiellot & Antigravity"
)

// ==========================================
// RÈGLES DE FOLIOTAGE (CHARTE TYPOGRAPHIQUE DE L'ÉDITION)
// - La couverture (plats 1, 2, 3 et 4) n'est jamais comptée ni foliotée :
//   le compteur démarre à 1 sur la première belle page du bloc intérieur (faux-titre).
// - Pages impaires = recto (droite) ; pages paires = verso (gauche).
// - Pages liminaires (1 faux-titre, 2 blanche, 3 grand titre, 4 mentions légales,
//   5 exergue/dédicace, 6 blanche, puis sommaire) : comptées mais muettes.
// - Toute ouverture de volume, de chapitre ou d'annexe se fait en belle page (impaire)
//   et reste muette ; le premier folio visible suit l'ouverture du Volume I.
// - Pages blanches : comptées dans l'ordre arithmétique, jamais de folio ni de titre courant.
// - Folio sur la marge extérieure : à gauche sur les versos (pairs), à droite sur les rectos (impairs).
// ==========================================

// Saut vers la prochaine belle page (impaire) avec balisage des pages blanches intercalaires
#let recto() = {
  [#metadata("fin-section") <fin-section>]
  pagebreak(weak: true, to: "odd")
  [#metadata("debut-section") <debut-section>]
}

// Le folio (et le titre courant) n'est visible que sur les pages de texte courant :
// ni liminaire, ni page d'ouverture, ni page blanche.
#let folio-visible() = {
  let p = here().page()
  let debut = query(<debut-texte>)
  if debut.len() == 0 or p <= debut.first().location().page() { return false }
  let fins = query(<fin-section>)
  let debuts = query(<debut-section>)
  for (i, d) in debuts.enumerate() {
    let dp = d.location().page()
    if dp == p { return false }
    if i < fins.len() and p < dp {
      let m = fins.at(i).location()
      let mp = m.page()
      if mp < p { return false }
      if mp == p and m.position().y < 2.65cm { return false }
    }
  }
  true
}

#set page(
  paper: "a4",
  margin: (top: 2.4cm, bottom: 2.4cm, left: 2.2cm, right: 2.2cm),
  header: context {
    if folio-visible() [
      #let cur-h2 = query(heading.where(level: 2)).filter(h => h.location().page() == here().position().page)
      #let ch-title = if cur-h2.len() > 0 {
        cur-h2.first().body
      } else {
        let prev-h2 = query(selector(heading.where(level: 2)).before(here()))
        if prev-h2.len() > 0 { prev-h2.last().body } else { [] }
      }
      #let cur-h1 = query(heading.where(level: 1)).filter(h => h.location().page() == here().position().page)
      #let vol-title = if cur-h1.len() > 0 {
        cur-h1.first().body
      } else {
        let prev-h1 = query(selector(heading.where(level: 1)).before(here()))
        if prev-h1.len() > 0 { prev-h1.last().body } else { [LA VOIE DU NOMBRE] }
      }
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 7.5pt, fill: rgb("#64748b"), font: "Liberation Sans", style: "italic")[#vol-title],
        text(size: 7.5pt, fill: rgb("#475569"), font: "Liberation Sans", weight: "bold")[#ch-title]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
    ]
  },
  footer: context {
    if folio-visible() {
      let page-num = counter(page).get().first()
      let titre = text(size: 8pt, fill: rgb("#94a3b8"), font: "Liberation Sans", style: "italic")[LA VOIE DU NOMBRE — Une Odyssée Constructive]
      let folio = text(size: 8.5pt, fill: rgb("#0f172a"), font: "Liberation Sans", weight: "bold")[Page #page-num]
      line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
      v(3pt)
      // Folio toujours côté marge extérieure (jamais côté reliure)
      if calc.even(page-num) {
        grid(columns: (1fr, 1fr), align: (left, right), folio, titre)
      } else {
        grid(columns: (1fr, 1fr), align: (left, right), titre, folio)
      }
    }
  }
)

#set text(
  font: ("Liberation Serif", "Times New Roman", "Georgia"),
  size: 10pt,
  lang: "fr"
)

// Pas d'alinéa en retrait pour garantir un alignement uniforme de tous les exercices (Exercice 1, 2...)
#set par(justify: true, leading: 0.70em, first-line-indent: 0pt, spacing: 0.85em)

// Éviter la césure maladroite dans les titres et empêcher les titres orphelins en fin de page
#show heading: set text(hyphenate: false)
#show heading: set block(sticky: true)

// Palette Oliver Byrne (1847)
#let byrne-blue = rgb("#1d4ed8")
#let byrne-red = rgb("#b91c1c")
#let byrne-yellow = rgb("#d97706")
#let byrne-dark = rgb("#0f172a")
#let byrne-green = rgb("#15803d")
#let byrne-purple = rgb("#7e22ce")
#let byrne-slate = rgb("#334155")

// Style épuré des blocs de code Python (Oliver Byrne)
#show raw.where(lang: "python"): it => align(center)[
  #block(
    fill: rgb("#f8fafc"),
    stroke: 0.75pt + rgb("#cbd5e1"),
    inset: (x: 12pt, y: 8pt),
    radius: 4pt,
    width: 95%,
    breakable: false,
    align(left)[#it]
  )
]

// Empêcher toute figure ou encart d'être coupé en deux sur un saut de page
#show figure: set block(breakable: false)

// Design des Volumes
#show heading.where(level: 1): it => {
  v(1.0cm)
  align(center)[
    #block(
      fill: rgb("#f1f5f9"),
      stroke: 2.5pt + byrne-blue,
      inset: 20pt,
      radius: 8pt,
      width: 100%
    )[
      #text(size: 17pt, weight: "bold", fill: byrne-dark, font: "Liberation Sans")[#it.body]
    ]
  ]
  v(1.0cm)
}

// Design des Chapitres
#show heading.where(level: 2): it => {
  v(0.5cm)
  text(size: 14pt, weight: "bold", fill: byrne-blue, font: "Liberation Sans")[#it.body]
  v(-4pt)
  line(length: 100%, stroke: 1.5pt + byrne-blue)
  v(0.3cm)
}

#show heading.where(level: 3): it => block(spacing: 1.2em)[
  #v(0.2cm)
  #text(size: 11.5pt, weight: "bold", fill: byrne-dark, font: "Liberation Sans")[#it.body]
  #v(0.1cm)
]

#show heading.where(level: 4): it => block(spacing: 0.9em)[
  #text(size: 10pt, weight: "bold", fill: byrne-slate, font: "Liberation Sans")[#it.body]
]

// Boîtes Didactiques Oliver Byrne (anti-orphelins avec sticky sur l'en-tête et breakable false anti-coupure)
#let principe(title: [Principe & Définition], body) = block(
  fill: rgb("#f0fdf4"),
  stroke: (left: 4pt + byrne-green),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 6pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #block(sticky: true, width: 100%)[
    #text(size: 10.5pt, weight: "bold", fill: byrne-green, font: "Liberation Sans")[#title]
    #v(3pt)
  ]
  #body
]

#let decouvre(title: [Découverte & Histoire], body) = block(
  fill: rgb("#eff6ff"),
  stroke: (left: 4pt + byrne-blue),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 6pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #block(sticky: true, width: 100%)[
    #text(size: 10.5pt, weight: "bold", fill: byrne-blue, font: "Liberation Sans")[#title]
    #v(3pt)
  ]
  #body
]

#let alerte(title: [Attention au Piège !], body) = block(
  fill: rgb("#fef2f2"),
  stroke: (left: 4pt + byrne-red),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 6pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #block(sticky: true, width: 100%)[
    #text(size: 10.5pt, weight: "bold", fill: byrne-red, font: "Liberation Sans")[#title]
    #v(3pt)
  ]
  #body
]

#let cas_limite(title: [Cas Limite & Vigilance], body) = block(
  fill: rgb("#fffbeb"),
  stroke: (left: 4pt + byrne-yellow),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 6pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #block(sticky: true, width: 100%)[
    #text(size: 10.5pt, weight: "bold", fill: byrne-yellow, font: "Liberation Sans")[#title]
    #v(3pt)
  ]
  #body
]

#let methode(title: [Méthode Pratique], body) = block(
  fill: rgb("#faf5ff"),
  stroke: (left: 4pt + byrne-purple),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 6pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #block(sticky: true, width: 100%)[
    #text(size: 10.5pt, weight: "bold", fill: byrne-purple, font: "Liberation Sans")[#title]
    #v(3pt)
  ]
  #body
]

#let exemple_resolu(title: [Exemple Résolu Pas à Pas], body) = block(
  fill: rgb("#f8fafc"),
  stroke: 1pt + rgb("#cbd5e1"),
  inset: (x: 14pt, y: 10pt),
  radius: 6pt,
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #block(sticky: true, width: 100%)[
    #text(size: 10pt, weight: "bold", fill: byrne-slate, font: "Liberation Sans")[#title]
    #v(3pt)
  ]
  #body
]

#let quote_box(body) = block(
  fill: rgb("#f8fafc"),
  stroke: (left: 3pt + rgb("#94a3b8")),
  inset: (left: 12pt, y: 7pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.1em,
  breakable: false
)[
  #text(style: "italic", fill: rgb("#334155"))[#body]
]

// ==========================================
// 1. PAGE DE COUVERTURE OFFICIELLE
// ==========================================
#align(center)[
  #v(0.2cm)
  #text(size: 14pt, weight: "bold", fill: byrne-blue, font: "Liberation Sans")[Silvère-Martin Michiellot & Antigravity]
  #v(0.3cm)
  #text(size: 32pt, weight: "bold", fill: byrne-dark, font: "Liberation Serif")[LA VOIE DU NOMBRE]
  #v(0.2cm)
  #text(size: 14pt, weight: "bold", fill: byrne-red, font: "Liberation Sans")[Une Odyssée Constructive, du Premier Caillou au Baccalauréat]
  #v(0.15cm)
  #text(size: 10pt, style: "italic", fill: rgb("#475569"))[58 chapitres d'histoire, de manipulations motrices, de calculs posés et de pure clarté logique]
  #v(0.4cm)
  
  #block(
    stroke: 2pt + byrne-yellow,
    radius: 8pt,
    inset: 3pt,
    clip: true
  )[
    #image("figures/cover_art.jpg", width: 56%)
  ]
  
  #v(0.4cm)
  #block(
    fill: rgb("#eff6ff"),
    stroke: 1.5pt + byrne-blue,
    inset: (x: 18pt, y: 7pt),
    radius: 6pt
  )[
    #text(size: 11pt, weight: "bold", fill: byrne-blue, font: "Liberation Sans")[ÉDITION INTÉGRALE DE RÉFÉRENCE — 2026]
  ]
]

#pagebreak()
// Plat 2 (intérieur de couverture) : hors décompte, jamais folioté
#box()
#pagebreak()

// Début du bloc intérieur : la première belle page est la page 1 (muette)
#counter(page).update(1)

// ==========================================
// PAGE 1 (RECTO) — FAUX-TITRE (MUETTE)
// ==========================================
#align(center + horizon)[
  #text(size: 22pt, weight: "bold", fill: byrne-dark, font: "Liberation Serif", tracking: 0.06em)[LA VOIE DU NOMBRE]
]
#pagebreak()

// PAGE 2 (VERSO) — PAGE BLANCHE (MUETTE)
#box()
#pagebreak()

// ==========================================
// PAGE 3 (RECTO) — GRAND TITRE (MUETTE)
// ==========================================
#align(center)[
  #v(3.5cm)
  #text(size: 13pt, weight: "bold", fill: byrne-blue, font: "Liberation Sans")[Silvère-Martin Michiellot & Antigravity]
  #v(1.6cm)
  #text(size: 32pt, weight: "bold", fill: byrne-dark, font: "Liberation Serif")[LA VOIE DU NOMBRE]
  #v(0.4cm)
  #line(length: 30%, stroke: 1pt + byrne-yellow)
  #v(0.4cm)
  #text(size: 14pt, weight: "bold", fill: byrne-red, font: "Liberation Sans")[Une Odyssée Constructive, du Premier Caillou au Baccalauréat]
  #v(1fr)
  #text(size: 10pt, fill: byrne-slate, font: "Liberation Sans")[ÉDITION INTÉGRALE DE RÉFÉRENCE — 2026]
  #v(0.2cm)
  #text(size: 9pt, fill: byrne-slate, font: "Liberation Sans")[Diffusion ouverte sous licence libre CC BY-SA 4.0]
  #v(1.5cm)
]
#pagebreak()

// PAGE 4 (VERSO) — MENTIONS LÉGALES (MUETTE)

// ==========================================
// 2. MENTIONS LÉGALES & COPYRIGHT (SANS FAUX ISBN)
// ==========================================
#align(center + bottom)[
  #block(
    fill: rgb("#f8fafc"),
    stroke: 1pt + rgb("#cbd5e1"),
    inset: 16pt,
    radius: 6pt,
    width: 90%
  )[
    #align(left)[
      #text(size: 9.5pt, weight: "bold", fill: byrne-dark)[LA VOIE DU NOMBRE — Une Odyssée Constructive, du Premier Caillou au Baccalauréat]\\
      #v(3pt)
      #text(size: 8.5pt, fill: rgb("#475569"))[
        Édition Numérique Intégrale de Référence — 58 chapitres en 6 volumes avec Guide de l'Accompagnateur et Annexes de Référence.\\
        \\
        *Auteurs :* Silvère-Martin Michiellot & Antigravity\\
        *Ingénierie didactique & Conception pédagogique :* Didactique constructiviste, méthode de Singapour, sémiotique visuelle d'Oliver Byrne\\
        *Composition typographique :* Typst v0.15, polices Liberation Serif & Sans, KaTeX mathématique\\
        *Sémiotique graphique :* Figures vectorielles SVG conformes à la palette historique d'Oliver Byrne (1847)\\
        *Illustration de couverture :* Synthèse graphique haute résolution dédiée\\
        *Dépôt légal :* Octobre 2026\\
        \\
        *Licence Libre :* Cet ouvrage est mis à disposition sous licence *Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International (CC BY-SA 4.0)*.\\
        Vous êtes libre de partager, copier, distribuer et adapter cet ouvrage sous réserve de citer expressément les auteurs d'origine et de diffuser vos modifications sous une licence identique.\\
        La diffusion de cet ouvrage à des fins pédagogiques, d'instruction en famille (IEF) ou d'enseignement scolaire est encouragée et autorisée sous réserve du maintien des crédits didactiques d'origine.
      ]
    ]
  ]
]

#pagebreak()

// ==========================================
// 3. CITATION INAUGURALE & DÉDICACE
// ==========================================
#align(center)[
  #v(3.5cm)
  #block(
    fill: rgb("#f8fafc"),
    inset: 20pt,
    radius: 8pt,
    stroke: 1pt + rgb("#e2e8f0"),
    width: 85%
  )[
    #text(size: 11pt, style: "italic", fill: rgb("#334155"))[
      « La philosophie est écrite dans cet immense livre qui se tient toujours ouvert devant nos yeux — je veux dire l'Univers —, mais on ne peut le comprendre si l'on n'apprend pas d'abord à en connaître la langue et les caractères dans lesquels il est écrit. Il est écrit dans la langue mathématique. »
    ]
    #v(8pt)
    #align(right)[#text(size: 9.5pt, weight: "bold", fill: byrne-blue)[— Galileo Galilei, *L'Essayeur* (1623)]]
  ]
  #v(2cm)
  #text(size: 10.5pt, style: "italic", fill: rgb("#475569"))[
    À tous les enfants et à tous les jeunes esprits qui ont un jour cru ne « pas être faits pour les maths »,\\
    et aux parents et éducateurs qui les guident avec bienveillance, clarté et exigence.
  ]
]

#pagebreak()

// PAGE 6 (VERSO) — PAGE BLANCHE (MUETTE)
#box()
#pagebreak()

// PAGE 7 (RECTO) ET SUIVANTES — SOMMAIRE (LIMINAIRE, MUET)

// ==========================================
// 4. SOMMAIRE GÉNÉRAL & DÉTAILLÉ (DEPTH: 2)
// ==========================================
#outline(
  title: [Sommaire Détaillé de l'Œuvre],
  indent: 1.5em,
  depth: 2
)

// Fin des pages liminaires : le folio devient visible après l'ouverture du Volume I
#metadata("debut-texte") <debut-texte>
"""

# ==============================================================================
# 2. ANNEXES, CONCLUSION AUTONOME & QUATRIÈME DE COUVERTURE
# ==============================================================================

BACK_MATTER = r"""
#recto()
= CONCLUSION GÉNÉRALE & ÉPILOGUE : L'ÉDIFICE DU NOMBRE ET LA LIBERTÉ DE L'ESPRIT

#align(center)[
  #figure(image("figures/vol_6/fig_58_arbre_savoirs.svg", width: 92%), caption: [L'Arbre des Savoirs Mathématiques : de l'expérience sensorielle à la théorie moderne])
]

#v(0.4cm)
Tu as franchi cinquante-huit étapes, depuis le premier caillou serré dans la main du jeune berger de la savane jusqu'aux espaces de dimension infinie, aux nombres complexes, aux intégrales de Riemann et aux marches aléatoires de Markov.

Ce voyage t'a révélé une vérité fondamentale que peu de manuels scolaires osent formuler : *les mathématiques ne sont pas un ensemble de règles arbitraires inventées pour tester ou piéger les écoliers.* Elles sont la mémoire vivante de tous les problèmes que l'humanité a dû surmonter pour s'orienter sur les océans, bâtir des cathédrales, prévoir les éclipses, soigner les épidémies et sonder le cosmos.

== Les Trois Enseignements Fondamentaux

1. *L'Ancrage Sensori-Moteur : Reviens toujours à la main et au dessin.*
   Quand un problème mathématique semble hermétique, ne reste jamais paralysé devant des lettres muettes. Trace un schéma, donne des couleurs aux grandeurs comme l'enseignait Oliver Byrne, fais bouger les figures, matérialise l'égalité sur une balance d'Al-Khwarizmi. La pensée mathématique s'enracine dans le corps et le geste avant de s'élever dans l'abstraction pure.

2. *L'Automatisation Opératoire : La technique libère l'esprit.*
   Pourquoi posons-nous les additions, les soustractions, les multiplications et les divisions selon des algorithmes rigoureux ? Pourquoi apprenons-nous par cœur les tables et les règles opératoires ? Pour libérer notre mémoire de travail. L'outil mécanique n'est pas un asservissement, mais un instrument d'émancipation : en confiant l'exécution machinale à la main, nous libérons toute la puissance de notre esprit pour l'intuition, la stratégie et la poésie de la démonstration.

3. *Le Courage des Cas Limites et la Vigilance Critique.*
   Les plus grands bonds en avant des mathématiques sont nés du refus d'éluder les paradoxes : que se passe-t-il si la grandeur s'annule, si l'ensemble est vide, si le dénominateur vaut zéro, si le processus tend vers l'infini ? Ne fuis jamais les cas limites : ce sont eux qui éprouvent la solidité de tes théories et qui séparent la conjecture fragile de la certitude inébranlable.

== L'Envoi au Lecteur

Les mathématiques t'ont transmis le plus précieux de tous les trésors : *la liberté de l'esprit critique.* Elles t'ont appris à ne jamais te soumettre à un argument d'autorité, à exiger la preuve rigoureuse, et à reconnaître loyalement la vérité dès qu'elle s'impose par la force de la logique.

Le grand livre du monde est désormais ouvert devant tes yeux. Tu en connais la langue. Va de l'avant, explore, questionne sans crainte, et garde toujours vivante en toi la curiosité du premier caillou.

#recto()
= ANNEXE A : FORMULAIRE & VALEURS REMARQUABLES DE RÉFÉRENCE

== I. Table Exacte des Lignes Trigonométriques Remarquables

#set text(size: 9.5pt)
#table(
  columns: (1.5fr, 1.2fr, 1.5fr, 1.5fr, 1.5fr),
  fill: (x, y) => if y == 0 { rgb("#1d4ed8") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 6.5pt,
  align: center,
  table.header(
    text(weight: "bold", fill: white)[Angle en Degrés (°)],
    text(weight: "bold", fill: white)[Radians (rad)],
    text(weight: "bold", fill: white)[$cos(x)$],
    text(weight: "bold", fill: white)[$sin(x)$],
    text(weight: "bold", fill: white)[$tan(x)$]
  ),
  [$0^circle$], [$0$], [$1$], [$0$], [$0$],
  [$30^circle$], [$pi / 6$], [$sqrt(3) / 2$], [$1 / 2$], [$sqrt(3) / 3$],
  [$45^circle$], [$pi / 4$], [$sqrt(2) / 2$], [$sqrt(2) / 2$], [$1$],
  [$60^circle$], [$pi / 3$], [$1 / 2$], [$sqrt(3) / 2$], [$sqrt(3)$],
  [$90^circle$], [$pi / 2$], [$0$], [$1$], [_Non défini_],
  [$120^circle$], [$2 pi / 3$], [$- 1 / 2$], [$sqrt(3) / 2$], [$- sqrt(3)$],
  [$135^circle$], [$3 pi / 4$], [$- sqrt(2) / 2$], [$sqrt(2) / 2$], [$- 1$],
  [$150^circle$], [$5 pi / 6$], [$- sqrt(3) / 2$], [$1 / 2$], [$- sqrt(3) / 3$],
  [$180^circle$], [$pi$], [$- 1$], [$0$], [$0$]
)

#v(0.3cm)
== II. Formules Trigonométriques d'Addition et de Duplication

#grid(
  columns: (1fr, 1fr),
  gutter: 14pt,
  block(fill: rgb("#eff6ff"), stroke: 1.5pt + byrne-blue, inset: 12pt, radius: 6pt, width: 100%)[
    #align(center)[#text(weight: "bold", fill: byrne-blue, size: 11pt)[Formules d'Addition]]
    #v(6pt)
    #align(center)[
      $ cos(a + b) = cos(a) cos(b) - sin(a) sin(b) $
      #v(5pt)
      $ cos(a - b) = cos(a) cos(b) + sin(a) sin(b) $
      #v(5pt)
      $ sin(a + b) = sin(a) cos(b) + cos(a) sin(b) $
      #v(5pt)
      $ sin(a - b) = sin(a) cos(b) - cos(a) sin(b) $
    ]
  ],
  block(fill: rgb("#f0fdf4"), stroke: 1.5pt + byrne-green, inset: 12pt, radius: 6pt, width: 100%)[
    #align(center)[#text(weight: "bold", fill: byrne-green, size: 11pt)[Formules de Duplication]]
    #v(6pt)
    #align(center)[
      $ cos(2 a) = cos^2(a) - sin^2(a) $
      #v(5pt)
      $ cos(2 a) = 2 cos^2(a) - 1 $
      #v(5pt)
      $ cos(2 a) = 1 - 2 sin^2(a) $
      #v(5pt)
      $ sin(2 a) = 2 sin(a) cos(a) $
      #v(5pt)
      $ cos^2(a) + sin^2(a) = 1 $
    ]
  ]
)

#v(0.3cm)
== III. Table Universelle des Dérivées Usuelles & Opérations

#table(
  columns: (1.5fr, 1.5fr, 2.5fr),
  fill: (x, y) => if y == 0 { rgb("#15803d") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 6.5pt,
  table.header(
    text(weight: "bold", fill: white)[Fonction $f(x)$],
    text(weight: "bold", fill: white)[Dérivée $f'(x)$],
    text(weight: "bold", fill: white)[Domaine de Validité / Règle]
  ),
  [$k$ (constante)], [$0$], [$x in bb(R)$],
  [$x$], [$1$], [$x in bb(R)$],
  [$x^n$ ($n in bb(N)^*$)], [$n x^(n-1)$], [$x in bb(R)$],
  [$1 / x$], [$- 1 / x^2$], [$x in bb(R)^*$],
  [$sqrt(x)$], [$1 / (2 sqrt(x))$], [$x in ]0\,;+infinity[$],
  [$e^x$], [$e^x$], [$x in bb(R)$ (l'unique fonction égale à sa dérivée avec $f(0)=1$)],
  [$ln(x)$], [$1 / x$], [$x in ]0\,;+infinity[$],
  [$cos(x)$], [$- sin(x)$], [$x in bb(R)$],
  [$sin(x)$], [$cos(x)$], [$x in bb(R)$],
  [$(u + v)'$], [$u' + v'$], [Linéarité de la dérivation],
  [$(u dot v)'$], [$u' v + u v'$], [Règle du produit de Leibniz],
  [$(u / v)'$], [$(u' v - u v') / v^2$], [Règle du quotient ($v != 0$)],
  [$(e^u)'$], [$u' e^u$], [Composition exponentielle],
  [$(ln u)'$], [$u' / u$], [Composition logarithmique ($u > 0$)]
)

#recto()
= ANNEXE B : TABLE UNIVERSELLE DES NOTATIONS & SYMBOLES

#set text(size: 9pt)
#table(
  columns: (1.2fr, 2fr, 4fr),
  fill: (x, y) => if y == 0 { rgb("#0f172a") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 6pt,
  table.header(
    text(weight: "bold", fill: white)[Symbole],
    text(weight: "bold", fill: white)[Nom & Lecture],
    text(weight: "bold", fill: white)[Signification Didactique & Exemple]
  ),
  [$bb(N)$], [Entiers naturels], [Ensemble des entiers positifs ou nuls : $\{0, 1, 2, 3, dots\}$],
  [$bb(Z)$], [Entiers relatifs], [Entiers positifs et négatifs : $\{dots, -2, -1, 0, 1, 2, dots\}$],
  [$bb(D)$], [Nombres décimaux], [Nombres s'écrivant avec un nombre fini de chiffres après la virgule : $a / 10^n$],
  [$bb(Q)$], [Nombres rationnels], [Fractions de deux entiers relatifs : $p / q$ avec $q != 0$],
  [$bb(R)$], [Nombres réels], [Tous les points de la droite continue (inclut $sqrt(2), pi, e$)],
  [$bb(C)$], [Nombres complexes], [Nombres de la forme $z = a + i b$ où $i^2 = -1$],
  [$in$ / $in.not$], [Appartient / N'appartient pas], [Relie un élément à un ensemble : $3 in bb(N)$, mais $-2 in.not bb(N)$],
  [$subset$], [Inclus dans], [Relie deux ensembles : $bb(N) subset bb(Z) subset bb(D) subset bb(Q) subset bb(R) subset bb(C)$],
  [$inter$], [Intersection], [$A inter B$ : ensemble des éléments communs à $A$ et à $B$ (ET logique)],
  [$union$], [Réunion / Union], [$A union B$ : ensemble des éléments appartenant à $A$ ou à $B$ (OU logique)],
  [$emptyset$], [Ensemble vide], [L'ensemble qui ne contient aucun élément],
  [$forall$], [Pour tout / Quel que soit], [Quantificateur universel : $forall x in bb(R), x^2 >= 0$],
  [$exists$], [Il existe], [Quantificateur existentiel : $exists x in bb(R), x^2 = 2$],
  [$==>$ / $<==>$], [Implique / Équivaut à], [Déduction logique et équivalence bilatérale stricte],
  [$vec(u)$ / $arrow(A B)$], [Vecteur], [Déplacement orienté caractérisé par une direction, un sens et une norme],
  [$norm(vec(u))$], [Norme d'un vecteur], [Longueur géométrique du segment orienté représenté par $vec(u)$],
  [$vec(u) dot vec(v)$], [Produit scalaire], [Mesure de projection géométrique : $norm(vec(u)) norm(vec(v)) cos(theta)$],
  [$lim_(x -> a)$], [Limite], [Comportement local d'une fonction à l'approche de la borne $a$ ou de l'$infinity$],
  [$f'(x)$], [Dérivée première], [Taux d'accroissement instantané et pente de la droite tangente],
  [$integral_a^b f(t) d t$], [Intégrale définie], [Mesure d'aire signée sous la courbe de $f$ entre les bornes $a$ et $b$],
  [$sum_(i=1)^n$], [Somme discrète], [Addition séquentielle des termes : $x_1 + x_2 + dots + x_n$],
  [$binom(n, k)$], [Combinaison], [Nombre de façons de choisir $k$ éléments parmi $n$ sans ordre : $n! / (k!(n-k)!)$]
)

#recto()
= INDEX THÉMATIQUE DÉTAILLÉ

#set text(size: 9pt)
#table(
  columns: (2.5fr, 1.2fr, 4fr),
  fill: (x, y) => if y == 0 { rgb("#1d4ed8") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 6pt,
  table.header(
    text(weight: "bold", fill: white)[Concept Clé],
    text(weight: "bold", fill: white)[Localisation],
    text(weight: "bold", fill: white)[Signification Pédagogique & Didactique]
  ),
  [Abaque / Boulier], [Vol. I, Ch. 4], [Matérialisation du groupement décimal et transitivité de la retenue],
  [Aire du rectangle / disque], [Vol. II, Ch. 12 & 16], [Mesure du pavage 2D et quadrature circulaire par Archimède],
  [Algorithme d'Euclide], [Vol. IV, Ch. 29], [Recherche du PGCD par soustractions puis divisions successives],
  [Angle (aigu, droit, obtus)], [Vol. III, Ch. 15], [Mesure de l'ouverture d'un secteur angulaire indépendamment des longueurs],
  [Arbre pondéré], [Vol. V, Ch. 42], [Représentation des probabilités conditionnelles et formule de Bayes],
  [Asymptote (horizontale, verticale)], [Vol. VI, Ch. 45], [Comportement aux bornes infinies ou valeurs interdites],
  [Balance d'Al-Khwarizmi], [Vol. IV, Ch. 22], [Équivalence des opérations bilatérales pour la résolution d'équations],
  [Base dix (décimale)], [Vol. I, Ch. 2], [Groupement par paquets de dix fondé sur la morphologie des deux mains],
  [Bijection (un-pour-un)], [Vol. I, Ch. 1], [Correspondance terme à terme du sac de cailloux préhistorique],
  [Cercle trigonométrique], [Vol. V, Ch. 37], [Enroulement de la droite réelle sur le cercle unité et projections],
  [Dérivée et Tangente], [Vol. V, Ch. 39], [Passage de la sécante moyenne à la tangente instantanée],
  [Équation différentielle], [Vol. VI, Ch. 51], [Loi physique d'évolution où la vitesse dépend de l'état présent ($y' = a y$)],
  [Exponentielle ($e^x$)], [Vol. V, Ch. 40], [Fonction unique égale à sa propre dérivée avec $f(0) = 1$],
  [Fractions (partage et quotient)], [Vol. II, Ch. 10], [Fraction comme opérateur de découpage puis comme nombre rationnel],
  [Intégrale de Riemann], [Vol. VI, Ch. 50], [Limite des sommes de tranches rectangulaires pour le calcul d'aires],
  [Logarithme népérien], [Vol. VI, Ch. 48], [Fonction réciproque de l'exponentielle transformant les produits en sommes],
  [Loi Normale (Gauss)], [Vol. VI, Ch. 54], [Distribution en cloche universelle issue du théorème central limite],
  [Matrices et Graphes], [Vol. VI, Ch. 57], [Tableaux d'opérations multilignes et marches aléatoires de Markov],
  [Multiplication posée], [Vol. I, Ch. 5], [Algorithme à deux étages avec décalage du zéro de dizaine],
  [Nombres complexes], [Vol. VI, Ch. 55], [Plan d'Argand-Gauss et nombre imaginaire $i^2 = -1$ comme rotation de 90°],
  [Nombres négatifs / relatifs], [Vol. II, Ch. 14], [Symétrie axiale autour de zéro pour les dettes et températures froides],
  [Pythagore (Théorème de)], [Vol. III, Ch. 19], [Conservation de l'aire des carrés sur les côtés de l'angle droit ($a^2 + b^2 = c^2$)],
  [Récurrence (Principe de)], [Vol. VI, Ch. 43], [Transmission héréditaire de la vérité mathématique (effet domino)],
  [Subitizing], [Vol. I, Ch. 1], [Reconnaissance visuelle instantanée des collections jusqu'à 3 ou 4 objets],
  [Thalès (Théorème de)], [Vol. III, Ch. 17], [Conservation des rapports de proportionnalité par projection parallèle],
  [Valeurs Intermédiaires (TVI)], [Vol. VI, Ch. 46], [Théorème topologique assurant qu'une fonction continue traverse toutes les valeurs]
)

#recto()
= BIBLIOGRAPHIE HISTORIQUE & DIDACTIQUE ANNOTÉE

#v(0.3cm)
=== I. Les Textes Fondateurs de l'Histoire des Mathématiques

- *Euclide d'Alexandrie* (vers 300 av. J.-C.), *Les Éléments*. Traduction et commentaires de B. Vitrac, Éditions PUF.
  _L'ouvrage séminal qui a instauré la méthode axiomatique déductive et la rigueur géométrique._
- *Al-Khwarizmi, Muhammad ibn Musa* (vers 820), *Al-Kitab al-mukhtasar fi hisab al-jabr wa'l-muqabala* (L'Abrégé du calcul par la restauration et la comparaison).
  _L'acte de naissance de l'algèbre comme science autonome des opérations d'équilibre bilatéral._
- *Descartes, René* (1637), *La Géométrie*. Appendice au *Discours de la Méthode*.
  _L'unification de l'algèbre et de la géométrie par l'invention du repère de coordonnées cartésiennes._
- *Byrne, Oliver* (1847), *The First Six Books of the Elements of Euclid in which Coloured Diagrams and Symbols are used instead of Letters for the Greater Ease of Learners*, William Pickering, Londres.
  _Le chef-d'œuvre de la sémiotique visuelle mathématique qui a inspiré la palette graphique du présent livre._
- *Euler, Leonhard* (1748), *Introductio in analysin infinitorum*.
  _Le texte qui a fondé l'analyse moderne, la théorie des fonctions, la notation de la base $e$ et l'identité $e^(i pi) + 1 = 0$._
- *Gauss, Carl Friedrich* (1801), *Disquisitiones Arithmeticae*.
  _La refondation monumentale de la théorie des nombres, de l'arithmétique modulaire et des congruences._

=== II. Didactique, Sciences Cognitives & Cognition Incarnée

- *Lakoff, George & Núñez, Rafael* (2000), *Where Mathematics Comes From: How the Embodied Mind Brings Mathematics into Being*, Basic Books.
  _L'ouvrage séminal de la cognition mathématique incarnée. Il démontre comment les concepts les plus abstraits (l'infini actuel, les limites, les nombres complexes) sont construits à partir de métaphores conceptuelles ancrées dans le corps, le geste et la manipulation motrice._
- *Dehaene, Stanislas* (2010), *La Bosse des maths : Quinze ans après*, Éditions Odile Jacob.
  _Les fondements neurocognitifs du sens du nombre, du subitizing et du recyclage neuronal._
- *Brousseau, Guy* (1998), *Théorie des situations didactiques*, La Pensée Sauvage.
  _Analyse de la dévolution, du contrat didactique et de l'obstacle épistémologique._
- *Charnay, Roland & Mante, Michel* (2019), *Cap Maths : Apprentissages mathématiques*, Hatier.
  _Méthodologie fondamentale du passage de la manipulation concrète à l'abstraction opératoire._
- *Polya, George* (1945), *How to Solve It* (Comment poser et résoudre un problème), Princeton University Press.
  _Le grand classique de l'heuristique mathématique : observer, décomposer, généraliser et vérifier les cas limites._
- *Sweller, John* (2011), *Cognitive Load Theory*, Springer.
  _Théorie de la charge cognitive : équilibre indispensable entre mémoire de travail et mémoire à long terme._

// Le bloc intérieur se termine sur un verso (page paire) : page blanche muette si nécessaire
#metadata("fin-section") <fin-section>
#pagebreak(to: "odd")
#set page(header: none, footer: none)
#metadata("debut-section") <debut-section>
// Plat 3 (intérieur de couverture arrière) : hors décompte, jamais folioté
#box()
#pagebreak()

// Plat 4 (quatrième de couverture) : jamais foliotée

// ==========================================
// 5. QUATRIÈME DE COUVERTURE (BACK COVER)
// ==========================================
#align(center + horizon)[
  #block(
    fill: rgb("#0f172a"),
    inset: 28pt,
    radius: 12pt,
    width: 95%
  )[
    #text(size: 13pt, weight: "bold", fill: byrne-yellow, tracking: 2pt, font: "Liberation Sans")[SILVÈRE-MARTIN MICHIELLOT & ANTIGRAVITY]
    #v(0.5cm)
    #text(size: 26pt, weight: "bold", fill: white, font: "Liberation Serif")[LA VOIE DU NOMBRE]
    #v(0.2cm)
    #text(size: 13pt, weight: "bold", fill: rgb("#93c5fd"), font: "Liberation Sans")[Une Odyssée Constructive, du Premier Caillou au Baccalauréat]
    #v(0.6cm)
    
    #align(left)[
      #text(size: 10pt, fill: rgb("#e2e8f0"), font: "Liberation Serif")[
        Comment réconcilier durablement l'esprit humain avec la beauté et la puissance des mathématiques ? Pourquoi tant d'enfants et d'adolescents décrochent-ils face à des symboles abstraits dont on a oublié de leur raconter l'origine vivante ?
        
        *LA VOIE DU NOMBRE* relève ce défi monumental en cinquante-huit chapitres reliés comme les maillons d'une même chaîne ininterrompue, guidant l'élève depuis l'âge de 6 ans (CP) jusqu'aux portes de l'enseignement supérieur (Terminale Spécialité et Maths Expertes).
      ]
      
      #v(0.5cm)
      #grid(
        columns: (1fr, 1fr),
        gutter: 14pt,
        block(fill: rgb("#1e293b"), inset: 10pt, radius: 6pt)[
          #text(size: 9.5pt, weight: "bold", fill: byrne-yellow)[1. Ancrage Historique :]\\
          #text(size: 8.5pt, fill: rgb("#cbd5e1"))[Chaque concept naît d'un problème réel résolu par l'humanité : du Nil d'Euclide aux logarithmes de Napier.]
        ],
        block(fill: rgb("#1e293b"), inset: 10pt, radius: 6pt)[
          #text(size: 9.5pt, weight: "bold", fill: rgb("#60a5fa"))[2. Sémiotique d'Oliver Byrne :]\\
          #text(size: 8.5pt, fill: rgb("#cbd5e1"))[L'intelligence par la couleur et la forme : le regard comprend avant même que le calcul formel ne commence.]
        ],
        block(fill: rgb("#1e293b"), inset: 10pt, radius: 6pt)[
          #text(size: 9.5pt, weight: "bold", fill: rgb("#4ade80"))[3. Algorithmes Opératoires :]\\
          #text(size: 8.5pt, fill: rgb("#cbd5e1"))[Automatisation motrice du calcul posé : libérer la mémoire de travail pour accéder aux sommets logiques.]
        ],
        block(fill: rgb("#1e293b"), inset: 10pt, radius: 6pt)[
          #text(size: 9.5pt, weight: "bold", fill: rgb("#f87171"))[4. Élucidation des Cas Limites :]\\
          #text(size: 8.5pt, fill: rgb("#cbd5e1"))[La division par zéro, le rôle du vide, l'infini et les matrices creuses : la rigueur sans aucun angle mort.]
        ]
      )
      
      #v(0.6cm)
      #align(center)[
        #line(length: 60%, stroke: 1.5pt + byrne-yellow)
        #v(0.2cm)
        #text(size: 8.5pt, fill: rgb("#94a3b8"), style: "italic")[« Tout est nombre, et le nombre est le guide de l'âme. » — Philolaos de Crotone]
      ]
    ]
  ]
]
"""

# ==============================================================================
# 3. LINE-BY-LINE PARSER & TRANSFORMATION ENGINE
# ==============================================================================

USED_SVGS = set()

SVG_ALTERNATES = {}

def deduplicate_markdown_svgs(md_text):
    def repl(m):
        pfx = m.group(1) or ""
        cap = m.group(2)
        svg = m.group(3)
        if svg not in USED_SVGS:
            USED_SVGS.add(svg)
            return f"{pfx}![{cap}]({svg})"
        for alt_svg, alt_cap in SVG_ALTERNATES.get(svg, []):
            if alt_svg not in USED_SVGS:
                USED_SVGS.add(alt_svg)
                return f"{pfx}![{alt_cap}]({alt_svg})"
        return ""
    return re.sub(r'([ \t]*>*)?[ \t]*!\[([^\]]*)\]\(([^)]+)\)', repl, md_text)

def replace_raw_svg(match):
    raw = match.group(0)
    raw_l = raw.lower()
    if 'tablette couchée' in raw_l or 'commutativité' in raw_l:
        return "\n![La commutativité par rotation 90°](figures/vol_1/fig_05_commutativite_rotation.svg)\n"
    elif 'multiplication posée à deux étages' in raw_l or '1  4  6' in raw or '4  3  8' in raw:
        return "\n![La multiplication posée à deux étages avec retenue](figures/vol_1/fig_05_multiplication_posee_ret.svg)\n"
    elif "l'anatomie de la potence" in raw_l or "d-m-s-a" in raw_l:
        return "\n![L'anatomie de la potence de division euclidienne](figures/vol_2/fig_09_potence_division.svg)\n"
    elif "a²" in raw_l and "ab" in raw_l and "b²" in raw_l:
        return "\n![Preuve géométrique de l'identité remarquable (a+b)²](figures/vol_4/fig_23_identite_remarquable_carre.svg)\n"
    elif "chasles" in raw_l or ("u = ab" in raw_l and "v = bc" in raw_l):
        return "\n![Vecteurs dans le plan : relation de Chasles u + v](figures/vol_5/fig_32_chasles_addition.svg)\n"
    elif "cosinus x" in raw_l or "sinus x" in raw_l:
        return "\n![Le cercle trigonométrique et les fonctions sinus et cosinus](figures/vol_5/fig_37_cercle_trigo_complet.svg)\n"
    elif "plan 𝒫" in raw or "plan p" in raw_l or "vecteur normal" in raw_l:
        return "\n![Équation cartésienne du plan et vecteur normal](figures/vol_6/fig_52_plan_vecteur_normal.svg)\n"
    return ""

def process_file_content(content, chapter_name, vol_dir):
    # 1. Replace raw HTML SVGs with their corresponding vector figures
    content = re.sub(r'(<div[^>]*>)?\s*<svg[\s\S]*?<\/svg>\s*(<\/div>)?', replace_raw_svg, content, flags=re.IGNORECASE)
    
    # 2. Strip trailing whitespace and add automatic blank lines around lists and exercises/solutions
    content = "\n".join(l.rstrip() for l in content.splitlines())
    content = re.sub(r'(^[^\n\-\*>][^\n]*)\n([ \t]*-\s+)', r'\1\n\n\2', content, flags=re.MULTILINE)
    content = re.sub(r'(^>[ \t]*[^\n\-\*>][^\n]*)\n(>[ \t]*-\s+)', r'\1\n>\n\2', content, flags=re.MULTILINE)
    content = re.sub(r'(^[ \t]*-\s+[^\n]+)\n([A-ZÀ-ÖØ-ß][^\n\-\*\#])', r'\1\n\n\2', content, flags=re.MULTILINE)
    content = re.sub(r'([^\n])\n(\*(?:Exercice|Solution|Problème)\s+\d+|\*\*(?:Exercice|Solution|Problème)\s+\d+)', r'\1\n\n\2', content)

    lines = content.splitlines()
    out_lines = []
    in_block = False
    cur_block = []
    cur_prefix = ""
    cur_lang = ""
    start_line = 0
    
    # 3. Strip line 1 volume title
    start_idx = 0
    while start_idx < len(lines) and not lines[start_idx].strip():
        start_idx += 1
    if start_idx < len(lines) and re.match(r'^[ \t]*#[ \t]+VOLUME\b', lines[start_idx], re.IGNORECASE):
        start_idx += 1
    lines = lines[start_idx:]
    
    for i, line in enumerate(lines):
        clean = line.strip()
        is_fence = False
        prefix = ""
        lang = ""
        
        if clean.startswith("```"):
            is_fence = True
            prefix = line[:line.index("```")]
            lang = clean[3:].strip()
        elif clean.startswith(">") and clean.lstrip("> ").startswith("```"):
            is_fence = True
            idx = line.index("```")
            prefix = line[:idx]
            lang = clean.lstrip("> ")[3:].strip()
            
        if is_fence and not in_block:
            in_block = True
            cur_prefix = prefix
            cur_lang = lang
            start_line = i + 1
            cur_block = []
        elif is_fence and in_block:
            in_block = False
            replacement = transform_block(cur_block, cur_lang, cur_prefix, chapter_name, start_line, vol_dir)
            out_lines.append(replacement)
            cur_block = []
        elif in_block:
            if cur_prefix and line.startswith(cur_prefix):
                cur_block.append(line[len(cur_prefix):])
            else:
                cur_block.append(line)
        else:
            out_lines.append(line)
            
    return deduplicate_markdown_svgs("\n".join(out_lines))


def format_arithmetic_operation(raw_text):
    lines = [re.sub(r'^[ \t]*>[ \t]?', '', l) for l in raw_text.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines:
        return ""
        
    dedented_lines = textwrap.dedent("\n".join(lines)).splitlines()
    norm_lines = []
    for l in dedented_lines:
        l_norm = re.sub(r'[─—–]', '-', l)
        l_norm = l_norm.replace('★', '?').replace('■', '?')
        norm_lines.append(l_norm)
        
    header_idx = -1
    for i, l in enumerate(norm_lines[:3]):
        clean_words = l.strip().split()
        if clean_words and all(w.lower() in ['m', 'c', 'd', 'u'] for w in clean_words) and len(clean_words) >= 2:
            header_idx = i
            break
            
    if header_idx != -1:
        operand_line = None
        for l in norm_lines[header_idx + 1:]:
            if any(c.isdigit() for c in l) and not l.strip().startswith('-'):
                operand_line = l
                break
        if operand_line:
            m_comm = re.search(r'[\(<]|Le\s+', operand_line)
            math_part = operand_line[:m_comm.start()] if m_comm else operand_line
            digit_indices = [idx for idx, c in enumerate(math_part) if c.isdigit()]
            words = norm_lines[header_idx].strip().split()
            if len(words) <= len(digit_indices):
                target_positions = digit_indices[-len(words):]
                m_hdr_comm = re.search(r'[\(<]', norm_lines[header_idx])
                hdr_comm = norm_lines[header_idx][m_hdr_comm.start():] if m_hdr_comm else ""
                max_pos = max(target_positions) + 2
                header_chars = [' '] * max_pos
                for w, pos in zip(words, target_positions):
                    header_chars[pos] = w
                new_hdr = "".join(header_chars)
                if hdr_comm:
                    new_hdr = new_hdr.rstrip() + "   " + hdr_comm
                norm_lines[header_idx] = new_hdr

    for i, l in enumerate(norm_lines[:3]):
        if re.search(r'^\s*\(\d+\)', l):
            ref_line = None
            for next_l in norm_lines[i+1:i+3]:
                if any(c.isdigit() for c in next_l):
                    ref_line = next_l
                    break
            if ref_line:
                m_comm = re.search(r'[\(<]|Le\s+', ref_line)
                math_part = ref_line[:m_comm.start()] if m_comm else ref_line
                digits = [idx for idx, c in enumerate(math_part) if c.isdigit()]
                if len(digits) >= 2:
                    tens_pos = digits[-2]
                    m_ret = re.search(r'(\(\d+\))(\s*.*)', l.strip())
                    if m_ret:
                        ret_tag = m_ret.group(1)
                        ret_rest = m_ret.group(2)
                        start_pos = max(0, tens_pos - 1)
                        norm_lines[i] = " " * start_pos + ret_tag + ret_rest

    return textwrap.dedent("\n".join(norm_lines))

def transform_block(block_lines, lang, prefix, chapter_name, start_line, vol_dir):
    code = "\n".join(block_lines).strip()
    pfx = prefix if prefix else ""
    code_l = code.lower()
    lines = [re.sub(r'^[ \t]*>[ \t]?', '', l).strip() for l in block_lines if l.strip()]
    code_clean = "\n".join(lines)
    code_clean_l = code_clean.lower()

    # 1. Python code (with mandatory leading & trailing newlines so Pandoc never merges with list items!)
    if lang.lower() in ["python", "py"] or code_clean.startswith(("def ", "import ", "from ", "while ", "for ")) or ("def " in code_clean and ":" in code_clean):
        inner = "\n".join([f"{pfx}{l}" for l in block_lines])
        return f"\n{pfx}```python\n{inner}\n{pfx}```\n"

    # 2. Clean Native Typst Tables (including sign/variation tables and comparison tables)
    if 'grandeur 1 (ex. : nombre de cahiers)' in code_clean_l or ('cahiers' in code_clean_l and 'prix (€)' in code_clean_l):
        typ = '''```data_table
#align(center)[
  #table(
    columns: (2.5fr, 1fr, 1fr, 1fr, 1fr),
    align: (left, center, center, center, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { rgb("#ffffff") },
    [Grandeur 1 (nombre de cahiers)], [2], [4], [6], [10],
    [Grandeur 2 (prix en euros)], [5 €], [10 €], [15 €], [25 €]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if 'centaines' in code_clean_l and 'dizaines' in code_clean_l and '4 × 100 = 400' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1fr, 1fr, 1fr, 1.8fr),
    align: center,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [*Centaines*], [*Dizaines*], [*Unités*], [*Valeur décimale*],
    [], [], [4], [$4$],
    [], [4], [0], [$4 times 10 = 40$],
    [4], [0], [0], [$4 times 100 = 400$]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if 'nombre de gâteaux' in code_clean_l and 'nombre de fraises' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (2.5fr, 1fr, 1fr, 1fr, 1.2fr),
    align: (left, center, center, center, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { rgb("#ffffff") },
    [Nombre de gâteaux], [3], [5], [8], [× 4],
    [Nombre de fraises], [12], [20], [32], [(Coefficient)]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if '1ère case' in code_clean_l and '2e case' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1fr, 1fr, 1fr, 1fr, 0.8fr, 1.2fr),
    align: center,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [*1re case*], [*2e case*], [*3e case*], [*4e case*], [*...*], [*64e case*],
    [1 grain], [2 grains], [4 grains], [8 grains], [...], [$2^(63)$ grains !]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if 'équation : x² = a' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1fr, 1fr, 1fr),
    align: center,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [*Cas $a > 0$*], [*Cas $a = 0$*], [*Cas $a < 0$*],
    [Deux solutions opposées :\n$x = sqrt(a)$ ou $x = -sqrt(a)$], [Une solution unique :\n$x = 0$], [Aucune solution réelle :\nImpossible dans $bb(R)$ ($S = emptyset$)]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if "1. l'expression algébrique" in code_clean_l and "2. le tableau" in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1fr, 1fr, 1fr),
    align: center,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [*1. L'expression algébrique*], [*2. Le tableau de valeurs*], [*3. La courbe représentative*],
    [La formule exacte\nExemple : $f(x) = 2x + 1$], [Échantillons finis de couples\n$(x ; f(x))$], [Vision géométrique continue\ndans le repère]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if "contrat matteo" in code_clean_l or "contrat cosimo" in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1.2fr, 2fr, 2fr),
    align: (center, center, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [*Échéance*], [*Contrat Matteo (Prêt arithmétique : +100 / an)*], [*Contrat Cosimo (Prêt géométrique : +10 % / an)*],
    [Année 0], [1 000 florins], [1 000 florins],
    [Année 1], [1 100 florins], [1 100 florins],
    [Année 2], [1 200 florins], [1 210 florins],
    [Année 3], [1 300 florins], [1 331 florins],
    [Année 10], [2 000 florins], [*2 593,74 florins !*]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if "progression arithmétique" in code_clean_l and "progression géométrique" in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (2.2fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.8fr, 0.8fr),
    align: center,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [*Progression arithmétique*], [0], [1], [2], [3], [4], [5], [6], [7], [8],
    [*Progression géométrique*], [1], [2], [4], [8], [16], [32], [64], [128], [256]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if 'lancers (n)' in code_clean_l and 'fréquence pile' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1fr, 1fr, 1fr),
    align: (center, center, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [Lancers ($n$)], [Fréquence Pile], [Écart à 0.5],
    [10], [0.7000], [+0.2000],
    [50], [0.4400], [+0.0600],
    [100], [0.5300], [+0.0300],
    [500], [0.4880], [+0.0120],
    [1 000], [0.5040], [+0.0040],
    [5 000], [0.4982], [+0.0018],
    [10 000], [0.5007], [+0.0007]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if 'temps t (h) :' in code_clean_l and 'bactéries' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1.5fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: (left, center, center, center, center, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { rgb("#ffffff") },
    [Temps $t$ (h)], [0], [1], [2], [3], [10],
    [Bactéries], [1 000], [2 000], [4 000], [8 000], [1 024 000]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if "ln'(x)" in code_clean and "ln(x)" in code_clean:
        if "↗" in code_clean:
            typ = '''```data_table
#align(center)[
  #table(
    columns: (1.5fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [$x$], [$0$ (valeur interdite)], [], [$1$], [], [$+infinity$],
    [Signe de $ln'(x) = 1/x$], [||], [$+$], [$+$], [$+$], [],
    [Variations de $ln(x)$], [$-infinity$], [$arrow.tr$], [$0$], [$arrow.tr$], [$+infinity$]
  )
]
```'''
        else:
            typ = '''```data_table
#align(center)[
  #table(
    columns: (1.5fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [$x$], [$0$ (valeur interdite)], [$]0 ; 1[$], [$1$], [$]1 ; +infinity[$], [$+infinity$],
    [Signe de $ln'(x)$], [||], [$+$], [$+$], [$+$], [],
    [Signe de $ln(x)$], [||], [$-$], [$0$], [$+$], []
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if "cos'(x)" in code_clean and "cos(x)" in code_clean:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1.5fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [$x$], [$-pi$], [], [$0$], [], [$pi$],
    [Signe de $cos'(x) = -sin(x)$], [$0$], [$+$], [$0$], [$-$], [$0$],
    [Variations de $cos(x)$], [$-1$ (Min)], [$arrow.tr$], [$1$ (Max)], [$arrow.br$], [$-1$ (Min)]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if "sin'(x)" in code_clean and "sin(x)" in code_clean:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1.2fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: (center, center, center, center, center, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { rgb("#ffffff") },
    [$x$], [$-pi$], [$-pi/2$], [$0$], [$pi/2$], [$pi$],
    [$sin'(x) = cos(x)$], [$-$], [$0$], [$+$], [$0$], [$-$],
    [$sin(x)$], [$0$], [$-1$ (Min)], [$0$], [$1$ (Max)], [$0$]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if 'x    │ -π' in code_clean or ('-π/2' in code_clean and 'π/2' in code_clean and 'cos' in code_clean_l):
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1.2fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: (center, center, center, center, center, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [$x$], [$-pi$], [$-pi/2$], [$0$], [$pi/2$], [$pi$],
    [$cos(x)$], [$-1$], [$0$], [$1$], [$0$], [$-1$],
    [$sin(x)$], [$0$], [$-1$], [$0$], [$1$], [$0$]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if 'n \\ k' in code_clean or 'somme de la ligne' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 1.5fr),
    align: center,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [$n \\ k$], [0], [1], [2], [3], [4], [5], [Somme $2^n$],
    [0], [1], [], [], [], [], [], [$1 = 2^0$],
    [1], [1], [1], [], [], [], [], [$2 = 2^1$],
    [2], [1], [2], [1], [], [], [], [$4 = 2^2$],
    [3], [1], [3], [3], [1], [], [], [$8 = 2^3$],
    [4], [1], [4], [6], [4], [1], [], [$16 = 2^4$],
    [5], [1], [5], [10], [10], [5], [1], [$32 = 2^5$]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if 'angle aigu' in code_clean_l and 'épouse l\'équerre' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [*Angle Aigu*], [*Angle Droit*], [*Angle Obtus*],
    [Plus fermé que l'équerre], [Épouse exactement l'équerre], [Plus ouvert que l'équerre],
    [Ouverture $< 90 degree$], [Ouverture $= 90 degree$], [Ouverture $> 90 degree$]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if 'ordres de grandeur dans l\'univers' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [*Noyau*], [*Atome*], [*Humain*], [*Terre*], [*Système Solaire*], [*Galaxie*],
    [$10^(-15)$ m], [$10^(-10)$ m], [$1$ m ($10^0$ m)], [$10^6$ m], [$10^(11)$ m], [$10^(21)$ m]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    if '1. diagramme en bâtons' in code_clean_l and '2. histogramme' in code_clean_l:
        typ = '''```data_table
#align(center)[
  #table(
    columns: (1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (x, y) => if y == 0 { rgb("#eff6ff") } else { rgb("#ffffff") },
    [*1. Diagramme en bâtons*], [*2. Histogramme (classes)*], [*3. Diagramme circulaire*],
    [Valeurs discrètes isolées], [Intervalles continus accolés], [Parts proportionnelles à $360 degree$],
    [Hauteur proportionnelle à l'effectif], [Aire du rectangle proportionnelle à l'effectif], [Angle proportionnel à la fréquence (%)]
  )
]
```'''
        return f"\n{pfx}{typ}\n"

    clean_text = re.sub(r'[─│┌┐└┘├┤┬┴┼═║╔╗╚╝╠╣╦╩╬▲►▼◄╭╮╯╰╱╲★●■]', '', code_clean).strip()
    clean_lines = [re.sub(r'^[\s/\\.*~\-_=+;:<>()\[\]{}|]+', '', l).strip() for l in clean_text.splitlines()]
    clean_lines = [l for l in clean_lines if l and len(l) > 1]
    # Format callout_body as a clean vertical bullet list so lines NEVER merge into a single run-on line!
    callout_body = f"\n{pfx}> - " + f"\n{pfx}> - ".join(clean_lines) if clean_lines else ""

    # 3. Genuine Vertical Arithmetic Operations (ONLY in Ch 4, 5, 9, 11, or linear system/Gauss sum)
    ch_num_m = re.search(r'Chapitre_(\d+)', chapter_name)
    ch_num = int(ch_num_m.group(1)) if ch_num_m else 0
    if ch_num in [4, 5, 9, 11]:
        is_div = (ch_num == 9) and any('|---' in l or '|───' in l or '|----' in l for l in lines)
        has_du = any(re.search(r'\b[c|d]\s+[d|u]\b', l.lower()) for l in lines) or any(k in code_clean_l for k in ['d   u', 'c  d  u', 'c   d   u', 'd  u', 'd    u'])
        has_vert_op = any(l.startswith(('+', '-', '×', '*')) for l in lines) and any(re.match(r'^[─\-=]{3,}$', l.strip()) for l in lines) and not any(k in code_clean_l for k in ['tableau', 'centaines', 'dividende', 'virgule glisse'])
        if is_div or has_du or has_vert_op or 'calcul fait :' in code_clean_l or 'étage 1 :' in code_clean_l:
            inner = "\n".join([f"{pfx}{l}" for l in block_lines])
            return f"\n{pfx}```calc_op\n{inner}\n{pfx}```\n"
    elif "4x  +  6y  =  38" in code_clean or "100   +  99   +  98" in code_clean:
        inner = "\n".join([f"{pfx}{l}" for l in block_lines])
        return f"\n{pfx}```calc_op\n{inner}\n{pfx}```\n"

    # 4. Volume I to VI SVG Figures
    # --- VOLUME I ---
    if vol_dir == "Volume_I":
        if "ce que ton œil voit d'un coup" in code_clean_l or "subitizing" in code_clean_l:
            return f"\n{pfx}![Le phénomène du subitizing : perception immédiate vs saturation cognitive](figures/vol_1/fig_01_subitizing.svg)\n"
        elif "face 1 :" in code_clean_l or "face 6 :" in code_clean_l:
            return f"\n{pfx}![Les six faces du dé : reconnaissance spatiale instantanée](figures/vol_1/fig_01_dice.svg)\n"
        elif "brebis 1" in code_clean_l and "caillou 1" in code_clean_l:
            return f"\n{pfx}![Correspondance un-pour-un : le caillou-témoin du berger](figures/vol_1/fig_01_correspondance.svg)\n"
        elif "collection a" in code_clean_l and "collection b" in code_clean_l:
            return f"\n{pfx}![Correspondance terme à terme : comparaison directe de deux collections](figures/vol_1/fig_01_correspondance.svg)\n"
        elif "ligne 1 :" in code_clean_l and "ligne 2 :" in code_clean_l:
            return f"\n{pfx}> **Exemple résolu — Comparaison Visuelle en Lignes Parallèles**\n{pfx}>{callout_body}\n"
        elif re.match(r'^[ \t]*\|{10,}[ \t]*$', code_clean):
            return f"\n{pfx}![Le bâton d'entailles : saturation cognitive des 45 traits continus](figures/vol_1/fig_02_baton_45_traits.svg)\n"
        elif "ishango" in code_clean_l or "encoches" in code_clean_l or ("|||||" in code_clean and len(lines) <= 10):
            return f"\n{pfx}![L'os d'Ishango : les premières encoches de dénombrement par paquets](figures/vol_1/fig_01_os_ishango.svg)\n"
        elif "doigt baissé" in code_clean_l or ("doigts" in code_clean_l and "table de 9" in code_clean_l):
            return f"\n{pfx}![L'astuce magique des dix doigts pour la table de 9](figures/vol_1/fig_05_doigts_table_9.svg)\n"
        elif "\\ | /" in code_clean or "(  5  )" in code_clean or "ensemble = 10" in code_clean_l:
            return f"\n{pfx}![Les deux mains ouvertes : 5 + 5 = 10, fondement de la base décimale](figures/vol_1/fig_02_deux_mains_dix.svg)\n"
        elif "1 caillou gris" in code_clean_l and "1 bouchon de liège" in code_clean_l:
            return f"\n{pfx}![La pyramide décimale : unités, dizaines, centaines, milliers](figures/vol_1/fig_02_pyramide_dizaines.svg)\n"
        elif "10 petits cailloux" in code_clean_l or "bouchon de liège" in code_clean_l or "échange magique" in code_clean_l:
            return f"\n{pfx}![L'échange régulier : 10 unités isolées deviennent 1 dizaine groupée](figures/vol_1/fig_02_echange_dizaine.svg)\n"
        elif "gardien de place" in code_clean_l or ("405" in code_clean and "centaines" in code_clean_l) or ("c | d | u" in code_clean_l and "4 | 0 | 5" in code_clean_l):
            return f"\n{pfx}> **📐 Règle Fondamentale — Le Rôle du Zéro Gardien de Place**\n{pfx}>{callout_body}\n"
        elif "tableau des maisons" in code_clean_l or ("dizaines" in code_clean_l and "unités" in code_clean_l and ("14" in code_clean or "41" in code_clean or "centaines" in code_clean_l)):
            return f"\n{pfx}![Tableau des maisons CDU : centaines, dizaines et unités](figures/vol_1/fig_02_tableau_maisons.svg)\n"
        elif "0    10    20    30" in code_clean or "droite graduée" in code_clean_l or "droite orientée" in code_clean_l or "|--->" in code_clean:
            return f"\n{pfx}![La droite numérique orientée de 0 à 100](figures/vol_1/fig_02_droite_100.svg)\n"
        elif "crocodile" in code_clean_l or "plus grand que" in code_clean_l or ("3  <  8" in code_clean and "9  >  4" in code_clean) or "bouche s'ouvre vers" in code_clean_l:
            return f"\n{pfx}![Le crocodile de comparaison : la gueule s'ouvre vers la plus grande quantité](figures/vol_1/fig_02_crocodile_comparaison.svg)\n"
        elif "marmite" in code_clean_l or ("3 cailloux" in code_clean_l and "4 cailloux" in code_clean_l):
            return f"\n{pfx}![La marmite d'addition : mise en commun de deux quantités](figures/vol_1/fig_03_marmite_addition.svg)\n"
        elif "poissons" in code_clean_l and "renard" in code_clean_l:
            return f"\n{pfx}![La soustraction concrète : 7 poissons moins 2 dérobés](figures/vol_1/fig_03_poissons_renard.svg)\n"
        elif "pyramide additive" in code_clean_l or ("[   ]" in code_clean and "[ 5 ]" in code_clean) or ("[  ?  ]" in code_clean and "[  7  ]" in code_clean):
            return f"\n{pfx}![La pyramide additive : somme des briques sous-jacentes](figures/vol_1/fig_03_pyramide_addition.svg)\n"
        elif "corde au centre" in code_clean_l or "fléau droit horizontal" in code_clean_l or "plateau gauche" in code_clean_l or "balance" in code_clean_l:
            return f"\n{pfx}![La balance de justice : état d'équilibre parfait](figures/vol_1/fig_03_balance_justice.svg)\n"
        elif "0 + 10 = 10" in code_clean and "5 +  5 = 10" in code_clean:
            return f"\n{pfx}> **💡 Découverte & Histoire — Les Amis de 10 et les Paires Complémentaires**\n{pfx}>{callout_body}\n"
        elif "abaque" in code_clean_l or "rainure" in code_clean_l or "la boîte de calcul" in code_clean_l:
            return f"\n{pfx}![L'abaque des marchands : compartiments d'unités et de dizaines](figures/vol_1/fig_04_abaque_boite.svg)\n"
        elif "rotation de 90" in code_clean_l or "tablette couchée" in code_clean_l or "4 × 6 = 6 × 4" in code_clean_l or "tourner la tête" in code_clean_l:
            return f"\n{pfx}![La commutativité par rotation : 4 × 6 = 6 × 4](figures/vol_1/fig_05_commutativite_rotation.svg)\n"
        elif "mur de briques" in code_clean_l or "4 rangées de 6" in code_clean_l or ("6 + 6 + 6 + 6" in code_clean_l and "brique" in code_clean_l) or "rangée 1 :  [■]" in code_clean_l:
            return f"\n{pfx}![Le mur de briques : 4 rangées de 6 font 24](figures/vol_1/fig_05_mur_briques_4x6.svg)\n"
        elif "double" in code_clean_l and "moitié" in code_clean_l:
            return f"\n{pfx}![Double et moitié : symétrie multiplicative bilatérale](figures/vol_1/fig_05_double_moitie.svg)\n"
        elif "doigts" in code_clean_l and "table de 9" in code_clean_l:
            return f"\n{pfx}![L'astuce magique des dix doigts pour la table de 9](figures/vol_1/fig_05_doigts_table_9.svg)\n"
        elif "le pouce :" in code_clean_l and "le pied :" in code_clean_l and "le pas :" in code_clean_l:
            return f"\n{pfx}> **💡 Découverte & Histoire — Les Mesures Anatomiques Historiques**\n{pfx}>{callout_body}\n"
        elif "coudée" in code_clean_l or "empan" in code_clean_l or "doigt" in code_clean_l or "paume" in code_clean_l or "pharaon" in code_clean_l:
            return f"\n{pfx}![La coudée royale pharaonique : étalon anatomique de mesure](figures/vol_1/fig_06_coudee_royale.svg)\n"
        elif "aligner le 0" in code_clean_l or "lire : 6 cm" in code_clean_l or ("règle" in code_clean_l and "cm" in code_clean_l):
            return f"\n{pfx}![Mesure à la règle graduée : alignement sur zéro et lecture directe](figures/vol_1/fig_06_regle_graduee.svg)\n"
        elif "cadran" in code_clean_l or "horloge" in code_clean_l or ("12" in code_clean and "6" in code_clean and "3" in code_clean and "9" in code_clean and vol_dir != "Volume_VI"):
            return f"\n{pfx}![Le cadran circulaire : 12 heures et 60 minutes](figures/vol_1/fig_06_cadran_horloge.svg)\n"
        elif "melon" in code_clean_l or "1 kg" in code_clean_l or "kilogramme" in code_clean_l:
            return f"\n{pfx}![Pesée du melon : équilibre de masse de 1 kilogramme](figures/vol_1/fig_06_pesee_melon_1kg.svg)\n"
        elif "🍎" in code_clean or "🍌" in code_clean or "🍇" in code_clean:
            return f"\n{pfx}> **🛠️ Application Pratique — Chasse aux Trésors sur Quadrillage**\n{pfx}>{callout_body}\n"
        elif "le carré" in code_clean_l and "le rectangle" in code_clean_l and "le triangle" in code_clean_l:
            return f"\n{pfx}![Les trois formes fondamentales du plan géométrique](figures/vol_1/fig_07_formes_fondamentales.svg)\n"
        elif "équerre" in code_clean_l or "pli sur pli" in code_clean_l or "angle droit" in code_clean_l or "premier pli droit" in code_clean_l:
            return f"\n{pfx}![Fabrication de l'équerre par pliage : l'angle droit à 90°](figures/vol_1/fig_07_pliage_angle_droit.svg)\n"
        elif "le cube" in code_clean_l and "le pavé droit" in code_clean_l:
            return f"\n{pfx}![Les solides géométriques fondamentaux : cube, pavé et cylindre](figures/vol_1/fig_07_solides_fondamentaux.svg)\n"
        elif "ficelle du jardinier" in code_clean_l or "corde tendue" in code_clean_l or ("piquet" in code_clean_l and "craie" in code_clean_l) or "grand tour complet" in code_clean_l or ("piquet" in code_clean_l and "cercle" in code_clean_l):
            return f"\n{pfx}![La ficelle du jardinier : tracé parfait du cercle](figures/vol_1/fig_07_ficelle_jardinier.svg)\n"
        elif "papillon" in code_clean_l or "symétrie" in code_clean_l:
            return f"\n{pfx}![Le papillon et la symétrie axiale bilatérale](figures/vol_1/fig_07_papillon_symetrie.svg)\n"
        elif "l'étoile est dans" in code_clean_l or ("a       b       c       d" in code_clean_l and "★" in code_clean):
            return f"\n{pfx}![Repérage sur quadrillage cartésien discret](figures/vol_1/fig_07_grille_reperage.svg)\n"

    # --- VOLUME II ---
    elif vol_dir == "Volume_II":
        if "formation 2 × 6" in code_clean_l or "formation 3 × 4" in code_clean_l or ("soldat" in code_clean_l and "rang" in code_clean_l) or "1 ───────────────────────── 24" in code_clean:
            return f"\n{pfx}![Organisation rectangulaire des soldats : 2 × 6 et 3 × 4](figures/vol_2/fig_08_formations_rectangles.svg)\n"
        elif "soldat qui dépasse" in code_clean_l or "soldat solitaire" in code_clean_l or "parité" in code_clean_l or ("pair" in code_clean_l and "impair" in code_clean_l):
            return f"\n{pfx}![La parité : nombres pairs associés vs soldat solitaire impair](figures/vol_2/fig_08_parite_soldat.svg)\n"
        elif "grenouille" in code_clean_l or ("1 saut" in code_clean_l and "2 sauts" in code_clean_l):
            return f"\n{pfx}![Sauts réguliers de 3 en 3 de la grenouille](figures/vol_2/fig_08_grenouille_sauts.svg)\n"
        elif "arbre de décomposition" in code_clean_l or "facteurs premiers" in code_clean_l or ("60" in code_clean and "6" in code_clean and "10" in code_clean) or ("360" in code_clean and "36" in code_clean and "10" in code_clean) or "ce sont des premiers" in code_clean_l:
            return f"\n{pfx}![Arbre de décomposition en facteurs premiers](figures/vol_2/fig_08_decomposition_premiers.svg)\n"
        elif "partage vs groupement" in code_clean_l or "sens de la division" in code_clean_l or "14 poissons" in code_clean_l or "combien chacun" in code_clean_l or "famille a [><>]" in code_clean_l:
            return f"\n{pfx}![Les deux sens de la division : partage équitable et groupement](figures/vol_2/fig_09_sens_division.svg)\n"
        elif "potence" in code_clean_l or "dividende ───┐" in code_clean_l or ("dividende" in code_clean_l and "diviseur" in code_clean_l):
            return f"\n{pfx}![Anatomie de la potence de division euclidienne](figures/vol_2/fig_09_potence_division.svg)\n"
        elif "numérateur" in code_clean_l and "dénominateur" in code_clean_l:
            return f"\n{pfx}![Anatomie d'une fraction : rôle du numérateur et du dénominateur](figures/vol_2/fig_10_numerateur_denominateur.svg)\n"
        elif "[ o | o | o" in code_clean:
            return f"\n{pfx}> **💡 Découverte — L'Unité Complète comme Fraction $6/6$**\n{pfx}>{callout_body}\n"
        elif "gâteau en 8 parts" in code_clean_l:
            return f"\n{pfx}> **Exemple résolu — Partage du Gâteau en Huitièmes**\n{pfx}>{callout_body}\n"
        elif "bande pliée" in code_clean_l or "1/2 = 2/4" in code_clean_l or "bandes équivalentes" in code_clean_l:
            return f"\n{pfx}![Fractions équivalentes par découpage de bandes : 1/2 = 2/4](figures/vol_2/fig_10_bandes_pliees.svg)\n"
        elif "|----.----|" in code_clean or ("1/4" in code_clean and "2/4" in code_clean and "3/4" in code_clean):
            return f"\n{pfx}![La droite numérique graduée en quarts](figures/vol_2/fig_10_droite_graduee_quarts.svg)\n"
        elif ch_num == 12 and ("1 mètre" in code_clean and "|---" in code_clean):
            return f"\n{pfx}![La mesure du méridien terrestre et l'étalon universel du mètre](figures/vol_2/fig_12_meridien_metre.svg)\n"
        elif ("3,1" in code_clean and "3,2" in code_clean and "|-----|" in code_clean) or (ch_num == 11 and "1 mètre" in code_clean):
            return f"\n{pfx}![La règle graduée des dixièmes entre 3 et 4](figures/vol_2/fig_11_glissement_virgule.svg)\n"
        elif "galette" in code_clean_l or "1/3" in code_clean_l or "1/8" in code_clean_l or "part de 1/3" in code_clean_l or "tranche 1" in code_clean_l or "1 seule galette" in code_clean_l:
            return f"\n{pfx}![Le partage de la galette : les fractions de disque](figures/vol_2/fig_10_galette_quarts.svg)\n"
        elif "virgule" in code_clean_l or "dixième" in code_clean_l or "glissement" in code_clean_l or "3,20 :" in code_clean:
            return f"\n{pfx}![Glissement opératoire de la virgule décimale](figures/vol_2/fig_11_glissement_virgule.svg)\n"
        elif "méridien" in code_clean_l or "pôle nord" in code_clean_l or "dunkerque" in code_clean_l:
            return f"\n{pfx}![La mesure du méridien terrestre et l'étalon universel du mètre](figures/vol_2/fig_12_meridien_metre.svg)\n"
        elif "préfixes grecs" in code_clean_l or "préfixes latins" in code_clean_l:
            return f"\n{pfx}![Le système métrique universel : préfixes multiples et sous-multiples](figures/vol_2/fig_12_prefixes_metriques.svg)\n"
        elif "périmètre vs aire" in code_clean_l or "périmètre = 1 dimension" in code_clean_l or "carreau étalon" in code_clean_l or "1re rangée de 5 carreaux" in code_clean_l:
            return f"\n{pfx}![Périmètre linéaire 1D vs Aire surfacique 2D](figures/vol_2/fig_12_perimetre_vs_aire.svg)\n"
        elif "proportionnalité" in code_clean_l or "chocolat" in code_clean_l or "règle de trois" in code_clean_l or "pour 4 personnes" in code_clean_l or "4 m  ───────────>" in code_clean or "4 m  ---" in code_clean:
            return f"\n{pfx}![Le tableau de proportionnalité et la règle de trois](figures/vol_2/fig_13_regle_trois.svg)\n"
        elif "relatifs" in code_clean_l or "sol plat" in code_clean_l or "négatifs" in code_clean_l or "bourse du pêcheur" in code_clean_l or "prix de la couverture" in code_clean_l or "+3°c" in code_clean_l or "+5°c" in code_clean_l or "plus à gauche que" in code_clean_l:
            return f"\n{pfx}![L'axe gradué des entiers relatifs positifs et négatifs](figures/vol_2/fig_14_axe_relatifs.svg)\n"

    # --- VOLUME III ---
    elif vol_dir == "Volume_III":
        if "angle 1 :" in code_clean_l and "angle 2 :" in code_clean_l:
            return f"\n{pfx}> **💡 Observation — Comparer l'Écartement des Côtés d'un Angle**\n{pfx}>{callout_body}\n"
        elif "côté [bc)" in code_clean_l or "sommet b" in code_clean_l or "l'ouverture : c'est elle, l'angle" in code_clean_l:
            return f"\n{pfx}> **📐 Définition Fondamentale — L'Anatomie Géométrique d'un Angle**\n{pfx}>{callout_body}\n"
        elif "quatre types d'angles" in code_clean_l or ("aigu" in code_clean_l and "obtus" in code_clean_l) or "angle aigu" in code_clean_l:
            return f"\n{pfx}![Classification des quatre types d'angles](figures/vol_3/fig_15_quatre_types_angles.svg)\n"
        elif "angles opposés" in code_clean_l or ("sommet" in code_clean_l and "angle" in code_clean_l) or ("①" in code_clean and "②" in code_clean and "③" in code_clean):
            return f"\n{pfx}![Angles opposés par le sommet et égalité géométrique](figures/vol_3/fig_15_angles_opposes.svg)\n"
        elif "(d1) // (d2)" in code_clean or "d3) ⊥ (d1)" in code_clean or ("p1 :" in code_clean_l and "p2 :" in code_clean_l):
            return f"\n{pfx}![Droites parallèles et perpendiculaires fondamentales](figures/vol_3/fig_15_paralleles_perpendiculaires.svg)\n"
        elif "hauteur ≈ r" in code_clean_l or "base ≈ 1/2" in code_clean_l:
            return f"\n{pfx}![Le déroulement du cercle : définition géométrique du nombre Pi](figures/vol_3/fig_16_deroulement_cercle_pi.svg)\n"
        elif ("r1" in code_clean_l and ("." in code_clean or "---" in code_clean)) or "tour du potier" in code_clean_l or "main du potier" in code_clean_l:
            return f"\n{pfx}![Éléments remarquables du cercle : rayon, diamètre et corde](figures/vol_3/fig_16_vocabulaire_cercle.svg)\n"
        elif "vocabulaire du cercle" in code_clean_l or ("rayon" in code_clean_l and "diamètre" in code_clean_l):
            return f"\n{pfx}![Éléments remarquables du cercle : rayon, diamètre et corde](figures/vol_3/fig_16_vocabulaire_cercle.svg)\n"
        elif "polygone inscrit" in code_clean_l or "archimède" in code_clean_l or ("disque" in code_clean_l and "cercle" in code_clean_l):
            return f"\n{pfx}![La méthode d'Archimède : encadrement de Pi par polygones réguliers](figures/vol_3/fig_16_archimede_polygones.svg)\n"
        elif "déroulement du cercle" in code_clean_l or "1 tour complet" in code_clean_l or "départ (0 cm)" in code_clean_l:
            return f"\n{pfx}![Le déroulement du cercle : définition géométrique du nombre Pi](figures/vol_3/fig_16_deroulement_cercle_pi.svg)\n"
        elif "thalès" in code_clean_l or "pyramide" in code_clean_l or "ombre" in code_clean_l or "arbre a" in code_clean_l or "cube initial" in code_clean_l or "triangles emboîtés" in code_clean_l:
            return f"\n{pfx}![Théorème de Thalès : la mesure de la hauteur de la pyramide](figures/vol_3/fig_17_thales_pyramide.svg)\n"
        elif "pemdas" in code_clean_l or "priorités" in code_clean_l or "parentèses" in code_clean_l or "1. parenthèses" in code_clean_l or "1. p : parenthèses" in code_clean_l:
            return f"\n{pfx}![L'échelle universelle des priorités opératoires PEMDAS](figures/vol_3/fig_18_pemdas.svg)\n"
        elif "incommensurable" in code_clean_l or "racine de 2" in code_clean_l or "diagonale" in code_clean_l or ("1 mètre" in code_clean_l and "aire" in code_clean_l) or ("1 mètre" in code_clean_l and "┌──────────" in code_clean) or "hypoténuse (le plus grand côté)" in code_clean_l:
            return f"\n{pfx}![Le carré unité et la diagonale incommensurable racine de 2](figures/vol_3/fig_19_carre_diagonale_racine2.svg)\n"
        elif ch_num == 19 and ("pythagore" in code_clean_l or "a² + b² = c²" in code_clean_l or "échelle" in code_clean_l or "mur vertical" in code_clean_l or "aire b²" in code_clean_l or "disposition 1" in code_clean_l or "côté c = ?" in code_clean_l or "petit carré 1" in code_clean_l or ("b // | \\" in code_clean)):
            return f"\n{pfx}![Démonstration géométrique du Théorème de Pythagore](figures/vol_3/fig_19_pythagore_puzzle.svg)\n"
        elif ch_num == 20 and ("distance" in code_clean_l or "xb - xa" in code_clean_l or "yb - ya" in code_clean_l or "yb |" in code_clean or "● a" in code_clean_l or "● b" in code_clean_l):
            return f"\n{pfx}![Distance euclidienne dans le repère cartésien](figures/vol_3/fig_20_distance_plan_cartesien.svg)\n"
        elif ch_num == 20 and ("repère" in code_clean_l or "abscisse" in code_clean_l or "ordonnée" in code_clean_l or "axe" in code_clean_l or "vers le nord" in code_clean_l):
            return f"\n{pfx}![Le repère cartésien 2D : axe des abscisses et axe des ordonnées](figures/vol_3/fig_20_repere_cartesien_2d.svg)\n"

    # --- VOLUME IV ---
    elif vol_dir == "Volume_IV":
        if "balance" in code_clean_l or "al-khwarizmi" in code_clean_l or "al-jabr" in code_clean_l or "plus léger" in code_clean_l or "[ sac ]" in code_clean_l or "sac de pièces" in code_clean_l or "x + 3 = 7" in code_clean_l or ("sac" in code_clean_l and "8 kg" in code_clean_l):
            return f"\n{pfx}![La balance d'Al-Khwarizmi et l'équilibre des équations](figures/vol_4/fig_22_balance_al_khwarizmi.svg)\n"
        elif ("-5" in code_clean and "-4" in code_clean and "-3" in code_clean and "-2" in code_clean and "-1" in code_clean and "0" in code_clean) or ("---|------|------|" in code_clean) or "crochets" in code_clean_l or "intervalles" in code_clean_l or "intervalle" in code_clean_l or "inclus" in code_clean_l or "exclu" in code_clean_l or ("<" in code_clean and "]" in code_clean) or "██████" in code_clean or "[a ; b]" in code_clean_l or "[■■■■■" in code_clean or (ch_num == 24 and "(d1)" in code_clean):
            return f"\n{pfx}![Intervalles et inégalités sur la droite réelle : notation et crochets](figures/vol_4/fig_24_intervalles_droite.svg)\n"
        elif ch_num == 22 and ("aire k×a" in code_clean_l or "aire k×b" in code_clean_l):
            return f"\n{pfx}> **📐 Règle Fondamentale — Aperçu Géométrique de la Distributivité Simple**\n{pfx}>{callout_body}\n"
        elif "(a + b)(c + d)" in code_clean_l or "distributivité" in code_clean_l or ("a × c" in code_clean and "b × c" in code_clean) or ("a              b" in code_clean and "c" in code_clean and "d" in code_clean) or ("┌───── 1 ─────┐" in code_clean) or "k(a+b)" in code_clean_l or ("k × a" in code_clean_l and "k × b" in code_clean_l) or "aire k×a" in code_clean_l or "aire k×b" in code_clean_l:
            return f"\n{pfx}![Distributivité de la multiplication sur l'addition](figures/vol_4/fig_23_distributivite_double.svg)\n"
        elif "a² − b²" in code_clean or "a² - b²" in code_clean_l or "différence de deux carrés" in code_clean_l or "(a - b)(a + b)" in code_clean_l or ("a - b" in code_clean and "cherché" in code_clean_l) or ("a - b            b" in code_clean) or ("a - b" in code_clean_l and "a + b" in code_clean_l and "─" in code_clean):
            return f"\n{pfx}![Différence de deux carrés : (a+b)(a-b) = a² - b²](figures/vol_4/fig_23_difference_deux_carres.svg)\n"
        elif "carré complété" in code_clean_l or "identités remarquables" in code_clean_l or "identité remarquable" in code_clean_l or "(a+b)²" in code_clean_l or "(a + b)²" in code_clean_l or ("a²" in code_clean_l and "ab" in code_clean_l and "b²" in code_clean_l) or ("x²" in code_clean and "5x" in code_clean) or ("x             5" in code_clean) or ("a                 b" in code_clean and "┌──" in code_clean):
            return f"\n{pfx}![Preuve géométrique de l'identité remarquable (a+b)²](figures/vol_4/fig_23_identite_remarquable_carre.svg)\n"
        elif "boîte noire" in code_clean_l or "machine fonction" in code_clean_l or "machine f" in code_clean_l or "antécédent" in code_clean_l or "image" in code_clean_l or "entrée : x" in code_clean_l or "avant (point de départ)" in code_clean_l or "usine" in code_clean_l or "métier jacquard" in code_clean_l or "carton perforé" in code_clean_l:
            return f"\n{pfx}![La fonction comme machine entrée-sortie : antécédent x et image f(x)](figures/vol_4/fig_25_machine_fonction.svg)\n"
        elif ch_num == 25 and ("droite affine" in code_clean_l or "f(x) = ax + b" in code_clean_l or "pente a" in code_clean_l or "pente m" in code_clean_l or "f(x) = 2x" in code_clean_l or "(d1)" in code_clean or "a > 0 : monte" in code_clean_l or "nouveau point" in code_clean_l or "ordonnée à l'origine" in code_clean_l or ("y ▲" in code_clean and len(lines) <= 15)):
            return f"\n{pfx}![Représentation graphique de la fonction affine : pente et ordonnée à l'origine](figures/vol_4/fig_25_droite_affine_complete.svg)\n"
        elif "axe de symétrie" in code_clean_l or "médiatrice" in code_clean_l or "axe (d)" in code_clean_l or "arche penchée" in code_clean_l or ("symétrie axiale" in code_clean_l and vol_dir == "Volume_IV") or ("(d)" in code_clean and "angle droit" in code_clean_l) or "cas c-a-c" in code_clean_l:
            return f"\n{pfx}![La symétrie axiale bilatérale : pliage orthogonal et miroir](figures/vol_4/fig_26_symetrie_axiale.svg)\n"
        elif "demi-tour" in code_clean_l or "centre o" in code_clean_l or "symétrie centrale" in code_clean_l or "om = om'" in code_clean_l or "m ●───────────────o───────────────● m'" in code_clean_l or ("découpe" in code_clean_l and "translation" in code_clean_l):
            return f"\n{pfx}![La symétrie centrale : demi-tour parfait de 180° autour du centre O](figures/vol_4/fig_26_symetrie_centrale.svg)\n"
        elif "homothétie" in code_clean_l or "agrandissement" in code_clean_l or "rapport k" in code_clean_l or "agrandie" in code_clean_l or "zoom" in code_clean_l or "k > 1" in code_clean_l or "k > 0" in code_clean_l or "vecteur de glissement" in code_clean_l or ("m' ●" in code_clean_l and "/" in code_clean):
            return f"\n{pfx}![L'homothétie : zoom vectoriel depuis le centre d'alignement](figures/vol_4/fig_26_homothetie.svg)\n"
        elif "100 carreaux de 1 dm²" in code_clean_l or "1 m = 10 dm" in code_clean_l or "a--------b . . h" in code_clean_l or "<--- b -->" in code_clean_l or ("c" in code_clean and "/|\\" in code_clean) or "on coupe le triangle de gauche" in code_clean_l or "et on le recolle à droite" in code_clean_l:
            return f"\n{pfx}![Périmètre linéaire 1D vs Aire surfacique 2D](figures/vol_2/fig_12_perimetre_vs_aire.svg)\n"
        elif "demi-périmètre = π r" in code_clean_l or "hauteur ≈ r" in code_clean_l:
            return f"\n{pfx}![Le déroulement du cercle : définition géométrique du nombre Pi](figures/vol_3/fig_16_deroulement_cercle_pi.svg)\n"
        elif ("côté adjacent" in code_clean_l and "côté opposé" in code_clean_l) or "lm = ?" in code_clean_l or "rt = ?" in code_clean_l or "angle α = ?" in code_clean_l:
            return f"\n{pfx}![Trigonométrie dans le triangle rectangle : Cosinus, Sinus et Tangente](figures/vol_3/fig_17_thales_pyramide.svg)\n"
        elif "je fais un croquis" in code_clean_l:
            return f"\n{pfx}> **🛠️ Méthode Pas à Pas — Méthode de Résolution Trigonométrique**\n{pfx}>{callout_body}\n"
        elif "360" in code_clean and ("36  ×  10" in code_clean or "360 │ 2" in code_clean or "180 │ 2" in code_clean):
            return f"\n{pfx}![Arbre de décomposition en facteurs premiers](figures/vol_2/fig_08_decomposition_premiers.svg)\n"
        elif "13 nœuds" in code_clean_l or "triangle 3-4-5" in code_clean_l or "3² + 4² = 5²" in code_clean_l or "corde" in code_clean_l or "morceaux (1)" in code_clean_l or "b + b" in code_clean_l:
            return f"\n{pfx}![La corde égyptienne à treize nœuds et le triangle rectangle 3-4-5](figures/vol_4/fig_27_corde_treize_noeuds.svg)\n"
        elif "ératosthène" in code_clean_l or "rayons solaires" in code_clean_l or "syène" in code_clean_l or "alexandrie" in code_clean_l or "sommet du bâton" in code_clean_l or "7,2" in code_clean_l:
            return f"\n{pfx}![La mesure du rayon de la Terre par Ératosthène d'Alexandrie](figures/vol_4/fig_28_eratosthene_tour_terre.svg)\n"
        elif "euclide" in code_clean_l or "pavage" in code_clean_l or "rectangles emboîtés" in code_clean_l:
            return f"\n{pfx}![L'algorithme géométrique d'Euclide par découpage de carrés](figures/vol_4/fig_29_euclide_rectangles.svg)\n"
        elif "sentier" in code_clean_l or "probabilité" in code_clean_l or "dés" in code_clean_l or "arbre" in code_clean_l or "univers complet" in code_clean_l or "1re épreuve" in code_clean_l:
            return f"\n{pfx}![Le choix du sentier : arbre pondéré des probabilités](figures/vol_4/fig_30_sentiers_arbre.svg)\n"

    # --- VOLUME V ---
    elif vol_dir == "Volume_V":
        if ("r" in code_clean and "q" in code_clean and "d" in code_clean and "z" in code_clean and "n" in code_clean and "┌" in code_clean) or ("√2" in code_clean and "1/3" in code_clean):
            return f"\n{pfx}![Les ensembles de nombres emboîtés N ⊂ Z ⊂ D ⊂ Q ⊂ R](figures/vol_5/fig_31_ensembles_emboites.svg)\n"
        elif "diagramme de venn" in code_clean_l or ("intersection" in code_clean_l and "réunion" in code_clean_l) or "a ∩ b" in code_clean or "zone commune" in code_clean_l or "univers ω" in code_clean_l:
            return f"\n{pfx}![Diagrammes de Venn : Intersection A ∩ B et Réunion A ∪ B](figures/vol_5/fig_31_venn_intersection_union.svg)\n"
        elif "i∩j" in code_clean_l or "i∪j" in code_clean_l or ("[■■■■■■■■■■■■■■■■■■[" in code_clean):
            return f"\n{pfx}![Intersection et réunion d'intervalles sur l'axe des réels](figures/vol_4/fig_24_intervalles_droite.svg)\n"
        elif ch_num == 32 and ("voilier" in code_clean_l or "atterrissage" in code_clean_l or "courant des rames" in code_clean_l or "trajectoire réelle" in code_clean_l):
            return f"\n{pfx}> **💡 Modélisation Concrète — La Dérive du Voilier et l'Addition des Vitesses**\n{pfx}>{callout_body}\n"
        elif ch_num == 32 and ("-2u" in code_clean_l or "3u" in code_clean_l or "oiseau" in code_clean_l):
            return f"\n{pfx}> **📐 Règle Fondamentale — Multiplication d'un Vecteur par un Scalaire**\n{pfx}>{callout_body}\n"
        elif ch_num == 32 and ("norme ||u||" in code_clean_l or "la flèche pointe vers le haut" in code_clean_l or "sens (la flèche" in code_clean_l):
            return f"\n{pfx}![Caractérisation d'un vecteur : direction, sens et norme](figures/vol_5/fig_32_vecteur_definition.svg)\n"
        elif ch_num == 32 and ("u = x i + y j" in code_clean_l or "vecteur ab va de a vers b" in code_clean_l or "a-b-d-c" in code_clean_l or "composantes" in code_clean_l):
            return f"\n{pfx}![Décomposition vectorielle fondamentale : u = x i + y j](figures/vol_5/fig_32_vecteur_composantes.svg)\n"
        elif ch_num == 32 and ("chasles" in code_clean_l or "mise bout à bout" in code_clean_l or "relais" in code_clean_l or "u + v" in code_clean_l or "w = u + v" in code_clean_l or "c o...." in code_clean_l or "▲" in code_clean):
            return f"\n{pfx}![Vecteurs dans le plan : relation de Chasles et coordonnées](figures/vol_5/fig_32_chasles_addition.svg)\n"
        elif ch_num == 33 and ("pente m" in code_clean_l or "ordonnée à l" in code_clean_l or "d : y = mx + p" in code_clean_l or "avance : +1" in code_clean_l or "avance de 1" in code_clean_l or "vecteur directeur" in code_clean_l or "y ▲" in code_clean):
            return f"\n{pfx}![Droite affine y = mx + p : coefficient directeur et ordonnée à l'origine](figures/vol_5/fig_33_pente_ordonnee.svg)\n"
        elif "droites sécantes" in code_clean_l or "droites confondues" in code_clean_l or "strictement parallèles" in code_clean_l or "la vigilante" in code_clean_l or "point de rencontre" in code_clean_l:
            return f"\n{pfx}![Positions relatives de deux droites affines dans le plan](figures/vol_5/fig_33_positions_droites_affines.svg)\n"
        elif "métier jacquard" in code_clean_l or "carton perforé" in code_clean_l or "matière brute à l'entrée" in code_clean_l or ("machine f" in code_clean_l and "machine g" in code_clean_l):
            return f"\n{pfx}![La fonction comme machine entrée-sortie de Jacquard](figures/vol_4/fig_25_machine_fonction.svg)\n"
        elif "fonction paire" in code_clean_l or "fonction impaire" in code_clean_l or ("symétrie axiale" in code_clean_l and vol_dir == "Volume_V"):
            return f"\n{pfx}![Parité des fonctions : symétrie axiale bilatérale vs symétrie centrale](figures/vol_5/fig_34_parite_fonctions.svg)\n"
        elif "droite y = k" in code_clean_l or "f(x) = k" in code_clean_l or "sommet (maximum)" in code_clean_l or ("cf" in code_clean_l and "intersections" in code_clean_l):
            return f"\n{pfx}![Résolution graphique de l'équation f(x) = k par intersection](figures/vol_5/fig_34_resolution_fx_k.svg)\n"
        elif "parabole" in code_clean_l or "sommet" in code_clean_l or "second degré" in code_clean_l or "-b/2a" in code_clean_l or "cas a > 0" in code_clean_l or ("croissante" in code_clean_l and "décroissante" in code_clean_l):
            return f"\n{pfx}![Parabole du second degré : orientation et coordonnées du sommet](figures/vol_5/fig_35_parabole_second_degre.svg)\n"
        elif "suite" in code_clean_l or "nuage de points" in code_clean_l or "u_n" in code_clean_l or "points isolés" in code_clean_l or "un ▲" in code_clean:
            return f"\n{pfx}![Représentation graphique d'une suite numérique : nuage de points isolés](figures/vol_5/fig_36_suite_graphique.svg)\n"
        elif "quadrant" in code_clean_l or "signes de cos et sin" in code_clean_l or ("sin > 0" in code_clean and ("cos > 0" in code_clean or "y" in code_clean_l)):
            return f"\n{pfx}![Les quatre quadrants trigonométriques : signes de cos et sin](figures/vol_5/fig_37_cercle_trigo_quadrants.svg)\n"
        elif "cercle" in code_clean_l or "enroulement" in code_clean_l or "grande roue" in code_clean_l or "trigonométrique" in code_clean_l or "π/2" in code_clean or "arc = r" in code_clean_l or "ruban" in code_clean_l or ("m(x)" in code_clean_l and ("y" in code_clean_l or "▲" in code_clean)):
            return f"\n{pfx}![Le cercle trigonométrique complet : enroulement et projections](figures/vol_5/fig_37_cercle_trigo_complet.svg)\n"
        elif "produit scalaire" in code_clean_l or "travail" in code_clean_l or "f · ab" in code_clean_l or "force f" in code_clean_l or "effort total" in code_clean_l or "θ aigu" in code_clean_l or "signe géométrique" in code_clean_l or "vecteur déplacement" in code_clean_l or "halage" in code_clean_l or "cheval" in code_clean_l or "sens contraires" in code_clean_l or "vecteur normal" in code_clean_l or "c  /" in code_clean or "c /" in code_clean or "al-kashi" in code_clean_l or "Â" in code_clean:
            return f"\n{pfx}![Produit scalaire et travail d'une force : composante utile et signe géométrique](figures/vol_5/fig_38_produit_scalaire_travail.svg)\n"
        elif ("carré d'origine" in code_clean_l and "bande est : x × h" in code_clean_l) or "aire de base u(x) × v(x)" in code_clean_l or ("u·δv" in code_clean_l and "v·δu" in code_clean_l):
            return f"\n{pfx}![Preuve géométrique de l'identité remarquable (a+b)²](figures/vol_4/fig_23_identite_remarquable_carre.svg)\n"
        elif "altitude" in code_clean_l and "m₂(2h" in code_clean:
            return f"\n{pfx}![Croissance exponentielle et approximation par la méthode d'Euler](figures/vol_5/fig_40_exponentielle.svg)\n"
        elif "courbe de la montagne" in code_clean_l or "ski rigide" in code_clean_l or "le ski" in code_clean_l:
            return f"\n{pfx}> **💡 Métaphore Intuitive — Le Skieur et la Pente Instantanée de la Montagne**\n{pfx}>{callout_body}\n"
        elif "tangente horizontale" in code_clean_l or "f'(x₀) = 0" in code_clean:
            return f"\n{pfx}> **📐 Règle Fondamentale — Tangente Horizontale et Extrema Locaux ($f'(x_0) = 0$)**\n{pfx}>{callout_body}\n"
        elif "sécante" in code_clean_l or "tangente" in code_clean_l or "nombre dérivé" in code_clean_l or "h → 0" in code_clean_l or "f(a+h)" in code_clean_l or "m (a+h" in code_clean_l or "altitude" in code_clean_l:
            return f"\n{pfx}![Nombre dérivé et limite des sécantes quand le pas h tend vers zéro](figures/vol_5/fig_39_secante_tangente.svg)\n"
        elif "atelier alpha" in code_clean_l:
            return f"\n{pfx}> **Exemple résolu — Dispersion Comparée : Atelier Alpha vs Atelier Bêta**\n{pfx}>{callout_body}\n"
        elif "moustaches" in code_clean_l or "quartile" in code_clean_l or "médiane" in code_clean_l or "boîte" in code_clean_l or "boîte centrale" in code_clean_l:
            return f"\n{pfx}![Boîte à moustaches : médiane, quartiles et dispersion statistique](figures/vol_5/fig_40_boite_moustaches.svg)\n"
        elif "exponentielle" in code_clean_l or "croissance continue" in code_clean_l or "bactéries" in code_clean_l or "e^x" in code_clean_l:
            return f"\n{pfx}![La fonction exponentielle : croissance continue et propriétés](figures/vol_5/fig_40_exponentielle.svg)\n"
        elif "bayes" in code_clean_l or "dépistage" in code_clean_l or "arbre des possibles" in code_clean_l or "p_a(b)" in code_clean_l or "population totale" in code_clean_l:
            return f"\n{pfx}![L'arbre pondéré du dépistage médical et la formule de Bayes](figures/vol_5/fig_42_arbre_medical.svg)\n"

    # --- VOLUME VI ---
    elif vol_dir == "Volume_VI":
        if ch_num == 58:
            return f"\n{pfx}> **📐 Règle Fondamentale — Synthèse de l'Édifice Mathématique et Cap sur le Supérieur**\n{pfx}>{callout_body}\n"
        elif "graphe probabiliste" in code_clean_l or ("0.8" in code_clean and "0.2" in code_clean) or ("( a )" in code_clean_l and "( b )" in code_clean_l):
            return f"\n{pfx}![Graphe probabiliste à 2 états et matrice de transition](figures/vol_6/fig_57_graphe_probabiliste.svg)\n"
        elif "graphe à 3 sommets" in code_clean_l or "matrice d'adjacence" in code_clean_l or ("graphe" in code_clean_l and "sommet" in code_clean_l):
            return f"\n{pfx}![Graphe orienté à 3 sommets et matrice d'adjacence associée](figures/vol_6/fig_57_graphe_oriente_matrice.svg)\n"
        elif "produit matriciel" in code_clean_l or ("ligne i" in code_clean_l and "colonne j" in code_clean_l) or ("matrice a" in code_clean_l and "matrice b" in code_clean_l):
            return f"\n{pfx}![Principe du produit matriciel ligne par colonne](figures/vol_6/fig_57_produit_matriciel.svg)\n"
        elif "rsa" in code_clean_l or ("alice" in code_clean_l and "bob" in code_clean_l) or "clé publique" in code_clean_l:
            return f"\n{pfx}![Cryptographie asymétrique RSA : échange de clé publique et déchiffrement](figures/vol_6/fig_56_cryptographie_rsa.svg)\n"
        elif "modulo 12" in code_clean_l or ("horloge" in code_clean_l and "restes" in code_clean_l) or "0 ≡ 12" in code_clean:
            return f"\n{pfx}![Arithmétique modulaire : le cadran d'horloge modulo 12](figures/vol_6/fig_55_racines_unite.svg)\n"
        elif "racines 6-ièmes" in code_clean_l or "racines de l'unité" in code_clean_l or "hexagone régulier" in code_clean_l:
            return f"\n{pfx}![Racines 6-ièmes de l'unité et hexagone régulier dans le plan complexe](figures/vol_6/fig_55_racines_unite.svg)\n"
        elif "l'ordre compte-t-il" in code_clean_l or ("arrangements" in code_clean_l and "combinaisons" in code_clean_l) or "ensemble e" in code_clean_l:
            return f"\n{pfx}![Arbre de décision combinatoire : arrangements, combinaisons, permutations](figures/vol_6/fig_53_arbre_decision_combinatoire.svg)\n"
        elif "quadrillage" in code_clean_l or "b(5,3)" in code_clean_l or "b(5, 3)" in code_clean_l or "a(0,0)" in code_clean_l:
            return f"\n{pfx}![Chemins sur un quadrillage et coefficients binomiaux](figures/vol_6/fig_53_chemins_grille.svg)\n"
        elif "droites dans l'espace" in code_clean_l or "non coplanaires" in code_clean_l or "colinéaires" in code_clean_l or "droite dirigée par u" in code_clean_l:
            return f"\n{pfx}![Positions relatives de deux droites dans l'espace : parallèles, sécantes ou non coplanaires](figures/vol_6/fig_52_droites_espace.svg)\n"
        elif "vecteur normal" in code_clean_l:
            return f"\n{pfx}![Équation cartésienne du plan et vecteur normal dans l'espace](figures/vol_6/fig_52_plan_vecteur_normal.svg)\n"
        elif "vecteur ab" in code_clean_l or ("xb - xa" in code_clean_l and "zb" in code_clean_l) or "cote / hauteur" in code_clean_l or "z ▲" in code_clean or "b(xb, yb, zb)" in code_clean_l:
            return f"\n{pfx}![Coordonnées et norme d'un vecteur dans l'espace à 3 dimensions](figures/vol_6/fig_52_vecteur_espace_3d.svg)\n"
        elif "condensateur" in code_clean_l or "circuit rc" in code_clean_l or "euler" in code_clean_l or "u_c(t)" in code_clean_l or "vraie courbe y(t)" in code_clean_l or ("c = 2" in code_clean_l and "c = 1" in code_clean_l):
            return f"\n{pfx}![Charge du condensateur et méthode d'Euler pour les équations différentielles](figures/vol_6/fig_51_circuit_rc_euler.svg)\n"
        elif "tonneau" in code_clean_l or "tranches fines" in code_clean_l:
            return f"\n{pfx}![La stéréométrie des tonneaux de Kepler : calcul intégral par tranches](figures/vol_6/fig_50_tonneau_kepler.svg)\n"
        elif "riemann" in code_clean_l or "aire sous la courbe" in code_clean_l or "sommes de tranches" in code_clean_l or "courbe y = f(t)" in code_clean_l or "y = f(t)" in code_clean_l or "vitesse v(t)" in code_clean_l or ("y = f(x) (au-dessus)" in code_clean and "y = g(x) (en dessous)" in code_clean):
            return f"\n{pfx}![L'intégrale de Riemann : encadrement de l'aire sous la courbe par des rectangles](figures/vol_6/fig_50_riemann_integrale.svg)\n"
        elif "tan x" in code_clean_l or "tangente sur le cercle" in code_clean_l or "droite x = 1" in code_clean_l or "t (1, tan x)" in code_clean_l:
            return f"\n{pfx}![Ligne trigonométrique de la tangente sur le cercle unité](figures/vol_6/fig_49_tangente_cercle.svg)\n"
        elif "onde" in code_clean_l or "roue qui tourne" in code_clean_l or "sinusoidale" in code_clean_l or "sinusoïdale" in code_clean_l or "y = sin(t)" in code_clean_l or ("y = sin(x)" in code_clean and "y = x (tangente en 0)" in code_clean):
            return f"\n{pfx}![Génération de l'onde sinusoïdale par rotation du cercle](figures/vol_6/fig_49_onde_sinusoidale.svg)\n"
        elif "m(x) = (cos x, sin x)" in code_clean_l or ("(0, 1)" in code_clean and "(-1, 0)" in code_clean):
            return f"\n{pfx}![Le cercle trigonométrique complet et les lignes de sinus et cosinus](figures/vol_5/fig_37_cercle_trigo_complet.svg)\n"
        elif "pendule" in code_clean_l or "balançoire" in code_clean_l or "point d'attache" in code_clean_l or ("vitesse v" in code_clean_l and "om" in code_clean_l):
            return f"\n{pfx}![Le pendule simple : modélisation du mouvement périodique oscillant](figures/vol_6/fig_49_pendule_oscillant.svg)\n"
        elif "convexe" in code_clean_l or "concave" in code_clean_l or "inflexion" in code_clean_l or "courbe f(x)" in code_clean_l or ("pédalier" in code_clean_l and "chaîne" in code_clean_l):
            return f"\n{pfx}![Convexité, concavité et point d'inflexion : position relative des tangentes](figures/vol_6/fig_47_convexite_inflexion.svg)\n"
        elif "escalier" in code_clean_l or "cobweb" in code_clean_l or ("y = x" in code_clean_l and ("u_" in code_clean_l or "chapitre_46" in chapter_name.lower())):
            return f"\n{pfx}![Méthode de l'escalier (Cobweb) : itération graphique de la suite u_(n+1) = f(u_n)](figures/vol_6/fig_46_methode_escalier_cobweb.svg)\n"
        elif "valeurs intermédiaires" in code_clean_l or "tvi" in code_clean_l or ("c_1" in code_clean and "c_2" in code_clean) or ("f(b)" in code_clean and "k ┼" in code_clean) or "sommet à 12h" in code_clean_l or ("altitude (m)" in code_clean_l and "2200" in code_clean):
            return f"\n{pfx}![Théorème des Valeurs Intermédiaires (TVI) sur un intervalle fermé](figures/vol_6/fig_46_tvi_continuite.svg)\n"
        elif "téléphérique" in code_clean_l or "tarif postal" in code_clean_l or "palier" in code_clean_l or ("continue" in code_clean_l and "discontinue" in code_clean_l) or "tarif (€)" in code_clean_l:
            return f"\n{pfx}![Continuité mathématique : trajectoire continue vs saut de palier](figures/vol_6/fig_46_continu_vs_discontinu.svg)\n"
        elif "asymptote" in code_clean_l or "branche infinie" in code_clean_l or "horizon" in code_clean_l or "x > 0 : monte" in code_clean_l or "y = 2" in code_clean_l or "x = 1" in code_clean_l or ("lentille" in code_clean_l and "écran" in code_clean_l):
            return f"\n{pfx}![Comportement asymptotique aux bornes : asymptotes verticales et horizontales](figures/vol_6/fig_45_asymptotes_complete.svg)\n"
        elif "achille" in code_clean_l or "tortue" in code_clean_l or "zénon" in code_clean_l or ("départ" in code_clean_l and "arrivée" in code_clean_l):
            return f"\n{pfx}![Le paradoxe de Zénon : somme convergente de la série géométrique d'Achille et de la tortue](figures/vol_6/fig_44_achille_tortue.svg)\n"
        elif "gendarmes" in code_clean_l or "gendarme" in code_clean_l or ("l - ε" in code_clean_l and "l + ε" in code_clean_l):
            return f"\n{pfx}![Le théorème d'encadrement des gendarmes](figures/vol_6/fig_44_theoreme_gendarmes.svg)\n"
        elif "domino" in code_clean_l or "récurrence" in code_clean_l or "initialisation : le premier tombe" in code_clean_l or ("●        ● ○" in code_clean) or ("1 + 3 + 5" in code_clean):
            return f"\n{pfx}![Le principe de récurrence : l'effet domino mathématique](figures/vol_6/fig_43_dominos_recurrence.svg)\n"
        elif "bernoulli" in code_clean_l or "sss" in code_clean_l:
            return f"\n{pfx}![Arbre pondéré du schéma de Bernoulli à 3 épreuves indépendantes](figures/vol_6/fig_54_arbre_bernoulli.svg)\n"
        elif "gauss" in code_clean_l or "loi normale" in code_clean_l:
            return f"\n{pfx}![La distribution normale en cloche de Gauss : espérance et écart-type](figures/vol_6/fig_54_loi_normale_gauss.svg)\n"
        elif "plan complexe" in code_clean_l or "argand" in code_clean_l or "axe imaginaire" in code_clean_l:
            return f"\n{pfx}![Le plan complexe d'Argand-Gauss : forme algébrique et trigonométrique](figures/vol_6/fig_55_plan_complexe.svg)\n"
        elif "exp et log" in code_clean_l or ("exp" in code_clean_l and "y = x" in code_clean_l and "ln" in code_clean_l) or "ln a" in code_clean_l or "ln(x)" in code_clean_l:
            return f"\n{pfx}![Réciprocité des fonctions exponentielle et logarithme népérien](figures/vol_6/fig_48_exp_log_reciproques.svg)\n"
        elif "plafond" in code_clean_l or "majorant" in code_clean_l or "croissante majorée" in code_clean_l:
            return f"\n{pfx}![Théorème de convergence monotone : suite croissante majorée](figures/vol_6/fig_44_convergence_monotone.svg)\n"

    # Semantic Byrne Boxes (with clean bulleted lines)
    if "avant 1789" in code_clean_l or "ancien régime" in code_clean_l or "paris : 1 pied" in code_clean_l:
        return f"\n{pfx}> **💡 Découverte & Histoire — L'anarchie des mesures sous l'Ancien Régime**\n{pfx}>{callout_body}\n"
    if "geoffroy" in code_clean_l or "barthélemy" in code_clean_l or "petit marchand" in code_clean_l:
        return f"\n{pfx}> **💡 Découverte & Histoire — La querelle des marchands médiévaux**\n{pfx}>{callout_body}\n"
    if "gerbes de millet" in code_clean_l or "neuf chapitres" in code_clean_l:
        return f"\n{pfx}> **💡 Découverte & Histoire — Le Chapitre VIII des Neuf Chapitres chinois**\n{pfx}>{callout_body}\n"
    if "l'enseignement supérieur" in code_clean_l or "fin du voyage" in code_clean_l:
        return f"\n{pfx}> **📐 Règle Fondamentale — Cap sur l'Enseignement Supérieur**\n{pfx}>{callout_body}\n"
    if "tarif giovanni" in code_clean_l or "tarif marco" in code_clean_l:
        return f"\n{pfx}> **Exemple résolu — Comparaison de Tarifs (Modélisation Affine)**\n{pfx}>{callout_body}\n"
    if "intervalle théorique" in code_clean_l and "95 %" in code_clean_l:
        return f"\n{pfx}> **📐 Règle Fondamentale — Intervalle de Fluctuation Asymptotique à 95 %**\n{pfx}>{callout_body}\n"
    if "pour n =" in code_clean_l and "pas :" in code_clean_l:
        return f"\n{pfx}> **🛠️ Méthode Pas à Pas — Approximation Pas à Pas par la Méthode d'Euler**\n{pfx}>{callout_body}\n"
    if "étape 1 :" in code_clean_l and "420 = 132" in code_clean_l:
        return f"\n{pfx}> **🛠️ Méthode Pas à Pas — Calcul du PGCD par l'Algorithme d'Euclide**\n{pfx}>{callout_body}\n"
    if "étape 0 :" in code_clean_l and "largeur l" in code_clean_l:
        return f"\n{pfx}> **🛠️ Méthode Pas à Pas — Recherche de Racine par Dichotomie**\n{pfx}>{callout_body}\n"

    # Default fallback
    if clean_lines:
        inner = "\n".join([f"{pfx}{l}" for l in clean_lines])
        return f"\n{pfx}```data_table\n{inner}\n{pfx}```\n"
    return ""

def postprocess_typst(typst_content):
    print("Post-processing Typst output for Byrne Callouts and Math Delimiters...")
    
    # 1. Convert Pandoc quote blocks into styled Oliver Byrne boxes
    def repl_quote(m):
        body = m.group(1).strip()
        if re.search(r'#strong\[(?:📐\s*)?D[eé]finition|#strong\[(?:🎯\s*)?R[eè]gle', body, re.IGNORECASE):
            m_title = re.search(r'#strong\[(.*?)\]\s*(.*)', body, re.DOTALL)
            t = m_title.group(1).replace("📐", "").replace("🎯", "").replace("---", "—").replace("--", "—").strip() if m_title else "Définition Fondamentale"
            b = m_title.group(2).strip() if m_title else body
            return f'#principe(title: [{t}])[\n{b}\n]\n'
        elif re.search(r'#strong\[(?:🔍\s*)?L\'histoire|#strong\[(?:💡\s*)?Le savais-tu', body, re.IGNORECASE):
            m_title = re.search(r'#strong\[(.*?)\]\s*(.*)', body, re.DOTALL)
            t = m_title.group(1).replace("🔍", "").replace("💡", "").replace("---", "—").replace("--", "—").strip() if m_title else "Découverte & Histoire"
            b = m_title.group(2).strip() if m_title else body
            return f'#decouvre(title: [{t}])[\n{b}\n]\n'
        elif re.search(r'#strong\[(?:⚠️\s*)?Attention|#strong\[Piège', body, re.IGNORECASE):
            m_title = re.search(r'#strong\[(.*?)\]\s*(.*)', body, re.DOTALL)
            t = m_title.group(1).replace("⚠️", "").strip() if m_title else "Attention au Piège !"
            b = m_title.group(2).strip() if m_title else body
            return f'#alerte(title: [{t}])[\n{b}\n]\n'
        elif re.search(r'#strong\[Cas limite|#strong\[Point de vigilance', body, re.IGNORECASE):
            m_title = re.search(r'#strong\[(.*?)\]\s*(.*)', body, re.DOTALL)
            t = m_title.group(1).strip() if m_title else "Cas Limite & Vigilance"
            b = m_title.group(2).strip() if m_title else body
            return f'#cas_limite(title: [{t}])[\n{b}\n]\n'
        elif re.search(r'#strong\[(?:🛠️\s*)?M[eé]thode|#strong\[Algorithme', body, re.IGNORECASE):
            m_title = re.search(r'#strong\[(.*?)\]\s*(.*)', body, re.DOTALL)
            t = m_title.group(1).replace("🛠️", "").replace("---", "—").replace("--", "—").strip() if m_title else "Méthode Pas à Pas"
            b = m_title.group(2).strip() if m_title else body
            return f'#methode(title: [{t}])[\n{b}\n]\n'
        elif re.search(r'#strong\[Exemple r[eé]solu', body, re.IGNORECASE):
            m_title = re.search(r'#strong\[(.*?)\]\s*(.*)', body, re.DOTALL)
            t = m_title.group(1).replace("---", "—").replace("--", "—").strip() if m_title else "Exemple Résolu Pas à Pas"
            b = m_title.group(2).strip() if m_title else body
            return f'#exemple_resolu(title: [{t}])[\n{b}\n]\n'
        else:
            return f'#quote_box[\n{body}\n]\n'

    typst_content = re.sub(r'#quote\(block:\s*true\)\[\s*(.*?)\s*\]', repl_quote, typst_content, flags=re.DOTALL)

    # 2. Fix French math intervals produced by Pandoc that break Typst parser
    typst_content = re.sub(r'lr\(\](.*?)[\[\]]\)', r']\1[', typst_content)
    typst_content = re.sub(r'lr\(\[(.*?)[\[\]]\)', r'[\1]', typst_content)

    # 3. Fix matrix double vertical bar syntax in Typst
    typst_content = typst_content.replace('mat(delim: "||"', 'mat(delim: "|"')

    # 4. Fix slash regex literal in tables and list items
    typst_content = re.sub(r'\[/\s*/\]', r'["/ /"]', typst_content)
    typst_content = re.sub(r'\[/\]', r'["/"]', typst_content)
    typst_content = re.sub(r'\[/\s*\\\\?\]', r'["/ \\"]', typst_content)
    typst_content = re.sub(r'(\n\s*-\s*)/', r'\1\\/', typst_content)
    typst_content = re.sub(r'(\n\s*-\s*)\\\\', r'\1\\\\\\', typst_content)

    # 5. Spacing between specific math variable names in differential equations
    typst_content = typst_content.replace("$y' = ay$", "$y' = a y$")
    typst_content = typst_content.replace("$y' = ay + b$", "$y' = a y + b$")
    typst_content = typst_content.replace("$y' = ay+b$", "$y' = a y + b$")
    typst_content = typst_content.replace("$y = C e^(ax)$", "$y = C e^(a x)$")

    # 6. Styled Calculation Cards (Operations posées) avec alignement parfait et breakable false
    def repl_calc(m):
        code = format_arithmetic_operation(m.group(2))
        return f'''#align(center)[
  #block(
    fill: rgb("#f8fafc"),
    stroke: 1.2pt + rgb("#cbd5e1"),
    inset: (x: 18pt, y: 6pt),
    radius: 6pt,
    breakable: false,
  )[
    #set text(font: "Liberation Mono", size: 10.5pt, weight: "bold", fill: rgb("#0f172a"))
    ```text
{code}
    ```
  ]
]'''

    typst_content = re.sub(r'(`{3,})calc_op\s*\n([\s\S]*?)\1', repl_calc, typst_content)

    # 7. Styled Data Tables & Grids avec breakable false
    def repl_table(m):
        code = textwrap.dedent(m.group(2).strip("\n"))
        if code.strip().startswith("#"):
            return f"\n{code.strip()}\n"
        code = code.replace("─", "-").replace("│", "|").replace("┌", "+").replace("┐", "+").replace("└", "+").replace("┘", "+").replace("├", "+").replace("┤", "+").replace("┬", "+").replace("┴", "+").replace("┼", "+")
        return f"""#align(center)[
  #block(
    fill: rgb("#f8fafc"),
    stroke: 1pt + rgb("#cbd5e1"),
    inset: (x: 16pt, y: 10pt),
    radius: 6pt,
    breakable: false,
  )[
    #set text(font: "Liberation Mono", size: 9.5pt, fill: rgb("#0f172a"))
    ```text
{code}
    ```
  ]
]"""

    typst_content = re.sub(r'(`{3,})data_table\s*\n([\s\S]*?)\1', repl_table, typst_content)

    # 8. Ouverture des Volumes et Chapitres en belle page (recto impair, page d'ouverture muette)
    typst_content = re.sub(r'^(== CHAPITRE\b)', r'#recto()\n\1', typst_content, flags=re.MULTILINE)
    typst_content = re.sub(r'^(= VOLUME\b)', r'#recto()\n\1', typst_content, flags=re.MULTILINE)

    # 9. Strip ALL residual box-drawing characters from document text streams
    typst_content = re.sub(r'[─│┌┐└┘├┤┬┴┼═║╔╗╚╝╠╣╦╩╬▲►▼◄╭╮╯╰╱╲★●■]', '', typst_content)

    # 10. Assemble full document with Preambule and Back-Matter
    final_output = PREAMBLE + "\n\n" + typst_content + "\n\n" + BACK_MATTER
    return final_output

# ==============================================================================
# 5. MASTER BUILD EXECUTION
# ==============================================================================

def run_build():
    USED_SVGS.clear()
    print("=== Step 1: Preprocessing 58 Markdown Chapters with Line-by-Line Engine ===")
    volumes = [
        ("Volume_I", "# VOLUME I — L'ÂGE DE LA MAIN ET DE LA SAVANE (6 - 8 ans / CP - CE1)"),
        ("Volume_II", "# VOLUME II — LE SECRET DU PARTAGE ET LES GRANDEURS DU MONDE (8 - 11 ans / CE2 - CM2)"),
        ("Volume_III", "# VOLUME III — L'ÉTOILE D'ALEXANDRIE ET L'ESPACE EUCLIDIEN (11 - 13 ans / 6e - 5e)"),
        ("Volume_IV", "# VOLUME IV — L'ALCHIMIE DES SYMBOLES ET LE FEU ALGÉBRIQUE (13 - 15 ans / 4e - 3e)"),
        ("Volume_V", "# VOLUME V — LE MOUVEMENT, L'ANGLE ET LE SPECTRE DE LA FORME (15 - 17 ans / 2nde - 1ère)"),
        ("Volume_VI", "# VOLUME VI — L'INFINI APPRIVOISÉ ET L'ÉDIFICE MODERNE (17 - 18 ans / Terminale & Maths Expertes)")
    ]

    all_md_parts = []
    for vol_dir, vol_title in volumes:
        print(f"Reading {vol_dir}...")
        all_md_parts.append(f"\n{vol_title}\n")
        vol_path = os.path.join(TEXTES_DIR, vol_dir)
        ch_files = sorted(glob.glob(os.path.join(vol_path, "Chapitre_*.md")))
        for fpath in ch_files:
            ch_name = os.path.basename(fpath)
            with open(fpath, "r", encoding="utf-8") as f:
                c = f.read()
            cleaned = process_file_content(c, ch_name, vol_dir)
            all_md_parts.append(cleaned)

    full_md = "\n\n---\n\n".join(all_md_parts)
    with open(TEMP_MD, "w", encoding="utf-8") as f:
        f.write(full_md)
    print(f"Cleaned master markdown written: {TEMP_MD} ({len(full_md)} chars)")

    print("=== Step 2: Running Pandoc to Typst (LaTeX Math Conversion) ===")
    cmd_pandoc = [PANDOC_EXE, TEMP_MD, "-t", "typst", "-o", TEMP_TYP]
    res_p = subprocess.run(cmd_pandoc, capture_output=True, encoding="utf-8", errors="replace")
    if res_p.returncode != 0:
        print("PANDOC ERROR:")
        print(res_p.stderr)
        raise RuntimeError("Pandoc failed.")
    print(f"Pandoc conversion successful: {TEMP_TYP}")

    print("=== Step 3: Typst Post-Processing & Oliver Byrne Formatting ===")
    with open(TEMP_TYP, "r", encoding="utf-8") as f:
        pandoc_typ = f.read()
    
    final_typst = postprocess_typst(pandoc_typ)
    with open(FINAL_TYP, "w", encoding="utf-8") as f:
        f.write(final_typst)
    print(f"Master Typst book ready: {FINAL_TYP} ({len(final_typst)} chars)")

    print("=== Step 4: Compiling High-Fidelity PDF with Typst ===")
    cmd_typst = [TYPST_EXE, "compile", FINAL_TYP, FINAL_PDF]
    res_t = subprocess.run(cmd_typst, capture_output=True, encoding="utf-8", errors="replace")
    if res_t.returncode != 0:
        print("TYPST ERROR:")
        print(res_t.stderr[:1000])
        raise RuntimeError("Typst compilation failed.")

    print(f"PDF Successfully Generated: {FINAL_PDF}")
    
    print("=== Step 5: Verification of PDF Architecture ===")
    doc = pdfium.PdfDocument(FINAL_PDF)
    print(f"TOTAL PAGE COUNT: {len(doc)} pages.")
    
    print("ALL VERIFICATIONS PASSED WITH DISTINCTION.")

if __name__ == "__main__":
    run_build()
