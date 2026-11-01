# -*- coding: utf-8 -*-
"""
SVG Generator for Volume IV (LA VOIE DU NOMBRE)
"""
import os
import xml.etree.ElementTree as ET

out_dir = r"c:\Silvere\Encours\Developpement\Articles\livre_mathematiques\figures\vol_4"
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
# Chapitre 22 : Balance d'Al-Khwarizmi & Équations
# -------------------------------------------------------------
save_and_verify("fig_22_balance_al_khwarizmi.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">L'ÉQUATION D'AL-KHWARIZMI : x + 3 = 8</text>
  <!-- Balance -->
  <polygon points="270,60 245,150 295,150" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>
  <rect x="215" y="150" width="110" height="14" rx="3" fill="#0f172a"/>
  <circle cx="270" cy="60" r="6" fill="#d97706"/>
  <line x1="90" y1="60" x2="450" y2="60" stroke="#0f172a" stroke-width="3.5"/>
  <!-- Plateau gauche : Sac mystère [x] + 3 kg -->
  <line x1="130" y1="60" x2="105" y2="115" stroke="#64748b" stroke-width="1.5"/>
  <line x1="130" y1="60" x2="155" y2="115" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 95,115 Q 130,135 165,115 Z" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <rect x="100" y="85" width="30" height="30" rx="4" fill="#b91c1c"/>
  <text x="115" y="105" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">x</text>
  <circle cx="145" cy="100" r="10" fill="#d97706"/>
  <text x="145" y="104" font-family="Liberation Sans" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
  <!-- Plateau droit : 8 kg -->
  <line x1="410" y1="60" x2="385" y2="115" stroke="#64748b" stroke-width="1.5"/>
  <line x1="410" y1="60" x2="435" y2="115" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 375,115 Q 410,135 445,115 Z" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <rect x="395" y="80" width="32" height="35" rx="4" fill="#15803d"/>
  <text x="411" y="103" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">8 kg</text>
  <text x="270" y="190" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Al-Jabr (restauration) : Retrancher 3 kg sur chaque plateau ➔ x = 8 - 3 = 5 kg</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 23 : Identités remarquables d'Oliver Byrne
# -------------------------------------------------------------
save_and_verify("fig_23_identite_remarquable_carre.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="100%" height="220">
  <rect width="540" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">DÉMONSTRATION GÉOMÉTRIQUE : (a + b)² = a² + 2ab + b²</text>
  <g transform="translate(80, 45)">
    <!-- Carré a² (bleu) -->
    <rect x="0" y="0" width="90" height="90" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <text x="45" y="52" font-family="Liberation Sans" font-size="16" font-weight="bold" fill="#1d4ed8" text-anchor="middle">a²</text>
    <text x="45" y="-8" font-family="Liberation Sans" font-size="12" fill="#1d4ed8" text-anchor="middle">a</text>
    <text x="-12" y="50" font-family="Liberation Sans" font-size="12" fill="#1d4ed8" text-anchor="middle">a</text>
    
    <!-- Rectangle a x b (jaune haut-droit) -->
    <rect x="90" y="0" width="45" height="90" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
    <text x="112" y="52" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#d97706" text-anchor="middle">a·b</text>
    <text x="112" y="-8" font-family="Liberation Sans" font-size="12" fill="#d97706" text-anchor="middle">b</text>
    
    <!-- Rectangle b x a (jaune bas-gauche) -->
    <rect x="0" y="90" width="90" height="45" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
    <text x="45" y="118" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#d97706" text-anchor="middle">a·b</text>
    <text x="-12" y="118" font-family="Liberation Sans" font-size="12" fill="#d97706" text-anchor="middle">b</text>
    
    <!-- Carré b² (rouge bas-droit) -->
    <rect x="90" y="90" width="45" height="45" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
    <text x="112" y="118" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#b91c1c" text-anchor="middle">b²</text>
  </g>
  <g transform="translate(260, 85)" font-family="Liberation Sans">
    <rect x="0" y="0" width="220" height="70" rx="6" fill="#f0fdf4" stroke="#15803d" stroke-width="1.5"/>
    <text x="110" y="28" font-size="14" font-weight="bold" fill="#15803d" text-anchor="middle">Aire Totale du Grand Carré :</text>
    <text x="110" y="52" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">(a + b)² = a² + 2ab + b²</text>
  </g>
  <text x="270" y="200" font-family="Liberation Sans" font-size="11" fill="#475569" text-anchor="middle">Les 4 pièces du puzzle s'assemblent pour former un carré parfait de côté (a + b)</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 24, 25 : Inégalités & Fonctions affines
# -------------------------------------------------------------
# Droite affine y = ax + b
save_and_verify("fig_25_droite_affine_complete.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(140, 140)">
    <!-- Axes -->
    <line x1="-60" y1="0" x2="200" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="205,0 195,-4 195,4" fill="#0f172a"/>
    <text x="195" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">x</text>
    
    <line x1="0" y1="40" x2="0" y2="-120" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-125 -4,-115 4,-115" fill="#0f172a"/>
    <text x="10" y="-115" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">y</text>
    
    <!-- Droite y = 0.5x + 30 (pente positive a > 0) -->
    <line x1="-40" y1="-10" x2="160" y2="-110" stroke="#1d4ed8" stroke-width="3"/>
    
    <!-- Ordonnée à l'origine (0, b) -->
    <circle cx="0" cy="-30" r="5" fill="#b91c1c"/>
    <text x="-35" y="-26" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">b (0, b)</text>
    
    <!-- Triangle de pente Δx, Δy -->
    <line x1="40" y1="-50" x2="120" y2="-50" stroke="#d97706" stroke-width="2" stroke-dasharray="3"/>
    <line x1="120" y1="-50" x2="120" y2="-90" stroke="#15803d" stroke-width="2" stroke-dasharray="3"/>
    <text x="80" y="-38" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#d97706" text-anchor="middle">Δx</text>
    <text x="135" y="-68" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#15803d">Δy</text>
  </g>
  <g transform="translate(340, 50)" font-family="Liberation Sans" font-size="12">
    <rect x="0" y="0" width="160" height="90" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="80" y="25" font-weight="bold" fill="#1d4ed8" text-anchor="middle">f(x) = a x + b</text>
    <text x="10" y="50" fill="#b91c1c">• b : ordonnée à l'origine</text>
    <text x="10" y="70" fill="#15803d">• a = Δy / Δx : coefficient</text>
    <text x="25" y="84" fill="#15803d">directeur (pente)</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 28 : Ératosthène et le tour de la Terre
# -------------------------------------------------------------
save_and_verify("fig_28_eratosthene_tour_terre.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="100%" height="220">
  <rect width="540" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">LA MESURE DE LA TERRE PAR ÉRATOSTHÈNE (~240 av. J.-C.)</text>
  <g transform="translate(180, 130)">
    <!-- Arc de la Terre -->
    <circle cx="0" cy="0" r="85" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <circle cx="0" cy="0" r="4" fill="#0f172a"/>
    <text x="-12" y="15" font-family="Liberation Sans" font-size="11" fill="#0f172a">Centre</text>
    
    <!-- Syène (midi solaire, rayons verticaux au fond du puits) -->
    <line x1="0" y1="0" x2="85" y2="0" stroke="#0f172a" stroke-width="1.5"/>
    <line x1="85" y1="0" x2="160" y2="0" stroke="#d97706" stroke-width="2"/>
    <text x="95" y="-8" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#d97706">Syène (puits sans ombre)</text>
    
    <!-- Alexandrie (obélisque avec ombre sous angle de 7,2°) -->
    <line x1="0" y1="0" x2="81" y2="-26" stroke="#0f172a" stroke-width="1.5"/>
    <line x1="81" y1="-26" x2="155" y2="-26" stroke="#d97706" stroke-width="2"/>
    <text x="92" y="-35" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c">Alexandrie (obélisque)</text>
    
    <!-- Angle 7,2° au centre -->
    <path d="M 40,0 A 40 40 0 0 0 38,-12" fill="none" stroke="#b91c1c" stroke-width="2"/>
    <text x="46" y="-3" font-family="Liberation Sans" font-size="10" font-weight="bold" fill="#b91c1c">7,2°</text>
  </g>
  <g transform="translate(360, 65)" font-family="Liberation Sans" font-size="11.5">
    <text x="0" y="15" font-weight="bold" fill="#b91c1c">Angle = 7,2° = 360° / 50</text>
    <text x="0" y="35" fill="#0f172a">Arc = 5 000 stades (~800 km)</text>
    <text x="0" y="60" font-weight="bold" fill="#15803d">Tour de la Terre = 50 × Arc</text>
    <text x="0" y="80" font-size="13" font-weight="bold" fill="#1d4ed8">≈ 40 000 km !</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 29 & 30 : Algorithme d'Euclide & Arbre Probabilités
# -------------------------------------------------------------
save_and_verify("fig_29_euclide_rectangles.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 180" width="100%" height="180">
  <rect width="540" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">L'ALGORITHME D'EUCLIDE PAR DÉCOUPAGE EN CARRÉS : PGCD(21, 15)</text>
  <!-- Grand rectangle 210 x 150 (échelle 0.8) -->
  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="168" height="120" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <!-- 1er grand carré 15x15 (120x120) -->
    <rect x="0" y="0" width="120" height="120" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="60" y="65" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Carré 15 × 15</text>
    <!-- Reste 6x15 (48x120) -->
    <!-- Deux carrés 6x6 (48x48) -->
    <rect x="120" y="0" width="48" height="48" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="144" y="28" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">6 × 6</text>
    <rect x="120" y="48" width="48" height="48" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="144" y="76" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">6 × 6</text>
    <!-- Reste final 6x3 (48x24) pavé par deux carrés 3x3 -->
    <rect x="120" y="96" width="24" height="24" fill="#f0fdf4" stroke="#15803d" stroke-width="1.5"/>
    <rect x="144" y="96" width="24" height="24" fill="#f0fdf4" stroke="#15803d" stroke-width="1.5"/>
    <text x="132" y="112" font-family="Liberation Sans" font-size="9" font-weight="bold" fill="#15803d" text-anchor="middle">3</text>
    <text x="156" y="112" font-family="Liberation Sans" font-size="9" font-weight="bold" fill="#15803d" text-anchor="middle">3</text>
  </g>
  <g transform="translate(260, 60)" font-family="Liberation Sans" font-size="12">
    <text x="0" y="15" fill="#0f172a">• 21 = 1 × 15 + 6</text>
    <text x="0" y="35" fill="#0f172a">• 15 = 2 × 6 + 3</text>
    <text x="0" y="55" fill="#0f172a">• 6 = 2 × 3 + 0 (reste nul !)</text>
    <text x="0" y="85" font-size="14" font-weight="bold" fill="#15803d">PGCD(21, 15) = 3 (taille du plus petit carré)</text>
  </g>
</svg>""")

print("Volume IV: All SVG figures generated and verified successfully.")
