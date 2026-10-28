# -*- coding: utf-8 -*-
"""
SVG Generator for Volume I (LA VOIE DU NOMBRE)
Oliver Byrne Palette:
  Navy: #0f172a
  Blue: #1d4ed8
  Red: #b91c1c
  Yellow/Amber: #d97706
  Green: #15803d
  Purple: #7e22ce
  Slate: #475569
  Light Blue: #eff6ff
  Light Gray: #f8fafc
  Border: #cbd5e1
"""
import os
import xml.etree.ElementTree as ET

out_dir = r"c:\Silvere\Encours\Developpement\Articles\livre_mathematiques\figures\vol_1"
os.makedirs(out_dir, exist_ok=True)

def save_and_verify(name, svg_content):
    path = os.path.join(out_dir, name)
    svg_clean = svg_content.strip()
    # Verify XML validity
    try:
        ET.fromstring(svg_clean)
    except Exception as e:
        print(f"XML ERROR in {name}: {e}")
        raise e
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_clean)
    return path

# -------------------------------------------------------------
# Chapitre 1
# -------------------------------------------------------------
# diag_001: Subitizing 3 vs 8
save_and_verify("fig_01_subitizing.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 220" width="100%" height="220">
  <rect width="600" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <rect x="30" y="25" width="250" height="170" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <text x="155" y="55" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#1d4ed8" text-anchor="middle">SUBITIZING IMMÉDIAT (3)</text>
  <circle cx="105" cy="115" r="14" fill="#1d4ed8"/>
  <circle cx="155" cy="115" r="14" fill="#1d4ed8"/>
  <circle cx="205" cy="115" r="14" fill="#1d4ed8"/>
  <text x="155" y="170" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">Perception directe sans compter</text>
  
  <rect x="320" y="25" width="250" height="170" rx="6" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
  <text x="445" y="55" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#b91c1c" text-anchor="middle">SATURATION COGNITIVE (8)</text>
  <circle cx="360" cy="95" r="12" fill="#b91c1c"/>
  <circle cx="410" cy="100" r="12" fill="#b91c1c"/>
  <circle cx="465" cy="90" r="12" fill="#b91c1c"/>
  <circle cx="510" cy="110" r="12" fill="#b91c1c"/>
  <circle cx="380" cy="140" r="12" fill="#b91c1c"/>
  <circle cx="430" cy="135" r="12" fill="#b91c1c"/>
  <circle cx="480" cy="145" r="12" fill="#b91c1c"/>
  <circle cx="525" cy="140" r="12" fill="#b91c1c"/>
  <text x="445" y="175" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">Dénombrement séquentiel nécessaire</text>
</svg>""")

# diag_002: Bijection Collection A vs Collection B (un pour un)
save_and_verify("fig_01_correspondance.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200" width="100%" height="200">
  <rect width="600" height="200" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="50" y="50" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#1d4ed8">Collection A (4 ronds) :</text>
  <circle cx="240" cy="45" r="12" fill="#1d4ed8"/>
  <circle cx="310" cy="45" r="12" fill="#1d4ed8"/>
  <circle cx="380" cy="45" r="12" fill="#1d4ed8"/>
  <circle cx="450" cy="45" r="12" fill="#1d4ed8"/>
  
  <!-- Flèches d'appariement -->
  <line x1="240" y1="65" x2="240" y2="105" stroke="#d97706" stroke-width="2" stroke-dasharray="4"/>
  <polygon points="240,112 236,104 244,104" fill="#d97706"/>
  <line x1="310" y1="65" x2="310" y2="105" stroke="#d97706" stroke-width="2" stroke-dasharray="4"/>
  <polygon points="310,112 306,104 314,104" fill="#d97706"/>
  <line x1="380" y1="65" x2="380" y2="105" stroke="#d97706" stroke-width="2" stroke-dasharray="4"/>
  <polygon points="380,112 376,104 384,104" fill="#d97706"/>
  <line x1="450" y1="65" x2="450" y2="105" stroke="#d97706" stroke-width="2" stroke-dasharray="4"/>
  <polygon points="450,112 446,104 454,104" fill="#d97706"/>
  
  <text x="50" y="140" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#b91c1c">Collection B (5 carrés) :</text>
  <rect x="228" y="125" width="24" height="24" fill="#b91c1c" rx="3"/>
  <rect x="298" y="125" width="24" height="24" fill="#b91c1c" rx="3"/>
  <rect x="368" y="125" width="24" height="24" fill="#b91c1c" rx="3"/>
  <rect x="438" y="125" width="24" height="24" fill="#b91c1c" rx="3"/>
  <rect x="508" y="125" width="24" height="24" fill="#b91c1c" rx="3" stroke="#0f172a" stroke-width="2"/>
  <text x="520" y="175" font-family="Liberation Sans, sans-serif" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">Isolé !</text>
  <text x="300" y="185" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">Correspondance terme à terme : 5 &gt; 4 car un élément n'a pas de partenaire</text>
</svg>""")

