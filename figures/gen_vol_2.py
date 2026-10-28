# -*- coding: utf-8 -*-
"""
SVG Generator for Volume II (LA VOIE DU NOMBRE)
"""
import os
import xml.etree.ElementTree as ET

out_dir = r"c:\Silvere\Encours\Developpement\Articles\livre_mathematiques\figures\vol_2"
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
# Chapitre 8 & 9 : Premiers & Division
# -------------------------------------------------------------
# Arbre de décomposition de 60
save_and_verify("fig_08_decomposition_premiers.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 200" width="100%" height="200">
  <rect width="500" height="200" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="250" y="25" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">L'ARBRE DES FACTEURS PREMIERS DE 60</text>
  <!-- Racine 60 -->
  <circle cx="250" cy="55" r="16" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <text x="250" y="60" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#1d4ed8" text-anchor="middle">60</text>
  <!-- Branche 1 : 6 et 10 -->
  <line x1="238" y1="68" x2="170" y2="105" stroke="#64748b" stroke-width="2"/>
  <line x1="262" y1="68" x2="330" y2="105" stroke="#64748b" stroke-width="2"/>
  <circle cx="170" cy="110" r="14" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
  <text x="170" y="115" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">6</text>
  <circle cx="330" cy="110" r="14" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
  <text x="330" y="115" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">10</text>
  <!-- Feuilles : 2, 3, 2, 5 (premiers) -->
  <line x1="160" y1="122" x2="125" y2="155" stroke="#64748b" stroke-width="2"/>
  <line x1="180" y1="122" x2="215" y2="155" stroke="#64748b" stroke-width="2"/>
  <circle cx="125" cy="160" r="13" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
  <text x="125" y="165" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c" text-anchor="middle">2</text>
  <circle cx="215" cy="160" r="13" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
  <text x="215" y="165" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c" text-anchor="middle">3</text>
  
  <line x1="320" y1="122" x2="285" y2="155" stroke="#64748b" stroke-width="2"/>
  <line x1="340" y1="122" x2="375" y2="155" stroke="#64748b" stroke-width="2"/>
  <circle cx="285" cy="160" r="13" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
  <text x="285" y="165" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c" text-anchor="middle">2</text>
  <circle cx="375" cy="160" r="13" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
  <text x="375" y="165" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c" text-anchor="middle">5</text>
  
  <text x="435" y="165" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c">Atomes premiers</text>
</svg>""")

# Deux sens de la division
save_and_verify("fig_09_sens_division.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 160" width="100%" height="160">
  <rect width="540" height="160" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <rect x="20" y="55" width="130" height="50" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <text x="85" y="85" font-family="Liberation Sans" font-size="15" font-weight="bold" fill="#1d4ed8" text-anchor="middle">LA DIVISION</text>
  
  <line x1="150" y1="70" x2="210" y2="45" stroke="#0f172a" stroke-width="2"/>
  <polygon points="215,43 205,42 209,50" fill="#0f172a"/>
  <rect x="220" y="20" width="290" height="48" rx="6" fill="#f0fdf4" stroke="#15803d" stroke-width="1.5"/>
  <text x="235" y="38" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#15803d">1. LE PARTAGE (Combien chacun ?)</text>
  <text x="235" y="55" font-family="Liberation Sans" font-size="11" fill="#475569">On connaît le nombre de parts, on cherche la taille.</text>
  
  <line x1="150" y1="90" x2="210" y2="115" stroke="#0f172a" stroke-width="2"/>
  <polygon points="215,117 209,110 205,118" fill="#0f172a"/>
  <rect x="220" y="90" width="290" height="48" rx="6" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
  <text x="235" y="108" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#d97706">2. LE GROUPEMENT (Combien de paquets ?)</text>
  <text x="235" y="125" font-family="Liberation Sans" font-size="11" fill="#475569">On connaît la taille d'un paquet, on cherche le nombre.</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 10 : Fractions
# -------------------------------------------------------------
save_and_verify("fig_10_galette_quarts.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 170" width="100%" height="170">
  <rect width="500" height="170" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Galette coupée en 4 -->
  <g transform="translate(100, 85)">
    <circle cx="0" cy="0" r="55" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
    <line x1="-55" y1="0" x2="55" y2="0" stroke="#b91c1c" stroke-width="2"/>
    <line x1="0" y1="-55" x2="0" y2="55" stroke="#b91c1c" stroke-width="2"/>
    <path d="M 0,0 L 55,0 A 55 55 0 0 1 0,55 Z" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <text x="25" y="32" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">1/4</text>
  </g>
  <g transform="translate(230, 45)" font-family="Liberation Sans">
    <text x="0" y="20" font-size="14" font-weight="bold" fill="#0f172a">1 galette partagée entre 4 enfants</text>
    <text x="0" y="45" font-size="12" fill="#475569">Chaque tranche représente exactement un quart (1/4).</text>
    <text x="0" y="70" font-size="12" fill="#15803d" font-weight="bold">4 tranches de 1/4 reforment la galette entière :</text>
    <text x="0" y="95" font-size="14" font-weight="bold" fill="#1d4ed8">1/4 + 1/4 + 1/4 + 1/4 = 4/4 = 1 entier</text>
  </g>
</svg>""")

