# -*- coding: utf-8 -*-
"""
SVG Generator for Volume III (LA VOIE DU NOMBRE)
"""
import os
import xml.etree.ElementTree as ET

out_dir = r"c:\Silvere\Encours\Developpement\Articles\livre_mathematiques\figures\vol_3"
os.makedirs(out_dir, exist_ok=True)

def save_and_verify(name, svg_content):
    path = os.path.join(out_dir, name)
    svg_clean = svg_content.strip()
    try:
        ET.fromstring(svg_clean)
    except Exception as e:
        print(f"XML ERROR in {name}: {e}")
        raise e
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_clean)
    return path

# -------------------------------------------------------------
# Chapitre 15 : Angles & Géométrie du Nil
# -------------------------------------------------------------
# Anatomie d'un angle
save_and_verify("fig_15_anatomie_angle.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 180" width="100%" height="180">
  <rect width="500" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(80, 130)">
    <!-- Côté [BA) horizontal -->
    <line x1="0" y1="0" x2="220" y2="0" stroke="#1d4ed8" stroke-width="3"/>
    <circle cx="220" cy="0" r="4" fill="#1d4ed8"/>
    <text x="235" y="5" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#1d4ed8">A</text>
    <text x="120" y="22" font-family="Liberation Sans" font-size="12" fill="#64748b">Côté [BA)</text>
    
    <!-- Côté [BC) oblique -->
    <line x1="0" y1="0" x2="160" y2="-90" stroke="#1d4ed8" stroke-width="3"/>
    <circle cx="160" cy="-90" r="4" fill="#1d4ed8"/>
    <text x="175" y="-95" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#1d4ed8">C</text>
    <text x="60" y="-65" font-family="Liberation Sans" font-size="12" fill="#64748b">Côté [BC)</text>
    
    <!-- Sommet B -->
    <circle cx="0" cy="0" r="6" fill="#b91c1c"/>
    <text x="-25" y="5" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#b91c1c">B</text>
    <text x="-45" y="24" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c">Sommet</text>
    
    <!-- Arc d'ouverture angulaire -->
    <path d="M 60,0 A 60 60 0 0 0 52,-29" fill="none" stroke="#d97706" stroke-width="2.5"/>
    <text x="75" y="-12" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#d97706">Ouverture angulaire</text>
  </g>
  <text x="250" y="165" font-family="Liberation Sans" font-size="12" fill="#475569" text-anchor="middle">L'angle mesure l'écartement des deux demi-droites, indépendamment de leur longueur</text>
</svg>""")

# 4 types d'angles
save_and_verify("fig_15_quatre_types_angles.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 160" width="100%" height="160">
  <rect width="580" height="160" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Aigu -->
  <g transform="translate(30, 30)">
    <line x1="0" y1="80" x2="80" y2="80" stroke="#1d4ed8" stroke-width="2.5"/>
    <line x1="0" y1="80" x2="60" y2="20" stroke="#1d4ed8" stroke-width="2.5"/>
    <path d="M 30,80 A 30 30 0 0 0 21,59" fill="none" stroke="#d97706" stroke-width="2"/>
    <text x="40" y="110" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">ANGLE AIGU</text>
    <text x="40" y="125" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">&lt; 90°</text>
  </g>
  <!-- Droit -->
  <g transform="translate(170, 30)">
    <line x1="0" y1="80" x2="80" y2="80" stroke="#15803d" stroke-width="2.5"/>
    <line x1="0" y1="80" x2="0" y2="10" stroke="#15803d" stroke-width="2.5"/>
    <rect x="0" y="66" width="14" height="14" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="40" y="110" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">ANGLE DROIT</text>
    <text x="40" y="125" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">= 90°</text>
  </g>
  <!-- Obtus -->
  <g transform="translate(310, 30)">
    <line x1="40" y1="80" x2="110" y2="80" stroke="#d97706" stroke-width="2.5"/>
    <line x1="40" y1="80" x2="0" y2="30" stroke="#d97706" stroke-width="2.5"/>
    <path d="M 65,80 A 25 25 0 0 0 24,60" fill="none" stroke="#b91c1c" stroke-width="2"/>
    <text x="60" y="110" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#d97706" text-anchor="middle">ANGLE OBTUS</text>
    <text x="60" y="125" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">&gt; 90° et &lt; 180°</text>
  </g>
  <!-- Plat -->
  <g transform="translate(460, 30)">
    <line x1="0" y1="80" x2="90" y2="80" stroke="#7e22ce" stroke-width="2.5"/>
    <circle cx="45" cy="80" r="3.5" fill="#7e22ce"/>
    <path d="M 65,80 A 20 20 0 0 0 25,80" fill="none" stroke="#7e22ce" stroke-width="2"/>
    <text x="45" y="110" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#7e22ce" text-anchor="middle">ANGLE PLAT</text>
    <text x="45" y="125" font-family="Liberation Sans" font-size="10.5" fill="#64748b" text-anchor="middle">= 180°</text>
  </g>
</svg>""")

