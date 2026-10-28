# -*- coding: utf-8 -*-
"""
SVG Generator for Volume V (LA VOIE DU NOMBRE)
"""
import os
import math
import xml.etree.ElementTree as ET

out_dir = r"c:\Silvere\Encours\Developpement\Articles\livre_mathematiques\figures\vol_5"
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
# Chapitre 31 : Ensembles, Logique, Intervalles
# -------------------------------------------------------------
# Boîtes emboîtées des nombres
save_and_verify("fig_31_ensembles_emboites.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="100%" height="220">
  <rect width="540" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- R (rouge) -->
  <rect x="25" y="20" width="490" height="180" rx="6" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
  <text x="45" y="42" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#b91c1c">ℝ (Réels) : √2, π, -√3</text>
  <!-- Q (orange) -->
  <rect x="50" y="50" width="440" height="135" rx="6" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
  <text x="70" y="72" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#d97706">ℚ (Rationnels) : 1/3, -2/7</text>
  <!-- D (violet) -->
  <rect x="75" y="80" width="390" height="95" rx="6" fill="#faf5ff" stroke="#7e22ce" stroke-width="2"/>
  <text x="95" y="102" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#7e22ce">𝔻 (Décimaux) : 0,25, -1,7</text>
  <!-- Z (vert) -->
  <rect x="100" y="110" width="340" height="55" rx="6" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="120" y="132" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#15803d">ℤ (Entiers relatifs) : -3, -1</text>
  <!-- N (bleu) -->
  <rect x="260" y="120" width="165" height="35" rx="4" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <text x="342" y="142" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8" text-anchor="middle">ℕ (Naturels) : 0, 1, 7</text>
</svg>""")

# Venn A ∩ B et A ∪ B
save_and_verify("fig_31_venn_intersection_union.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 180" width="100%" height="180">
  <rect width="540" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Intersection A ∩ B -->
  <g transform="translate(40, 20)">
    <text x="100" y="20" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#1d4ed8" text-anchor="middle">INTERSECTION A ∩ B</text>
    <circle cx="75" cy="80" r="50" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <circle cx="125" cy="80" r="50" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
    <!-- Intersection colorée -->
    <path d="M 100,40 A 50 50 0 0 1 100,120 A 50 50 0 0 1 100,40 Z" fill="#b91c1c"/>
    <text x="50" y="85" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">A</text>
    <text x="145" y="85" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#15803d">B</text>
    <text x="100" y="150" font-family="Liberation Sans" font-size="11" fill="#b91c1c" font-weight="bold" text-anchor="middle">Dans A ET dans B</text>
  </g>
  <!-- Union A ∪ B -->
  <g transform="translate(300, 20)">
    <text x="100" y="20" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#15803d" text-anchor="middle">RÉUNION A ∪ B</text>
    <circle cx="75" cy="80" r="50" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
    <circle cx="125" cy="80" r="50" fill="#dbeafe" stroke="#15803d" stroke-width="2"/>
    <text x="50" y="85" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">A</text>
    <text x="145" y="85" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#15803d">B</text>
    <text x="100" y="150" font-family="Liberation Sans" font-size="11" fill="#1d4ed8" font-weight="bold" text-anchor="middle">Dans A OU dans B</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 32 : Vecteurs & Relation de Chasles
# -------------------------------------------------------------
# Définition du vecteur (direction, sens, norme)
save_and_verify("fig_32_vecteur_definition.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 180" width="100%" height="180">
  <rect width="520" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(80, 130)">
    <!-- Droite support (direction) en pointillé -->
    <line x1="-30" y1="20" x2="230" y2="-120" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
    <text x="210" y="-125" font-family="Liberation Sans" font-size="11" fill="#64748b">Direction (pente de la droite)</text>
    
    <!-- Vecteur AB -->
    <line x1="20" y1="-10" x2="160" y2="-85" stroke="#1d4ed8" stroke-width="3.5"/>
    <polygon points="168,-90 155,-80 160,-92" fill="#1d4ed8"/>
    
    <circle cx="20" cy="-10" r="4.5" fill="#0f172a"/>
    <text x="10" y="10" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#0f172a">A (origine)</text>
    <circle cx="160" cy="-85" r="4.5" fill="#0f172a"/>
    <text x="175" y="-80" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#0f172a">B (extrémité)</text>
    
    <text x="90" y="-60" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#1d4ed8">u = AB</text>
  </g>
  <g transform="translate(340, 50)" font-family="Liberation Sans" font-size="12">
    <rect x="0" y="0" width="150" height="85" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="12" y="22" font-weight="bold" fill="#0f172a">Les 3 composantes :</text>
    <text x="12" y="42" fill="#1d4ed8">1. Direction (la droite)</text>
    <text x="12" y="60" fill="#b91c1c">2. Sens (la flèche ➔)</text>
    <text x="12" y="78" fill="#15803d">3. Norme ||u|| (longueur)</text>
  </g>
</svg>""")

