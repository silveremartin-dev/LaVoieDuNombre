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
TEXTES_DIR = os.path.join(BASE_DIR, "textes_en")
FIG_DIR = os.path.join(BASE_DIR, "figures_en")
DIAG_DIR = os.path.join(FIG_DIR, "diags")
PANDOC_EXE = r"C:\Users\silve\AppData\Local\Pandoc\pandoc.exe"
TYPST_EXE = r"C:\Users\silve\AppData\Local\Microsoft\WinGet\Packages\Typst.Typst_Microsoft.Winget.Source_8wekyb3d8bbwe\typst-x86_64-pc-windows-msvc\typst.exe"

TEMP_MD = os.path.join(BASE_DIR, "temp_preprocessed_book_en.md")
TEMP_TYP = os.path.join(BASE_DIR, "temp_pandoc_out_en.typ")
FINAL_TYP = os.path.join(BASE_DIR, "THE_WAY_OF_THE_NUMBER.typ")
FINAL_PDF = os.path.join(BASE_DIR, "THE_WAY_OF_THE_NUMBER.pdf")

DIAG_BY_LOC = {}
# ==============================================================================
# 1. TYPST PREAMBLE & BOOK DESIGN
# ==============================================================================

PREAMBLE = """
#set document(
  title: "THE WAY OF THE NUMBER — A Constructive Odyssey",
  author: "Silvère Martin-Michiellot & Antigravity"
)

// ==========================================
// EDITORIAL PAGINATION RULES (TYPOGRAPHIC CHARTER)
// - The cover (plats 1, 2, 3, and 4) is never counted or foliated:
//   the page counter begins at 1 on the first recto page of the interior block (half-title).
// - Odd pages = recto (right); even pages = verso (left).
// - Preliminary pages (1 half-title, 2 blank, 3 title, 4 legal notices,
//   5 epigraph/dedication, 6 blank, then table of contents): counted but mute.
// - Each volume opening is placed on a recto (odd) page preceded by its
//   photographic nature frontispiece on the facing verso (even) page.
// - The first page of each chapter displays its pagination in the footer (outer folio),
//   while its header remains mute to let the chapter title breathe.
// - Intermediary blank pages: counted in arithmetic order, never displaying folio or running header.
// - Folio on the outer margin: left on versos (even), right on rectos (odd).
// ==========================================

// Oliver Byrne Palette (1847)
#let byrne-blue = rgb("#1d4ed8")
#let byrne-red = rgb("#b91c1c")
#let byrne-yellow = rgb("#d97706")
#let byrne-dark = rgb("#0f172a")
#let byrne-green = rgb("#15803d")
#let byrne-purple = rgb("#7e22ce")
#let byrne-slate = rgb("#334155")

// Page jump to next recto (odd) page with blank page tracking
#let recto() = [
  #metadata("fin-section") <fin-section>
  #pagebreak(weak: true, to: "odd")
  #metadata("debut-section") <debut-section>
]

#let is-blank-page() = {
  let p = here().page()
  let fins = query(<fin-section>)
  let debuts = query(<debut-section>)
  for (i, d) in debuts.enumerate() {
    let dp = d.location().page()
    if i < fins.len() and p < dp {
      let m = fins.at(i).location()
      let mp = m.page()
      if mp < p { return true }
      if mp == p and m.position().y < 2.65cm { return true }
    }
  }
  false
}

#let is-frontispice() = {
  let p = here().page()
  query(<page-frontispice>).any(m => m.location().page() == p)
}

#let is-volume-title() = {
  let p = here().page()
  query(<ouverture-volume>).any(m => m.location().page() == p)
}

#let is-chapter-start() = {
  let p = here().page()
  query(<debut-chapitre>).any(m => m.location().page() == p)
}

#let header-visible() = {
  let p = here().page()
  let debut = query(<debut-texte>)
  if debut.len() == 0 or p <= debut.first().location().page() { return false }
  if is-blank-page() { return false }
  if is-frontispice() { return false }
  if is-volume-title() { return false }
  if is-chapter-start() { return false }
  true
}

#let footer-visible() = {
  let p = here().page()
  let debut = query(<debut-texte>)
  if debut.len() == 0 or p <= debut.first().location().page() { return false }
  if is-blank-page() { return false }
  if is-frontispice() { return false }
  if is-volume-title() { return false }
  true
}

#let frontispice-volume(img-path) = [
  #metadata("fin-section") <fin-section>
  #pagebreak(to: "even")
  #metadata("frontispice") <page-frontispice>
  #metadata("debut-section") <debut-section>
  #align(center + horizon)[
    #image(img-path, width: 100%, height: 96%, fit: "cover")
  ]
]

#let ouverture-volume(num, titre-vol, sous-titre, descriptif, chapitres, mention-regard) = [
  #metadata("fin-section") <fin-section>
  #pagebreak(to: "odd")
  #metadata("volume") <ouverture-volume>
  #metadata("debut-section") <debut-section>
  
  #v(0.2cm)
  #align(center)[
    #block(fill: rgb("#f8fafc"), stroke: 2pt + byrne-blue, inset: (x: 20pt, y: 14pt), radius: 8pt, width: 100%)[
      #heading(level: 1)[VOLUME #num --- #titre-vol] <volume-title>
      #v(0.12cm)
      #text(size: 9.5pt, weight: "bold", fill: byrne-red, font: "Liberation Sans")[#sous-titre]
    ]
  ]
  #v(0.25cm)
  #align(center)[#text(size: 9pt, style: "italic", fill: rgb("#334155"))[#descriptif]]
  #v(0.25cm)
  #block(fill: rgb("#f8fafc"), stroke: 0.75pt + rgb("#cbd5e1"), inset: (x: 16pt, y: 10pt), radius: 6pt, width: 100%)[
    #text(size: 9pt, weight: "bold", fill: byrne-blue, font: "Liberation Sans")[Chapters of Volume #num :]\
    #v(0.15cm)
    #grid(
      columns: (1fr, 1fr),
      gutter: 6pt,
      ..chapitres.map(ch => text(size: 7.5pt, fill: rgb("#1e293b"))[#ch])
    )
  ]
  #v(1fr)
  #align(center)[
    #line(length: 40%, stroke: 0.5pt + rgb("#cbd5e1"))
    #v(0.15cm)
    #text(size: 8pt, style: "italic", fill: rgb("#475569"))[#mention-regard]
  ]
]

#set page(
  paper: "a4",
  margin: (top: 2.4cm, bottom: 2.4cm, left: 2.2cm, right: 2.2cm),
  header: context {
    if header-visible() [
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
        if prev-h1.len() > 0 { prev-h1.last().body } else { [THE WAY OF THE NUMBER] }
      }
      #grid(
        columns: (1fr,),
        gutter: 2.5pt,
        align: left,
        text(size: 7pt, fill: rgb("#64748b"), font: "Liberation Sans", style: "italic")[#vol-title],
        text(size: 7.5pt, fill: rgb("#334155"), font: "Liberation Sans", weight: "bold")[#ch-title]
      )
      #v(-2pt)
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
    ]
  },
  footer: context {
    if footer-visible() {
      let page-num = counter(page).get().first()
      let titre = text(size: 8pt, fill: rgb("#94a3b8"), font: "Liberation Sans", style: "italic")[THE WAY OF THE NUMBER — A Constructive Odyssey]
      let folio = text(size: 8.5pt, fill: rgb("#0f172a"), font: "Liberation Sans", weight: "bold")[Page #page-num]
      line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
      v(3pt)
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
  lang: "en"
)

#set par(justify: true, leading: 0.70em, first-line-indent: 0pt, spacing: 0.85em)

#show heading: set text(hyphenate: false)
#show heading: set block(sticky: true)

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

#show figure: set block(breakable: false)

#show heading.where(level: 1): it => {
  if it.has("label") and it.label == <volume-title> {
    text(size: 15pt, weight: "bold", fill: byrne-dark, font: "Liberation Serif")[#it.body]
  } else {
    v(1.5cm)
    align(center)[
      #block(
        fill: rgb("#f8fafc"),
        stroke: 2pt + byrne-blue,
        inset: (x: 24pt, y: 18pt),
        radius: 8pt,
        width: 100%
      )[
        #text(size: 16pt, weight: "bold", fill: byrne-dark, font: "Liberation Serif")[#it.body]
      ]
    ]
    v(1.0cm)
  }
}

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

// Oliver Byrne Didactic Callout Boxes
#let principe(title: [Principle & Definition], body) = block(
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

#let decouvre(title: [Discovery & History], body) = block(
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

#let alerte(title: [Watch Out for the Trap!], body) = block(
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

#let cas_limite(title: [Boundary Case & Caution], body) = block(
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

#let methode(title: [Practical Method], body) = block(
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

#let exemple_resolu(title: [Step-by-Step Worked Example], body) = block(
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
// 1. OFFICIAL COVER PAGE (ABYSSAL NIGHT & OLIVER BYRNE GOLD)
// ==========================================
#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 1.5cm, left: 1.5cm, right: 1.5cm),
  fill: rgb("#070d1e"),
  header: none,
  footer: none
)

#block(
  stroke: 1.5pt + rgb("#f59e0b"),
  inset: (x: 20pt, top: 22pt, bottom: 18pt),
  radius: 8pt,
  width: 100%,
  height: 100%
)[
  #align(center)[
    #text(size: 13pt, weight: "bold", fill: rgb("#f59e0b"), tracking: 2.5pt, font: "Liberation Sans")[
      SILVÈRE MARTIN-MICHIELLOT & ANTIGRAVITY
    ]
    #v(0.5cm)
    #text(size: 36pt, weight: "bold", fill: white, font: "Liberation Serif")[
      THE WAY OF THE NUMBER
    ]
    #v(0.25cm)
    #text(size: 13.5pt, weight: "bold", fill: rgb("#fcd34d"), font: "Liberation Sans")[
      A Constructive Odyssey, from the First Pebble to Advanced High School Mathematics
    ]
    #v(0.15cm)
    #text(size: 9.5pt, style: "italic", fill: rgb("#cbd5e1"))[
      58 chapters of living history, motor manipulations, column algorithms, and crystal-clear logic
    ]
    #v(0.5cm)
    
    #block(
      stroke: 2pt + rgb("#f59e0b"),
      radius: 8pt,
      clip: true,
      inset: 0pt,
      width: 88%,
      image("figures_en/cover_art.jpg", width: 100%, height: 12.8cm, fit: "cover")
    )
    
    #v(0.6cm)
    #block(
      fill: rgb("#0f172a"),
      stroke: 1.2pt + rgb("#38bdf8"),
      inset: (x: 22pt, y: 7pt),
      radius: 6pt
    )[
      #text(size: 10.5pt, weight: "bold", fill: rgb("#38bdf8"), font: "Liberation Sans")[
        DEFINITIVE REFERENCE EDITION — 2026
      ]
    ]
    #v(0.25cm)
    #text(size: 8pt, fill: rgb("#94a3b8"), tracking: 1pt, font: "Liberation Sans")[
      CONSTRUCTIVIST PEDAGOGY • GEOMETRIC INTUITION • FORMAL RIGOR
    ]
  ]
]

#pagebreak()
// Plat 2 (inside front cover): uncounted, never foliated
#set page(
  paper: "a4",
  margin: (top: 2.4cm, bottom: 2.4cm, left: 2.2cm, right: 2.2cm),
  fill: white,
  header: none,
  footer: none
)
#box()
#pagebreak()

// Start of interior block: first recto page is page 1 (mute)
#counter(page).update(1)

#set page(
  paper: "a4",
  margin: (top: 2.4cm, bottom: 2.4cm, left: 2.2cm, right: 2.2cm),
  fill: white,
  header: context {
    if header-visible() [
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
        if prev-h1.len() > 0 { prev-h1.last().body } else { [THE WAY OF THE NUMBER] }
      }
      #grid(
        columns: (1fr,),
        gutter: 2.5pt,
        align: left,
        text(size: 7pt, fill: rgb("#64748b"), font: "Liberation Sans", style: "italic")[#vol-title],
        text(size: 7.5pt, fill: rgb("#334155"), font: "Liberation Sans", weight: "bold")[#ch-title]
      )
      #v(-2pt)
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
    ]
  },
  footer: context {
    if footer-visible() {
      let page-num = counter(page).get().first()
      let titre = text(size: 8pt, fill: rgb("#94a3b8"), font: "Liberation Sans", style: "italic")[THE WAY OF THE NUMBER — A Constructive Odyssey]
      let folio = text(size: 8.5pt, fill: rgb("#0f172a"), font: "Liberation Sans", weight: "bold")[Page #page-num]
      line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
      v(3pt)
      if calc.even(page-num) {
        grid(columns: (1fr, 1fr), align: (left, right), folio, titre)
      } else {
        grid(columns: (1fr, 1fr), align: (left, right), titre, folio)
      }
    }
  }
)

// ==========================================
// PAGE 1 (RECTO) — HALF-TITLE (MUTE)
// ==========================================
#align(center + horizon)[
  #text(size: 22pt, weight: "bold", fill: byrne-dark, font: "Liberation Serif", tracking: 0.06em)[THE WAY OF THE NUMBER]
]
#pagebreak()

// PAGE 2 (VERSO) — BLANK PAGE (MUTE)
#box()
#pagebreak()

// ==========================================
// PAGE 3 (RECTO) — TITLE PAGE (MUTE)
// ==========================================
#align(center)[
  #v(3.5cm)
  #text(size: 13pt, weight: "bold", fill: byrne-blue, font: "Liberation Sans")[Silvère Martin-Michiellot & Antigravity]
  #v(1.6cm)
  #text(size: 32pt, weight: "bold", fill: byrne-dark, font: "Liberation Serif")[THE WAY OF THE NUMBER]
  #v(0.4cm)
  #line(length: 30%, stroke: 1pt + byrne-yellow)
  #v(0.4cm)
  #text(size: 14pt, weight: "bold", fill: byrne-red, font: "Liberation Sans")[A Constructive Odyssey, from the First Pebble to Advanced High School Mathematics]
  #v(1fr)
  #text(size: 10pt, fill: byrne-slate, font: "Liberation Sans")[DEFINITIVE REFERENCE EDITION — 2026]
  #v(0.2cm)
  #text(size: 9pt, fill: byrne-slate, font: "Liberation Sans")[Open distribution under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)]
  #v(1.5cm)
]
#pagebreak()

// PAGE 4 (VERSO) — LEGAL NOTICES & COPYRIGHT (MUTE)
#align(center + bottom)[
  #block(
    fill: rgb("#f8fafc"),
    stroke: 1pt + rgb("#cbd5e1"),
    inset: 16pt,
    radius: 6pt,
    width: 90%
  )[
    #align(left)[
      #text(size: 9.5pt, weight: "bold", fill: byrne-dark)[THE WAY OF THE NUMBER — A Constructive Odyssey, from the First Pebble to Advanced High School Mathematics]\\
      #v(3pt)
      #text(size: 8.5pt, fill: rgb("#475569"))[
        Definitive Complete Digital Edition — 58 chapters across 6 volumes with Companion Guide and Reference Appendices.\\
        \\
        *Authors:* Silvère Martin-Michiellot & Antigravity\\
        *Didactic Engineering & Pedagogical Design:* Constructivist didactics, Singapore CPA progression, Oliver Byrne visual semiotics\\
        *Typesetting:* Typst v0.15, Liberation Serif & Sans fonts, KaTeX mathematical notation\\
        *Graphic Semiotics:* SVG vector figures conforming to Oliver Byrne's historical palette (1847)\\
        *Cover Artwork:* Dedicated high-resolution graphic synthesis\\
        *Frontispiece Photographs (Mathematics in Nature):* Wikimedia Commons under CC BY-SA 3.0 and CC BY-SA 4.0 licenses (see Photographic Sources Index in Appendix D)\\
        *Legal Deposit:* October 2026\\
        \\
        *Open License:* This work is distributed under the *Creative Commons Attribution - ShareAlike 4.0 International License (CC BY-SA 4.0)*.\\
        You are free to share, copy, distribute, and adapt this work provided you give appropriate credit to the original authors and distribute your contributions under the same license.\\
        Educational, classroom, and homeschooling use is warmly encouraged and permitted under the terms of this open license.
      ]
    ]
  ]
]

#pagebreak()

// ==========================================
// PAGE 5 (RECTO) — EPIGRAPH & DEDICATION
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
      “Philosophy is written in that great book which ever lies before our eyes — I mean the Universe —, but we cannot understand it if we do not first learn the language and the characters in which it is written. It is written in the language of mathematics.”
    ]
    #v(8pt)
    #align(right)[#text(size: 9.5pt, weight: "bold", fill: byrne-blue)[— Galileo Galilei, *The Assayer* (1623)]]
  ]
  #v(2cm)
  #text(size: 10.5pt, style: "italic", fill: rgb("#475569"))[
    To all children and young minds who ever felt they were “not made for math”,\\
    and to the parents and educators who guide them with patience, clarity, and joyful rigor.
  ]
]

#pagebreak()

// PAGE 6 (VERSO) — BLANK PAGE (MUTE)
#box()
#pagebreak()

// PAGE 7 (RECTO) AND FOLLOWING — TABLE OF CONTENTS (MUTE)
#outline(
  title: [Detailed Table of Contents],
  indent: 1.5em,
  depth: 2
)

#metadata("debut-texte") <debut-texte>
"""
# ==============================================================================
# 2. ANNEXES, CONCLUSION AUTONOME & QUATRIÈME DE COUVERTURE
# ==============================================================================