# Angles opposés par le sommet
save_and_verify("fig_15_angles_opposes.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 170" width="100%" height="170">
  <rect width="480" height="170" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="240" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">ANGLES OPPOSÉS PAR LE SOMMET</text>
  <g transform="translate(240, 95)">
    <!-- Droite 1 -->
    <line x1="-150" y1="0" x2="150" y2="0" stroke="#0f172a" stroke-width="2"/>
    <!-- Droite 2 sécante -->
    <line x1="-120" y1="50" x2="120" y2="-50" stroke="#0f172a" stroke-width="2"/>
    <circle cx="0" cy="0" r="4" fill="#0f172a"/>
    <!-- Angles opposés 1 et 3 en bleu -->
    <path d="M 40,0 A 40 40 0 0 1 37,-15" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <text x="60" y="-12" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8">1</text>
    
    <path d="M -40,0 A 40 40 0 0 1 -37,15" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <text x="-65" y="18" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8">3</text>
    
    <!-- Angles 2 et 4 en vert -->
    <text x="-15" y="-22" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#15803d">2</text>
    <text x="15" y="28" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#15803d">4</text>
  </g>
  <text x="240" y="155" font-family="Liberation Sans" font-size="12" fill="#1d4ed8" font-weight="bold" text-anchor="middle">Les angles opposés par le sommet ont exactement la même mesure : Angle 1 = Angle 3</text>
</svg>""")

# Propriété des droites perpendiculaires et parallèles
save_and_verify("fig_15_paralleles_perpendiculaires.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 170" width="100%" height="170">
  <rect width="520" height="170" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Propriété 1 -->
  <g transform="translate(40, 25)">
    <line x1="0" y1="60" x2="200" y2="60" stroke="#0f172a" stroke-width="2"/>
    <text x="205" y="64" font-family="Liberation Sans" font-size="11" fill="#0f172a">(d)</text>
    
    <line x1="50" y1="10" x2="50" y2="110" stroke="#1d4ed8" stroke-width="2.5"/>
    <text x="45" y="125" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#1d4ed8">(d₁)</text>
    <rect x="50" y="48" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
    
    <line x1="140" y1="10" x2="140" y2="110" stroke="#1d4ed8" stroke-width="2.5"/>
    <text x="135" y="125" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#1d4ed8">(d₂)</text>
    <rect x="140" y="48" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
    
    <text x="100" y="145" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">(d₁) ⊥ (d) et (d₂) ⊥ (d) ⟹ (d₁) // (d₂)</text>
  </g>
  <!-- Séparateur -->
  <line x1="280" y1="20" x2="280" y2="150" stroke="#cbd5e1" stroke-width="1.5"/>
  <!-- Propriété 2 -->
  <g transform="translate(300, 25)">
    <line x1="10" y1="35" x2="190" y2="35" stroke="#15803d" stroke-width="2"/>
    <text x="195" y="39" font-family="Liberation Sans" font-size="11" fill="#15803d">(d₁)</text>
    
    <line x1="10" y1="85" x2="190" y2="85" stroke="#15803d" stroke-width="2"/>
    <text x="195" y="89" font-family="Liberation Sans" font-size="11" fill="#15803d">(d₂)</text>
    
    <line x1="80" y1="10" x2="80" y2="110" stroke="#b91c1c" stroke-width="2.5"/>
    <text x="75" y="125" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c">(d₃)</text>
    <rect x="80" y="23" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
    <rect x="80" y="73" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
    
    <text x="100" y="145" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">(d₁) // (d₂) et (d₃) ⊥ (d₁) ⟹ (d₃) ⊥ (d₂)</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 16 : Le Cercle & Archimède
# -------------------------------------------------------------
# Vocabulaire du cercle
save_and_verify("fig_16_vocabulaire_cercle.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(160, 105)">
    <circle cx="0" cy="0" r="75" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <circle cx="0" cy="0" r="4" fill="#0f172a"/>
    <text x="-12" y="4" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">O</text>
    
    <!-- Rayon OA -->
    <line x1="0" y1="0" x2="53" y2="-53" stroke="#15803d" stroke-width="2.5"/>
    <text x="32" y="-22" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#15803d">Rayon r</text>
    
    <!-- Diamètre BC -->
    <line x1="-75" y1="0" x2="75" y2="0" stroke="#b91c1c" stroke-width="2.5"/>
    <text x="-40" y="-8" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c">Diamètre d = 2r</text>
    
    <!-- Corde et Arc DE -->
    <line x1="-53" y1="53" x2="53" y2="53" stroke="#d97706" stroke-width="2"/>
    <text x="0" y="47" font-family="Liberation Sans" font-size="10.5" font-weight="bold" fill="#d97706" text-anchor="middle">Corde [DE]</text>
    <path d="M -53,53 A 75 75 0 0 0 53,53" fill="none" stroke="#7e22ce" stroke-width="3"/>
  </g>
  <g transform="translate(310, 40)" font-family="Liberation Sans" font-size="12">
    <text x="0" y="20" fill="#0f172a" font-weight="bold">Éléments géométriques :</text>
    <text x="0" y="45" fill="#15803d">• Rayon r : distance du centre au bord</text>
    <text x="0" y="70" fill="#b91c1c">• Diamètre d = 2r : corde passant par le centre</text>
    <text x="0" y="95" fill="#d97706">• Corde : segment joignant 2 points</text>
    <text x="0" y="120" fill="#7e22ce">• Arc : portion courbe du cercle</text>
    <text x="0" y="150" fill="#1d4ed8" font-weight="bold">Périmètre = 2 × π × r = π × d</text>
  </g>
</svg>""")