# diag_003: Deux lignes d'objets (4 ronds vs 6 carrés)
save_and_verify("fig_01_comparaison_lignes.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 550 140" width="100%" height="140">
  <rect width="550" height="140" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="30" y="45" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#1d4ed8">Ligne 1 (4) :</text>
  <circle cx="160" cy="40" r="10" fill="#1d4ed8"/>
  <circle cx="230" cy="40" r="10" fill="#1d4ed8"/>
  <circle cx="300" cy="40" r="10" fill="#1d4ed8"/>
  <circle cx="370" cy="40" r="10" fill="#1d4ed8"/>
  
  <text x="30" y="95" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#15803d">Ligne 2 (6) :</text>
  <rect x="150" y="85" width="20" height="20" fill="#15803d" rx="2"/>
  <rect x="220" y="85" width="20" height="20" fill="#15803d" rx="2"/>
  <rect x="290" y="85" width="20" height="20" fill="#15803d" rx="2"/>
  <rect x="360" y="85" width="20" height="20" fill="#15803d" rx="2"/>
  <rect x="430" y="85" width="20" height="20" fill="#15803d" rx="2"/>
  <rect x="500" y="85" width="20" height="20" fill="#15803d" rx="2"/>
  <line x1="390" y1="20" x2="390" y2="120" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="4"/>
  <text x="460" y="45" font-family="Liberation Sans, sans-serif" font-size="11" fill="#b91c1c">+2 de surplus</text>
</svg>""")

# diag_004: Os d'Ishango et ses entailles par paquets
save_and_verify("fig_01_os_ishango.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 130" width="100%" height="130">
  <rect width="600" height="130" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <path d="M 50,65 C 50,45 80,40 120,42 L 480,42 C 530,40 550,45 550,65 C 550,85 530,90 480,88 L 120,88 C 80,90 50,85 50,65 Z" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
  <!-- Entailles groupées par 5 -->
  <!-- Groupe 1 -->
  <line x1="120" y1="50" x2="120" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="128" y1="50" x2="128" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="136" y1="50" x2="136" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="144" y1="50" x2="144" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="152" y1="50" x2="152" y2="80" stroke="#0f172a" stroke-width="2"/>
  <!-- Groupe 2 -->
  <line x1="180" y1="50" x2="180" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="188" y1="50" x2="188" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="196" y1="50" x2="196" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="204" y1="50" x2="204" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="212" y1="50" x2="212" y2="80" stroke="#0f172a" stroke-width="2"/>
  <!-- Groupe 3 -->
  <line x1="240" y1="50" x2="240" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="248" y1="50" x2="248" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="256" y1="50" x2="256" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="264" y1="50" x2="264" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="272" y1="50" x2="272" y2="80" stroke="#0f172a" stroke-width="2"/>
  <!-- Groupe 4 -->
  <line x1="300" y1="50" x2="300" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="308" y1="50" x2="308" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="316" y1="50" x2="316" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="324" y1="50" x2="324" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="332" y1="50" x2="332" y2="80" stroke="#0f172a" stroke-width="2"/>
  <!-- 2 entailles isolées -->
  <line x1="365" y1="50" x2="365" y2="80" stroke="#b91c1c" stroke-width="2"/>
  <line x1="375" y1="50" x2="375" y2="80" stroke="#b91c1c" stroke-width="2"/>
  <text x="300" y="112" font-family="Liberation Sans, sans-serif" font-size="11" fill="#475569" text-anchor="middle">L'Os d'Ishango (~20 000 av. J.-C.) : entailles groupées par paquets de 5</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 2
# -------------------------------------------------------------
# diag_005: Deux mains de 5 doigts = 10
save_and_verify("fig_02_deux_mains_dix.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 180" width="100%" height="180">
  <rect width="540" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Main gauche -->
  <g transform="translate(110, 30)">
    <circle cx="50" cy="45" r="35" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <text x="50" y="52" font-family="Liberation Sans, sans-serif" font-size="20" font-weight="bold" fill="#1d4ed8" text-anchor="middle">5</text>
    <line x1="20" y1="15" x2="10" y2="0" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <line x1="35" y1="10" x2="30" y2="-5" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <line x1="50" y1="10" x2="50" y2="-8" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <line x1="65" y1="10" x2="70" y2="-5" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <line x1="80" y1="15" x2="90" y2="0" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <text x="50" y="105" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">Main gauche (5)</text>
  </g>
  <text x="270" y="85" font-family="Liberation Sans, sans-serif" font-size="28" font-weight="bold" fill="#0f172a" text-anchor="middle">+</text>
  <!-- Main droite -->
  <g transform="translate(330, 30)">
    <circle cx="50" cy="45" r="35" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <text x="50" y="52" font-family="Liberation Sans, sans-serif" font-size="20" font-weight="bold" fill="#1d4ed8" text-anchor="middle">5</text>
    <line x1="20" y1="15" x2="10" y2="0" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <line x1="35" y1="10" x2="30" y2="-5" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <line x1="50" y1="10" x2="50" y2="-8" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <line x1="65" y1="10" x2="70" y2="-5" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <line x1="80" y1="15" x2="90" y2="0" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
    <text x="50" y="105" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">Main droite (5)</text>
  </g>
  <text x="270" y="155" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#15803d" text-anchor="middle">5 + 5 = 10 : Le fondement biologique de la base décimale</text>
</svg>""")