# Anatomie fraction 3/4
save_and_verify("fig_10_numerateur_denominateur.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 160" width="100%" height="160">
  <rect width="520" height="160" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Fraction 3/4 -->
  <g transform="translate(80, 80)">
    <text x="0" y="-12" font-family="Liberation Serif" font-size="34" font-weight="bold" fill="#1d4ed8" text-anchor="middle">3</text>
    <line x1="-25" y1="0" x2="25" y2="0" stroke="#0f172a" stroke-width="3.5"/>
    <text x="0" y="35" font-family="Liberation Serif" font-size="34" font-weight="bold" fill="#b91c1c" text-anchor="middle">4</text>
  </g>
  <!-- Explications fléchées -->
  <g transform="translate(140, 30)" font-family="Liberation Sans">
    <path d="M 0,25 L 30,10 L 70,10" fill="none" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="80" y="14" font-size="12" font-weight="bold" fill="#1d4ed8">LE NUMÉRATEUR (latin numerare = compter)</text>
    <text x="80" y="30" font-size="11" fill="#475569">Il COMPTE le nombre de parts choisies (ici 3 parts).</text>
    
    <path d="M 0,50 L 50,50" fill="none" stroke="#0f172a" stroke-width="1.5"/>
    <text x="60" y="54" font-size="11" font-weight="bold" fill="#0f172a">Trait de fraction : l'opérateur de partage (division)</text>
    
    <path d="M 0,75 L 30,90 L 70,90" fill="none" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="80" y="94" font-size="12" font-weight="bold" fill="#b91c1c">LE DÉNOMINATEUR (latin denominare = nommer)</text>
    <text x="80" y="110" font-size="11" fill="#475569">Il NOMME la taille de la famille (coupé en 4 parts égales).</text>
  </g>
</svg>""")

# Fractions équivalentes 1/2 = 2/4
save_and_verify("fig_10_bandes_equivalentes.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 150" width="100%" height="150">
  <rect width="520" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Bande 1/2 -->
  <g transform="translate(40, 25)">
    <rect x="0" y="0" width="200" height="35" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <rect x="0" y="0" width="100" height="35" fill="#1d4ed8"/>
    <text x="50" y="23" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1 / 2</text>
    <text x="150" y="23" font-family="Liberation Sans" font-size="12" fill="#1d4ed8" text-anchor="middle">1 / 2</text>
    <text x="215" y="23" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8">1 part sur 2</text>
  </g>
  <!-- Bande 2/4 -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="200" height="35" fill="#eff6ff" stroke="#15803d" stroke-width="2"/>
    <rect x="0" y="0" width="100" height="35" fill="#15803d"/>
    <line x1="50" y1="0" x2="50" y2="35" stroke="#ffffff" stroke-width="2"/>
    <text x="25" y="23" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1/4</text>
    <text x="75" y="23" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1/4</text>
    <text x="215" y="23" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#15803d">2 parts sur 4</text>
  </g>
  <text x="260" y="135" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Égalité visuelle : 1/2 = 2/4 (la même surface colorée)</text>
</svg>""")