# Relation de Chasles AB + BC = AC
save_and_verify("fig_32_chasles_addition.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 190" width="100%" height="190">
  <rect width="520" height="190" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="260" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">LA RELATION DE CHASLES : AB + BC = AC</text>
  <g transform="translate(100, 140)">
    <!-- Vecteur AB -->
    <line x1="0" y1="0" x2="140" y2="-20" stroke="#1d4ed8" stroke-width="3"/>
    <polygon points="147,-21 136,-16 138,-27" fill="#1d4ed8"/>
    <text x="65" y="-2" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">AB</text>
    
    <!-- Vecteur BC -->
    <line x1="140" y1="-20" x2="190" y2="-90" stroke="#15803d" stroke-width="3"/>
    <polygon points="194,-96 184,-88 193,-82" fill="#15803d"/>
    <text x="180" y="-50" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#15803d">BC</text>
    
    <!-- Vecteur somme AC (résultante directe) -->
    <line x1="0" y1="0" x2="190" y2="-90" stroke="#b91c1c" stroke-width="3.5" stroke-dasharray="5"/>
    <polygon points="196,-93 186,-84 193,-77" fill="#b91c1c"/>
    <text x="80" y="-60" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#b91c1c">AC = AB + BC</text>
    
    <circle cx="0" cy="0" r="4.5" fill="#0f172a"/>
    <text x="-15" y="5" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a">A</text>
    <circle cx="140" cy="-20" r="4.5" fill="#0f172a"/>
    <text x="145" y="-5" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a">B</text>
    <circle cx="190" cy="-90" r="4.5" fill="#0f172a"/>
    <text x="195" y="-95" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a">C</text>
  </g>
  <text x="260" y="170" font-family="Liberation Sans" font-size="12" fill="#475569" text-anchor="middle">Enchaînement de deux translations successives : l'arrivée de la 1ère est le départ de la 2nde</text>
</svg>""")

# -------------------------------------------------------------
# Chapitre 35 : Parabole du second degré
# -------------------------------------------------------------
save_and_verify("fig_35_parabole_second_degre.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="100%" height="220">
  <rect width="540" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(180, 160)">
    <!-- Axes -->
    <line x1="-120" y1="0" x2="180" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="185,0 175,-4 175,4" fill="#0f172a"/>
    <text x="175" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">x</text>
    
    <line x1="0" y1="30" x2="0" y2="-130" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-135 -4,-125 4,-125" fill="#0f172a"/>
    <text x="10" y="-125" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">y</text>
    
    <!-- Courbe parabole y = a(x-x0)^2 + y0 calculée -->
""" + f"""
    <path d="{' '.join([f'{"M" if i==0 else "L"} {x:.1f},{-(-0.02*(x-40)**2 + 90):.1f}' for i, x in enumerate(range(-60, 145, 5))])}" fill="none" stroke="#1d4ed8" stroke-width="3"/>
""" + """
    <!-- Sommet S (40, 90) -->
    <line x1="40" y1="20" x2="40" y2="-110" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3"/>
    <circle cx="40" cy="-90" r="5" fill="#b91c1c"/>
    <text x="50" y="-95" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">Sommet S (-b / 2a)</text>
    
    <!-- Racines x1 et x2 -->
    <circle cx="-27" cy="0" r="4.5" fill="#15803d"/>
    <text x="-40" y="18" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#15803d">x₁</text>
    <circle cx="107" cy="0" r="4.5" fill="#15803d"/>
    <text x="107" y="18" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#15803d">x₂</text>
  </g>
  <g transform="translate(380, 50)" font-family="Liberation Sans" font-size="11.5">
    <rect x="0" y="0" width="140" height="90" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="70" y="22" font-weight="bold" fill="#1d4ed8" text-anchor="middle">f(x) = ax² + bx + c</text>
    <text x="10" y="44" fill="#b91c1c">• Δ = b² - 4ac &gt; 0</text>
    <text x="10" y="62" fill="#15803d">• 2 racines réelles</text>
    <text x="10" y="80" fill="#0f172a">• a &lt; 0 (tournée bas)</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 37 : Cercle Trigonométrique
# -------------------------------------------------------------
save_and_verify("fig_37_cercle_trigo_complet.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 230" width="100%" height="230">
  <rect width="540" height="230" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(180, 115)">
    <!-- Cercle unité R = 80 -->
    <circle cx="0" cy="0" r="80" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    
    <!-- Axes cos et sin -->
    <line x1="-105" y1="0" x2="115" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="120,0 110,-4 110,4" fill="#0f172a"/>
    <text x="110" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8">cos x</text>
    
    <line x1="0" y1="105" x2="0" y2="-115" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-120 -4,-110 4,-110" fill="#0f172a"/>
    <text x="10" y="-110" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">sin x</text>
    
    <!-- Rayon angle θ = 45° -->
    <line x1="0" y1="0" x2="56.5" y2="-56.5" stroke="#0f172a" stroke-width="2.5"/>
    <circle cx="56.5" cy="-56.5" r="5" fill="#d97706"/>
    <text x="68" y="-62" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#d97706">M (cos θ, sin θ)</text>
    
    <!-- Projections cos et sin -->
    <line x1="56.5" y1="0" x2="56.5" y2="-56.5" stroke="#b91c1c" stroke-width="2" stroke-dasharray="3"/>
    <line x1="0" y1="-56.5" x2="56.5" y2="-56.5" stroke="#1d4ed8" stroke-width="2" stroke-dasharray="3"/>
    
    <line x1="0" y1="0" x2="56.5" y2="0" stroke="#1d4ed8" stroke-width="4"/>
    <line x1="0" y1="0" x2="0" y2="-56.5" stroke="#b91c1c" stroke-width="4"/>
    
    <!-- Arc angle θ -->
    <path d="M 25,0 A 25 25 0 0 0 17.6,-17.6" fill="none" stroke="#d97706" stroke-width="2"/>
    <text x="32" y="-8" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#d97706">θ</text>
  </g>
  <g transform="translate(360, 50)" font-family="Liberation Sans" font-size="11.5">
    <rect x="0" y="0" width="160" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="80" y="22" font-weight="bold" fill="#0f172a" text-anchor="middle">Propriétés clés :</text>
    <text x="12" y="45" fill="#1d4ed8">• cos² θ + sin² θ = 1</text>
    <text x="12" y="65" fill="#b91c1c">• -1 ≤ cos θ ≤ 1</text>
    <text x="12" y="85" fill="#b91c1c">• -1 ≤ sin θ ≤ 1</text>
    <text x="12" y="102" fill="#15803d">• Rayon unité : R = 1</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 39 : Tangente et Nombre Dérivé
# -------------------------------------------------------------
save_and_verify("fig_39_tangente_nombre_derivee.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="100%" height="220">
  <rect width="540" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(120, 160)">
    <!-- Axes -->
    <line x1="-30" y1="0" x2="240" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="245,0 235,-4 235,4" fill="#0f172a"/>
    <text x="235" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">x</text>
    
    <line x1="0" y1="30" x2="0" y2="-130" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-135 -4,-125 4,-125" fill="#0f172a"/>
    <text x="10" y="-125" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">y</text>
    
    <!-- Courbe f(x) -->
    <path d="M 10,-20 Q 90,-40 180,-120" fill="none" stroke="#1d4ed8" stroke-width="3"/>
    <text x="195" y="-115" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8">y = f(x)</text>
    
    <!-- Point A (80, -35) -->
    <circle cx="80" cy="-35" r="5" fill="#b91c1c"/>
    <text x="65" y="-45" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">A (a, f(a))</text>
    
    <!-- Tangente en A -->
    <line x1="20" y1="5" x2="160" y2="-90" stroke="#b91c1c" stroke-width="2.5"/>
    <text x="165" y="-85" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">Tangente (T)</text>
    
    <!-- Sécante en pointillé -->
    <line x1="20" y1="0" x2="160" y2="-115" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
    <circle cx="140" cy="-78" r="4" fill="#64748b"/>
    <text x="148" y="-70" font-family="Liberation Sans" font-size="10" fill="#64748b">M(a+h)</text>
  </g>
  <g transform="translate(360, 50)" font-family="Liberation Sans" font-size="12">
    <rect x="0" y="0" width="160" height="90" rx="6" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="80" y="24" font-weight="bold" fill="#b91c1c" text-anchor="middle">Nombre dérivé f'(a)</text>
    <text x="80" y="48" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Pente de la tangente</text>
    <text x="80" y="72" font-size="11" fill="#475569" text-anchor="middle">lim h➔0 [f(a+h)-f(a)] / h</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 40 : Exponentielle
# -------------------------------------------------------------
save_and_verify("fig_40_exponentielle.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(180, 150)">
    <!-- Axes -->
    <line x1="-140" y1="0" x2="160" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="165,0 155,-4 155,4" fill="#0f172a"/>
    <text x="155" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">x</text>
    
    <line x1="0" y1="20" x2="0" y2="-130" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-135 -4,-125 4,-125" fill="#0f172a"/>
    <text x="10" y="-125" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">y</text>
    
    <!-- Courbe y = e^x calculée -->
""" + f"""
    <path d="{' '.join([f'{"M" if i==0 else "L"} {x:.1f},{-min(125, 25*math.exp(x/40)):.1f}' for i, x in enumerate(range(-120, 65, 5))])}" fill="none" stroke="#1d4ed8" stroke-width="3"/>
""" + """
    <!-- Point (0, 1) -->
    <circle cx="0" cy="-25" r="5" fill="#b91c1c"/>
    <text x="-35" y="-22" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">(0, 1)</text>
    
    <!-- Tangente en 0 de pente 1 : y = x + 1 -->
    <line x1="-40" y1="0" x2="40" y2="-50" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="3"/>
    <text x="45" y="-50" font-family="Liberation Sans" font-size="10.5" fill="#b91c1c">Pente = 1</text>
  </g>
  <g transform="translate(370, 50)" font-family="Liberation Sans" font-size="12">
    <rect x="0" y="0" width="150" height="90" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="75" y="24" font-weight="bold" fill="#1d4ed8" text-anchor="middle">f(x) = e^x</text>
    <text x="12" y="48" fill="#15803d">• (e^x)' = e^x</text>
    <text x="12" y="68" fill="#0f172a">• e⁰ = 1</text>
    <text x="12" y="84" fill="#b91c1c">• Toujours strictement &gt; 0</text>
  </g>
</svg>""")

print("Volume V: All SVG figures generated and verified successfully.")