# diag_006: 10 cailloux échangés contre 1 bouchon (dizaine)
save_and_verify("fig_02_echange_dizaine.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 180" width="100%" height="180">
  <rect width="540" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- 10 cailloux -->
  <g transform="translate(60, 40)">
    <text x="70" y="-10" font-family="Liberation Sans, sans-serif" font-size="12" font-weight="bold" fill="#475569" text-anchor="middle">10 unités isolées</text>
    <circle cx="15" cy="20" r="10" fill="#64748b"/>
    <circle cx="45" cy="20" r="10" fill="#64748b"/>
    <circle cx="75" cy="20" r="10" fill="#64748b"/>
    <circle cx="105" cy="20" r="10" fill="#64748b"/>
    <circle cx="135" cy="20" r="10" fill="#64748b"/>
    <circle cx="15" cy="55" r="10" fill="#64748b"/>
    <circle cx="45" cy="55" r="10" fill="#64748b"/>
    <circle cx="75" cy="55" r="10" fill="#64748b"/>
    <circle cx="105" cy="55" r="10" fill="#64748b"/>
    <circle cx="135" cy="55" r="10" fill="#64748b"/>
  </g>
  <!-- Flèche échange -->
  <line x1="250" y1="75" x2="310" y2="75" stroke="#d97706" stroke-width="3"/>
  <polygon points="318,75 308,70 308,80" fill="#d97706"/>
  <text x="280" y="65" font-family="Liberation Sans, sans-serif" font-size="11" font-weight="bold" fill="#d97706" text-anchor="middle">Échange</text>
  <!-- 1 bouchon (dizaine) -->
  <g transform="translate(360, 40)">
    <rect x="20" y="10" width="80" height="55" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2.5"/>
    <text x="60" y="42" font-family="Liberation Sans, sans-serif" font-size="16" font-weight="bold" fill="#1d4ed8" text-anchor="middle">1 DIZAINE</text>
    <text x="60" y="90" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">= 10 unités</text>
  </g>
  <text x="270" y="155" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">L'échange régulier : la clé universelle de la numération de position</text>
</svg>""")

# diag_007: Tableau C D U pour 405 (rôle du zéro)
save_and_verify("fig_02_tableau_cdu_zero.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 170" width="100%" height="170">
  <rect width="540" height="170" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(90, 20)">
    <rect x="0" y="0" width="120" height="40" fill="#eff6ff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="120" y="0" width="120" height="40" fill="#fffbeb" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="240" y="0" width="120" height="40" fill="#f0fdf4" stroke="#cbd5e1" stroke-width="1.5"/>
    
    <text x="60" y="26" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Centaines (C)</text>
    <text x="180" y="26" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#d97706" text-anchor="middle">Dizaines (D)</text>
    <text x="300" y="26" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#15803d" text-anchor="middle">Unités (U)</text>
    
    <rect x="0" y="40" width="120" height="50" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="120" y="40" width="120" height="50" fill="#fffbeb" stroke="#b91c1c" stroke-width="2"/>
    <rect x="240" y="40" width="120" height="50" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    
    <text x="60" y="75" font-family="Liberation Sans, sans-serif" font-size="24" font-weight="bold" fill="#0f172a" text-anchor="middle">4</text>
    <text x="180" y="75" font-family="Liberation Sans, sans-serif" font-size="26" font-weight="bold" fill="#b91c1c" text-anchor="middle">0</text>
    <text x="300" y="75" font-family="Liberation Sans, sans-serif" font-size="24" font-weight="bold" fill="#0f172a" text-anchor="middle">5</text>
  </g>
  <text x="270" y="145" font-family="Liberation Sans, sans-serif" font-size="12" font-style="italic" fill="#b91c1c" text-anchor="middle">Le zéro garde la place vide de la dizaine : sans lui, 405 deviendrait 45 !</text>
</svg>""")