# Droite graduée en quarts
save_and_verify("fig_10_droite_graduee_quarts.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 140" width="100%" height="140">
  <rect width="560" height="140" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Axe horizontal -->
  <line x1="40" y1="70" x2="520" y2="70" stroke="#0f172a" stroke-width="2"/>
  <polygon points="525,70 515,66 515,74" fill="#0f172a"/>
  <!-- Graduations de 0 à 2 par pas de 1/4 -->
""" + "\n".join([
    f'<line x1="{50 + i*55}" y1="{60 if i%4==0 else 64}" x2="{50 + i*55}" y2="{80 if i%4==0 else 76}" stroke="#0f172a" stroke-width="{2.5 if i%4==0 else 1.5}"/>\n'
    f'<text x="{50 + i*55}" y="98" font-family="Liberation Sans" font-size="{12 if i%4==0 else 10}" font-weight="{"bold" if i%4==0 else "normal"}" fill="#0f172a" text-anchor="middle">{i//4 if i%4==0 else f"{i}/4"}</text>'
    for i in range(9)
]) + """
  <!-- Point A (1/4), B (1 = 4/4), C (7/4) -->
  <circle cx="105" cy="70" r="5" fill="#1d4ed8"/>
  <text x="105" y="50" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">A (1/4)</text>
  <circle cx="270" cy="70" r="5" fill="#15803d"/>
  <text x="270" y="50" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">B (1 = 4/4)</text>
  <circle cx="435" cy="70" r="5" fill="#b91c1c"/>
  <text x="435" y="50" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">C (7/4)</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 11, 12, 13, 14 : Nombres décimaux, mesures, relatifs
# -------------------------------------------------------------
# Glissement de la virgule
save_and_verify("fig_11_glissement_virgule.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 160" width="100%" height="160">
  <rect width="520" height="160" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="260" y="25" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">MULTIPLICATION PAR 10, 100, 1000 : GLISSEMENT DE LA VIRGULE</text>
  <g transform="translate(60, 45)" font-family="Liberation Sans" font-size="13">
    <text x="0" y="25" font-weight="bold" fill="#1d4ed8">3,45 × 10</text>
    <text x="140" y="25" fill="#0f172a">➔ glisse de 1 rang vers la droite ➔</text>
    <text x="360" y="25" font-weight="bold" fill="#15803d">34,5</text>
    
    <text x="0" y="55" font-weight="bold" fill="#1d4ed8">3,45 × 100</text>
    <text x="140" y="55" fill="#0f172a">➔ glisse de 2 rangs vers la droite ➔</text>
    <text x="360" y="55" font-weight="bold" fill="#15803d">345</text>
    
    <text x="0" y="85" font-weight="bold" fill="#1d4ed8">3,45 × 1 000</text>
    <text x="140" y="85" fill="#0f172a">➔ glisse de 3 rangs vers la droite ➔</text>
    <text x="360" y="85" font-weight="bold" fill="#15803d">3 450</text>
  </g>
</svg>""")

# Méridienne terrestre et le Mètre
save_and_verify("fig_12_meridienne_metre.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 180" width="100%" height="180">
  <rect width="520" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="260" y="25" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">LA DÉFINITION RÉVOLUTIONNAIRE DU MÈTRE (1795)</text>
  <!-- Globe terrestre schématique -->
  <g transform="translate(110, 105)">
    <circle cx="0" cy="0" r="55" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <ellipse cx="0" cy="0" rx="55" ry="16" fill="none" stroke="#94a3b8" stroke-dasharray="3"/>
    <!-- Quart de méridien Pôle Nord -> Équateur -->
    <path d="M 0,-55 A 55 55 0 0 1 55,0" fill="none" stroke="#b91c1c" stroke-width="3.5"/>
    <circle cx="0" cy="-55" r="4" fill="#b91c1c"/>
    <text x="-5" y="-62" font-family="Liberation Sans" font-size="10" font-weight="bold" fill="#b91c1c" text-anchor="end">Pôle Nord</text>
    <circle cx="55" cy="0" r="4" fill="#b91c1c"/>
    <text x="65" y="4" font-family="Liberation Sans" font-size="10" font-weight="bold" fill="#b91c1c">Équateur</text>
    <circle cx="38" cy="-38" r="3" fill="#d97706"/>
    <text x="45" y="-38" font-family="Liberation Sans" font-size="9" fill="#d97706">Dunkerque-Barcelone</text>
  </g>
  <g transform="translate(230, 65)" font-family="Liberation Sans">
    <text x="0" y="15" font-size="12" font-weight="bold" fill="#b91c1c">Distance Pôle Nord - Équateur</text>
    <text x="0" y="35" font-size="12" fill="#0f172a">divisée par 10 000 000</text>
    <text x="0" y="60" font-size="15" font-weight="bold" fill="#15803d">= EXACTEMENT 1 MÈTRE !</text>
    <text x="0" y="80" font-size="11" fill="#64748b">Une mesure universelle empruntée à la Terre</text>
  </g>
</svg>""")

# Périmètre (1D) vs Aire (2D)
save_and_verify("fig_12_perimetre_vs_aire.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 170" width="100%" height="170">
  <rect width="540" height="170" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Périmètre -->
  <g transform="translate(40, 25)">
    <rect x="20" y="20" width="160" height="80" fill="none" stroke="#1d4ed8" stroke-width="3"/>
    <text x="100" y="65" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Le Tour (Bord)</text>
    <text x="100" y="125" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">PÉRIMÈTRE = 1D</text>
    <text x="100" y="142" font-family="Liberation Sans" font-size="11" fill="#475569" text-anchor="middle">Se mesure en mètres (m)</text>
  </g>
  <!-- Aire -->
  <g transform="translate(300, 25)">
    <rect x="20" y="20" width="160" height="80" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="100" y="65" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#15803d" text-anchor="middle">L'Intérieur Rempli</text>
    <text x="100" y="125" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#15803d" text-anchor="middle">AIRE = 2D</text>
    <text x="100" y="142" font-family="Liberation Sans" font-size="11" fill="#475569" text-anchor="middle">Se mesure en mètres carrés (m²)</text>
  </g>
</svg>""")

# Axe des nombres relatifs et thermomètre
save_and_verify("fig_14_axe_relatifs.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 150" width="100%" height="150">
  <rect width="560" height="150" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="280" y="25" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">L'AXE DES NOMBRES RELATIFS : SYMÉTRIE AUTOUR DU ZÉRO</text>
  <!-- Axe -->
  <line x1="30" y1="75" x2="520" y2="75" stroke="#0f172a" stroke-width="2"/>
  <polygon points="525,75 515,71 515,79" fill="#0f172a"/>
""" + "\n".join([
    f'<line x1="{60 + i*45}" y1="{65 if i==5 else 68}" x2="{60 + i*45}" y2="{85 if i==5 else 82}" stroke="{"#b91c1c" if i==5 else "#0f172a"}" stroke-width="{3 if i==5 else 1.5}"/>\n'
    f'<text x="{60 + i*45}" y="102" font-family="Liberation Sans" font-size="12" font-weight="{"bold" if i==5 else "normal"}" fill="{"#b91c1c" if i==5 else ("#1d4ed8" if i<5 else "#15803d")}" text-anchor="middle">{i-5}</text>'
    for i in range(11)
]) + """
  <text x="150" y="55" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Nombres négatifs (&lt; 0)</text>
  <text x="410" y="55" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">Nombres positifs (&gt; 0)</text>
  <text x="280" y="135" font-family="Liberation Sans" font-size="11" fill="#475569" text-anchor="middle">-5 est plus petit que -2 car il est situé plus à gauche sur l'axe</text>
</svg>""")

print("Volume II: All SVG figures generated and verified successfully.")