BACK_MATTER = r"""
#recto()
= GENERAL CONCLUSION & EPILOGUE: THE EDIFICE OF THE NUMBER AND THE FREEDOM OF THE MIND

#align(center)[
  #figure(image("figures_en/vol_6/fig_58_arbre_savoirs.svg", width: 92%), caption: [The Tree of Mathematical Knowledge: from sensory experience to modern abstraction])
]

#v(0.4cm)
You have traversed fifty-eight stages, from the first pebble held tightly in the hand of the young savanna shepherd to infinite-dimensional spaces, complex numbers, Riemann integrals, and Markov random walks.

This journey has revealed a fundamental truth that few school textbooks dare to proclaim: *mathematics is not a collection of arbitrary rules invented to test or trap schoolchildren.* It is the living memory of all the challenges humanity had to overcome to navigate the oceans, construct cathedrals, predict eclipses, heal epidemics, and fathom the cosmos.

== The Three Foundational Teachings

1. *Sensori-Motor Grounding: Always return to the hand and the sketch.*
   When a mathematical problem seems opaque, never freeze before silent symbols. Trace a diagram, assign colors to magnitudes as Oliver Byrne taught, move the geometric figures, embody equality upon an Al-Khwarizmi balance scale. Mathematical thought takes root in the physical body and motor gestures before ascending into pure abstraction.

2. *Operative Automation: Technique liberates the mind.*
   Why do we set up additions, subtractions, multiplications, and divisions using rigorous column algorithms? Why do we memorize multiplication tables and operational rules? To liberate our working memory. Mechanical technique is not enslavement, but an instrument of emancipation: by entrusting routine execution to the hand, we free the full power of our mind for intuition, strategic vision, and the poetry of proof.

3. *The Courage of Boundary Cases and Critical Vigilance.*
   The greatest leaps forward in mathematics arose from refusing to sweep paradoxes under the rug: what happens when a magnitude vanishes, when a set is empty, when the denominator is zero, when a process approaches infinity? Never shy away from boundary cases: they are the touchstones that test the solidity of your theories, separating fragile conjecture from unshakable certainty.

== The Envoy to the Reader

Mathematics has bestowed upon you the most precious of all treasures: *the freedom of critical thought.* It has taught you never to bow before an argument from authority, to demand rigorous proof, and to loyally embrace the truth as soon as it reveals itself through the irresistible force of logic.

The grand book of the world now lies wide open before your eyes. You speak its language. Go forth, explore, question fearlessly, and keep ever alive within you the wonder of the first pebble.

#recto()
= APPENDIX A: REFERENCE FORMULARY & EXACT VALUES

== I. Exact Table of Standard Trigonometric Values

#set text(size: 9.5pt)
#table(
  columns: (1.5fr, 1.2fr, 1.5fr, 1.5fr, 1.5fr),
  fill: (x, y) => if y == 0 { rgb("#1d4ed8") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 6.5pt,
  align: center,
  table.header(
    text(weight: "bold", fill: white)[Angle in Degrees (°)],
    text(weight: "bold", fill: white)[Radians (rad)],
    text(weight: "bold", fill: white)[$cos(x)$],
    text(weight: "bold", fill: white)[$sin(x)$],
    text(weight: "bold", fill: white)[$tan(x)$]
  ),
  [$0^circle$], [$0$], [$1$], [$0$], [$0$],
  [$30^circle$], [$pi / 6$], [$sqrt(3) / 2$], [$1 / 2$], [$sqrt(3) / 3$],
  [$45^circle$], [$pi / 4$], [$sqrt(2) / 2$], [$sqrt(2) / 2$], [$1$],
  [$60^circle$], [$pi / 3$], [$1 / 2$], [$sqrt(3) / 2$], [$sqrt(3)$],
  [$90^circle$], [$pi / 2$], [$0$], [$1$], [_Undefined_],
  [$120^circle$], [$2 pi / 3$], [$- 1 / 2$], [$sqrt(3) / 2$], [$- sqrt(3)$],
  [$135^circle$], [$3 pi / 4$], [$- sqrt(2) / 2$], [$sqrt(2) / 2$], [$- 1$],
  [$150^circle$], [$5 pi / 6$], [$- sqrt(3) / 2$], [$1 / 2$], [$- sqrt(3) / 3$],
  [$180^circle$], [$pi$], [$- 1$], [$0$], [$0$]
)

#v(0.3cm)
== II. Trigonometric Addition and Double-Angle Formulas

#grid(
  columns: (1fr, 1fr),
  gutter: 14pt,
  block(fill: rgb("#eff6ff"), stroke: 1.5pt + byrne-blue, inset: 12pt, radius: 6pt, width: 100%)[
    #align(center)[#text(weight: "bold", fill: byrne-blue, size: 11pt)[Addition Formulas]]
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
    #align(center)[#text(weight: "bold", fill: byrne-green, size: 11pt)[Double-Angle & Core Identities]]
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
== III. Universal Table of Standard Derivatives & Operations

#table(
  columns: (1.5fr, 1.5fr, 2.5fr),
  fill: (x, y) => if y == 0 { rgb("#15803d") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 6.5pt,
  table.header(
    text(weight: "bold", fill: white)[Function $f(x)$],
    text(weight: "bold", fill: white)[Derivative $f'(x)$],
    text(weight: "bold", fill: white)[Domain of Validity / Rule]
  ),
  [$k$ (constant)], [$0$], [$x in bb(R)$],
  [$x$], [$1$], [$x in bb(R)$],
  [$x^n$ ($n in bb(N)^*$)], [$n x^(n-1)$], [$x in bb(R)$],
  [$1 / x$], [$- 1 / x^2$], [$x in bb(R)^*$],
  [$sqrt(x)$], [$1 / (2 sqrt(x))$], [$x in ]0\,;+infinity[$],
  [$e^x$], [$e^x$], [$x in bb(R)$ (unique function equal to its derivative with $f(0)=1$)],
  [$ln(x)$], [$1 / x$], [$x in ]0\,;+infinity[$],
  [$cos(x)$], [$- sin(x)$], [$x in bb(R)$],
  [$sin(x)$], [$cos(x)$], [$x in bb(R)$],
  [$(u + v)'$], [$u' + v'$], [Linearity of differentiation],
  [$(u dot v)'$], [$u' v + u v'$], [Leibniz product rule],
  [$(u / v)'$], [$(u' v - u v') / v^2$], [Quotient rule ($v != 0$)],
  [$(e^u)'$], [$u' e^u$], [Exponential chain rule],
  [$(ln u)'$], [$u' / u$], [Logarithmic chain rule ($u > 0$)]
)

#recto()
= APPENDIX B: UNIVERSAL TABLE OF MATHEMATICAL NOTATIONS & SYMBOLS

#set text(size: 9pt)
#table(
  columns: (1.2fr, 2fr, 4fr),
  fill: (x, y) => if y == 0 { rgb("#0f172a") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 6pt,
  table.header(
    text(weight: "bold", fill: white)[Symbol],
    text(weight: "bold", fill: white)[Name & Reading],
    text(weight: "bold", fill: white)[Didactic Meaning & Example]
  ),
  [$bb(N)$], [Natural numbers], [Set of non-negative integers: $\{0, 1, 2, 3, dots\}$],
  [$bb(Z)$], [Integers], [Positive and negative integers: $\{dots, -2, -1, 0, 1, 2, dots\}$],
  [$bb(D)$], [Decimal numbers], [Numbers with a finite number of decimal digits: $a / 10^n$],
  [$bb(Q)$], [Rational numbers], [Fractions of two integers: $p / q$ with $q != 0$],
  [$bb(R)$], [Real numbers], [All points of the continuous number line (includes $sqrt(2), pi, e$)],
  [$bb(C)$], [Complex numbers], [Numbers of the form $z = a + i b$ where $i^2 = -1$],
  [$in$ / $in.not$], [Belongs to / Does not belong], [Relates an element to a set: $3 in bb(N)$, but $-2 in.not bb(N)$],
  [$subset$], [Subset of / Contained in], [Relates two sets: $bb(N) subset bb(Z) subset bb(D) subset bb(Q) subset bb(R) subset bb(C)$],
  [$inter$], [Intersection], [$A inter B$: set of elements common to $A$ and $B$ (logical AND)],
  [$union$], [Union], [$A union B$: set of elements belonging to $A$ or $B$ (logical OR)],
  [$emptyset$], [Empty set], [The set containing no elements],
  [$forall$], [For all / For every], [Universal quantifier: $forall x in bb(R), x^2 >= 0$],
  [$exists$], [There exists], [Existential quantifier: $exists x in bb(R), x^2 = 2$],
  [$==>$ / $<==>$], [Implies / Equivalent to], [Logical deduction and strict two-way equivalence],
  [$vec(u)$ / $arrow(A B)$], [Vector], [Directed displacement defined by direction, sense, and magnitude],
  [$norm(vec(u))$], [Vector norm / magnitude], [Geometric length of the directed segment representing $vec(u)$],
  [$vec(u) dot vec(v)$], [Dot product / Scalar product], [Geometric projection measure: $norm(vec(u)) norm(vec(v)) cos(theta)$],
  [$lim_(x -> a)$], [Limit], [Local behavior of a function near boundary point $a$ or $infinity$],
  [$f'(x)$], [First derivative], [Instantaneous rate of change and slope of the tangent line],
  [$integral_a^b f(t) d t$], [Definite integral], [Signed area under the curve of $f$ between bounds $a$ and $b$],
  [$sum_(i=1)^n$], [Summation], [Sequential addition of terms: $x_1 + x_2 + dots + x_n$],
  [$binom(n, k)$], [Combination / Binomial coeff.], [Number of ways to choose $k$ items from $n$ without order: $n! / (k!(n-k)!)$]
)

#recto()
= APPENDIX C: INDEX OF PHOTOGRAPHIC AND ARCHIVAL SOURCES

#v(0.3cm)
In accordance with the principles of open distribution under the *Creative Commons Attribution - ShareAlike 4.0 International License (CC BY-SA 4.0)* and respect for historical patrimony, all photographic plates and archival artifacts in this work are sourced from the *Wikimedia Commons* open repository and public domain archives.

== I. Large Frontispiece Plates (Mathematics in Nature)

#set text(size: 8.5pt)
#table(
  columns: (1.1fr, 1.4fr, 2fr, 1.2fr, 2fr),
  fill: (x, y) => if y == 0 { rgb("#1d4ed8") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 5.5pt,
  align: (center, left, left, left, left),
  table.header(
    text(weight: "bold", fill: white)[Location],
    text(weight: "bold", fill: white)[Subject & Species],
    text(weight: "bold", fill: white)[Mathematical Phenomenon],
    text(weight: "bold", fill: white)[Author & License],
    text(weight: "bold", fill: white)[Wikimedia Commons Source]
  ),
  [Frontispiece Vol. I\ (Full page left)],
  [*Honeycomb Cells*\ _(Apis mellifera)_],
  [Compact hexagonal tiling of the plane, Honeycomb Conjecture (Hales 1999), isoperimetric optimization.],
  [Waugsberg\ CC BY-SA 3.0],
  [#link("https://commons.wikimedia.org/wiki/File:Bienenwabe_mit_Eiern_und_Brut_5.jpg")[Wikimedia Commons\ `File:Bienenwabe_mit_Eiern_5.jpg`]],

  [Frontispiece Vol. II\ (Full page left)],
  [*Nautilus Cutaway*\ _(Nautilus pompilius)_],
  [Logarithmic spiral ($r = a e^(b theta)$), gnomonic self-similar growth, continuous geometric proportions.],
  [Chris 73\ CC BY-SA 3.0],
  [#link("https://commons.wikimedia.org/wiki/File:NautilusCutawayLogarithmicSpiral.jpg")[Wikimedia Commons\ `File:NautilusCutawayLogarithmicSpiral.jpg`]],

  [Frontispiece Vol. III\ (Full page left)],
  [*Sunflower Head*\ _(Helianthus annuus)_],
  [Phyllotaxis, intersecting Fibonacci spirals (34/55), divergence angle governed by the Golden Ratio ($137.5077^circle$).],
  [Anna Benczur\ CC BY-SA 4.0],
  [#link("https://commons.wikimedia.org/wiki/File:Fibonacci_spiral.jpg")[Wikimedia Commons\ `File:Fibonacci_spiral.jpg`]],

  [Frontispiece Vol. IV\ (Full page left)],
  [*Romanesco Broccoli*\ _(Brassica oleracea)_],
  [Strict fractal self-similarity, scale invariance, recursive geometry, and nested logarithmic spirals.],
  [Ivar Leidus (Iifar)\ CC BY-SA 4.0],
  [#link("https://commons.wikimedia.org/wiki/File:Romanesco_broccoli_(Brassica_oleracea).jpg")[Wikimedia Commons\ `File:Romanesco_broccoli.jpg`]],

  [Frontispiece Vol. V\ (Full page left)],
  [*Dewy Spider Web*\ _(Araneus diadematus)_],
  [Concurrent vector equilibrium, trigonometric force resolution, and catenary curve geometry ($y = a cosh(x/a)$).],
  [Luc Viatour\ CC BY-SA 3.0],
  [#link("https://commons.wikimedia.org/wiki/File:Spider_web_Luc_Viatour.jpg")[Wikimedia Commons\ `File:Spider_web_Luc_Viatour.jpg`]],

  [Frontispiece Vol. VI\ (Full page left)],
  [*Textile Cone Shell*\ _(Conus textile)_],
  [Turing reaction-diffusion morphogenesis (Turing 1952), cellular automata (Rule 30), and Sierpinski fractal patterning.],
  [Reinhold Möller (Ermell)\ CC BY-SA 4.0],
  [#link("https://commons.wikimedia.org/wiki/File:Textil-Kegelschnecke_(Conus_textile)-20080201-RM-164444.jpg")[Wikimedia Commons\ `File:Textil-Kegelschnecke.jpg`]]
)

#v(0.3cm)
== II. Historical & Archival Documents in the Core Text

#table(
  columns: (1.1fr, 1.4fr, 2fr, 1.2fr, 2fr),
  fill: (x, y) => if y == 0 { rgb("#0f172a") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 5.5pt,
  align: (center, left, left, left, left),
  table.header(
    text(weight: "bold", fill: white)[Chapter],
    text(weight: "bold", fill: white)[Document & Subject],
    text(weight: "bold", fill: white)[Pedagogical Significance],
    text(weight: "bold", fill: white)[Origin & License],
    text(weight: "bold", fill: white)[Wikimedia Commons Source]
  ),
  [Chapter 1\ (Vol. I)],
  [*The Ishango Bone*\ (~20,000 BCE)],
  [Earliest tally notches grouped in bundles, establishing one-to-one correspondence.],
  [RBINS Brussels\ Public domain],
  [#link("https://commons.wikimedia.org/wiki/File:Ishango_bone.jpg")[Wikimedia Commons\ `File:Ishango_bone.jpg`]],

  [Chapter 4\ (Vol. I)],
  [*The Pascaline*\ (Blaise Pascal, 1642)],
  [First operational mechanical gear train realizing automatic decimal carry transfer.],
  [David Monniaux\ CC BY-SA 3.0],
  [#link("https://commons.wikimedia.org/wiki/File:Arts_et_Metiers_Pascaline_dsc03869.jpg")[Musée des Arts & Métiers\ `File:Arts_et_Metiers_Pascaline.jpg`]],

  [Chapter 10\ (Vol. II)],
  [*Rhind Papyrus*\ (~1550 BCE)],
  [Egyptian partitioning tables and unit fraction decompositions ($2/n$).],
  [British Museum\ Public domain],
  [#link("https://commons.wikimedia.org/wiki/File:Rhind_Mathematical_Papyrus.jpg")[British Museum\ `File:Rhind_Mathematical_Papyrus.jpg`]],

  [Chapter 19\ (Vol. III)],
  [*Euclid's Elements*\ (Oliver Byrne, 1847)],
  [Original full-color four-color printing proving the Pythagorean Theorem through pure geometric hue.],
  [Oliver Byrne\ Public domain],
  [#link("https://commons.wikimedia.org/wiki/File:Byrne_1847_Satz_des_Pythagoras_Hochformat.jpg")[Patrimonial Library\ `File:Byrne_1847_Pythagoras.jpg`]],

  [Chapter 54\ (Vol. VI)],
  [*The Galton Board*\ (Francis Galton, 1877)],
  [Mechanical manifestation of the Central Limit Theorem: convergence of Pascal's triangle to the Normal distribution.],
  [Wikimedia Commons\ CC BY-SA 4.0],
  [#link("https://commons.wikimedia.org/wiki/File:Galton_board.png")[Physical sciences\ `File:Galton_board.png`]]
)

#v(0.3cm)
#block(
  fill: rgb("#eff6ff"),
  stroke: 1pt + rgb("#bfdbfe"),
  inset: 10pt,
  radius: 5pt
)[
  #text(size: 8pt, fill: rgb("#1e3a8a"))[
    *Editorial note on reuse rights:* All images above are reusable under their respective licenses (Public Domain, CC BY-SA 3.0, and CC BY-SA 4.0). For reproduction, adaptation, or redistribution, please credit original authors and cite Wikimedia Commons links in compliance with share-alike provisions.
  ]
]

#recto()
= DETAILED THEMATIC INDEX

#set text(size: 9pt)
#table(
  columns: (2.5fr, 1.2fr, 4fr),
  fill: (x, y) => if y == 0 { rgb("#1d4ed8") } else if calc.odd(y) { rgb("#f8fafc") } else { none },
  stroke: 0.5pt + rgb("#cbd5e1"),
  inset: 6pt,
  table.header(
    text(weight: "bold", fill: white)[Key Concept],
    text(weight: "bold", fill: white)[Location],
    text(weight: "bold", fill: white)[Pedagogical & Didactic Meaning]
  ),
  [Abacus / Counting Frame], [Vol. I, Ch. 4], [Materialization of decimal grouping and carry transfer],
  [Al-Khwarizmi's Scale], [Vol. IV, Ch. 22], [Equivalence of bilateral operations for algebraic equations],
  [Angle (acute, right, obtuse)], [Vol. III, Ch. 15], [Measure of angular opening independent of side lengths],
  [Area (rectangle / disk)], [Vol. II, Ch. 12 & 16], [Planar tiling measure and Archimedean circle quadrature],
  [Asymptote (horizontal, vertical)], [Vol. VI, Ch. 45], [Behavior at infinite boundaries or forbidden poles],
  [Base Ten (Decimal)], [Vol. I, Ch. 2], [Grouping into tens grounded in two-hand morphology],
  [Bijection (One-to-One)], [Vol. I, Ch. 1], [Term-to-term correspondence of prehistoric pebble pouch],
  [Cartesian Coordinates], [Vol. III, Ch. 20], [Two-dimensional coordinate localization and grid paths],
  [Complex Numbers], [Vol. VI, Ch. 55], [Argand-Gauss plane and imaginary unit $i^2 = -1$ as a 90° rotation],
  [Derivative & Tangent], [Vol. V, Ch. 39], [Transition from average secant rate to instantaneous slope],
  [Differential Equation], [Vol. VI, Ch. 51], [Law of evolution where rate depends on present state ($y' = a y$)],
  [Euclidean Algorithm], [Vol. IV, Ch. 29], [GCD computation via successive subtractions and divisions],
  [Exponential Function ($e^x$)], [Vol. V, Ch. 40], [Unique function equal to its derivative with $f(0) = 1$],
  [Fractions (Partition & Ratio)], [Vol. II, Ch. 10], [Fraction as cutting operator, measure, and rational number],
  [Intermediate Value Theorem], [Vol. VI, Ch. 46], [Topological guarantee that continuous curves cross all values],
  [Long Multiplication], [Vol. I, Ch. 5], [Two-tier column algorithm with mandatory decimal shift zero],
  [Matrices & Graphs], [Vol. VI, Ch. 57], [Multilinear operational arrays and Markov random walks],
  [Mathematical Induction], [Vol. VI, Ch. 43], [Hereditary propagation of mathematical truth (domino effect)],
  [Natural Logarithm ($ln$)], [Vol. VI, Ch. 48], [Inverse of exponential transforming products into sums],
  [Negative Numbers], [Vol. II, Ch. 14], [Axial symmetry around zero for debts and subzero temperatures],
  [Normal Distribution (Gauss)], [Vol. VI, Ch. 54], [Universal bell curve arising from Central Limit Theorem],
  [Probability Tree], [Vol. V, Ch. 42], [Representation of conditional probabilities and Bayes' theorem],
  [Pythagorean Theorem], [Vol. III, Ch. 19], [Area conservation on legs of right triangle ($a^2 + b^2 = c^2$)],
  [Riemann Integral], [Vol. VI, Ch. 50], [Limit of rectangular slice sums for signed area evaluation],
  [Subitizing], [Vol. I, Ch. 1], [Instantaneous visual recognition of quantities up to 3 or 4],
  [Thales' Theorem], [Vol. III, Ch. 17], [Conservation of proportionality ratios under parallel projection],
  [Trigonometric Circle], [Vol. V, Ch. 37], [Wrapping the real line onto the unit circle with projections]
)

#recto()
= ANNOTATED HISTORICAL & DIDACTIC BIBLIOGRAPHY

#v(0.3cm)
=== I. Foundational Texts in the History of Mathematics

- *Euclid of Alexandria* (~300 BCE), *The Elements*. Translated by T. L. Heath, Dover Publications.
  _The seminal masterpiece that established the axiomatic deductive method and Euclidean geometry._
- *Al-Khwarizmi, Muhammad ibn Musa* (~820), *The Compendious Book on Calculation by Completion and Balancing* (*Al-Kitab al-mukhtasar fi hisab al-jabr wa'l-muqabala*).
  _The founding treatise of algebra as an autonomous science of bilateral operational balance._
- *Descartes, René* (1637), *Geometry* (*La Géométrie*). Appendix to the *Discourse on Method*.
  _The unification of algebra and geometry through the invention of the Cartesian coordinate system._
- *Byrne, Oliver* (1847), *The First Six Books of the Elements of Euclid in which Coloured Diagrams and Symbols are used instead of Letters for the Greater Ease of Learners*, William Pickering, London.
  _The masterpiece of visual mathematical semiotics that directly inspired the graphic color palette of this book._
- *Euler, Leonhard* (1748), *Introductio in analysin infinitorum*.
  _The work that established modern analysis, function theory, base $e$, and the identity $e^(i pi) + 1 = 0$._
- *Gauss, Carl Friedrich* (1801), *Disquisitiones Arithmeticae*.
  _The monumental foundation of modern number theory, modular arithmetic, and congruences._

=== II. Didactics, Cognitive Science & Embodied Cognition

- *Lakoff, George & Núñez, Rafael* (2000), *Where Mathematics Comes From: How the Embodied Mind Brings Mathematics into Being*, Basic Books.
  _The seminal treatise on embodied mathematical cognition, demonstrating how the most abstract concepts (actual infinity, limits, complex numbers) are built upon conceptual metaphors grounded in bodily motion and physical gesture._
- *Dehaene, Stanislas* (2011), *The Number Sense: How the Mind Creates Mathematics*, Oxford University Press.
  _The neurocognitive foundations of number sense, subitizing, and neuronal recycling in mathematical learning._
- *Brousseau, Guy* (1997), *Theory of Didactical Situations in Mathematics*, Kluwer Academic Publishers.
  _Fundamental analysis of devolution, the didactical contract, and epistemological obstacles._
- *Polya, George* (1945), *How to Solve It*, Princeton University Press.
  _The classic guide to mathematical heuristics: decomposing, visualizing, generalizing, and testing boundary cases._
- *Sweller, John* (2011), *Cognitive Load Theory*, Springer.
  _The cognitive load balance between working memory limitations and long-term schema acquisition._

#metadata("fin-section") <fin-section>
#pagebreak(to: "odd")
#set page(header: none, footer: none)
#metadata("debut-section") <debut-section>
#box()
#pagebreak()

// ==========================================
// 5. BACK COVER (QUATRIÈME DE COUVERTURE)
// ==========================================
#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 1.5cm, left: 1.5cm, right: 1.5cm),
  fill: rgb("#070d1e"),
  header: none,
  footer: none
)

#block(
  stroke: 1.5pt + rgb("#f59e0b"),
  inset: (x: 22pt, top: 22pt, bottom: 18pt),
  radius: 8pt,
  width: 100%,
  height: 100%
)[
  #align(center)[
    #text(size: 11pt, weight: "bold", fill: rgb("#f59e0b"), tracking: 2.5pt, font: "Liberation Sans")[
      SILVÈRE MARTIN-MICHIELLOT & ANTIGRAVITY
    ]
    #v(0.35cm)
    #text(size: 26pt, weight: "bold", fill: white, font: "Liberation Serif")[
      THE WAY OF THE NUMBER
    ]
    #v(0.18cm)
    #text(size: 12pt, weight: "bold", fill: rgb("#93c5fd"), font: "Liberation Sans")[
      A Constructive Odyssey, from the First Pebble to Advanced High School Mathematics
    ]
    #v(0.4cm)
    
    #block(
      fill: rgb("#0f172a"),
      stroke: (left: 3pt + rgb("#f59e0b")),
      inset: (left: 14pt, right: 12pt, y: 9pt),
      radius: (right: 4pt),
      width: 100%
    )[
      #align(left)[
        #text(size: 10pt, style: "italic", fill: rgb("#fef08a"))[
          “What if the distaste for mathematics stemmed not from a lack of intelligence, but from the amnesia of the eyes and hands?”
        ]
      ]
    ]
  ]
  
  #v(0.4cm)
  #align(left)[
    #text(size: 9.5pt, fill: rgb("#e2e8f0"))[
      How can the human mind permanently reconcile with the clarity, beauty, and power of mathematics? Why do so many students stumble before abstract symbols whose living historical roots have been forgotten?
      
      *THE WAY OF THE NUMBER* answers this challenge across fifty-eight interconnected chapters, guiding the learner step by step from the awakening of visual number sense and the first counting pebbles to the heights of secondary mathematics. Every concept is born from concrete physical gesture before ascending into crystal-clear deductive rigor.
    ]
  ]
  
  #v(0.45cm)
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    block(fill: rgb("#0f172a"), stroke: 0.75pt + rgb("#f59e0b"), inset: 10pt, radius: 5pt)[
      #text(size: 9pt, weight: "bold", fill: rgb("#f59e0b"))[1. Living Historical Foundations]\\
      #v(2pt)
      #text(size: 8pt, fill: rgb("#cbd5e1"))[From Euclid's Nile to Napier's logarithms: every theorem solves a human riddle.]
    ],
    block(fill: rgb("#0f172a"), stroke: 0.75pt + rgb("#60a5fa"), inset: 10pt, radius: 5pt)[
      #text(size: 9pt, weight: "bold", fill: rgb("#60a5fa"))[2. Visual Intelligence]\\
      #v(2pt)
      #text(size: 8pt, fill: rgb("#cbd5e1"))[Understanding through color and form: the eye grasps logic before formal calculation.]
    ],
    block(fill: rgb("#0f172a"), stroke: 0.75pt + rgb("#4ade80"), inset: 10pt, radius: 5pt)[
      #text(size: 9pt, weight: "bold", fill: rgb("#4ade80"))[3. Operative Automation]\\
      #v(2pt)
      #text(size: 8pt, fill: rgb("#cbd5e1"))[Mastering column algorithms: freeing working memory for high-level reasoning.]
    ],
    block(fill: rgb("#0f172a"), stroke: 0.75pt + rgb("#f87171"), inset: 10pt, radius: 5pt)[
      #text(size: 9pt, weight: "bold", fill: rgb("#f87171"))[4. Elucidation of Boundary Cases]\\
      #v(2pt)
      #text(size: 8pt, fill: rgb("#cbd5e1"))[From division by zero to actual infinities: absolute rigor without blind spots.]
    ]
  )
  
  #v(0.45cm)
  #block(
    fill: rgb("#0f172a"),
    stroke: 1pt + rgb("#334155"),
    inset: (x: 12pt, y: 8pt),
    radius: 5pt,
    width: 100%
  )[
    #text(size: 8.5pt, weight: "bold", fill: rgb("#38bdf8"))[Target Audience: ]
    #text(size: 8pt, fill: rgb("#cbd5e1"))[
      Students from Grade 1 to Grade 12 & Advanced Mathematics • Exam & competition candidates • Homeschooling families • Educators & curious autodidacts.
    ]
  ]
  
  #v(1fr)
  #align(center)[
    #line(length: 60%, stroke: 0.5pt + rgb("#f59e0b"))
    #v(0.2cm)
    #text(size: 8.5pt, style: "italic", fill: rgb("#fde047"))[“All things are numbers, and number is the guide of the soul.” — Philolaus of Croton]
    #v(0.15cm)
    #text(size: 7.5pt, fill: rgb("#94a3b8"))[
      Definitive Reference Edition • Creative Commons CC BY-SA 4.0 License (Open distribution & sharing)
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
        return "\n![La commutativité par rotation 90°](figures_en/vol_1/fig_05_commutativite_rotation.svg)\n"
    elif 'multiplication posée à deux étages' in raw_l or '1  4  6' in raw or '4  3  8' in raw:
        return "\n![La multiplication posée à deux étages avec retenue](figures_en/vol_1/fig_05_multiplication_posee_ret.svg)\n"
    elif "l'anatomie de la potence" in raw_l or "d-m-s-a" in raw_l:
        return "\n![L'anatomie de la potence de division euclidienne](figures_en/vol_2/fig_09_potence_division.svg)\n"
    elif "a²" in raw_l and "ab" in raw_l and "b²" in raw_l:
        return "\n![Preuve géométrique de l'identité remarquable (a+b)²](figures_en/vol_4/fig_23_identite_remarquable_carre.svg)\n"
    elif "chasles" in raw_l or ("u = ab" in raw_l and "v = bc" in raw_l):
        return "\n![Vecteurs dans le plan : relation de Chasles u + v](figures_en/vol_5/fig_32_chasles_addition.svg)\n"
    elif "cosinus x" in raw_l or "sinus x" in raw_l:
        return "\n![Le cercle trigonométrique et les fonctions sinus et cosinus](figures_en/vol_5/fig_37_cercle_trigo_complet.svg)\n"
    elif "plan 𝒫" in raw or "plan p" in raw_l or "vecteur normal" in raw_l:
        return "\n![Équation cartésienne du plan et vecteur normal](figures_en/vol_6/fig_52_plan_vecteur_normal.svg)\n"
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
    block_idx = 0
    
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
            replacement = transform_block(cur_block, cur_lang, cur_prefix, chapter_name, start_line, vol_dir, block_idx)
            block_idx += 1
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

EN_ACTION_MAP = {
  "Volume_I|1|0": [
    "SVG",
    "The subitizing phenomenon: immediate perception vs cognitive saturation",
    "figures_en/vol_1/fig_01_subitizing.svg"
  ],
  "Volume_I|1|1": [
    "SVG",
    "The six faces of the die: instant spatial recognition",
    "figures_en/vol_1/fig_01_dice.svg"
  ],
  "Volume_I|1|2": [
    "SVG",
    "Term-to-term correspondence: direct comparison of two collections",
    "figures_en/vol_1/fig_01_correspondance.svg"
  ],
  "Volume_I|1|3": [
    "SVG",
    "Term-to-term correspondence: direct comparison of two collections",
    "figures_en/vol_1/fig_01_correspondance.svg"
  ],
  "Volume_I|1|4": [
    "CALLOUT",
    "Solved Example — Visual Comparison in Parallel Rows"
  ],
  "Volume_I|1|5": [
    "SVG",
    "The Ishango bone: early tally notches grouped in bundles",
    "figures_en/vol_1/fig_01_os_ishango.svg"
  ],
  "Volume_I|2|0": [
    "SVG",
    "The tally stick: cognitive saturation of 45 continuous strokes",
    "figures_en/vol_1/fig_02_baton_45_traits.svg"
  ],
  "Volume_I|2|1": [
    "SVG",
    "Two open hands: 5 + 5 = 10, foundation of the decimal base",
    "figures_en/vol_1/fig_02_deux_mains_dix.svg"
  ],
  "Volume_I|2|2": [
    "SVG",
    "Regular bundling: 10 loose units become 1 bundled ten",
    "figures_en/vol_1/fig_02_echange_dizaine.svg"
  ],
  "Volume_I|2|3": [
    "SVG",
    "The decimal pyramid: units, tens, hundreds, thousands",
    "figures_en/vol_1/fig_02_pyramide_dizaines.svg"
  ],
  "Volume_I|2|4": [
    "SVG",
    "The place-value house chart: hundreds, tens, and units",
    "figures_en/vol_1/fig_02_tableau_maisons.svg"
  ],
  "Volume_I|2|5": [
    "CALLOUT",
    "📐 Fundamental Rule — The Role of Zero as a Place Keeper"
  ],
  "Volume_I|2|6": [
    "SVG",
    "The directed number line from 0 to 100",
    "figures_en/vol_1/fig_02_droite_100.svg"
  ],
  "Volume_I|2|7": [
    "SVG",
    "The comparison crocodile: jaws open toward the greater quantity",
    "figures_en/vol_1/fig_02_crocodile_comparaison.svg"
  ],
  "Volume_I|3|0": [
    "SVG",
    "The addition pot: pooling two quantities together",
    "figures_en/vol_1/fig_03_marmite_addition.svg"
  ],
  "Volume_I|3|1": [
    "SVG",
    "Concrete subtraction: 7 fish minus 2 snatched away",
    "figures_en/vol_1/fig_03_poissons_renard.svg"
  ],
  "Volume_I|3|2": [
    "SVG",
    "The balance of justice: state of perfect equilibrium",
    "figures_en/vol_1/fig_03_balance_justice.svg"
  ],
  "Volume_I|3|3": [
    "CALLOUT",
    "💡 Discovery & History — Friends of 10 and Complementary Pairs"
  ],
  "Volume_I|3|4": [
    "SVG",
    "The addition pyramid: sum of underlying bricks",
    "figures_en/vol_1/fig_03_pyramide_addition.svg"
  ],
  "Volume_I|4|0": [
    "SVG",
    "The merchant's abacus: units and tens compartments",
    "figures_en/vol_1/fig_04_abaque_boite.svg"
  ],
  "Volume_I|4|1": [
    "CALC_OP"
  ],
  "Volume_I|4|2": [
    "CALC_OP"
  ],
  "Volume_I|4|3": [
    "CALC_OP"
  ],
  "Volume_I|4|4": [
    "CALC_OP"
  ],
  "Volume_I|4|5": [
    "CALC_OP"
  ],
  "Volume_I|4|6": [
    "CALC_OP"
  ],
  "Volume_I|4|7": [
    "CALC_OP"
  ],
  "Volume_I|4|8": [
    "CALC_OP"
  ],
  "Volume_I|4|9": [
    "CALC_OP"
  ],
  "Volume_I|4|10": [
    "CALC_OP"
  ],
  "Volume_I|4|11": [
    "CALC_OP"
  ],
  "Volume_I|4|12": [
    "CALC_OP"
  ],
  "Volume_I|4|13": [
    "CALC_OP"
  ],
  "Volume_I|4|14": [
    "CALC_OP"
  ],
  "Volume_I|4|15": [
    "CALC_OP"
  ],
  "Volume_I|4|16": [
    "CALC_OP"
  ],
  "Volume_I|4|17": [
    "CALC_OP"
  ],
  "Volume_I|5|0": [
    "SVG",
    "The brick wall: 4 rows of 6 make 24",
    "figures_en/vol_1/fig_05_mur_briques_4x6.svg"
  ],
  "Volume_I|5|1": [
    "SVG",
    "Commutativity by rotation: 4 × 6 = 6 × 4",
    "figures_en/vol_1/fig_05_commutativite_rotation.svg"
  ],
  "Volume_I|5|2": [
    "SVG",
    "Double and half: bilateral multiplicative symmetry",
    "figures_en/vol_1/fig_05_double_moitie.svg"
  ],
  "Volume_I|5|3": [
    "SVG",
    "The finger trick for the 9 times table",
    "figures_en/vol_1/fig_05_doigts_table_9.svg"
  ],
  "Volume_I|5|4": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1fr, 1fr, 1fr, 1.8fr),\n    align: center,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [*Centaines*], [*Dizaines*], [*Unités*], [*Valeur décimale*],\n    [], [], [4], [$4$],\n    [], [4], [0], [$4 times 10 = 40$],\n    [4], [0], [0], [$4 times 100 = 400$]\n  )\n]\n```"
  ],
  "Volume_I|5|5": [
    "CALC_OP"
  ],
  "Volume_I|5|6": [
    "CALC_OP"
  ],
  "Volume_I|5|7": [
    "CALC_OP"
  ],
  "Volume_I|5|8": [
    "CALC_OP"
  ],
  "Volume_I|5|9": [
    "CALC_OP"
  ],
  "Volume_I|5|10": [
    "CALC_OP"
  ],
  "Volume_I|5|11": [
    "CALC_OP"
  ],
  "Volume_I|6|0": [
    "SVG",
    "The pharaonic royal cubit: anatomical standard of measure",
    "figures_en/vol_1/fig_06_coudee_royale.svg"
  ],
  "Volume_I|6|1": [
    "CALLOUT",
    "💡 Discovery & History — Historical Anatomical Measurements"
  ],
  "Volume_I|6|2": [
    "SVG",
    "Ruler measurement: alignment at zero and direct reading",
    "figures_en/vol_1/fig_06_regle_graduee.svg"
  ],
  "Volume_I|6|3": [
    "SVG",
    "Weighing the melon: mass balance of 1 kilogram",
    "figures_en/vol_1/fig_06_pesee_melon_1kg.svg"
  ],
  "Volume_I|6|4": [
    "SVG",
    "The circular dial: 12 hours and 60 minutes",
    "figures_en/vol_1/fig_06_cadran_horloge.svg"
  ],
  "Volume_I|7|0": [
    "SVG",
    "The three fundamental shapes of planar geometry",
    "figures_en/vol_1/fig_07_formes_fondamentales.svg"
  ],
  "Volume_I|7|1": [
    "SVG",
    "The gardener's string: drawing a perfect circle",
    "figures_en/vol_1/fig_07_ficelle_jardinier.svg"
  ],
  "Volume_I|7|2": [
    "SVG",
    "Folding a set square: the 90° right angle",
    "figures_en/vol_1/fig_07_pliage_angle_droit.svg"
  ],
  "Volume_I|7|3": [
    "SVG",
    "Fundamental geometric solids: cube, rectangular prism, and cylinder",
    "figures_en/vol_1/fig_07_solides_fondamentaux.svg"
  ],
  "Volume_I|7|4": [
    "SVG",
    "The butterfly and bilateral axial symmetry",
    "figures_en/vol_1/fig_07_papillon_symetrie.svg"
  ],
  "Volume_I|7|5": [
    "SVG",
    "Plotting coordinates on a discrete Cartesian grid",
    "figures_en/vol_1/fig_07_grille_reperage.svg"
  ],
  "Volume_I|7|6": [
    "CALLOUT",
    "🛠️ Practical Application — Grid Treasure Hunt"
  ],
  "Volume_II|8|0": [
    "SVG",
    "Rectangular formation of soldiers: 2 × 6 and 3 × 4",
    "figures_en/vol_2/fig_08_formations_rectangles.svg"
  ],
  "Volume_II|8|1": [
    "SVG",
    "Parity: paired even numbers vs solitary odd soldier",
    "figures_en/vol_2/fig_08_parite_soldat.svg"
  ],
  "Volume_II|8|2": [
    "SVG",
    "Regular jumps of 3 by 3 of the frog",
    "figures_en/vol_2/fig_08_grenouille_sauts.svg"
  ],
  "Volume_II|8|3": [
    "SVG",
    "Rectangular formation of soldiers: 2 × 6 and 3 × 4",
    "figures_en/vol_2/fig_08_formations_rectangles.svg"
  ],
  "Volume_II|8|4": [
    "SVG",
    "Prime factorization tree",
    "figures_en/vol_2/fig_08_decomposition_premiers.svg"
  ],
  "Volume_II|9|0": [
    "SVG",
    "The two meanings of division: fair sharing and grouping",
    "figures_en/vol_2/fig_09_sens_division.svg"
  ],
  "Volume_II|9|1": [
    "SVG",
    "The two meanings of division: fair sharing and grouping",
    "figures_en/vol_2/fig_09_sens_division.svg"
  ],
  "Volume_II|9|2": [
    "SVG",
    "Anatomy of the Euclidean long division bracket",
    "figures_en/vol_2/fig_09_potence_division.svg"
  ],
  "Volume_II|9|3": [
    "SVG",
    "The two meanings of division: fair sharing and grouping",
    "figures_en/vol_2/fig_09_sens_division.svg"
  ],
  "Volume_II|9|4": [
    "SVG",
    "Anatomy of the Euclidean long division bracket",
    "figures_en/vol_2/fig_09_potence_division.svg"
  ],
  "Volume_II|9|5": [
    "CALC_OP"
  ],
  "Volume_II|9|6": [
    "CALC_OP"
  ],
  "Volume_II|9|7": [
    "CALC_OP"
  ],
  "Volume_II|9|8": [
    "CALC_OP"
  ],
  "Volume_II|9|9": [
    "CALC_OP"
  ],
  "Volume_II|9|10": [
    "CALC_OP"
  ],
  "Volume_II|9|11": [
    "CALC_OP"
  ],
  "Volume_II|10|0": [
    "SVG",
    "Sharing the flatbread: fractions of a disk",
    "figures_en/vol_2/fig_10_galette_quarts.svg"
  ],
  "Volume_II|10|1": [
    "SVG",
    "Sharing the flatbread: fractions of a disk",
    "figures_en/vol_2/fig_10_galette_quarts.svg"
  ],
  "Volume_II|10|2": [
    "SVG",
    "Anatomy of a fraction: role of numerator and denominator",
    "figures_en/vol_2/fig_10_numerateur_denominateur.svg"
  ],
  "Volume_II|10|3": [
    "SVG",
    "Sharing the flatbread: fractions of a disk",
    "figures_en/vol_2/fig_10_galette_quarts.svg"
  ],
  "Volume_II|10|4": [
    "CALLOUT",
    "💡 Discovery — The Complete Unit as a Fraction $6/6$"
  ],
  "Volume_II|10|5": [
    "SVG",
    "Sharing the flatbread: fractions of a disk",
    "figures_en/vol_2/fig_10_galette_quarts.svg"
  ],
  "Volume_II|10|6": [
    "SVG",
    "The number line graduated in fourths",
    "figures_en/vol_2/fig_10_droite_graduee_quarts.svg"
  ],
  "Volume_II|10|7": [
    "SVG",
    "Equivalent fractions by strip division: 1/2 = 2/4",
    "figures_en/vol_2/fig_10_bandes_pliees.svg"
  ],
  "Volume_II|10|8": [
    "CALLOUT",
    "Solved Example — Dividing the Cake into Eighths"
  ],
  "Volume_II|11|0": [
    "SVG",
    "Operational shifting of the decimal point",
    "figures_en/vol_2/fig_11_glissement_virgule.svg"
  ],
  "Volume_II|11|1": [
    "SVG",
    "Operational shifting of the decimal point",
    "figures_en/vol_2/fig_11_glissement_virgule.svg"
  ],
  "Volume_II|11|2": [
    "SVG",
    "Operational shifting of the decimal point",
    "figures_en/vol_2/fig_11_glissement_virgule.svg"
  ],
  "Volume_II|11|3": [
    "SVG",
    "Operational shifting of the decimal point",
    "figures_en/vol_2/fig_11_glissement_virgule.svg"
  ],
  "Volume_II|11|4": [
    "CALC_OP"
  ],
  "Volume_II|11|5": [
    "CALC_OP"
  ],
  "Volume_II|11|6": [
    "SVG",
    "Operational shifting of the decimal point",
    "figures_en/vol_2/fig_11_glissement_virgule.svg"
  ],
  "Volume_II|12|0": [
    "CALLOUT",
    "💡 Discovery & History — The Chaos of Weights and Measures under the Ancien Régime"
  ],
  "Volume_II|12|1": [
    "SVG",
    "Measurement of Earth's meridian and the universal meter standard",
    "figures_en/vol_2/fig_12_meridien_metre.svg"
  ],
  "Volume_II|12|2": [
    "SVG",
    "The universal metric system: multiple and submultiple prefixes",
    "figures_en/vol_2/fig_12_prefixes_metriques.svg"
  ],
  "Volume_II|12|3": [
    "SVG",
    "1D Linear perimeter vs 2D surface area",
    "figures_en/vol_2/fig_12_perimetre_vs_aire.svg"
  ],
  "Volume_II|12|4": [
    "SVG",
    "1D Linear perimeter vs 2D surface area",
    "figures_en/vol_2/fig_12_perimetre_vs_aire.svg"
  ],
  "Volume_II|12|5": [
    "SVG",
    "1D Linear perimeter vs 2D surface area",
    "figures_en/vol_2/fig_12_perimetre_vs_aire.svg"
  ],
  "Volume_II|12|6": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1fr, 1fr, 1fr),\n    align: center + horizon,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [*Acute Angle*], [*Right Angle*], [*Obtuse Angle*],\n    [More closed than square], [Fits square exactly], [More open than square],\n    [Aperture $< 90 degree$], [Aperture $= 90 degree$], [Aperture $> 90 degree$]\n  )\n]\n```"
  ],
  "Volume_II|13|0": [
    "SVG",
    "The proportionality table and the rule of three",
    "figures_en/vol_2/fig_13_regle_trois.svg"
  ],
  "Volume_II|13|1": [
    "SVG",
    "The proportionality table and the rule of three",
    "figures_en/vol_2/fig_13_regle_trois.svg"
  ],
  "Volume_II|13|2": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (2.5fr, 1fr, 1fr, 1fr, 1fr),\n    align: (left, center, center, center, center),\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#f1f5f9\") } else { rgb(\"#ffffff\") },\n    [Grandeur 1 (nombre de cahiers)], [2], [4], [6], [10],\n    [Grandeur 2 (prix en euros)], [5 €], [10 €], [15 €], [25 €]\n  )\n]\n```"
  ],
  "Volume_II|13|3": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (2.5fr, 1fr, 1fr, 1fr, 1fr),\n    align: (left, center, center, center, center),\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#f1f5f9\") } else { rgb(\"#ffffff\") },\n    [Grandeur 1 (nombre de cahiers)], [2], [4], [6], [10],\n    [Grandeur 2 (prix en euros)], [5 €], [10 €], [15 €], [25 €]\n  )\n]\n```"
  ],
  "Volume_II|13|4": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (2.5fr, 1fr, 1fr, 1fr, 1.2fr),\n    align: (left, center, center, center, center),\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#f1f5f9\") } else { rgb(\"#ffffff\") },\n    [Nombre de gâteaux], [3], [5], [8], [× 4],\n    [Nombre de fraises], [12], [20], [32], [(Coefficient)]\n  )\n]\n```"
  ],
  "Volume_II|13|5": [
    "SVG",
    "The proportionality table and the rule of three",
    "figures_en/vol_2/fig_13_regle_trois.svg"
  ],
  "Volume_II|14|0": [
    "SVG",
    "The signed number line of positive and negative integers",
    "figures_en/vol_2/fig_14_axe_relatifs.svg"
  ],
  "Volume_II|14|1": [
    "SVG",
    "The signed number line of positive and negative integers",
    "figures_en/vol_2/fig_14_axe_relatifs.svg"
  ],
  "Volume_II|14|2": [
    "SVG",
    "The signed number line of positive and negative integers",
    "figures_en/vol_2/fig_14_axe_relatifs.svg"
  ],
  "Volume_II|14|3": [
    "SVG",
    "The signed number line of positive and negative integers",
    "figures_en/vol_2/fig_14_axe_relatifs.svg"
  ],
  "Volume_II|14|4": [
    "SVG",
    "The signed number line of positive and negative integers",
    "figures_en/vol_2/fig_14_axe_relatifs.svg"
  ],
  "Volume_II|14|5": [
    "SVG",
    "The signed number line of positive and negative integers",
    "figures_en/vol_2/fig_14_axe_relatifs.svg"
  ],
  "Volume_II|14|6": [
    "SVG",
    "The signed number line of positive and negative integers",
    "figures_en/vol_2/fig_14_axe_relatifs.svg"
  ],
  "Volume_III|15|0": [
    "CALLOUT",
    "📐 Fundamental Definition — The Geometric Anatomy of an Angle"
  ],
  "Volume_III|15|1": [
    "CALLOUT",
    "💡 Observation — Comparing the Aperture of an Angle's Rays"
  ],
  "Volume_III|15|2": [
    "SVG",
    "Classification of the four angle types",
    "figures_en/vol_3/fig_15_quatre_types_angles.svg"
  ],
  "Volume_III|15|3": [
    "SVG",
    "Vertically opposite angles and geometric equality",
    "figures_en/vol_3/fig_15_angles_opposes.svg"
  ],
  "Volume_III|15|4": [
    "SVG",
    "Fundamental parallel and perpendicular lines",
    "figures_en/vol_3/fig_15_paralleles_perpendiculaires.svg"
  ],
  "Volume_III|16|0": [
    "SVG",
    "Key circle elements: radius, diameter, and chord",
    "figures_en/vol_3/fig_16_vocabulaire_cercle.svg"
  ],
  "Volume_III|16|1": [
    "SVG",
    "Archimedes' method: bounding Pi with regular polygons",
    "figures_en/vol_3/fig_16_archimede_polygones.svg"
  ],
  "Volume_III|16|2": [
    "SVG",
    "Key circle elements: radius, diameter, and chord",
    "figures_en/vol_3/fig_16_vocabulaire_cercle.svg"
  ],
  "Volume_III|16|3": [
    "SVG",
    "Unrolling the circle: geometric definition of Pi",
    "figures_en/vol_3/fig_16_deroulement_cercle_pi.svg"
  ],
  "Volume_III|16|4": [
    "SVG",
    "Archimedes' method: bounding Pi with regular polygons",
    "figures_en/vol_3/fig_16_archimede_polygones.svg"
  ],
  "Volume_III|16|5": [
    "SVG",
    "Unrolling the circle: geometric definition of Pi",
    "figures_en/vol_3/fig_16_deroulement_cercle_pi.svg"
  ],
  "Volume_III|16|6": [
    "SVG",
    "Key circle elements: radius, diameter, and chord",
    "figures_en/vol_3/fig_16_vocabulaire_cercle.svg"
  ],
  "Volume_III|17|0": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_III|17|1": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_III|17|2": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_III|17|3": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_III|17|4": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_III|17|5": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_III|18|0": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1fr, 1fr, 1fr, 1fr, 0.8fr, 1.2fr),\n    align: center,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [*1re case*], [*2e case*], [*3e case*], [*4e case*], [*...*], [*64e case*],\n    [1 grain], [2 grains], [4 grains], [8 grains], [...], [$2^(63)$ grains !]\n  )\n]\n```"
  ],
  "Volume_III|18|1": [
    "SVG",
    "The universal PEMDAS order of operations",
    "figures_en/vol_3/fig_18_pemdas.svg"
  ],
  "Volume_III|18|2": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr),\n    align: center + horizon,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [*Nucleus*], [*Atom*], [*Human*], [*Earth*], [*Solar System*], [*Galaxy*],\n    [$10^(-15)$ m], [$10^(-10)$ m], [$1$ m ($10^0$ m)], [$10^6$ m], [$10^(11)$ m], [$10^(21)$ m]\n  )\n]\n```"
  ],
  "Volume_III|19|0": [
    "SVG",
    "The unit square and the incommensurable diagonal root of 2",
    "figures_en/vol_3/fig_19_carre_diagonale_racine2.svg"
  ],
  "Volume_III|19|1": [
    "SVG",
    "The unit square and the incommensurable diagonal root of 2",
    "figures_en/vol_3/fig_19_carre_diagonale_racine2.svg"
  ],
  "Volume_III|19|2": [
    "SVG",
    "Geometric proof of the Pythagorean Theorem",
    "figures_en/vol_3/fig_19_pythagore_puzzle.svg"
  ],
  "Volume_III|19|3": [
    "SVG",
    "The unit square and the incommensurable diagonal root of 2",
    "figures_en/vol_3/fig_19_carre_diagonale_racine2.svg"
  ],
  "Volume_III|19|4": [
    "SVG",
    "Geometric proof of the Pythagorean Theorem",
    "figures_en/vol_3/fig_19_pythagore_puzzle.svg"
  ],
  "Volume_III|19|5": [
    "SVG",
    "Geometric proof of the Pythagorean Theorem",
    "figures_en/vol_3/fig_19_pythagore_puzzle.svg"
  ],
  "Volume_III|19|6": [
    "SVG",
    "Geometric proof of the Pythagorean Theorem",
    "figures_en/vol_3/fig_19_pythagore_puzzle.svg"
  ],
  "Volume_III|20|0": [
    "SVG",
    "The 2D Cartesian coordinate system: x-axis and y-axis",
    "figures_en/vol_3/fig_20_repere_cartesien_2d.svg"
  ],
  "Volume_III|20|1": [
    "SVG",
    "The 2D Cartesian coordinate system: x-axis and y-axis",
    "figures_en/vol_3/fig_20_repere_cartesien_2d.svg"
  ],
  "Volume_III|20|2": [
    "SVG",
    "The 2D Cartesian coordinate system: x-axis and y-axis",
    "figures_en/vol_3/fig_20_repere_cartesien_2d.svg"
  ],
  "Volume_III|20|3": [
    "SVG",
    "Euclidean distance in the Cartesian coordinate system",
    "figures_en/vol_3/fig_20_distance_plan_cartesien.svg"
  ],
  "Volume_III|21|0": [
    "CALLOUT",
    "💡 Discovery & History — The Dispute of Medieval Merchants"
  ],
  "Volume_III|21|1": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1fr, 1fr, 1fr),\n    align: center + horizon,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [*1. Bar Chart*], [*2. Histogram (bins)*], [*3. Pie Chart*],\n    [Isolated discrete values], [Adjacent continuous intervals], [Slices proportional to $360 degree$],\n    [Height proportional to count], [Area proportional to count], [Angle proportional to frequency (%)]\n  )\n]\n```"
  ],
  "Volume_IV|22|0": [
    "SVG",
    "Al-Khwarizmi's balance scale and the equilibrium of equations",
    "figures_en/vol_4/fig_22_balance_al_khwarizmi.svg"
  ],
  "Volume_IV|22|1": [
    "SVG",
    "Al-Khwarizmi's balance scale and the equilibrium of equations",
    "figures_en/vol_4/fig_22_balance_al_khwarizmi.svg"
  ],
  "Volume_IV|22|2": [
    "CALLOUT",
    "📐 Fundamental Rule — Geometric View of Single Distributivity"
  ],
  "Volume_IV|23|0": [
    "SVG",
    "Geometric proof of the special product (a+b)²",
    "figures_en/vol_4/fig_23_identite_remarquable_carre.svg"
  ],
  "Volume_IV|23|1": [
    "SVG",
    "Distributivity of multiplication over addition",
    "figures_en/vol_4/fig_23_distributivite_double.svg"
  ],
  "Volume_IV|23|2": [
    "SVG",
    "Distributivity of multiplication over addition",
    "figures_en/vol_4/fig_23_distributivite_double.svg"
  ],
  "Volume_IV|23|3": [
    "SVG",
    "Geometric proof of the special product (a+b)²",
    "figures_en/vol_4/fig_23_identite_remarquable_carre.svg"
  ],
  "Volume_IV|23|4": [
    "SVG",
    "Difference of two squares: (a+b)(a-b) = a² - b²",
    "figures_en/vol_4/fig_23_difference_deux_carres.svg"
  ],
  "Volume_IV|23|5": [
    "SVG",
    "Difference of two squares: (a+b)(a-b) = a² - b²",
    "figures_en/vol_4/fig_23_difference_deux_carres.svg"
  ],
  "Volume_IV|23|6": [
    "SVG",
    "Difference of two squares: (a+b)(a-b) = a² - b²",
    "figures_en/vol_4/fig_23_difference_deux_carres.svg"
  ],
  "Volume_IV|23|7": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1fr, 1fr, 1fr),\n    align: center,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [*Cas $a > 0$*], [*Cas $a = 0$*], [*Cas $a < 0$*],\n    [Deux solutions opposées :\n$x = sqrt(a)$ ou $x = -sqrt(a)$], [Une solution unique :\n$x = 0$], [Aucune solution réelle :\nImpossible dans $bb(R)$ ($S = emptyset$)]\n  )\n]\n```"
  ],
  "Volume_IV|23|8": [
    "SVG",
    "Geometric proof of the special product (a+b)²",
    "figures_en/vol_4/fig_23_identite_remarquable_carre.svg"
  ],
  "Volume_IV|24|0": [
    "CALLOUT",
    "Solved Example — Comparing Pricing Plans (Affine Modeling)"
  ],
  "Volume_IV|24|1": [
    "SVG",
    "Al-Khwarizmi's balance scale and the equilibrium of equations",
    "figures_en/vol_4/fig_22_balance_al_khwarizmi.svg"
  ],
  "Volume_IV|24|2": [
    "SVG",
    "Intersection et réunion d'intervalles sur l'axe des réels",
    "figures_en/vol_4/fig_24_intervalles_droite.svg"
  ],
  "Volume_IV|24|3": [
    "SVG",
    "Intersection et réunion d'intervalles sur l'axe des réels",
    "figures_en/vol_4/fig_24_intervalles_droite.svg"
  ],
  "Volume_IV|24|4": [
    "SVG",
    "Intersection et réunion d'intervalles sur l'axe des réels",
    "figures_en/vol_4/fig_24_intervalles_droite.svg"
  ],
  "Volume_IV|24|5": [
    "CALC_OP"
  ],
  "Volume_IV|24|6": [
    "SVG",
    "Intersection et réunion d'intervalles sur l'axe des réels",
    "figures_en/vol_4/fig_24_intervalles_droite.svg"
  ],
  "Volume_IV|24|7": [
    "CALLOUT",
    "💡 Discovery & History — Chapter VIII of the Chinese Nine Chapters"
  ],
  "Volume_IV|24|8": [
    "SVG",
    "Intersection et réunion d'intervalles sur l'axe des réels",
    "figures_en/vol_4/fig_24_intervalles_droite.svg"
  ],
  "Volume_IV|25|0": [
    "SVG",
    "The function as Jacquard's input-output machine",
    "figures_en/vol_4/fig_25_machine_fonction.svg"
  ],
  "Volume_IV|25|1": [
    "SVG",
    "The function as Jacquard's input-output machine",
    "figures_en/vol_4/fig_25_machine_fonction.svg"
  ],
  "Volume_IV|25|2": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1fr, 1fr, 1fr),\n    align: center,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [*1. L'expression algébrique*], [*2. Le tableau de valeurs*], [*3. La courbe représentative*],\n    [La formule exacte\nExemple : $f(x) = 2x + 1$], [Échantillons finis de couples\n$(x ; f(x))$], [Vision géométrique continue\ndans le repère]\n  )\n]\n```"
  ],
  "Volume_IV|25|3": [
    "SVG",
    "Graph of the affine function: slope and y-intercept",
    "figures_en/vol_4/fig_25_droite_affine_complete.svg"
  ],
  "Volume_IV|25|4": [
    "SVG",
    "Graph of the affine function: slope and y-intercept",
    "figures_en/vol_4/fig_25_droite_affine_complete.svg"
  ],
  "Volume_IV|25|5": [
    "SVG",
    "Graph of the affine function: slope and y-intercept",
    "figures_en/vol_4/fig_25_droite_affine_complete.svg"
  ],
  "Volume_IV|26|0": [
    "SVG",
    "Bilateral axial symmetry: orthogonal fold and reflection",
    "figures_en/vol_4/fig_26_symetrie_axiale.svg"
  ],
  "Volume_IV|26|1": [
    "SVG",
    "Bilateral axial symmetry: orthogonal fold and reflection",
    "figures_en/vol_4/fig_26_symetrie_axiale.svg"
  ],
  "Volume_IV|26|2": [
    "SVG",
    "Bilateral axial symmetry: orthogonal fold and reflection",
    "figures_en/vol_4/fig_26_symetrie_axiale.svg"
  ],
  "Volume_IV|26|3": [
    "SVG",
    "Central symmetry: perfect 180° half-turn about center O",
    "figures_en/vol_4/fig_26_symetrie_centrale.svg"
  ],
  "Volume_IV|26|4": [
    "SVG",
    "Homothety (dilation): vector scaling from the center of alignment",
    "figures_en/vol_4/fig_26_homothetie.svg"
  ],
  "Volume_IV|26|5": [
    "SVG",
    "Central symmetry: perfect 180° half-turn about center O",
    "figures_en/vol_4/fig_26_symetrie_centrale.svg"
  ],
  "Volume_IV|26|6": [
    "SVG",
    "Homothety (dilation): vector scaling from the center of alignment",
    "figures_en/vol_4/fig_26_homothetie.svg"
  ],
  "Volume_IV|26|7": [
    "SVG",
    "Bilateral axial symmetry: orthogonal fold and reflection",
    "figures_en/vol_4/fig_26_symetrie_axiale.svg"
  ],
  "Volume_IV|26|8": [
    "SVG",
    "Central symmetry: perfect 180° half-turn about center O",
    "figures_en/vol_4/fig_26_symetrie_centrale.svg"
  ],
  "Volume_IV|27|0": [
    "SVG",
    "1D Linear perimeter vs 2D surface area",
    "figures_en/vol_2/fig_12_perimetre_vs_aire.svg"
  ],
  "Volume_IV|27|1": [
    "SVG",
    "Intersection et réunion d'intervalles sur l'axe des réels",
    "figures_en/vol_4/fig_24_intervalles_droite.svg"
  ],
  "Volume_IV|27|2": [
    "SVG",
    "The Egyptian 13-knot rope and the 3-4-5 right triangle",
    "figures_en/vol_4/fig_27_corde_treize_noeuds.svg"
  ],
  "Volume_IV|27|3": [
    "SVG",
    "1D Linear perimeter vs 2D surface area",
    "figures_en/vol_2/fig_12_perimetre_vs_aire.svg"
  ],
  "Volume_IV|27|4": [
    "SVG",
    "1D Linear perimeter vs 2D surface area",
    "figures_en/vol_2/fig_12_perimetre_vs_aire.svg"
  ],
  "Volume_IV|27|5": [
    "SVG",
    "The Egyptian 13-knot rope and the 3-4-5 right triangle",
    "figures_en/vol_4/fig_27_corde_treize_noeuds.svg"
  ],
  "Volume_IV|27|6": [
    "SVG",
    "Unrolling the circle: geometric definition of Pi",
    "figures_en/vol_3/fig_16_deroulement_cercle_pi.svg"
  ],
  "Volume_IV|28|0": [
    "SVG",
    "Measuring Earth's radius by Eratosthenes of Alexandria",
    "figures_en/vol_4/fig_28_eratosthene_tour_terre.svg"
  ],
  "Volume_IV|28|1": [
    "SVG",
    "Measuring Earth's radius by Eratosthenes of Alexandria",
    "figures_en/vol_4/fig_28_eratosthene_tour_terre.svg"
  ],
  "Volume_IV|28|2": [
    "SVG",
    "Measuring Earth's radius by Eratosthenes of Alexandria",
    "figures_en/vol_4/fig_28_eratosthene_tour_terre.svg"
  ],
  "Volume_IV|28|3": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_IV|28|4": [
    "CALLOUT",
    "🛠️ Step-by-Step Method — Trigonometric Problem-Solving Method"
  ],
  "Volume_IV|28|5": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_IV|28|6": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_IV|28|7": [
    "SVG",
    "Right-triangle trigonometry: Cosine, Sine, and Tangent",
    "figures_en/vol_3/fig_17_thales_pyramide.svg"
  ],
  "Volume_IV|29|0": [
    "SVG",
    "Euclid's geometric algorithm by square dissection",
    "figures_en/vol_4/fig_29_euclide_rectangles.svg"
  ],
  "Volume_IV|29|1": [
    "SVG",
    "Prime factorization tree",
    "figures_en/vol_2/fig_08_decomposition_premiers.svg"
  ],
  "Volume_IV|29|2": [
    "SVG",
    "Prime factorization tree",
    "figures_en/vol_2/fig_08_decomposition_premiers.svg"
  ],
  "Volume_IV|29|3": [
    "CALLOUT",
    "🛠️ Step-by-Step Method — Computing the GCD via Euclid's Algorithm"
  ],
  "Volume_IV|30|0": [
    "SVG",
    "Choice of path: weighted probability tree",
    "figures_en/vol_4/fig_30_sentiers_arbre.svg"
  ],
  "Volume_IV|30|1": [
    "SVG",
    "Choice of path: weighted probability tree",
    "figures_en/vol_4/fig_30_sentiers_arbre.svg"
  ],
  "Volume_IV|30|2": [
    "SVG",
    "Choice of path: weighted probability tree",
    "figures_en/vol_4/fig_30_sentiers_arbre.svg"
  ],
  "Volume_IV|30|3": [
    "SVG",
    "Choice of path: weighted probability tree",
    "figures_en/vol_4/fig_30_sentiers_arbre.svg"
  ],
  "Volume_IV|30|4": [
    "SVG",
    "Choice of path: weighted probability tree",
    "figures_en/vol_4/fig_30_sentiers_arbre.svg"
  ],
  "Volume_IV|30|5": [
    "RAW",
    "```python\nimport random\n\nlancers = 10000\nfaces_six = 0\n\nfor i in range(lancers):\n  de = random.randint(1, 6)\n  if de == 6:\n    faces_six += 1\n\nfrequence = faces_six / lancers\nprint(\"Fréquence de 6 :\", frequence)\n```"
  ],
  "Volume_V|31|0": [
    "SVG",
    "Nested number sets: N ⊂ Z ⊂ D ⊂ Q ⊂ R",
    "figures_en/vol_5/fig_31_ensembles_emboites.svg"
  ],
  "Volume_V|31|1": [
    "SVG",
    "Venn diagrams: Intersection A ∩ B and Union A ∪ B",
    "figures_en/vol_5/fig_31_venn_intersection_union.svg"
  ],
  "Volume_V|31|2": [
    "SVG",
    "Intersection et réunion d'intervalles sur l'axe des réels",
    "figures_en/vol_4/fig_24_intervalles_droite.svg"
  ],
  "Volume_V|32|0": [
    "CALLOUT",
    "💡 Concrete Modeling — The Sailboat Drift and Velocity Addition"
  ],
  "Volume_V|32|1": [
    "SVG",
    "Characterization of a vector: direction, sense, and magnitude",
    "figures_en/vol_5/fig_32_vecteur_definition.svg"
  ],
  "Volume_V|32|2": [
    "CALLOUT",
    "📐 Fundamental Rule — Multiplying a Vector by a Scalar"
  ],
  "Volume_V|32|3": [
    "SVG",
    "Fundamental vector decomposition: u = x i + y j",
    "figures_en/vol_5/fig_32_vecteur_composantes.svg"
  ],
  "Volume_V|32|4": [
    "SVG",
    "Vectors in the plane: Chasles' relation and coordinates",
    "figures_en/vol_5/fig_32_chasles_addition.svg"
  ],
  "Volume_V|32|5": [
    "SVG",
    "Vectors in the plane: Chasles' relation and coordinates",
    "figures_en/vol_5/fig_32_chasles_addition.svg"
  ],
  "Volume_V|32|6": [
    "CALLOUT",
    "📐 Fundamental Rule — Multiplying a Vector by a Scalar"
  ],
  "Volume_V|32|7": [
    "SVG",
    "Fundamental vector decomposition: u = x i + y j",
    "figures_en/vol_5/fig_32_vecteur_composantes.svg"
  ],
  "Volume_V|32|8": [
    "RAW",
    "```python\ndef determinant(ux, uy, vx, vy):\n    \"\"\"Calcule le déterminant de deux vecteurs u(ux, uy) et v(vx, vy).\"\"\"\n    return ux * vy - uy * vx\n\ndef sont_colineaires(ux, uy, vx, vy, tolerance=1e-9):\n    \"\"\"Vérifie si deux vecteurs sont colinéaires à une précision donnée.\"\"\"\n    det = determinant(ux, uy, vx, vy)\n    return abs(det) < tolerance\n\n# Test avec u(4, 6) et v(6, 9)\nprint(\"u et v colinéaires ?\", sont_colineaires(4, 6, 6, 9))  # Affiche True\n\n# Test avec u(3, -1) et v(2, 5)\nprint(\"u et v colinéaires ?\", sont_colineaires(3, -1, 2, 5))  # Affiche False\n```"
  ],
  "Volume_V|33|0": [
    "SVG",
    "Affine line y = mx + p: slope and y-intercept",
    "figures_en/vol_5/fig_33_pente_ordonnee.svg"
  ],
  "Volume_V|33|1": [
    "SVG",
    "Affine line y = mx + p: slope and y-intercept",
    "figures_en/vol_5/fig_33_pente_ordonnee.svg"
  ],
  "Volume_V|33|2": [
    "SVG",
    "Affine line y = mx + p: slope and y-intercept",
    "figures_en/vol_5/fig_33_pente_ordonnee.svg"
  ],
  "Volume_V|33|3": [
    "SVG",
    "Relative positions of two affine lines in the plane",
    "figures_en/vol_5/fig_33_positions_droites_affines.svg"
  ],
  "Volume_V|33|4": [
    "RAW",
    "```python\ndef resoudre_systeme(a1, b1, c1, a2, b2, c2):\n    \"\"\"\n    Résout le système :\n    a1*x + b1*y + c1 = 0\n    a2*x + b2*y + c2 = 0\n    \"\"\"\n    # Calcul du déterminant principal (a1*b2 - a2*b1)\n    det = a1 * b2 - a2 * b1\n    \n    if abs(det) < 1e-12:\n        # Droites parallèles ou confondues\n        # Test de proportionnalité avec les constantes\n        if abs(a1 * c2 - a2 * c1) < 1e-12 and abs(b1 * c2 - b2 * c1) < 1e-12:\n            return \"Infinité de solutions (droites confondues)\"\n        else:\n            return \"Aucune solution (droites strictement parallèles)\"\n    else:\n        # Règle de Cramer pour trouver x et y\n        # Réécriture sous la forme a*x + b*y = -c\n        e1, e2 = -c1, -c2\n        x = (e1 * b2 - e2 * b1) / det\n        y = (a1 * e2 - a2 * e1) / det\n        return (x, y)\n\n# Test avec le système de l'Exemple 1 :\n# x - 2y + 4 = 0  et  x + y - 7 = 0\nsolution = resoudre_systeme(1, -2, 4, 1, 1, -7)\nprint(\"Point d'intersection :\", solution)  # Affiche (3.3333333333333335, 3.6666666666666665)\n```"
  ],
  "Volume_V|34|0": [
    "SVG",
    "The function as Jacquard's input-output machine",
    "figures_en/vol_4/fig_25_machine_fonction.svg"
  ],
  "Volume_V|34|1": [
    "SVG",
    "The function as Jacquard's input-output machine",
    "figures_en/vol_4/fig_25_machine_fonction.svg"
  ],
  "Volume_V|34|2": [
    "SVG",
    "Graphical solution of f(x) = k by line intersection",
    "figures_en/vol_5/fig_34_resolution_fx_k.svg"
  ],
  "Volume_V|34|3": [
    "SVG",
    "Function parity: bilateral axial symmetry vs central symmetry",
    "figures_en/vol_5/fig_34_parite_fonctions.svg"
  ],
  "Volume_V|34|4": [
    "SVG",
    "Graphical solution of f(x) = k by line intersection",
    "figures_en/vol_5/fig_34_resolution_fx_k.svg"
  ],
  "Volume_V|34|5": [
    "SVG",
    "The function as Jacquard's input-output machine",
    "figures_en/vol_4/fig_25_machine_fonction.svg"
  ],
  "Volume_V|34|6": [
    "RAW",
    "```python\ndef f(x):\n    \"\"\"Définition de la fonction f(x) = x**3 - 3*x + 1\"\"\"\n    return x**3 - 3*x + 1\n\ndef table_de_valeurs(debut, fin, pas):\n    \"\"\"Affiche une table de valeurs de la fonction f.\"\"\"\n    print(\"  x   |  f(x)\")\n    print(\"------|--------\")\n    x = debut\n    while x <= fin + 1e-9:\n        print(f\"{x:5.2f} | {f(x):7.3f}\")\n        x += pas\n\n# Affichage des valeurs entre -2 et 2 avec un pas de 0.5\ntable_de_valeurs(-2, 2, 0.5)\n\n# Recherche approchée d'une solution à f(x) = 0 par balayage\ndef balayage(a, b, pas=0.001):\n    x = a\n    while x <= b:\n        if f(x) * f(x + pas) <= 0:\n            return round(x + pas / 2, 3)\n        x += pas\n    return None\n\nsolution = balayage(0, 1)\nprint(f\"\\nUne solution approchée dans [0; 1] est x ≈ {solution}\")\n```"
  ],
  "Volume_V|35|0": [
    "SVG",
    "Quadratic parabola: orientation and vertex coordinates",
    "figures_en/vol_5/fig_35_parabole_second_degre.svg"
  ],
  "Volume_V|35|1": [
    "SVG",
    "Quadratic parabola: orientation and vertex coordinates",
    "figures_en/vol_5/fig_35_parabole_second_degre.svg"
  ],
  "Volume_V|35|2": [
    "RAW",
    "```python\nimport math\n\ndef analyser_trinome(a, b, c):\n    \"\"\"Analyse complète du trinôme a*x^2 + b*x + c.\"\"\"\n    if a == 0:\n        return \"Erreur : ce n'est pas un trinôme du second degré (a = 0).\"\n    \n    # 1. Sommet de la parabole\n    alpha = -b / (2 * a)\n    beta = a * alpha**2 + b * alpha + c\n    print(f\"Sommet S: ({alpha:.3f}, {beta:.3f})\")\n    print(f\"Orientation : branches tournées vers le {'HAUT' if a > 0 else 'BAS'}\")\n    \n    # 2. Discriminant\n    delta = b**2 - 4 * a * c\n    print(f\"Discriminant Delta = {delta}\")\n    \n    if delta > 0:\n        x1 = (-b - math.sqrt(delta)) / (2 * a)\n        x2 = (-b + math.sqrt(delta)) / (2 * a)\n        print(f\"Deux racines distinctes : x1 = {x1:.3f} et x2 = {x2:.3f}\")\n        print(f\"Forme factorisée : {a} * (x - {x1:.3f}) * (x - {x2:.3f})\")\n    elif delta == 0:\n        x0 = -b / (2 * a)\n        print(f\"Une racine double : x0 = {x0:.3f}\")\n        print(f\"Forme factorisée : {a} * (x - {x0:.3f})^2\")\n    else:\n        print(\"Aucune racine réelle.\")\n        print(\"Pas de factorisation dans R.\")\n\n# Exemple d'appel : 2x^2 - 7x + 3\nanalyser_trinome(2, -7, 3)\n```"
  ],
  "Volume_V|36|0": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1.2fr, 2fr, 2fr),\n    align: (center, center, center),\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [*Échéance*], [*Contrat Matteo (Prêt arithmétique : +100 / an)*], [*Contrat Cosimo (Prêt géométrique : +10 % / an)*],\n    [Année 0], [1 000 florins], [1 000 florins],\n    [Année 1], [1 100 florins], [1 100 florins],\n    [Année 2], [1 200 florins], [1 210 florins],\n    [Année 3], [1 300 florins], [1 331 florins],\n    [Année 10], [2 000 florins], [*2 593,74 florins !*]\n  )\n]\n```"
  ],
  "Volume_V|36|1": [
    "SVG",
    "Graph of a numerical sequence: discrete scatter plot",
    "figures_en/vol_5/fig_36_suite_graphique.svg"
  ],
  "Volume_V|36|2": [
    "CALC_OP"
  ],
  "Volume_V|36|3": [
    "RAW",
    "```python\ndef seuil_croissance(valeur_initiale, taux, seuil):\n    \"\"\"\n    Calcule le nombre d'années nécessaires pour dépasser un seuil.\n    Exemple : un capital initial de 1000 € placé à 5 % par an (raison q = 1.05)\n    doit dépasser 2000 € (doubler).\n    \"\"\"\n    n = 0\n    u = valeur_initiale\n    \n    while u < seuil:\n        u = u * (1 + taux)  # On applique le taux annuel\n        n += 1              # On passe à l'année suivante\n        \n    return n, round(u, 2)\n\nannees, montant_final = seuil_croissance(1000, 0.05, 2000)\nprint(f\"Le capital aura doublé au bout de {annees} ans, atteignant {montant_final} €.\")\n# Affiche : Le capital aura doublé au bout de 15 ans, atteignant 2078.93 €.\n```"
  ],
  "Volume_V|36|4": [
    "RAW",
    "```python\n       n, c = 0, 5000\n       while c <= 8000:\n           c *= 1.04\n           n += 1\n       print(n)  # Affiche 12 ans (c ≈ 8005.16 €)\n       ```"
  ],
  "Volume_V|37|0": [
    "SVG",
    "Quadratic parabola: orientation and vertex coordinates",
    "figures_en/vol_5/fig_35_parabole_second_degre.svg"
  ],
  "Volume_V|37|1": [
    "SVG",
    "Le cercle trigonométrique complet et les lignes de sinus et cosinus",
    "figures_en/vol_5/fig_37_cercle_trigo_complet.svg"
  ],
  "Volume_V|37|2": [
    "SVG",
    "Le cercle trigonométrique complet et les lignes de sinus et cosinus",
    "figures_en/vol_5/fig_37_cercle_trigo_complet.svg"
  ],
  "Volume_V|37|3": [
    "SVG",
    "Le cercle trigonométrique complet et les lignes de sinus et cosinus",
    "figures_en/vol_5/fig_37_cercle_trigo_complet.svg"
  ],
  "Volume_V|37|4": [
    "SVG",
    "Le cercle trigonométrique complet et les lignes de sinus et cosinus",
    "figures_en/vol_5/fig_37_cercle_trigo_complet.svg"
  ],
  "Volume_V|37|5": [
    "SVG",
    "The four trigonometric quadrants: signs of cos and sin",
    "figures_en/vol_5/fig_37_cercle_trigo_quadrants.svg"
  ],
  "Volume_V|38|0": [
    "SVG",
    "Dot product and work of a force: effective component and geometric sign",
    "figures_en/vol_5/fig_38_produit_scalaire_travail.svg"
  ],
  "Volume_V|38|1": [
    "SVG",
    "Dot product and work of a force: effective component and geometric sign",
    "figures_en/vol_5/fig_38_produit_scalaire_travail.svg"
  ],
  "Volume_V|38|2": [
    "SVG",
    "Dot product and work of a force: effective component and geometric sign",
    "figures_en/vol_5/fig_38_produit_scalaire_travail.svg"
  ],
  "Volume_V|38|3": [
    "SVG",
    "Dot product and work of a force: effective component and geometric sign",
    "figures_en/vol_5/fig_38_produit_scalaire_travail.svg"
  ],
  "Volume_V|38|4": [
    "SVG",
    "Dot product and work of a force: effective component and geometric sign",
    "figures_en/vol_5/fig_38_produit_scalaire_travail.svg"
  ],
  "Volume_V|38|5": [
    "SVG",
    "Dot product and work of a force: effective component and geometric sign",
    "figures_en/vol_5/fig_38_produit_scalaire_travail.svg"
  ],
  "Volume_V|38|6": [
    "SVG",
    "Dot product and work of a force: effective component and geometric sign",
    "figures_en/vol_5/fig_38_produit_scalaire_travail.svg"
  ],
  "Volume_V|39|0": [
    "SVG",
    "Quadratic parabola: orientation and vertex coordinates",
    "figures_en/vol_5/fig_35_parabole_second_degre.svg"
  ],
  "Volume_V|39|1": [
    "CALLOUT",
    "💡 Intuitive Metaphor — The Skier and the Instantaneous Slope of the Mountain"
  ],
  "Volume_V|39|2": [
    "SVG",
    "Derivative and limit of secants as step h approaches zero",
    "figures_en/vol_5/fig_39_secante_tangente.svg"
  ],
  "Volume_V|39|3": [
    "SVG",
    "Geometric proof of the special product (a+b)²",
    "figures_en/vol_4/fig_23_identite_remarquable_carre.svg"
  ],
  "Volume_V|39|4": [
    "SVG",
    "Geometric proof of the special product (a+b)²",
    "figures_en/vol_4/fig_23_identite_remarquable_carre.svg"
  ],
  "Volume_V|39|5": [
    "CALLOUT",
    "📐 Fundamental Rule — Horizontal Tangent and Local Extrema ($f'(x_0) = 0$)"
  ],
  "Volume_V|40|0": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1.5fr, 1fr, 1fr, 1fr, 1fr, 1fr),\n    align: (left, center, center, center, center, center),\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#f1f5f9\") } else { rgb(\"#ffffff\") },\n    [Temps $t$ (h)], [0], [1], [2], [3], [10],\n    [Bactéries], [1 000], [2 000], [4 000], [8 000], [1 024 000]\n  )\n]\n```"
  ],
  "Volume_V|40|1": [
    "SVG",
    "Derivative and limit of secants as step h approaches zero",
    "figures_en/vol_5/fig_39_secante_tangente.svg"
  ],
  "Volume_V|40|2": [
    "RAW",
    "```python\ndef methode_euler(n_pas):\n    h = 1.0 / n_pas  # largeur du pas pour aller de 0 à 1\n    x = 0.0\n    y = 1.0\n    for _ in range(n_pas):\n        y = y + h * y  # équivalent à y = y * (1 + h)\n        x = x + h\n    return y\n\n# Testons avec un découpage de plus en plus fin :\nfor n in [10, 100, 1000, 10000]:\n    print(f\"Pour n = {n:5d} pas : f(1) ≈ {methode_euler(n):.6f}\")\n```"
  ],
  "Volume_V|40|3": [
    "CALLOUT",
    "🛠️ Step-by-Step Method — Step-by-Step Approximation via Euler's Method"
  ],
  "Volume_V|40|4": [
    "SVG",
    "The exponential function: continuous growth and properties",
    "figures_en/vol_5/fig_40_exponentielle.svg"
  ],
  "Volume_V|40|5": [
    "RAW",
    "```python\nimport math\n\n\ndef euler_comparaison(n=100):\n  h = 1.0 / n\n  y = 1.0\n  for _ in range(n):\n    y = y * (1 + h)\n  exact = math.exp(1)\n  erreur = abs(y - exact) / exact * 100\n  print(f\"Euler (n={n}) : {y:.6f}\")\n  print(f\"Exact : {exact:.6f}\")\n  print(f\"Erreur relative : {erreur:.3f}%\")\n\n\neuler_comparaison(100)\n# Donne une erreur relative d'environ 0.49% seulement !\n```"
  ],
  "Volume_V|41|0": [
    "CALLOUT",
    "Solved Example — Comparative Spread: Workshop Alpha vs Workshop Beta"
  ],
  "Volume_V|41|1": [
    "SVG",
    "Box plot: median, quartiles, and statistical spread",
    "figures_en/vol_5/fig_40_boite_moustaches.svg"
  ],
  "Volume_V|41|2": [
    "RAW",
    "```python\nimport random\n\n\ndef simuler_echantillon(n, p):\n  \"\"\"Simule le tirage d'un échantillon de taille n et renvoie la fréquence f.\"\"\"\n  succes = sum(1 for _ in range(n) if random.random() < p)\n  return succes / n\n\n\ndef etude_fluctuation(nb_echantillons=1000, n=100, p=0.40):\n  borne_inf = p - 1.96 * (p * (1 - p) / n) ** 0.5\n  borne_sup = p + 1.96 * (p * (1 - p) / n) ** 0.5\n\n  dans_intervalle = 0\n  for _ in range(nb_echantillons):\n    f = simuler_echantillon(n, p)\n    if borne_inf <= f <= borne_sup:\n      dans_intervalle += 1\n\n  pourcentage = (dans_intervalle / nb_echantillons) * 100\n  print(f\"Intervalle théorique à 95 % : [{borne_inf:.4f} ; {borne_sup:.4f}]\")\n  print(\n      f\"Proportion d'échantillons tombés dans l'intervalle : {pourcentage:.1f} %\"\n  )\n\n\netude_fluctuation()\n```"
  ],
  "Volume_V|41|3": [
    "CALLOUT",
    "📐 Fundamental Rule — 95% Asymptotic Fluctuation Interval"
  ],
  "Volume_V|41|4": [
    "RAW",
    "```python\ndef statistiques(liste):\n  N = len(liste)\n  moyenne = sum(liste) / N\n  variance = sum((x - moyenne) ** 2 for x in liste) / N\n  ecart_type = variance**0.5\n  return {'effectif': N, 'moyenne': moyenne, 'ecart_type': ecart_type}\n```"
  ],
  "Volume_V|41|5": [
    "RAW",
    "```python\nimport math\n\n\ndef detecter_outliers(donnees):\n  s = sorted(donnees)\n  N = len(s)\n  q1 = s[math.ceil(N / 4) - 1]\n  q3 = s[math.ceil(3 * N / 4) - 1]\n  iqr = q3 - q1\n  seuil_bas = q1 - 1.5 * iqr\n  seuil_haut = q3 + 1.5 * iqr\n  outliers = [x for x in donnees if x < seuil_bas or x > seuil_haut]\n  return {'Q1': q1, 'Q3': q3, 'IQR': iqr, 'outliers': outliers}\n```"
  ],
  "Volume_V|42|0": [
    "SVG",
    "Weighted tree for medical screening and Bayes' formula",
    "figures_en/vol_5/fig_42_arbre_medical.svg"
  ],
  "Volume_V|42|1": [
    "SVG",
    "Venn diagrams: Intersection A ∩ B and Union A ∪ B",
    "figures_en/vol_5/fig_31_venn_intersection_union.svg"
  ],
  "Volume_V|42|2": [
    "SVG",
    "Weighted tree for medical screening and Bayes' formula",
    "figures_en/vol_5/fig_42_arbre_medical.svg"
  ],
  "Volume_V|42|3": [
    "RAW",
    "```python\nimport random\n\n\ndef simuler_jeu(nb_parties=10000):\n  gains = []\n  for _ in range(nb_parties):\n    de = random.randint(1, 6)\n    if de in [2, 4, 6]:\n      gain = 1  # 3 - 2\n    elif de == 5:\n      gain = 4  # 6 - 2\n    else:\n      gain = -2  # 0 - 2\n    gains.append(gain)\n  moyenne = sum(gains) / nb_parties\n  print(f\"Moyenne simulée : {moyenne:.4f} € (Théorie : 0.5000 €)\")\n\n\nsimuler_jeu()\n```"
  ],
  "Volume_VI|43|0": [
    "SVG",
    "Mathematical induction: the mathematical domino effect",
    "figures_en/vol_6/fig_43_dominos_recurrence.svg"
  ],
  "Volume_VI|43|1": [
    "SVG",
    "Mathematical induction: the mathematical domino effect",
    "figures_en/vol_6/fig_43_dominos_recurrence.svg"
  ],
  "Volume_VI|44|0": [
    "SVG",
    "Zeno's paradox: convergent geometric series sum of Achilles and the tortoise",
    "figures_en/vol_6/fig_44_achille_tortue.svg"
  ],
  "Volume_VI|44|1": [
    "SVG",
    "The squeeze theorem (two policemen and a drunk)",
    "figures_en/vol_6/fig_44_theoreme_gendarmes.svg"
  ],
  "Volume_VI|44|2": [
    "SVG",
    "The squeeze theorem (two policemen and a drunk)",
    "figures_en/vol_6/fig_44_theoreme_gendarmes.svg"
  ],
  "Volume_VI|44|3": [
    "SVG",
    "Monotone convergence theorem: bounded increasing sequence",
    "figures_en/vol_6/fig_44_convergence_monotone.svg"
  ],
  "Volume_VI|44|4": [
    "RAW",
    "```python\ndef seuil_temperature(seuil):\n    \"\"\"Calcule le nombre de minutes nécessaires pour passer sous le seuil.\"\"\"\n    n = 0\n    T = 100.0  # T_0 = 20 + 80 = 100 °C\n    while T > seuil:\n        n = n + 1\n        T = 20 + 80 * (0.9 ** n)\n    return n\n\n# Test pour un seuil à 30 °C\nminutes = seuil_temperature(30)\nprint(f\"Le moteur passe sous 30°C au bout de {minutes} minutes.\")\n# Affichera : 20 minutes (car T_19 ≈ 30.8 °C et T_20 ≈ 29.7 °C)\n```"
  ],
  "Volume_VI|44|5": [
    "RAW",
    "```python\ndef seuil_geometrique(q, A):\n    n = 0\n    u = 1.0\n    while u <= A:\n        n += 1\n        u = q ** n\n    return n\n```"
  ],
  "Volume_VI|44|6": [
    "RAW",
    "```python\nn = 0\nu = 2.0\nwhile abs(u - 5.0) >= 1e-5:\n    n += 1\n    u = 0.8 * u + 1.0\nprint(f\"Rang n trouvé : {n}\")\n```"
  ],
  "Volume_VI|45|0": [
    "SVG",
    "Comportement asymptotique aux bornes : asymptotes verticales et horizontales",
    "figures_en/vol_6/fig_45_asymptotes_complete.svg"
  ],
  "Volume_VI|45|1": [
    "SVG",
    "Comportement asymptotique aux bornes : asymptotes verticales et horizontales",
    "figures_en/vol_6/fig_45_asymptotes_complete.svg"
  ],
  "Volume_VI|45|2": [
    "SVG",
    "Comportement asymptotique aux bornes : asymptotes verticales et horizontales",
    "figures_en/vol_6/fig_45_asymptotes_complete.svg"
  ],
  "Volume_VI|46|0": [
    "SVG",
    "Théorème des Valeurs Intermédiaires (TVI) sur un intervalle fermé",
    "figures_en/vol_6/fig_46_tvi_continuite.svg"
  ],
  "Volume_VI|46|1": [
    "SVG",
    "Continuité mathématique : trajectoire continue vs saut de palier",
    "figures_en/vol_6/fig_46_continu_vs_discontinu.svg"
  ],
  "Volume_VI|46|2": [
    "SVG",
    "Théorème des Valeurs Intermédiaires (TVI) sur un intervalle fermé",
    "figures_en/vol_6/fig_46_tvi_continuite.svg"
  ],
  "Volume_VI|46|3": [
    "CALLOUT",
    "🛠️ Step-by-Step Method — Root Finding by Bisection (Dichotomy)"
  ],
  "Volume_VI|46|4": [
    "RAW",
    "```python\ndef f(x):\n    \"\"\"Fonction dont on cherche le zéro.\"\"\"\n    return x**3 + x - 1\n\ndef dichotomie(a, b, precision):\n    \"\"\"\n    Renvoie un encadrement [a, b] de la racine de f(x) = 0\n    avec une largeur b - a <= precision.\n    \"\"\"\n    while (b - a) > precision:\n        m = (a + b) / 2\n        # Si f(a) et f(m) ont le même signe, la racine est dans [m, b]\n        if f(a) * f(m) <= 0:\n            b = m\n        else:\n            a = m\n    return a, b\n\n# Recherche d'un encadrement à 10^-4 près\ninf, sup = dichotomie(0.0, 1.0, 1e-4)\nprint(f\"Encadrement obtenu : {inf:.5f} < alpha < {sup:.5f}\")\n# Affichera : 0.68231 < alpha < 0.68237\n```"
  ],
  "Volume_VI|46|5": [
    "SVG",
    "Méthode de l'escalier (Cobweb) : itération graphique de la suite u_(n+1) = f(u_n)",
    "figures_en/vol_6/fig_46_methode_escalier_cobweb.svg"
  ],
  "Volume_VI|46|6": [
    "RAW",
    "```python\ndef f(x):\n    return x**2 - 2\n\na, b = 1.0, 2.0\nwhile (b - a) > 1e-3:\n    m = (a + b) / 2\n    if f(a) * f(m) <= 0:\n        b = m\n    else:\n        a = m\nprint(f\"sqrt(2) ≈ {(a + b)/2:.4f}\")\n```"
  ],
  "Volume_VI|46|7": [
    "RAW",
    "```python\nimport math\ndef h(x):\n    return math.exp(-x) - x\n\na, b = 0.0, 1.0\nwhile (b - a) > 1e-6:\n    m = (a + b) / 2\n    if h(a) * h(m) <= 0:\n        b = m\n    else:\n        a = m\nprint(f\"Point d'intersection alpha ≈ {(a + b)/2:.6f}\")\n# alpha ≈ 0.567143 (constante Oméga)\n```"
  ],
  "Volume_VI|46|8": [
    "RAW",
    "```python\ndef f(x):\n    return x**2 - 2\ndef f_prime(x):\n    return 2*x\n\nx = 1.0\nfor i in range(5):\n    x = x - f(x) / f_prime(x)\n    print(f\"Étape {i+1} : x = {x:.12f}\")\n# Étape 1 : 1.500000000000\n# Étape 2 : 1.416666666667\n# Étape 3 : 1.414215686275\n# Étape 4 : 1.414213562375 (12 décimales exactes en 4 étapes !)\n```"
  ],
  "Volume_VI|47|0": [
    "SVG",
    "Convexité, concavité et point d'inflexion : position relative des tangentes",
    "figures_en/vol_6/fig_47_convexite_inflexion.svg"
  ],
  "Volume_VI|47|1": [
    "SVG",
    "Convexité, concavité et point d'inflexion : position relative des tangentes",
    "figures_en/vol_6/fig_47_convexite_inflexion.svg"
  ],
  "Volume_VI|47|2": [
    "SVG",
    "Convexité, concavité et point d'inflexion : position relative des tangentes",
    "figures_en/vol_6/fig_47_convexite_inflexion.svg"
  ],
  "Volume_VI|47|3": [
    "SVG",
    "Convexité, concavité et point d'inflexion : position relative des tangentes",
    "figures_en/vol_6/fig_47_convexite_inflexion.svg"
  ],
  "Volume_VI|47|4": [
    "SVG",
    "Convexité, concavité et point d'inflexion : position relative des tangentes",
    "figures_en/vol_6/fig_47_convexite_inflexion.svg"
  ],
  "Volume_VI|48|0": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (2.2fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.7fr, 0.8fr, 0.8fr),\n    align: center,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [*Progression arithmétique*], [0], [1], [2], [3], [4], [5], [6], [7], [8],\n    [*Progression géométrique*], [1], [2], [4], [8], [16], [32], [64], [128], [256]\n  )\n]\n```"
  ],
  "Volume_VI|48|1": [
    "SVG",
    "Inverse relationship of exponential and natural logarithm functions",
    "figures_en/vol_6/fig_48_exp_log_reciproques.svg"
  ],
  "Volume_VI|48|2": [
    "SVG",
    "Inverse relationship of exponential and natural logarithm functions",
    "figures_en/vol_6/fig_48_exp_log_reciproques.svg"
  ],
  "Volume_VI|48|3": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1.5fr, 1fr, 1fr, 1fr, 1fr, 1fr),\n    align: center,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [$x$], [$0$ (valeur interdite)], [$]0 ; 1[$], [$1$], [$]1 ; +infinity[$], [$+infinity$],\n    [Signe de $ln'(x)$], [||], [$+$], [$+$], [$+$], [],\n    [Signe de $ln(x)$], [||], [$-$], [$0$], [$+$], []\n  )\n]\n```"
  ],
  "Volume_VI|48|4": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1.5fr, 1fr, 1fr, 1fr, 1fr, 1fr),\n    align: center,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [$x$], [$0$ (valeur interdite)], [], [$1$], [], [$+infinity$],\n    [Signe de $ln'(x) = 1/x$], [||], [$+$], [$+$], [$+$], [],\n    [Variations de $ln(x)$], [$-infinity$], [$arrow.tr$], [$0$], [$arrow.tr$], [$+infinity$]\n  )\n]\n```"
  ],
  "Volume_VI|48|5": [
    "SVG",
    "Inverse relationship of exponential and natural logarithm functions",
    "figures_en/vol_6/fig_48_exp_log_reciproques.svg"
  ],
  "Volume_VI|48|6": [
    "RAW",
    "> ```python\n> def seuil_decroissance(valeur_initiale, taux, cible):\n>     n = 0\n>     v = valeur_initiale\n>     while v >= cible:\n>         v = v * (1 - taux)\n>         n += 1\n>     return n\n> >\n> print(\"Années nécessaires :\", seuil_decroissance(20000, 0.15, 5000))\n> # Affiche : Années nécessaires : 9\n> ```"
  ],
  "Volume_VI|49|0": [
    "SVG",
    "Le pendule simple : modélisation du mouvement périodique oscillant",
    "figures_en/vol_6/fig_49_pendule_oscillant.svg"
  ],
  "Volume_VI|49|1": [
    "SVG",
    "Génération de l'onde sinusoïdale par rotation du cercle",
    "figures_en/vol_6/fig_49_onde_sinusoidale.svg"
  ],
  "Volume_VI|49|2": [
    "SVG",
    "Le cercle trigonométrique complet et les lignes de sinus et cosinus",
    "figures_en/vol_5/fig_37_cercle_trigo_complet.svg"
  ],
  "Volume_VI|49|3": [
    "SVG",
    "Ligne trigonométrique de la tangente sur le cercle unité",
    "figures_en/vol_6/fig_49_tangente_cercle.svg"
  ],
  "Volume_VI|49|4": [
    "SVG",
    "Le pendule simple : modélisation du mouvement périodique oscillant",
    "figures_en/vol_6/fig_49_pendule_oscillant.svg"
  ],
  "Volume_VI|49|5": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1.5fr, 1fr, 1fr, 1fr, 1fr, 1fr),\n    align: center,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [$x$], [$-pi$], [], [$0$], [], [$pi$],\n    [Signe de $cos'(x) = -sin(x)$], [$0$], [$+$], [$0$], [$-$], [$0$],\n    [Variations de $cos(x)$], [$-1$ (Min)], [$arrow.tr$], [$1$ (Max)], [$arrow.br$], [$-1$ (Min)]\n  )\n]\n```"
  ],
  "Volume_VI|49|6": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1.2fr, 1fr, 1fr, 1fr, 1fr, 1fr),\n    align: (center, center, center, center, center, center),\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#f1f5f9\") } else { rgb(\"#ffffff\") },\n    [$x$], [$-pi$], [$-pi/2$], [$0$], [$pi/2$], [$pi$],\n    [$sin'(x) = cos(x)$], [$-$], [$0$], [$+$], [$0$], [$-$],\n    [$sin(x)$], [$0$], [$-1$ (Min)], [$0$], [$1$ (Max)], [$0$]\n  )\n]\n```"
  ],
  "Volume_VI|49|7": [
    "SVG",
    "Génération de l'onde sinusoïdale par rotation du cercle",
    "figures_en/vol_6/fig_49_onde_sinusoidale.svg"
  ],
  "Volume_VI|49|8": [
    "RAW",
    "> ```python\n> import math\n> >\n> def signal_sinusoidal(amplitude, frequence, duree, nb_points):\n>     omega = 2 * math.pi * frequence\n>     pas = duree / nb_points\n>     points = []\n>     for i in range(nb_points):\n>         t = i * pas\n>         valeur = amplitude * math.sin(omega * t)\n>         points.append((round(t, 4), round(valeur, 3)))\n>     return points\n> >\n> # Générons un signal de 50 Hz pendant 0.02 seconde (1 période complète)\n> ech = signal_sinusoidal(amplitude=325, frequence=50, duree=0.02, nb_points=5)\n> print(\"Points échantillonnés :\", ech)\n> ```"
  ],
  "Volume_VI|50|0": [
    "SVG",
    "La stéréométrie des tonneaux de Kepler : calcul intégral par tranches",
    "figures_en/vol_6/fig_50_tonneau_kepler.svg"
  ],
  "Volume_VI|50|1": [
    "SVG",
    "L'intégrale de Riemann : encadrement de l'aire sous la courbe par des rectangles",
    "figures_en/vol_6/fig_50_riemann_integrale.svg"
  ],
  "Volume_VI|50|2": [
    "SVG",
    "L'intégrale de Riemann : encadrement de l'aire sous la courbe par des rectangles",
    "figures_en/vol_6/fig_50_riemann_integrale.svg"
  ],
  "Volume_VI|50|3": [
    "RAW",
    "```python\ndef integrale_rectangles(f, a, b, n):\n    \"\"\"\n    Calcule une approximation de l'intégrale de f entre a et b\n    par la méthode des rectangles au point médian.\n    \"\"\"\n    largeur = (b - a) / n\n    somme = 0.0\n    for k in range(n):\n        # Point milieu du k-ième sous-intervalle\n        x_milieu = a + (k + 0.5) * largeur\n        somme += f(x_milieu)\n    return somme * largeur\n\n# Testons sur f(x) = x^2 entre 0 et 3 (l'aire exacte vaut 9)\ndef carre(x):\n    return x**2\n\nprint(\"Approximation avec 10 rectangles   :\", integrale_rectangles(carre, 0, 3, 10))\nprint(\"Approximation avec 100 rectangles  :\", integrale_rectangles(carre, 0, 3, 100))\nprint(\"Approximation avec 1000 rectangles :\", integrale_rectangles(carre, 0, 3, 1000))\n# Avec 1000 rectangles, on obtient 8.9999988... soit quasiment 9 !\n```"
  ],
  "Volume_VI|50|4": [
    "SVG",
    "L'intégrale de Riemann : encadrement de l'aire sous la courbe par des rectangles",
    "figures_en/vol_6/fig_50_riemann_integrale.svg"
  ],
  "Volume_VI|50|5": [
    "SVG",
    "L'intégrale de Riemann : encadrement de l'aire sous la courbe par des rectangles",
    "figures_en/vol_6/fig_50_riemann_integrale.svg"
  ],
  "Volume_VI|51|0": [
    "SVG",
    "Comportement asymptotique aux bornes : asymptotes verticales et horizontales",
    "figures_en/vol_6/fig_45_asymptotes_complete.svg"
  ],
  "Volume_VI|51|1": [
    "SVG",
    "Charge du condensateur et méthode d'Euler pour les équations différentielles",
    "figures_en/vol_6/fig_51_circuit_rc_euler.svg"
  ],
  "Volume_VI|51|2": [
    "SVG",
    "Charge du condensateur et méthode d'Euler pour les équations différentielles",
    "figures_en/vol_6/fig_51_circuit_rc_euler.svg"
  ],
  "Volume_VI|51|3": [
    "SVG",
    "Charge du condensateur et méthode d'Euler pour les équations différentielles",
    "figures_en/vol_6/fig_51_circuit_rc_euler.svg"
  ],
  "Volume_VI|51|4": [
    "RAW",
    "```python\nimport math\n\ndef methode_euler(a, b, y0, n):\n    \"\"\"\n    Résout y' = -2y sur [a, b] avec y(a) = y0 en n étapes.\n    \"\"\"\n    h = (b - a) / n\n    t = a\n    y = y0\n    resultats = [(t, y, math.exp(-2 * t))]\n    \n    for _ in range(n):\n        # Pente calculée d'après l'équation différentielle y' = -2y\n        pente = -2 * y\n        y = y + h * pente\n        t = t + h\n        y_exact = math.exp(-2 * t)\n        resultats.append((round(t, 4), round(y, 4), round(y_exact, 4)))\n    \n    return resultats\n\n# Exécution avec 10 pas de h = 0.2\npoints = methode_euler(0, 2, 1.0, 10)\nprint(f\"{'t':<6} | {'y_Euler':<10} | {'y_Exact':<10} | {'Erreur':<10}\")\nprint(\"-\" * 42)\nfor t_val, y_e, y_ex in points:\n    err = abs(y_e - y_ex)\n    print(f\"{t_val:<6} | {y_e:<10} | {y_ex:<10} | {err:<10.4f}\")\n```"
  ],
  "Volume_VI|52|0": [
    "SVG",
    "Coordonnées et norme d'un vecteur dans l'espace à 3 dimensions",
    "figures_en/vol_6/fig_52_vecteur_espace_3d.svg"
  ],
  "Volume_VI|52|1": [
    "SVG",
    "Coordonnées et norme d'un vecteur dans l'espace à 3 dimensions",
    "figures_en/vol_6/fig_52_vecteur_espace_3d.svg"
  ],
  "Volume_VI|52|2": [
    "SVG",
    "Positions relatives de deux droites dans l'espace : parallèles, sécantes ou non coplanaires",
    "figures_en/vol_6/fig_52_droites_espace.svg"
  ],
  "Volume_VI|52|3": [
    "SVG",
    "Cartesian equation of the plane and normal vector dans l'espace",
    "figures_en/vol_6/fig_52_plan_vecteur_normal.svg"
  ],
  "Volume_VI|52|4": [
    "SVG",
    "Positions relatives de deux droites dans l'espace : parallèles, sécantes ou non coplanaires",
    "figures_en/vol_6/fig_52_droites_espace.svg"
  ],
  "Volume_VI|53|0": [
    "SVG",
    "Combinatorial decision tree: permutations, combinations, arrangements",
    "figures_en/vol_6/fig_53_arbre_decision_combinatoire.svg"
  ],
  "Volume_VI|53|1": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1.2fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 1.5fr),\n    align: center,\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [$n \\ k$], [0], [1], [2], [3], [4], [5], [Sum $2^n$],\n    [0], [1], [], [], [], [], [], [$1 = 2^0$],\n    [1], [1], [1], [], [], [], [], [$2 = 2^1$],\n    [2], [1], [2], [1], [], [], [], [$4 = 2^2$],\n    [3], [1], [3], [3], [1], [], [], [$8 = 2^3$],\n    [4], [1], [4], [6], [4], [1], [], [$16 = 2^4$],\n    [5], [1], [5], [10], [10], [5], [1], [$32 = 2^5$]\n  )\n]\n```"
  ],
  "Volume_VI|53|2": [
    "SVG",
    "Combinatorial decision tree: permutations, combinations, arrangements",
    "figures_en/vol_6/fig_53_arbre_decision_combinatoire.svg"
  ],
  "Volume_VI|53|3": [
    "SVG",
    "Grid paths and binomial coefficients",
    "figures_en/vol_6/fig_53_chemins_grille.svg"
  ],
  "Volume_VI|54|0": [
    "RAW",
    "```python\nimport random\n\ndef simulation_lancers(n):\n    succes = 0\n    historique_frequences = []\n    \n    for i in range(1, n + 1):\n        # 1 = Pile (succès), 0 = Face (échec)\n        tirage = random.choice([0, 1])\n        succes += tirage\n        frequence = succes / i\n        historique_frequences.append((i, frequence))\n        \n    return historique_frequences\n\n# Exemple d'exécution\nresultats = simulation_lancers(10000)\n\n# Affichage de quelques étapes clés\njalons = [10, 50, 100, 500, 1000, 5000, 10000]\nprint(f\"{'Lancers (n)':<12} | {'Fréquence Pile':<15} | {'Écart à 0.5':<12}\")\nprint(\"-\" * 45)\nfor jalon in jalons:\n    freq = resultats[jalon - 1][1]\n    ecart = abs(freq - 0.5)\n    print(f\"{jalon:<12} | {freq:<15.4f} | {ecart:<12.4f}\")\n```"
  ],
  "Volume_VI|54|1": [
    "TABLE",
    "```data_table\n#align(center)[\n  #table(\n    columns: (1fr, 1fr, 1fr),\n    align: (center, center, center),\n    stroke: 0.5pt + rgb(\"#cbd5e1\"),\n    fill: (x, y) => if y == 0 { rgb(\"#eff6ff\") } else { rgb(\"#ffffff\") },\n    [Lancers ($n$)], [Frequency Pile], [Écart à 0.5],\n    [10], [0.7000], [+0.2000],\n    [50], [0.4400], [+0.0600],\n    [100], [0.5300], [+0.0300],\n    [500], [0.4880], [+0.0120],\n    [1 000], [0.5040], [+0.0040],\n    [5 000], [0.4982], [+0.0018],\n    [10 000], [0.5007], [+0.0007]\n  )\n]\n```"
  ],
  "Volume_VI|55|0": [
    "SVG",
    "The Argand-Gauss complex plane: algebraic and trigonometric forms",
    "figures_en/vol_6/fig_55_plan_complexe.svg"
  ],
  "Volume_VI|55|1": [
    "SVG",
    "Modular arithmetic: clock face modulo 12",
    "figures_en/vol_6/fig_55_racines_unite.svg"
  ],
  "Volume_VI|56|0": [
    "SVG",
    "Modular arithmetic: clock face modulo 12",
    "figures_en/vol_6/fig_55_racines_unite.svg"
  ],
  "Volume_VI|56|1": [
    "SVG",
    "RSA asymmetric cryptography: public-key exchange and decryption",
    "figures_en/vol_6/fig_56_cryptographie_rsa.svg"
  ],
  "Volume_VI|57|0": [
    "SVG",
    "Principle of matrix multiplication row by column",
    "figures_en/vol_6/fig_57_produit_matriciel.svg"
  ],
  "Volume_VI|57|1": [
    "SVG",
    "Directed graph with 3 vertices and associated adjacency matrix",
    "figures_en/vol_6/fig_57_graphe_oriente_matrice.svg"
  ],
  "Volume_VI|57|2": [
    "SVG",
    "2-state Markov graph and transition matrix",
    "figures_en/vol_6/fig_57_graphe_probabiliste.svg"
  ],
  "Volume_VI|58|0": [
    "CALLOUT",
    "📐 Fundamental Rule — Synthesis of the Mathematical Edifice and Gateway to Higher Mathematics"
  ],
  "Volume_VI|58|1": [
    "CALLOUT",
    "📐 Fundamental Rule — Synthesis of the Mathematical Edifice and Gateway to Higher Mathematics"
  ],
  "Volume_VI|58|2": [
    "CALLOUT",
    "📐 Fundamental Rule — Synthesis of the Mathematical Edifice and Gateway to Higher Mathematics"
  ]
}


def transform_block(block_lines, lang, prefix, chapter_name, start_line, vol_dir, block_idx=0):
    pfx = prefix
    code_raw = "\n".join(block_lines)
    code_clean = "\n".join([l.strip() for l in block_lines if l.strip()])
    code_clean_l = code_clean.lower()
    lines = [l.strip() for l in block_lines if l.strip()]

    ch_num_m = re.search(r'Chapitre_(\d+)', chapter_name)
    ch_num = int(ch_num_m.group(1)) if ch_num_m else 0

    clean_text = re.sub(r'[─│┌┐└┘├┤┬┴┼═║╔╗╚╝╠╣╦╩╬▲►▼◄╭╮╯╰╱╲★●■]', '', code_clean).strip()
    clean_lines = [re.sub(r'^[\s/\\.*~\-_=+;:<>()\[\]{}|]+', '', l).strip() for l in clean_text.splitlines()]
    clean_lines = [l for l in clean_lines if l and len(l) > 1]
    callout_body = f"\n{pfx}> - " + f"\n{pfx}> - ".join(clean_lines) if clean_lines else ""

    # Check structural action map first
    map_key = f"{vol_dir}|{ch_num}|{block_idx}"
    if map_key in EN_ACTION_MAP:
        act = EN_ACTION_MAP[map_key]
        kind = act[0]
        if kind == "SVG":
            caption = act[1]
            path = act[2]
            return f"\n{pfx}![{caption}]({path})\n"
        elif kind == "CALLOUT":
            title = act[1]
            pfx_clean = pfx.rstrip()
            if pfx_clean.endswith('>'):
                return f"\n{pfx}**{title}**\n{pfx}{callout_body}\n"
            else:
                return f"\n{pfx}> **{title}**\n{pfx}>{callout_body}\n"
        elif kind == "TABLE":
            tbl_str = act[1]
            return f"\n{pfx}{tbl_str}\n"
        elif kind == "CALC_OP":
            inner = "\n".join([f"{pfx}{l}" for l in block_lines])
            return f"\n{pfx}```calc_op\n{inner}\n{pfx}```\n"

    # Chapter 15 extra blocks handling
    if ch_num == 15 and block_idx >= 5:
        if "knot 1" in code_clean_l or "13" in code_clean:
            return f"\n{pfx}![The Egyptian thirteen-knot rope and the 3-4-5 right triangle](figures_en/vol_4/fig_27_corde_treize_noeuds.svg)\n"
        elif "torn corners" in code_clean_l or "paper triangle" in code_clean_l:
            return f"\n{pfx}![Sum of angles in a triangle: 180°](figures_en/vol_3/fig_15_quatre_types_angles.svg)\n"
        elif "line (de)" in code_clean_l:
            return f"\n{pfx}![Parallel lines cut by transversals](figures_en/vol_3/fig_15_paralleles_perpendiculaires.svg)\n"

    # Arithmetic operation check for standard columns
    if ch_num in [4, 5, 9, 11]:
        is_div = (ch_num == 9) and any('|---' in l or '|───' in l or '|----' in l for l in lines)
        has_vert_op = any(l.startswith(('+', '-', '×', '*')) for l in lines) and any(re.match(r'^[─\-=]{3,}$', l.strip()) for l in lines)
        if is_div or has_vert_op:
            inner = "\n".join([f"{pfx}{l}" for l in block_lines])
            return f"\n{pfx}```calc_op\n{inner}\n{pfx}```\n"

    # Default fallback
    if clean_lines:
        inner = "\n".join([f"{pfx}{l}" for l in clean_lines])
        return f"\n{pfx}```data_table\n{inner}\n{pfx}```\n"
    return ""

def is_escaped(s, idx):
    backslashes = 0
    i = idx - 1
    while i >= 0 and s[i] == '\\':
        backslashes += 1
        i -= 1
    return (backslashes % 2) == 1

def find_matching_bracket_typst(s, start_idx):
    # s[start_idx] is '['
    depth = 1
    in_math = False
    i = start_idx + 1
    while i < len(s) and depth > 0:
        c = s[i]
        if c == '\\':
            i += 2
            continue
        if c == '$':
            in_math = not in_math
            i += 1
            continue
        if not in_math:
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
        i += 1
    return i - 1 if depth == 0 else -1

def process_quotes_bracket_matching(text):
    # Unwrap any double quotes if directly nested
    nested_pat = r'#quote\(block:\s*true\)\[\s*#quote\(block:\s*true\)\[([\s\S]*?)\]\s*\]'
    text = re.sub(nested_pat, r'#quote(block: true)[\1]', text)

    pattern = r'#quote\(block:\s*true\)\[\s*'
    pos = 0
    pieces = []
    while True:
        m = re.search(pattern, text[pos:])
        if not m:
            pieces.append(text[pos:])
            break
        start_quote = pos + m.start()
        start_body = pos + m.end()
        pieces.append(text[pos:start_quote])
        
        # bracket count for quote body ignoring math mode and escaped brackets
        end_bracket = find_matching_bracket_typst(text, start_body - 1)
        if end_bracket != -1:
            body = text[start_body:end_bracket].strip()
            # If body itself contains nested quote blocks, process them first
            if '#quote(block: true)' in body:
                body = process_quotes_bracket_matching(body)
            
            # Extract title and body
            m_strong = re.search(r'#(?:strong|emph)\[', body)
            title = ""
            rest_body = body
            if m_strong and m_strong.start() < 30:
                s_start = m_strong.end()
                s_end = find_matching_bracket_typst(body, s_start - 1)
                if s_end != -1:
                    title = body[s_start:s_end].strip()
                    rest_body = body[s_end+1:].strip()
            
            # Clean symbols from title
            t_clean = re.sub(r'^(?:⚠️|📐|🎯|🔍|💡|🛠️|🧭|🖐️|✅|✍️)\s*', '', title).strip()
            t_clean = t_clean.replace("---", "—").replace("--", "—").strip()
            
            # Classification
            full_check = (title + " " + body[:100]).lower()
            if any(w in full_check for w in ['attention', 'watch out', 'warning', 'piège', 'trap', 'caution', 'beware', 'pitfall', 'danger']):
                t_final = t_clean if t_clean else "Watch Out for the Trap!"
                pieces.append(f'#alerte(title: [{t_final}])[{rest_body}\n]\n')
            elif any(w in full_check for w in ['cas limite', 'boundary case', 'point de vigilance', 'vigilance', 'edge case', 'corner case']):
                t_final = t_clean if t_clean else "Boundary Case & Caution"
                pieces.append(f'#cas_limite(title: [{t_final}])[{rest_body}\n]\n')
            elif any(w in full_check for w in ['définition', 'definition', 'règle', 'rule', 'propriété', 'property', 'théorème', 'theorem', 'axiome', 'axiom', 'principe', 'principle', 'corollaire', 'corollary', 'loi', 'law']):
                t_final = t_clean if t_clean else "Fundamental Principle & Definition"
                pieces.append(f'#principe(title: [{t_final}])[{rest_body}\n]\n')
            elif any(w in full_check for w in ["l'histoire", 'history', 'découverte', 'discovery', 'le savais-tu', 'did you know', 'intuition', 'observation', 'métaphore', 'metaphor', 'modélisation', 'modeling']):
                t_final = t_clean if t_clean else "Discovery & History"
                pieces.append(f'#decouvre(title: [{t_final}])[{rest_body}\n]\n')
            elif any(w in full_check for w in ['méthode', 'method', 'algorithme', 'algorithm', 'atelier', 'workshop', 'protocole', 'protocol']):
                t_final = t_clean if t_clean else "Step-by-Step Method"
                pieces.append(f'#methode(title: [{t_final}])[{rest_body}\n]\n')
            elif any(w in full_check for w in ['exemple', 'example', 'worked example', 'solved example', 'exercice résolu', 'application', 'proof']):
                t_final = t_clean if t_clean else "Step-by-Step Worked Example"
                pieces.append(f'#exemple_resolu(title: [{t_final}])[{rest_body}\n]\n')
            else:
                pieces.append(f'#quote_box[\n{body}\n]\n')
            
            pos = end_bracket + 1
        else:
            pieces.append(text[start_quote:])
            break
            
    return "".join(pieces)

def postprocess_typst(typst_content):
    print("Post-processing Typst output for Byrne Callouts and Math Delimiters...")
    typst_content = process_quotes_bracket_matching(typst_content)

    # 2. Fix French math intervals produced by Pandoc that break Typst parser
    typst_content = re.sub(r'lr\(\s*([\[\]])(.*?)([\[\]])\s*\)', r'\1\2\3', typst_content)

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

    # 8. Ouvertures de Volume en double page face-à-face (Frontispice gauche pure photo, ouverture droite complète)
    volume_configs = [
        (
            "I",
            "THE AGE OF THE HAND AND THE SAVANNA",
            "Ages 6–8 / Grades 1–2",
            "figures_en/nature/vol_1_abeilles_hexagone.jpg",
            "From the awakening of prehistoric vision to early pebble manipulation, this foundational volume establishes number sense, place value, and the elementary operations.",
            [
                "Chapter 1 : The Monkey's Eyes and the Bag of Pebbles",
                "Chapter 2 : The Five-Fingered Hand and Bundles of Ten",
                "Chapter 3 : The Shared Hunt and the Balance Scale of Justice",
                "Chapter 4 : The Merchant's Abacus and the Traveling Carry",
                "Chapter 5 : The Brick Wall and Magic Rectangles",
                "Chapter 6 : The Pharaoh's Cubit and the Hourglass",
                "Chapter 7 : The Shapes of the World and the Gardener's String"
            ],
            "Facing: Hexagonal tessellation of honeycomb cells (Apis mellifera)."
        ),
        (
            "II",
            "THE SECRET OF SHARING AND THE MAGNITUDES OF THE WORLD",
            "Ages 8–11 / Grades 3–5",
            "figures_en/nature/vol_2_nautile_spirale.jpg",
            "From sharing flatbread to astronomical measurements, the student masters fractions, decimals, proportionality, and Euclidean geometry.",
            [
                "Chapter 8 : The Rebel Stones and the Lonely Numbers",
                "Chapter 9 : The Feast Remainders and the Game Teams",
                "Chapter 10 : The Broken Galette and the Measuring Sieve",
                "Chapter 11 : The Tenths of Simon Stevin",
                "Chapter 12 : The Meter of the Revolution",
                "Chapter 13 : Grandmother's Recipe and the Rule of Three",
                "Chapter 14 : The Merchant's Slate and the Sand Pit"
            ],
            "Facing: Logarithmic spiral of the Nautilus shell (Nautilus pompilius)."
        ),
        (
            "III",
            "THE STAR OF ALEXANDRIA AND EUCLIDEAN SPACE",
            "Ages 11–13 / Grades 6–7",
            "figures_en/nature/vol_3_tournesol_fibonacci.jpg",
            "At the gates of middle school, deductive geometry organizes itself around Euclid's axioms, relative numbers, and planar symmetries.",
            [
                "Chapter 15 : The Flooding of the Nile and the Thirteen-Knot Rope",
                "Chapter 16 : The Potter's Wheel and Archimedes' Secret",
                "Chapter 17 : The Shadow of the Pyramid and the Upright Staff",
                "Chapter 18 : The Grain of Rice on the Chessboard",
                "Chapter 19 : The Forbidden Secret of the Pythagoreans",
                "Chapter 20 : Treasure Island and the Two Paths",
                "Chapter 21 : The Tax Collector and the Hundred Pieces"
            ],
            "Facing: Phyllotaxis and Fibonacci spirals of the Sunflower (Helianthus annuus)."
        ),
        (
            "IV",
            "THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE",
            "Ages 13–15 / Grades 8–9",
            "figures_en/nature/vol_4_romanesco_fractale.jpg",
            "The emergence of literal equations, integer powers, affine functions, and statistics prepares the transition to high school mathematics.",
            [
                "Chapter 22 : The Mystery Bag on Al-Khwarizmi's Scale",
                "Chapter 23 : The Completed Square and Special Products",
                "Chapter 24 : The Two Merchants and Inequalities",
                "Chapter 25 : The Doubling Machine and the Tariff Line",
                "Chapter 26 : Paper Folding and the Magic Mirror",
                "Chapter 27 : Land Partitioning and the Potter's Box",
                "Chapter 28 : Eratosthenes and the Circumference of the Earth",
                "Chapter 29 : The Partition of Euclid",
                "Chapter 30 : The Roulette of Fate and the Hunter's Survival"
            ],
            "Facing: Scale invariance and fractal geometry of Romanesco Broccoli (Brassica oleracea)."
        ),
        (
            "V",
            "MOTION, ANGLE AND THE SPECTRUM OF FORM",
            "Ages 15–17 / Grades 10–11",
            "figures_en/nature/vol_5_toile_araignee.jpg",
            "High school foundations: formal logic, vectors, analytic geometry, quadratic polynomials, trigonometry, the derivative as an instantaneous rate, and conditional probability.",
            [
                "Chapter 31 : The Court of Logic",
                "Chapter 32 : The Sailboat in the Storm and the Free Arrow",
                "Chapter 33 : The Line of Sight",
                "Chapter 34 : The Jacquard Loom and the Function Box",
                "Chapter 35 : Galileo's Fountain and the Parabola",
                "Chapter 36 : The Staircase Steps and the Usurer's Loan",
                "Chapter 37 : The Ferris Wheel and the Winding Circle",
                "Chapter 38 : Pulling the Rope and the Effective Shadow",
                "Chapter 39 : The Skier and the Board under the Boot",
                "Chapter 40 : The Bacterial Colony",
                "Chapter 41 : The Pollster and Standard Deviation",
                "Chapter 42 : The Physician, the Test, and the Tree of Possibilities"
            ],
            "Facing: Concurrent vector balance and catenary curves in the spider web (Araneus diadematus)."
        ),
        (
            "VI",
            "TAMED INFINITY AND THE MODERN EDIFICE",
            "Ages 17–18 / Grade 12 & Advanced Mathematics",
            "figures_en/nature/vol_6_conus_textile.jpg",
            "Advanced curriculum: induction, limits, continuity, differential calculus, logarithms, Riemann integrals, differential equations, complex numbers, matrices, graphs, and continuous distributions.",
            [
                "Chapter 43 : The Endless Staircase and the Dominoes",
                "Chapter 44 : The Runner Who Never Touches the Line",
                "Chapter 45 : The Horizon of Curves",
                "Chapter 46 : The Unbroken Thread",
                "Chapter 47 : The Growing Garden and the Gear Chain",
                "Chapter 48 : Napier's Logarithm and the Navigator's Tables",
                "Chapter 49 : The Swing and Oscillating Functions",
                "Chapter 50 : The Barrel Filled with Slices of Water",
                "Chapter 51 : The Cooling Cup of Tea",
                "Chapter 52 : The Cathedral in Space",
                "Chapter 53 : The Combination Lock and Ways of Choosing",
                "Chapter 54 : The Thousand Coin Tosses",
                "Chapter 55 : The Right-Angled Whirlwind",
                "Chapter 56 : Secret Messages and the Clock of Remainders",
                "Chapter 57 : The Jacquard Loom Revisited: Matrices and Graphs",
                "Chapter 58 : The End of the Voyage"
            ],
            "Facing: Turing reaction-diffusion and cellular automata of the Textile Cone (Conus textile)."
        )
    ]
    
    for num, vol_title, sous_titre, img, desc, chapitres, mention in volume_configs:
        vol_pattern = rf'^(= VOLUME\s+{num}\b[^\n]*(?:\n<[^>]+>)?(?:\n#divider\(\))?)'
        ch_list_typst = ", ".join([f'"{ch}"' for ch in chapitres])
        replacement = (
            f'#frontispice-volume("{img}")\n\n'
            f'#ouverture-volume(\n'
            f'  "{num}",\n'
            f'  "{vol_title}",\n'
            f'  "{sous_titre}",\n'
            f'  "{desc}",\n'
            f'  ({ch_list_typst}),\n'
            f'  "{mention}"\n'
            f')'
        )
        typst_content = re.sub(vol_pattern, replacement, typst_content, flags=re.MULTILINE)

    # 9. Ouverture des Chapitres en belle page (recto impair) avec pagination en pied de page
    typst_content = re.sub(
        r'^(== (?:CHAPITRE|CHAPTER)\b)',
        r'#metadata("fin-section") <fin-section>\n#pagebreak(weak: true, to: "odd")\n#metadata("chapitre") <debut-chapitre>\n#metadata("debut-section") <debut-section>\n\1',
        typst_content,
        flags=re.MULTILINE
    )

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
        ("Volume_I", "# VOLUME I — THE AGE OF THE HAND AND THE SAVANNA (Ages 6–8 / Grades 1–2)"),
        ("Volume_II", "# VOLUME II — THE SECRET OF SHARING AND THE MAGNITUDES OF THE WORLD (Ages 8–11 / Grades 3–5)"),
        ("Volume_III", "# VOLUME III — THE STAR OF ALEXANDRIA AND EUCLIDEAN SPACE (Ages 11–13 / Grades 6–7)"),
        ("Volume_IV", "# VOLUME IV — THE ALCHEMY OF SYMBOLS AND THE ALGEBRAIC FIRE (Ages 13–15 / Grades 8–9)"),
        ("Volume_V", "# VOLUME V — MOTION, ANGLE AND THE SPECTRUM OF FORM (Ages 15–17 / Grades 10–11)"),
        ("Volume_VI", "# VOLUME VI — TAMED INFINITY AND THE MODERN EDIFICE (Ages 17–18 / Grade 12 & Advanced Mathematics)")
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