# diag_008: Signes < et > (gueule du crocodile)
save_and_verify("fig_02_crocodile_comparaison.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 160" width="100%" height="160">
  <rect width="540" height="160" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- 3 < 8 -->
  <g transform="translate(60, 30)">
    <rect x="0" y="0" width="190" height="100" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="35" y="60" font-family="Liberation Sans, sans-serif" font-size="26" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>
    <!-- Crocodile ouvert vers la droite -->
    <path d="M 115,35 L 75,55 L 115,75" fill="none" stroke="#15803d" stroke-width="4" stroke-linecap="round"/>
    <polygon points="95,45 105,42 98,50" fill="#ffffff" stroke="#15803d"/>
    <polygon points="95,65 105,68 98,60" fill="#ffffff" stroke="#15803d"/>
    <text x="155" y="60" font-family="Liberation Sans, sans-serif" font-size="26" font-weight="bold" fill="#0f172a" text-anchor="middle">8</text>
    <text x="95" y="90" font-family="Liberation Sans, sans-serif" font-size="11" fill="#15803d" text-anchor="middle">mange le plus grand (8)</text>
  </g>
  <!-- 9 > 4 -->
  <g transform="translate(290, 30)">
    <rect x="0" y="0" width="190" height="100" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="35" y="60" font-family="Liberation Sans, sans-serif" font-size="26" font-weight="bold" fill="#0f172a" text-anchor="middle">9</text>
    <!-- Crocodile ouvert vers la gauche -->
    <path d="M 75,35 L 115,55 L 75,75" fill="none" stroke="#15803d" stroke-width="4" stroke-linecap="round"/>
    <polygon points="95,45 85,42 92,50" fill="#ffffff" stroke="#15803d"/>
    <polygon points="95,65 85,68 92,60" fill="#ffffff" stroke="#15803d"/>
    <text x="155" y="60" font-family="Liberation Sans, sans-serif" font-size="26" font-weight="bold" fill="#0f172a" text-anchor="middle">4</text>
    <text x="95" y="90" font-family="Liberation Sans, sans-serif" font-size="11" fill="#15803d" text-anchor="middle">mange le plus grand (9)</text>
  </g>
  <text x="270" y="148" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">La grande ouverture se tourne toujours vers la quantité la plus importante</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 3
# -------------------------------------------------------------
# diag_009: 4 pommes + 3 poires = 7 fruits dans la marmite
save_and_verify("fig_03_marmite_addition.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 160" width="100%" height="160">
  <rect width="560" height="160" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Panier 1 -->
  <g transform="translate(40, 30)">
    <rect x="0" y="10" width="110" height="60" rx="6" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.5"/>
    <circle cx="30" cy="40" r="8" fill="#b91c1c"/>
    <circle cx="50" cy="40" r="8" fill="#b91c1c"/>
    <circle cx="70" cy="40" r="8" fill="#b91c1c"/>
    <circle cx="90" cy="40" r="8" fill="#b91c1c"/>
    <text x="55" y="90" font-family="Liberation Sans, sans-serif" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">4 pommes</text>
  </g>
  <text x="175" y="70" font-family="Liberation Sans, sans-serif" font-size="24" font-weight="bold" fill="#0f172a" text-anchor="middle">+</text>
  <!-- Panier 2 -->
  <g transform="translate(200, 30)">
    <rect x="0" y="10" width="90" height="60" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <circle cx="25" cy="40" r="8" fill="#1d4ed8"/>
    <circle cx="45" cy="40" r="8" fill="#1d4ed8"/>
    <circle cx="65" cy="40" r="8" fill="#1d4ed8"/>
    <text x="45" y="90" font-family="Liberation Sans, sans-serif" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">3 poires</text>
  </g>
  <text x="325" y="70" font-family="Liberation Sans, sans-serif" font-size="24" font-weight="bold" fill="#0f172a" text-anchor="middle">=</text>
  <!-- Grande marmite -->
  <g transform="translate(360, 25)">
    <path d="M 10,25 Q 10,75 80,75 Q 150,75 150,25 Z" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
    <circle cx="35" cy="45" r="7" fill="#b91c1c"/>
    <circle cx="55" cy="45" r="7" fill="#b91c1c"/>
    <circle cx="75" cy="45" r="7" fill="#b91c1c"/>
    <circle cx="95" cy="45" r="7" fill="#b91c1c"/>
    <circle cx="115" cy="45" r="7" fill="#1d4ed8"/>
    <circle cx="65" cy="62" r="7" fill="#1d4ed8"/>
    <circle cx="95" cy="62" r="7" fill="#1d4ed8"/>
    <text x="80" y="100" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#15803d" text-anchor="middle">7 fruits au total</text>
  </g>
  <text x="280" y="145" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">L'addition réunit deux collections distinctes sous un même total</text>
</svg>""")

# diag_010: Balance de justice (5 = 3 + 2)
save_and_verify("fig_03_balance_justice.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Socle et fléau horizontal -->
  <polygon points="270,70 240,170 300,170" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>
  <rect x="210" y="170" width="120" height="15" rx="3" fill="#0f172a"/>
  <circle cx="270" cy="70" r="7" fill="#d97706"/>
  <line x1="80" y1="70" x2="460" y2="70" stroke="#0f172a" stroke-width="4"/>
  <!-- Plateau gauche : [5] -->
  <line x1="120" y1="70" x2="90" y2="125" stroke="#64748b" stroke-width="1.5"/>
  <line x1="120" y1="70" x2="150" y2="125" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 80,125 Q 120,145 160,125 Z" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <rect x="100" y="95" width="40" height="30" rx="4" fill="#1d4ed8"/>
  <text x="120" y="115" font-family="Liberation Sans, sans-serif" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">5</text>
  <!-- Plateau droit : [3] + [2] -->
  <line x1="420" y1="70" x2="390" y2="125" stroke="#64748b" stroke-width="1.5"/>
  <line x1="420" y1="70" x2="450" y2="125" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 380,125 Q 420,145 460,125 Z" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <rect x="390" y="95" width="30" height="30" rx="4" fill="#b91c1c"/>
  <text x="405" y="115" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
  <rect x="425" y="100" width="25" height="25" rx="4" fill="#15803d"/>
  <text x="437" y="117" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
  <text x="270" y="200" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Équilibre parfait : le signe « = » affirme l'égalité exacte des deux plateaux</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 4 : Abaque & Additions / Soustractions posées
# -------------------------------------------------------------
# diag_011: Boîte de calcul / Abaque Dizaines-Unités
save_and_verify("fig_04_abaque_boite.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 170" width="100%" height="170">
  <rect width="500" height="170" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="250" y="28" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">LA BOÎTE DE CALCUL À DEUX CASES</text>
  <g transform="translate(70, 45)">
    <rect x="0" y="0" width="180" height="90" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2" rx="4"/>
    <text x="90" y="30" font-family="Liberation Sans, sans-serif" font-size="15" font-weight="bold" fill="#1d4ed8" text-anchor="middle">DIZAINES (d)</text>
    <text x="90" y="60" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">[ Bouchons de liège ]</text>
    
    <rect x="180" y="0" width="180" height="90" fill="#f0fdf4" stroke="#15803d" stroke-width="2" rx="4"/>
    <text x="270" y="30" font-family="Liberation Sans, sans-serif" font-size="15" font-weight="bold" fill="#15803d" text-anchor="middle">UNITÉS (u)</text>
    <text x="270" y="60" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">[ Petits cailloux ]</text>
  </g>
  <text x="250" y="155" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">On ne mélange jamais les bouchons et les cailloux dans la même case</text>
</svg>""")

# Operations posées : SVG cards with crystal clear typography
def make_op_card(name, title, lines_data, note=""):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 180" width="100%" height="180">
  <rect width="340" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <rect x="15" y="12" width="310" height="28" rx="4" fill="#eff6ff"/>
  <text x="170" y="31" font-family="Liberation Sans, sans-serif" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">{title}</text>
  <g transform="translate(85, 48)" font-family="Liberation Mono, Courier, monospace" font-size="20" font-weight="bold" fill="#0f172a">
"""
    y = 25
    for item in lines_data:
        if item == "line":
            svg += f'    <line x1="0" y1="{y-5}" x2="160" y2="{y-5}" stroke="#0f172a" stroke-width="2"/>\n'
            y += 5
        elif isinstance(item, tuple) and item[0] == "retenue":
            svg += f'    <text x="{item[1]}" y="{y}" font-size="13" fill="#b91c1c">{item[2]}</text>\n'
            y += 18
        else:
            svg += f'    <text x="30" y="{y}">{item}</text>\n'
            y += 24
    svg += f"""  </g>
  <text x="170" y="165" font-family="Liberation Sans, sans-serif" font-size="11" fill="#64748b" text-anchor="middle">{note}</text>
</svg>"""
    save_and_verify(name, svg)

make_op_card("fig_04_addition_sans_retenue.svg", "Addition posée sans retenue", ["d   u", "2   3", "+   4   5", "line", "6   8"], "3 + 5 = 8 unités, 2 + 4 = 6 dizaines")
make_op_card("fig_04_addition_retenue_posee.svg", "Addition posée avec retenue", [("retenue", "42", "(1)"), "d   u", "4   7", "+   3   8", "line", "8   5"], "7 + 8 = 15 : on pose 5 et on retient 1 dizaine")
make_op_card("fig_04_soustraction_posee.svg", "Soustraction posée avec retenue", ["d   u", "8   5", "-   3   8", "line", "4   7"], "15 - 8 = 7 unités, 8 - (3 + 1) = 4 dizaines")
make_op_card("fig_04_operation_mystere_add.svg", "Recherche des chiffres manquants", [("retenue", "40", "(1)"), "3   ★", "+   ★   4", "line", "8   1"], "★ + 4 = 11 ⇒ ★ = 7, puis 1 + 3 + ★ = 8 ⇒ ★ = 4")
make_op_card("fig_04_operation_mystere_sous.svg", "Soustraction à trou", ["6   4", "-   2   ■", "line", "3   7"], "14 - ■ = 7 ⇒ ■ = 7, puis 6 - (2 + 1) = 3")

# -------------------------------------------------------------
# Chapitre 5 : Multiplication, rectangles et doigts
# -------------------------------------------------------------
# diag_016: Mur de briques 4 rangées de 6
save_and_verify("fig_05_mur_briques_4x6.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 190" width="100%" height="190">
  <rect width="540" height="190" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="28" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">LE MUR DE BRIQUES : 4 RANGÉES DE 6</text>
  <g transform="translate(110, 42)">
""" + "\n".join([
    "".join([f'<rect x="{c*52}" y="{r*26}" width="48" height="22" rx="3" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>' for c in range(6)])
    for r in range(4)
]) + """
  </g>
  <text x="80" y="95" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#1d4ed8">4 rangées</text>
  <text x="270" y="165" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#15803d" text-anchor="middle">4 × 6 = 6 + 6 + 6 + 6 = 24 briques</text>
</svg>""")