# Déroulement du cercle : mesure de pi
save_and_verify("fig_16_deroulement_cercle_pi.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 170" width="100%" height="170">
  <rect width="560" height="170" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">LE DÉROULEMENT DU CERCLE : 1 TOUR COMPLET = π × d</text>
  <!-- Ligne de sol -->
  <line x1="30" y1="120" x2="530" y2="120" stroke="#0f172a" stroke-width="2"/>
  <!-- Cercle de départ -->
  <circle cx="80" cy="80" r="40" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="80" cy="120" r="4" fill="#b91c1c"/>
  <text x="80" y="136" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">Départ (0)</text>
  <!-- Cercle d'arrivée (1 tour complet) -->
  <circle cx="430" cy="80" r="40" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2" stroke-dasharray="3"/>
  <circle cx="430" cy="120" r="4" fill="#b91c1c"/>
  <text x="430" y="136" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">Arrivée</text>
  <!-- Segment déroulé -->
  <line x1="80" y1="120" x2="430" y2="120" stroke="#b91c1c" stroke-width="3"/>
  <text x="255" y="112" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">Longueur déroulée = Périmètre = π × d ≈ 3,1416 × d</text>
  <text x="255" y="80" font-family="Liberation Sans" font-size="11" fill="#475569" text-anchor="middle">La roue fait un peu plus de 3 tours de son diamètre sur le sol</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 17, 18, 19, 20 : Thalès, Échiquier, Pythagore, Repère
# -------------------------------------------------------------
# Théorème de Thalès : Ombre de la pyramide
save_and_verify("fig_17_thales_pyramide.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 200" width="100%" height="200">
  <rect width="540" height="200" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">LA MESURE DE LA PYRAMIDE PAR THALÈS DE MILET</text>
  <!-- Sol -->
  <line x1="30" y1="150" x2="510" y2="150" stroke="#0f172a" stroke-width="2"/>
  <!-- Rayons solaires parallèles -->
  <line x1="70" y1="40" x2="250" y2="150" stroke="#d97706" stroke-width="1.5" stroke-dasharray="4"/>
  <line x1="280" y1="70" x2="410" y2="150" stroke="#d97706" stroke-width="1.5" stroke-dasharray="4"/>
  <!-- Pyramide -->
  <polygon points="120,50 30,150 210,150" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
  <line x1="120" y1="50" x2="120" y2="150" stroke="#b91c1c" stroke-width="2" stroke-dasharray="3"/>
  <text x="105" y="105" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">H ?</text>
  <text x="175" y="165" font-family="Liberation Sans" font-size="11" fill="#475569">Ombre L</text>
  <!-- Bâton planté droit -->
  <line x1="330" y1="100" x2="330" y2="150" stroke="#1d4ed8" stroke-width="3"/>
  <text x="315" y="130" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8">h</text>
  <text x="365" y="165" font-family="Liberation Sans" font-size="11" fill="#475569">Ombre l</text>
  <!-- Formule de proportionnalité -->
  <rect x="360" y="55" width="150" height="50" rx="4" fill="#eff6ff" stroke="#1d4ed8"/>
  <text x="435" y="75" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">H / L = h / l</text>
  <text x="435" y="95" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">H = h × (L / l)</text>
</svg>""")

# Théorème de Pythagore
save_and_verify("fig_19_pythagore_puzzle.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="220">
  <rect width="520" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="260" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">LE THÉORÈME DE PYTHAGORE : a² + b² = c²</text>
  <g transform="translate(180, 150)">
    <!-- Triangle rectangle (3, 4, 5) -->
    <polygon points="0,0 80,0 0,-60" fill="#f0fdf4" stroke="#15803d" stroke-width="2.5"/>
    <rect x="0" y="-12" width="12" height="12" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="40" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">b = 4</text>
    <text x="-18" y="-30" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#d97706" text-anchor="middle">a = 3</text>
    <text x="50" y="-38" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c" text-anchor="middle">c = 5</text>
    
    <!-- Carré sur b (4x4) -->
    <rect x="0" y="0" width="80" height="40" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="40" y="24" font-family="Liberation Sans" font-size="11" fill="#1d4ed8" text-anchor="middle">Aire b² = 16</text>
    
    <!-- Carré sur a (3x3) -->
    <rect x="-40" y="-60" width="40" height="60" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
    <text x="-20" y="-28" font-family="Liberation Sans" font-size="10" fill="#d97706" text-anchor="middle">Aire a² = 9</text>
  </g>
  <g transform="translate(350, 80)" font-family="Liberation Sans">
    <rect x="0" y="0" width="140" height="70" rx="6" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
    <text x="70" y="25" font-size="13" font-weight="bold" fill="#b91c1c" text-anchor="middle">a² + b² = c²</text>
    <text x="70" y="45" font-size="12" fill="#0f172a" text-anchor="middle">9 + 16 = 25</text>
    <text x="70" y="60" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">√25 = 5</text>
  </g>
</svg>""")

# Repère cartésien 2D
save_and_verify("fig_20_repere_cartesien_2d.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 210" width="100%" height="210">
  <rect width="520" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(160, 110)">
    <!-- Axes x et y -->
    <line x1="-130" y1="0" x2="150" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="155,0 145,-4 145,4" fill="#0f172a"/>
    <text x="145" y="18" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">x</text>
    
    <line x1="0" y1="90" x2="0" y2="-90" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-95 -4,-85 4,-85" fill="#0f172a"/>
    <text x="10" y="-85" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">y</text>
    <text x="-12" y="15" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#64748b">O</text>
    
    <!-- Graduations -->
""" + "\n".join([
    f'<line x1="{x*30}" y1="-3" x2="{x*30}" y2="3" stroke="#0f172a" stroke-width="1.5"/>\n'
    f'<text x="{x*30}" y="15" font-family="Liberation Sans" font-size="10" fill="#64748b" text-anchor="middle">{x}</text>'
    for x in [-3, -2, -1, 1, 2, 3, 4]
]) + "\n" + "\n".join([
    f'<line x1="-3" y1="{-y*30}" x2="3" y2="{-y*30}" stroke="#0f172a" stroke-width="1.5"/>\n'
    f'<text x="-12" y="{-y*30 + 4}" font-family="Liberation Sans" font-size="10" fill="#64748b" text-anchor="middle">{y}</text>'
    for y in [-2, -1, 1, 2]
]) + """
    <!-- Point A(3, 2) -->
    <line x1="90" y1="0" x2="90" y2="-60" stroke="#1d4ed8" stroke-width="1.5" stroke-dasharray="3"/>
    <line x1="0" y1="-60" x2="90" y2="-60" stroke="#1d4ed8" stroke-width="1.5" stroke-dasharray="3"/>
    <circle cx="90" cy="-60" r="5" fill="#b91c1c"/>
    <text x="105" y="-65" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c">A (3 ; 2)</text>
  </g>
  <g transform="translate(340, 60)" font-family="Liberation Sans" font-size="12">
    <text x="0" y="15" font-weight="bold" fill="#0f172a">Coordonnées du point :</text>
    <text x="0" y="40" fill="#1d4ed8">• Abscisse x = 3 (horizontal)</text>
    <text x="0" y="65" fill="#15803d">• Ordonnée y = 2 (vertical)</text>
    <text x="0" y="95" fill="#64748b">René Descartes (1637) :</text>
    <text x="0" y="112" fill="#64748b">unir algèbre et géométrie</text>
  </g>
</svg>""")

print("Volume III: All SVG figures generated and verified successfully.")