# diag_017: Tablette couchée vs tournée de 90° (Commutativité)
save_and_verify("fig_05_commutativite_rotation.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 190" width="100%" height="190">
  <rect width="580" height="190" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- 4 x 6 -->
  <g transform="translate(40, 35)">
    <text x="85" y="-10" font-family="Liberation Sans, sans-serif" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">4 rangées de 6 (4 × 6)</text>
""" + "\n".join([
    "".join([f'<rect x="{c*28}" y="{r*24}" width="24" height="20" rx="2" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1"/>' for c in range(6)])
    for r in range(4)
]) + """
  </g>
  <!-- Flèche rotation -->
  <g transform="translate(260, 85)">
    <path d="M 0,-15 A 25 25 0 0 1 35,10" fill="none" stroke="#d97706" stroke-width="3"/>
    <polygon points="35,18 28,8 40,8" fill="#d97706"/>
    <text x="20" y="-22" font-family="Liberation Sans, sans-serif" font-size="11" font-weight="bold" fill="#d97706" text-anchor="middle">Tourner de 90°</text>
  </g>
  <!-- 6 x 4 -->
  <g transform="translate(360, 25)">
    <text x="60" y="-5" font-family="Liberation Sans, sans-serif" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">6 rangées de 4 (6 × 4)</text>
""" + "\n".join([
    "".join([f'<rect x="{c*28}" y="{r*22}" width="24" height="18" rx="2" fill="#f0fdf4" stroke="#15803d" stroke-width="1"/>' for c in range(4)])
    for r in range(6)
]) + """
  </g>
  <text x="290" y="175" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Commutativité : 4 × 6 = 6 × 4 = 24 (l'aire ne change pas par rotation)</text>
</svg>""")

# diag_018: Double et Moitié
save_and_verify("fig_05_double_moitie.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 160" width="100%" height="160">
  <rect width="540" height="160" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Départ : 3 -->
  <g transform="translate(30, 30)">
    <rect x="0" y="10" width="100" height="55" rx="6" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
    <circle cx="25" cy="37" r="8" fill="#64748b"/>
    <circle cx="50" cy="37" r="8" fill="#64748b"/>
    <circle cx="75" cy="37" r="8" fill="#64748b"/>
    <text x="50" y="85" font-family="Liberation Sans, sans-serif" font-size="12" font-weight="bold" fill="#475569" text-anchor="middle">Départ (3)</text>
  </g>
  <!-- Double : x2 -->
  <g transform="translate(180, 20)">
    <rect x="0" y="10" width="150" height="65" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <circle cx="25" cy="42" r="8" fill="#1d4ed8"/>
    <circle cx="45" cy="42" r="8" fill="#1d4ed8"/>
    <circle cx="65" cy="42" r="8" fill="#1d4ed8"/>
    <text x="85" y="47" font-family="Liberation Sans" font-size="14" fill="#0f172a">+</text>
    <circle cx="105" cy="42" r="8" fill="#1d4ed8"/>
    <circle cx="125" cy="42" r="8" fill="#1d4ed8"/>
    <circle cx="145" cy="42" r="8" fill="#1d4ed8"/>
    <text x="85" y="95" font-family="Liberation Sans, sans-serif" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Double (× 2) = 6</text>
  </g>
  <!-- Moitié : ÷2 -->
  <g transform="translate(380, 20)">
    <rect x="0" y="10" width="130" height="65" rx="6" fill="#f0fdf4" stroke="#15803d" stroke-width="1.5"/>
    <circle cx="25" cy="42" r="8" fill="#15803d"/>
    <circle cx="45" cy="42" r="8" fill="#15803d"/>
    <circle cx="65" cy="42" r="8" fill="#15803d"/>
    <line x1="80" y1="20" x2="80" y2="65" stroke="#b91c1c" stroke-width="2" stroke-dasharray="3"/>
    <text x="105" y="47" font-family="Liberation Sans" font-size="12" fill="#64748b">(part)</text>
    <text x="65" y="95" font-family="Liberation Sans, sans-serif" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">Moitié de 6 = 3</text>
  </g>
  <text x="270" y="145" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">Doubler et partager en deux sont des opérations réciproques</text>
</svg>""")

# diag_019: Astuce de la table de 9 sur les doigts (4e doigt baissé = 36)
save_and_verify("fig_05_doigts_table_9.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 180" width="100%" height="180">
  <rect width="540" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="26" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">L'ASTUCE SENSORIELLE DE LA TABLE DE 9 (9 × 4 = 36)</text>
  <g transform="translate(60, 45)">
    <!-- Main gauche : doigts 1, 2, 3 levés, doigt 4 baissé, doigt 5 levé -->
    <rect x="0" y="20" width="16" height="45" rx="4" fill="#1d4ed8"/>
    <text x="8" y="80" font-family="Liberation Sans" font-size="11" fill="#1d4ed8" text-anchor="middle">1</text>
    <rect x="25" y="10" width="16" height="55" rx="4" fill="#1d4ed8"/>
    <text x="33" y="80" font-family="Liberation Sans" font-size="11" fill="#1d4ed8" text-anchor="middle">2</text>
    <rect x="50" y="5" width="16" height="60" rx="4" fill="#1d4ed8"/>
    <text x="58" y="80" font-family="Liberation Sans" font-size="11" fill="#1d4ed8" text-anchor="middle">3</text>
    <!-- Doigt 4 baissé -->
    <rect x="75" y="35" width="16" height="30" rx="4" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
    <text x="83" y="85" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">4 (baissé)</text>
    <rect x="100" y="20" width="16" height="45" rx="4" fill="#15803d"/>
    <text x="108" y="80" font-family="Liberation Sans" font-size="11" fill="#15803d" text-anchor="middle">5</text>
  </g>
  <!-- Main droite : doigts 6, 7, 8, 9, 10 levés -->
  <g transform="translate(260, 45)">
    <rect x="0" y="20" width="16" height="45" rx="4" fill="#15803d"/>
    <text x="8" y="80" font-family="Liberation Sans" font-size="11" fill="#15803d" text-anchor="middle">6</text>
    <rect x="25" y="10" width="16" height="55" rx="4" fill="#15803d"/>
    <text x="33" y="80" font-family="Liberation Sans" font-size="11" fill="#15803d" text-anchor="middle">7</text>
    <rect x="50" y="5" width="16" height="60" rx="4" fill="#15803d"/>
    <text x="58" y="80" font-family="Liberation Sans" font-size="11" fill="#15803d" text-anchor="middle">8</text>
    <rect x="75" y="10" width="16" height="55" rx="4" fill="#15803d"/>
    <text x="83" y="80" font-family="Liberation Sans" font-size="11" fill="#15803d" text-anchor="middle">9</text>
    <rect x="100" y="20" width="16" height="45" rx="4" fill="#15803d"/>
    <text x="108" y="80" font-family="Liberation Sans" font-size="11" fill="#15803d" text-anchor="middle">10</text>
  </g>
  <text x="120" y="155" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">3 doigts à gauche = 3 dizaines</text>
  <text x="360" y="155" font-family="Liberation Sans, sans-serif" font-size="13" font-weight="bold" fill="#15803d" text-anchor="middle">6 doigts à droite = 6 unités</text>
  <text x="480" y="155" font-family="Liberation Sans, sans-serif" font-size="16" font-weight="bold" fill="#b91c1c">➔ 36 !</text>
</svg>""")

# Multiplications posées
make_op_card("fig_05_multiplication_posee_sans_ret.svg", "Multiplication posée sans retenue", ["d   u", "2   4", "×       3", "line", "7   2"], "3 × 4 = 12 (pose 2, retient 1), 3 × 2 + 1 = 7")
make_op_card("fig_05_multiplication_posee_ret.svg", "Multiplication posée étape par étape", [("retenue", "40", "(1)"), "d   u", "2   4", "×       3", "line", "7   2"], "Le produit des unités donne une dizaine voyageuse")
make_op_card("fig_05_multiplication_32x3.svg", "Multiplication posée 32 × 3", ["d   u", "3   2", "×       3", "line", "9   6"], "3 × 2 = 6 unités, 3 × 3 = 9 dizaines")
make_op_card("fig_05_multiplication_mystere.svg", "Opération mystère 2★ × 4 = 96", [("retenue", "40", "(2)"), "2   ★", "×       4", "line", "9   6"], "★ × 4 se termine par 6 ⇒ ★ = 4, car 24 × 4 = 96")

# -------------------------------------------------------------
# Chapitre 6 : Coudée et Sablier (Mesures & Masses)
# -------------------------------------------------------------
# diag_024: La coudée royale égyptienne
save_and_verify("fig_06_coudee_royale.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 160" width="100%" height="160">
  <rect width="540" height="160" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="28" font-family="Liberation Sans, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">LA COUDÉE ROYALE DU PHARAON (~52,3 cm)</text>
  <!-- Dessin de l'avant-bras -->
  <g transform="translate(60, 50)">
    <path d="M 30,35 Q 120,40 250,30 Q 340,25 380,20 L 400,20 L 390,30 L 370,40 Q 250,48 120,45 Q 50,55 30,35 Z" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
    <circle cx="30" cy="35" r="5" fill="#b91c1c"/>
    <text x="30" y="65" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">Pointe du coude</text>
    
    <circle cx="390" cy="20" r="5" fill="#1d4ed8"/>
    <text x="390" y="65" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Bout du majeur</text>
    
    <line x1="30" y1="10" x2="390" y2="10" stroke="#0f172a" stroke-width="2"/>
    <polygon points="30,10 40,7 40,13" fill="#0f172a"/>
    <polygon points="390,10 380,7 380,13" fill="#0f172a"/>
  </g>
  <text x="270" y="145" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">Première étalon historique de longueur fondé sur l'anatomie humaine</text>
</svg>""")

# diag_025: Pesée du melon (1 kg)
save_and_verify("fig_06_pesee_melon_1kg.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 180" width="100%" height="180">
  <rect width="540" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Balance Roberval -->
  <polygon points="270,60 250,140 290,140" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>
  <rect x="220" y="140" width="100" height="15" rx="3" fill="#0f172a"/>
  <!-- Aiguille verticale au centre (équilibre) -->
  <line x1="270" y1="60" x2="270" y2="30" stroke="#b91c1c" stroke-width="2.5"/>
  <circle cx="270" cy="28" r="4" fill="#b91c1c"/>
  <!-- Fléau -->
  <line x1="100" y1="60" x2="440" y2="60" stroke="#0f172a" stroke-width="3"/>
  <!-- Plateau gauche : melon -->
  <line x1="130" y1="60" x2="110" y2="110" stroke="#64748b" stroke-width="1.5"/>
  <line x1="130" y1="60" x2="150" y2="110" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 100,110 Q 130,125 160,110 Z" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
  <circle cx="130" cy="98" r="15" fill="#15803d"/>
  <text x="130" y="140" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">Melon</text>
  <!-- Plateau droit : poids de 1 kg -->
  <line x1="410" y1="60" x2="390" y2="110" stroke="#64748b" stroke-width="1.5"/>
  <line x1="410" y1="60" x2="430" y2="110" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 380,110 Q 410,125 440,110 Z" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
  <rect x="395" y="85" width="30" height="25" rx="3" fill="#d97706"/>
  <text x="410" y="102" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1 kg</text>
  <text x="410" y="140" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#d97706" text-anchor="middle">Masse étalon</text>
  <text x="270" y="170" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">L'aiguille centrée prouve l'égalité rigoureuse des masses : Masse du melon = 1 kg</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 7 : Géométrie, ficelle, pliage et solides
# -------------------------------------------------------------
# diag_026: Carré, rectangle, triangle
save_and_verify("fig_07_formes_fondamentales.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 190" width="100%" height="190">
  <rect width="580" height="190" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Carré -->
  <g transform="translate(30, 25)">
    <rect x="20" y="20" width="80" height="80" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2.5"/>
    <rect x="20" y="80" width="14" height="14" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="60" y="125" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">LE CARRÉ</text>
    <text x="60" y="142" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">4 côtés égaux</text>
    <text x="60" y="156" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">4 angles droits</text>
  </g>
  <!-- Rectangle -->
  <g transform="translate(195, 25)">
    <rect x="10" y="30" width="130" height="70" fill="#f0fdf4" stroke="#15803d" stroke-width="2.5"/>
    <rect x="10" y="86" width="14" height="14" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="75" y="125" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#15803d" text-anchor="middle">LE RECTANGLE</text>
    <text x="75" y="142" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">Côtés opposés égaux</text>
    <text x="75" y="156" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">4 angles droits</text>
  </g>
  <!-- Triangle -->
  <g transform="translate(390, 25)">
    <polygon points="75,20 20,100 130,100" fill="#fffbeb" stroke="#d97706" stroke-width="2.5"/>
    <text x="75" y="125" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#d97706" text-anchor="middle">LE TRIANGLE</text>
    <text x="75" y="142" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">3 côtés</text>
    <text x="75" y="156" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">3 sommets</text>
  </g>
</svg>""")

# diag_027: Tracé du cercle à la ficelle du jardinier
save_and_verify("fig_07_ficelle_jardinier.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Cercle en pointillé -->
  <circle cx="270" cy="105" r="75" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2" stroke-dasharray="4"/>
  <!-- Centre piquet O -->
  <circle cx="270" cy="105" r="6" fill="#b91c1c"/>
  <text x="270" y="95" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">Piquet central (O)</text>
  <!-- Ficelle tendue vers le traceur -->
  <line x1="270" y1="105" x2="345" y2="105" stroke="#d97706" stroke-width="3"/>
  <circle cx="345" cy="105" r="5" fill="#0f172a"/>
  <text x="310" y="122" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#d97706" text-anchor="middle">Ficelle tendue (Rayon)</text>
  <text x="395" y="108" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#0f172a">Piquet traceur</text>
  <!-- Flèche de rotation -->
  <path d="M 345,90 A 75 75 0 0 0 270,30" fill="none" stroke="#15803d" stroke-width="2"/>
  <polygon points="263,30 273,26 273,34" fill="#15803d"/>
  <text x="270" y="195" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">Tous les points du cercle sont à égale distance du piquet central</text>
</svg>""")

# diag_028: Pliage papier pour créer un angle droit
save_and_verify("fig_07_pliage_angle_droit.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 160" width="100%" height="160">
  <rect width="540" height="160" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Étape 1 -->
  <g transform="translate(30, 25)">
    <path d="M 15,20 Q 30,10 60,18 Q 95,25 90,60 Q 80,95 45,90 Q 10,85 15,20 Z" fill="#fffbeb" stroke="#64748b" stroke-width="1.5"/>
    <text x="55" y="115" font-family="Liberation Sans" font-size="11" fill="#475569" text-anchor="middle">1. Feuille quelconque</text>
  </g>
  <text x="160" y="75" font-family="Liberation Sans" font-size="20" fill="#0f172a">➔</text>
  <!-- Étape 2 -->
  <g transform="translate(190, 25)">
    <path d="M 10,20 L 90,20 L 90,85 L 10,85 Z" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <line x1="10" y1="20" x2="90" y2="20" stroke="#b91c1c" stroke-width="3"/>
    <text x="50" y="115" font-family="Liberation Sans" font-size="11" fill="#475569" text-anchor="middle">2. Un pli droit</text>
  </g>
  <text x="315" y="75" font-family="Liberation Sans" font-size="20" fill="#0f172a">➔</text>
  <!-- Étape 3 -->
  <g transform="translate(350, 25)">
    <path d="M 20,20 L 70,20 L 70,85 L 20,85 Z" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
    <rect x="20" y="20" width="14" height="14" fill="none" stroke="#b91c1c" stroke-width="2"/>
    <text x="45" y="115" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">3. Pli sur pli</text>
    <text x="100" y="32" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c">Angle droit !</text>
  </g>
  <text x="270" y="148" font-family="Liberation Sans, sans-serif" font-size="12" fill="#475569" text-anchor="middle">Le demi-tour (180°) partagé en deux moitiés superposables produit exactement 90°</text>
</svg>""")

# diag_029: Les trois solides fondamentaux (Cube, Pavé droit, Cylindre)
save_and_verify("fig_07_solides_fondamentaux.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 180" width="100%" height="180">
  <rect width="580" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Cube -->
  <g transform="translate(30, 25)">
    <rect x="10" y="40" width="55" height="55" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <polygon points="10,40 30,20 85,20 65,40" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.5"/>
    <polygon points="65,40 85,20 85,75 65,95" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="47" y="125" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">LE CUBE</text>
    <text x="47" y="142" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">6 faces carrées</text>
  </g>
  <!-- Pavé droit -->
  <g transform="translate(190, 25)">
    <rect x="10" y="40" width="95" height="55" fill="#f0fdf4" stroke="#15803d" stroke-width="1.5"/>
    <polygon points="10,40 35,20 130,20 105,40" fill="#dcfce7" stroke="#15803d" stroke-width="1.5"/>
    <polygon points="105,40 130,20 130,75 105,95" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
    <text x="70" y="125" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#15803d" text-anchor="middle">LE PAVÉ DROIT</text>
    <text x="70" y="142" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">6 faces rectangulaires</text>
  </g>
  <!-- Cylindre -->
  <g transform="translate(390, 25)">
    <ellipse cx="60" cy="30" rx="35" ry="12" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
    <rect x="25" y="30" width="70" height="60" fill="#fffbeb"/>
    <line x1="25" y1="30" x2="25" y2="90" stroke="#d97706" stroke-width="1.5"/>
    <line x1="95" y1="30" x2="95" y2="90" stroke="#d97706" stroke-width="1.5"/>
    <ellipse cx="60" cy="90" rx="35" ry="12" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="60" y="125" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#d97706" text-anchor="middle">LE CYLINDRE</text>
    <text x="60" y="142" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">2 disques + 1 surface courbe</text>
  </g>
</svg>""")

# diag_030: Axe de symétrie du papillon
save_and_verify("fig_07_papillon_symetrie.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 180" width="100%" height="180">
  <rect width="500" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Axe vertical de symétrie -->
  <line x1="250" y1="15" x2="250" y2="155" stroke="#b91c1c" stroke-width="2" stroke-dasharray="5"/>
  <text x="250" y="170" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">Axe de symétrie (pliage)</text>
  <!-- Papillon gauche -->
  <g fill="#eff6ff" stroke="#1d4ed8" stroke-width="2">
    <path d="M 250,50 Q 150,20 160,80 Q 170,110 250,90 Z"/>
    <path d="M 250,90 Q 180,110 190,140 Q 220,150 250,110 Z"/>
    <circle cx="185" cy="65" r="8" fill="#d97706" stroke="none"/>
  </g>
  <text x="180" y="130" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Aile gauche</text>
  <!-- Papillon droite (symétrique exacte) -->
  <g fill="#eff6ff" stroke="#1d4ed8" stroke-width="2">
    <path d="M 250,50 Q 350,20 340,80 Q 330,110 250,90 Z"/>
    <path d="M 250,90 Q 320,110 310,140 Q 280,150 250,110 Z"/>
    <circle cx="315" cy="65" r="8" fill="#d97706" stroke="none"/>
  </g>
  <text x="320" y="130" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Aile droite</text>
  <!-- Corps au milieu -->
  <ellipse cx="250" cy="85" rx="5" ry="30" fill="#0f172a"/>
</svg>""")

# diag_031: Grille de repérage case (C, 3) et (B, 2)
save_and_verify("fig_07_grille_reperage.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 190" width="100%" height="190">
  <rect width="500" height="190" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(60, 30)">
    <!-- En-têtes colonnes A, B, C, D -->
    <text x="50" y="-10" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">A</text>
    <text x="110" y="-10" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">B</text>
    <text x="170" y="-10" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">C</text>
    <text x="230" y="-10" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">D</text>
    
    <!-- En-têtes lignes 3, 2, 1 -->
    <text x="8" y="25" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">3</text>
    <text x="8" y="65" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">2</text>
    <text x="8" y="105" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">1</text>
    
    <!-- Quadrillage -->
    <rect x="20" y="0" width="240" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    <line x1="80" y1="0" x2="80" y2="120" stroke="#cbd5e1" stroke-width="1.5"/>
    <line x1="140" y1="0" x2="140" y2="120" stroke="#cbd5e1" stroke-width="1.5"/>
    <line x1="200" y1="0" x2="200" y2="120" stroke="#cbd5e1" stroke-width="1.5"/>
    
    <line x1="20" y1="40" x2="260" y2="40" stroke="#cbd5e1" stroke-width="1.5"/>
    <line x1="20" y1="80" x2="260" y2="80" stroke="#cbd5e1" stroke-width="1.5"/>
    
    <!-- Étoile en (C, 3) -->
    <rect x="140" y="0" width="60" height="40" fill="#fffbeb"/>
    <text x="170" y="28" font-size="20" text-anchor="middle">★</text>
    
    <!-- Robot en (B, 2) -->
    <rect x="80" y="40" width="60" height="40" fill="#eff6ff"/>
    <text x="110" y="68" font-size="20" text-anchor="middle">🤖</text>
  </g>
  <g transform="translate(330, 60)" font-family="Liberation Sans" font-size="12">
    <text x="0" y="15" fill="#d97706" font-weight="bold">★ Étoile : Case (C, 3)</text>
    <text x="0" y="45" fill="#1d4ed8" font-weight="bold">🤖 Robot : Case (B, 2)</text>
    <text x="0" y="80" fill="#64748b">Colonne d'abord,</text>
    <text x="0" y="96" fill="#64748b">Ligne ensuite !</text>
  </g>
</svg>""")

# diag_032: Grille fruits 3x2
save_and_verify("fig_07_grille_fruits.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 170" width="100%" height="170">
  <rect width="460" height="170" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(60, 30)">
    <text x="50" y="-10" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">A</text>
    <text x="110" y="-10" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">B</text>
    <text x="170" y="-10" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">C</text>
    <text x="8" y="30" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">2</text>
    <text x="8" y="75" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">1</text>
    
    <rect x="20" y="0" width="180" height="90" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    <line x1="80" y1="0" x2="80" y2="90" stroke="#cbd5e1" stroke-width="1.5"/>
    <line x1="140" y1="0" x2="140" y2="90" stroke="#cbd5e1" stroke-width="1.5"/>
    <line x1="20" y1="45" x2="200" y2="45" stroke="#cbd5e1" stroke-width="1.5"/>
    
    <text x="110" y="32" font-size="20" text-anchor="middle">🍎</text>
    <text x="50" y="77" font-size="20" text-anchor="middle">🍌</text>
    <text x="170" y="77" font-size="20" text-anchor="middle">🍇</text>
  </g>
  <g transform="translate(280, 50)" font-family="Liberation Sans" font-size="12">
    <text x="0" y="15" fill="#b91c1c" font-weight="bold">🍎 Pomme : (B, 2)</text>
    <text x="0" y="40" fill="#d97706" font-weight="bold">🍌 Banane : (A, 1)</text>
    <text x="0" y="65" fill="#7e22ce" font-weight="bold">🍇 Raisin : (C, 1)</text>
  </g>
</svg>""")

print("Volume I: All 26 SVG figures generated and verified successfully.")
