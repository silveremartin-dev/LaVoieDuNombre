# -*- coding: utf-8 -*-
"""
SVG Generator for Volume VI (LA VOIE DU NOMBRE)
"""
import os
import math
import xml.etree.ElementTree as ET

out_dir = r"c:\Silvere\Encours\Developpement\Articles\livre_mathematiques\figures\vol_6"
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
# Chapitre 43 : Récurrence & Dominos
# -------------------------------------------------------------
save_and_verify("fig_43_dominos_recurrence.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 180" width="100%" height="180">
  <rect width="540" height="180" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">LE PRINCIPE DE RÉCURRENCE : L'EFFET DOMINO UNIVERSEL</text>
  <!-- Sol -->
  <line x1="30" y1="130" x2="510" y2="130" stroke="#0f172a" stroke-width="2"/>
  
  <!-- Domino 0 qui tombe (Initialisation) -->
  <g transform="translate(60, 60)">
    <rect x="0" y="0" width="12" height="65" rx="2" fill="#b91c1c" transform="rotate(30 0 65)"/>
    <text x="5" y="85" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">P(0)</text>
    <text x="5" y="98" font-family="Liberation Sans" font-size="10" fill="#b91c1c" text-anchor="middle">Initialisation</text>
  </g>
  
  <!-- Dominos 1, 2, 3 en chute -->
  <rect x="120" y="62" width="12" height="65" rx="2" fill="#d97706" transform="rotate(22 120 127)"/>
  <text x="135" y="145" font-family="Liberation Sans" font-size="11" fill="#d97706" text-anchor="middle">P(1)</text>
  
  <rect x="180" y="63" width="12" height="65" rx="2" fill="#d97706" transform="rotate(15 180 128)"/>
  <text x="195" y="145" font-family="Liberation Sans" font-size="11" fill="#d97706" text-anchor="middle">P(2)</text>
  
  <!-- Dominos n et n+1 (Hérédité) -->
  <g transform="translate(290, 65)">
    <rect x="0" y="0" width="12" height="65" rx="2" fill="#1d4ed8"/>
    <text x="6" y="80" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">P(n)</text>
    
    <path d="M 15,20 L 45,20" fill="none" stroke="#1d4ed8" stroke-width="2"/>
    <polygon points="50,20 42,16 42,24" fill="#1d4ed8"/>
    
    <rect x="55" y="0" width="12" height="65" rx="2" fill="#15803d"/>
    <text x="61" y="80" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">P(n+1)</text>
    <text x="33" y="102" font-family="Liberation Sans" font-size="10" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Hérédité</text>
  </g>
  
  <g transform="translate(420, 50)" font-family="Liberation Sans" font-size="11.5">
    <rect x="0" y="0" width="105" height="75" rx="4" fill="#eff6ff" stroke="#1d4ed8"/>
    <text x="52" y="20" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Conclusion :</text>
    <text x="52" y="42" font-weight="bold" fill="#0f172a" text-anchor="middle">Vrai pour</text>
    <text x="52" y="60" font-weight="bold" fill="#15803d" text-anchor="middle">tout entier n !</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 44, 45, 46 : Limites, Asymptotes, TVI
# -------------------------------------------------------------
# Théorème des gendarmes
save_and_verify("fig_44_theoreme_gendarmes.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 200" width="100%" height="200">
  <rect width="520" height="200" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="260" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">LE THÉORÈME DES GENDARMES (ÉTAU)</text>
  <g transform="translate(60, 150)">
    <!-- Axes -->
    <line x1="0" y1="0" x2="330" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="335,0 325,-4 325,4" fill="#0f172a"/>
    <text x="325" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">n</text>
    
    <line x1="0" y1="10" x2="0" y2="-120" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-125 -4,-115 4,-115" fill="#0f172a"/>
    <text x="10" y="-115" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">u_n</text>
    
    <!-- Ligne de limite L -->
    <line x1="0" y1="-60" x2="310" y2="-60" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="4"/>
    <text x="-15" y="-56" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">L</text>
    
    <!-- Gendarme supérieur w_n -->
    <path d="M 20,-115 Q 120,-80 300,-62" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>
    <text x="150" y="-95" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#1d4ed8">w_n (gendarme haut ➔ L)</text>
    
    <!-- Suite coincée u_n (ondulante) -->
    <path d="M 20,-90 Q 60,-50 100,-75 Q 160,-52 220,-65 Q 260,-58 300,-60" fill="none" stroke="#0f172a" stroke-width="2"/>
    <text x="180" y="-45" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">u_n coincée !</text>
    
    <!-- Gendarme inférieur v_n -->
    <path d="M 20,-15 Q 120,-40 300,-58" fill="none" stroke="#15803d" stroke-width="2.5"/>
    <text x="150" y="-22" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#15803d">v_n (gendarme bas ➔ L)</text>
  </g>
  <g transform="translate(400, 60)" font-family="Liberation Sans" font-size="11">
    <rect x="0" y="0" width="105" height="85" rx="4" fill="#eff6ff" stroke="#1d4ed8"/>
    <text x="52" y="18" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Encadrement :</text>
    <text x="52" y="38" fill="#0f172a" text-anchor="middle">v_n ≤ u_n ≤ w_n</text>
    <text x="52" y="58" fill="#b91c1c" text-anchor="middle">lim v_n = L</text>
    <text x="52" y="74" fill="#b91c1c" text-anchor="middle">lim w_n = L</text>
  </g>
</svg>""")

# Asymptotes
save_and_verify("fig_45_asymptotes_complete.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Asymptote verticale -->
  <g transform="translate(80, 110)">
    <text x="60" y="-85" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">Asymptote Verticale x = a</text>
    <line x1="-50" y1="40" x2="160" y2="40" stroke="#0f172a" stroke-width="1.5"/>
    <line x1="0" y1="80" x2="0" y2="-70" stroke="#0f172a" stroke-width="1.5"/>
    <!-- Ligne verticale x = 50 -->
    <line x1="50" y1="80" x2="50" y2="-70" stroke="#b91c1c" stroke-width="2" stroke-dasharray="4"/>
    <text x="50" y="55" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">x = a</text>
    <!-- Courbe 1/(x-a) -->
    <path d="M 46,-70 Q 44,20 10,35" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>
    <path d="M 54,80 Q 56,50 120,43" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>
  </g>
  <!-- Asymptote horizontale -->
  <g transform="translate(340, 110)">
    <text x="60" y="-85" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">Asymptote Horizontale y = L</text>
    <line x1="-50" y1="40" x2="160" y2="40" stroke="#0f172a" stroke-width="1.5"/>
    <line x1="0" y1="80" x2="0" y2="-70" stroke="#0f172a" stroke-width="1.5"/>
    <!-- Ligne horizontale y = -20 -->
    <line x1="-50" y1="-20" x2="160" y2="-20" stroke="#15803d" stroke-width="2" stroke-dasharray="4"/>
    <text x="145" y="-25" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#15803d">y = L</text>
    <!-- Courbe tendant vers y = L -->
    <path d="M 10,70 Q 40,-15 150,-19" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>
  </g>
</svg>""")

# TVI (Théorème des Valeurs Intermédiaires)
save_and_verify("fig_46_tvi_continuite.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="100%" height="220">
  <rect width="540" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(100, 160)">
    <!-- Axes -->
    <line x1="-20" y1="0" x2="280" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="285,0 275,-4 275,4" fill="#0f172a"/>
    <text x="275" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">x</text>
    
    <line x1="0" y1="20" x2="0" y2="-130" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-135 -4,-125 4,-125" fill="#0f172a"/>
    <text x="10" y="-125" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">y</text>
    
    <!-- Courbe continue f(x) -->
    <path d="M 40,-20 Q 90,-120 140,-70 T 240,-115" fill="none" stroke="#1d4ed8" stroke-width="3"/>
    
    <!-- a et f(a) -->
    <line x1="40" y1="0" x2="40" y2="-20" stroke="#94a3b8" stroke-dasharray="3"/>
    <line x1="0" y1="-20" x2="40" y2="-20" stroke="#94a3b8" stroke-dasharray="3"/>
    <text x="40" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">a</text>
    <text x="-25" y="-16" font-family="Liberation Sans" font-size="11" fill="#1d4ed8">f(a)</text>
    
    <!-- b et f(b) -->
    <line x1="240" y1="0" x2="240" y2="-115" stroke="#94a3b8" stroke-dasharray="3"/>
    <line x1="0" y1="-115" x2="240" y2="-115" stroke="#94a3b8" stroke-dasharray="3"/>
    <text x="240" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">b</text>
    <text x="-25" y="-111" font-family="Liberation Sans" font-size="11" fill="#1d4ed8">f(b)</text>
    
    <!-- Valeur cible k -->
    <line x1="0" y1="-65" x2="260" y2="-65" stroke="#b91c1c" stroke-width="2" stroke-dasharray="4"/>
    <text x="-18" y="-61" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c">k</text>
    
    <!-- Solution c telle que f(c) = k -->
    <circle cx="150" cy="-65" r="5" fill="#15803d"/>
    <line x1="150" y1="0" x2="150" y2="-65" stroke="#15803d" stroke-width="2" stroke-dasharray="3"/>
    <text x="150" y="16" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#15803d" text-anchor="middle">c</text>
  </g>
  <g transform="translate(390, 50)" font-family="Liberation Sans" font-size="11.5">
    <rect x="0" y="0" width="135" height="95" rx="6" fill="#f0fdf4" stroke="#15803d" stroke-width="1.5"/>
    <text x="67" y="20" font-weight="bold" fill="#15803d" text-anchor="middle">Théorème (TVI) :</text>
    <text x="10" y="40" fill="#0f172a">Si f est continue,</text>
    <text x="10" y="58" fill="#0f172a">elle passe par toutes</text>
    <text x="10" y="74" fill="#0f172a">les valeurs entre</text>
    <text x="10" y="90" fill="#b91c1c" font-weight="bold">f(a) et f(b) !</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 48 : Exponentielle et Logarithme (Réciproques)
# -------------------------------------------------------------
save_and_verify("fig_48_exp_log_reciproques.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="100%" height="220">
  <rect width="540" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(180, 130)">
    <!-- Axes -->
    <line x1="-120" y1="0" x2="150" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="155,0 145,-4 145,4" fill="#0f172a"/>
    <text x="145" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">x</text>
    
    <line x1="0" y1="80" x2="0" y2="-110" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-115 -4,-105 4,-105" fill="#0f172a"/>
    <text x="10" y="-105" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">y</text>
    
    <!-- Axe de symétrie y = x -->
    <line x1="-80" y1="80" x2="100" y2="-100" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
    <text x="105" y="-95" font-family="Liberation Sans" font-size="11" fill="#64748b">y = x</text>
    
    <!-- Courbe y = e^x -->
    <path d="M -110,-5 Q -30,-15 10,-35 T 50,-105" fill="none" stroke="#1d4ed8" stroke-width="3"/>
    <text x="25" y="-110" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8">y = e^x</text>
    <circle cx="0" cy="-30" r="4" fill="#1d4ed8"/>
    <text x="-25" y="-30" font-family="Liberation Sans" font-size="10" fill="#1d4ed8">(0, 1)</text>
    
    <!-- Courbe y = ln(x) (symétrique miroir) -->
    <path d="M 5,110 Q 15,30 35,-10 T 105,-50" fill="none" stroke="#15803d" stroke-width="3"/>
    <text x="110" y="-45" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#15803d">y = ln(x)</text>
    <circle cx="30" cy="0" r="4" fill="#15803d"/>
    <text x="30" y="16" font-family="Liberation Sans" font-size="10" fill="#15803d">(1, 0)</text>
  </g>
  <g transform="translate(370, 50)" font-family="Liberation Sans" font-size="12">
    <rect x="0" y="0" width="150" height="90" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="75" y="24" font-weight="bold" fill="#0f172a" text-anchor="middle">Fonctions Réciproques :</text>
    <text x="12" y="48" fill="#1d4ed8">• ln(e^x) = x</text>
    <text x="12" y="68" fill="#15803d">• e^(ln x) = x</text>
    <text x="12" y="85" fill="#64748b">Symétrie par y = x</text>
  </g>
</svg>""")

# -------------------------------------------------------------
# Chapitre 50, 52, 54, 55 : Intégrale, Espace 3D, Gauss, Complexe
# -------------------------------------------------------------
# Intégrale de Riemann
save_and_verify("fig_50_riemann_integrale.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(100, 160)">
    <!-- Axes -->
    <line x1="-20" y1="0" x2="270" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="275,0 265,-4 265,4" fill="#0f172a"/>
    <text x="265" y="16" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">t</text>
    
    <line x1="0" y1="20" x2="0" y2="-130" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-135 -4,-125 4,-125" fill="#0f172a"/>
    <text x="10" y="-125" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">f(t)</text>
    
    <!-- Rectangles de Riemann sous la courbe -->
""" + "\n".join([
    f'<rect x="{40 + i*25}" y="{-int(15 + 60*math.sin(i*0.4))}" width="25" height="{int(15 + 60*math.sin(i*0.4))}" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1"/>'
    for i in range(8)
]) + """
    <!-- Courbe continue f(t) -->
    <path d="M 30,-15 Q 120,-110 240,-45" fill="none" stroke="#b91c1c" stroke-width="3"/>
    
    <text x="40" y="18" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">a</text>
    <text x="240" y="18" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">b</text>
  </g>
  <g transform="translate(370, 50)" font-family="Liberation Sans" font-size="12">
    <rect x="0" y="0" width="150" height="90" rx="6" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="75" y="24" font-weight="bold" fill="#b91c1c" text-anchor="middle">Aire = ∫_a^b f(t) dt</text>
    <text x="10" y="50" font-size="11" fill="#0f172a">• Somme des tranches</text>
    <text x="10" y="68" font-size="11" fill="#0f172a">• Largeur Δx ➔ 0</text>
    <text x="10" y="85" font-size="11" font-weight="bold" fill="#15803d">• Aire sous la courbe</text>
  </g>
</svg>""")

# Géométrie de l'espace 3D : Plan et Vecteur Normal
save_and_verify("fig_52_plan_vecteur_normal.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(180, 140)">
    <!-- Plan P en perspective cavalière (parallélogramme) -->
    <polygon points="0,-20 180,-20 130,40 -50,40" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
    <text x="150" y="30" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#1d4ed8">Plan (P)</text>
    
    <!-- Point A dans le plan -->
    <circle cx="60" cy="10" r="4.5" fill="#0f172a"/>
    <text x="45" y="26" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#0f172a">A (x₀, y₀, z₀)</text>
    
    <!-- Vecteur normal n orthogonal au plan -->
    <line x1="60" y1="10" x2="60" y2="-85" stroke="#b91c1c" stroke-width="3.5"/>
    <polygon points="60,-92 55,-80 65,-80" fill="#b91c1c"/>
    <text x="72" y="-70" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c">n (a, b, c)</text>
    
    <!-- Angle droit avec le plan -->
    <line x1="60" y1="-10" x2="75" y2="-10" stroke="#b91c1c" stroke-width="1.5"/>
    <line x1="75" y1="-10" x2="75" y2="10" stroke="#b91c1c" stroke-width="1.5"/>
  </g>
  <g transform="translate(370, 50)" font-family="Liberation Sans" font-size="11.5">
    <rect x="0" y="0" width="150" height="95" rx="6" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="75" y="22" font-weight="bold" fill="#b91c1c" text-anchor="middle">Équation du Plan :</text>
    <text x="10" y="44" font-weight="bold" fill="#0f172a">a x + b y + c z + d = 0</text>
    <text x="10" y="66" fill="#475569">AM · n = 0</text>
    <text x="10" y="85" fill="#15803d">Orthogonal à toute droite de (P)</text>
  </g>
</svg>""")

# Loi Normale de Gauss (Courbe en cloche)
save_and_verify("fig_54_loi_normale_gauss.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 210" width="100%" height="210">
  <rect width="540" height="210" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <text x="270" y="24" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">LA LOI NORMALE DE GAUSS : N(μ, σ²)</text>
  <g transform="translate(180, 150)">
    <!-- Axe horizontal -->
    <line x1="-150" y1="0" x2="150" y2="0" stroke="#0f172a" stroke-width="2"/>
    
    <!-- Courbe en cloche calculée -->
""" + f"""
    <path d="{' '.join([f'{"M" if i==0 else "L"} {x:.1f},{-105*math.exp(-(x/50)**2):.1f}' for i, x in enumerate(range(-140, 145, 5))])}" fill="none" stroke="#1d4ed8" stroke-width="3"/>
""" + """
    <!-- Moyenne μ -->
    <line x1="0" y1="0" x2="0" y2="-105" stroke="#b91c1c" stroke-width="2" stroke-dasharray="3"/>
    <text x="0" y="18" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c" text-anchor="middle">μ (Moyenne)</text>
    
    <!-- Zone μ ± σ (68%) -->
    <line x1="-50" y1="0" x2="-50" y2="-65" stroke="#15803d" stroke-dasharray="2"/>
    <line x1="50" y1="0" x2="50" y2="-65" stroke="#15803d" stroke-dasharray="2"/>
    <text x="-50" y="18" font-family="Liberation Sans" font-size="11" fill="#15803d" text-anchor="middle">μ - σ</text>
    <text x="50" y="18" font-family="Liberation Sans" font-size="11" fill="#15803d" text-anchor="middle">μ + σ</text>
    <text x="0" y="-40" font-family="Liberation Sans" font-size="14" font-weight="bold" fill="#15803d" text-anchor="middle">68,3 %</text>
  </g>
  <g transform="translate(370, 50)" font-family="Liberation Sans" font-size="11.5">
    <rect x="0" y="0" width="150" height="90" rx="6" fill="#eff6ff" stroke="#1d4ed8" stroke-width="1.5"/>
    <text x="75" y="22" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Intervalles usuels :</text>
    <text x="10" y="44" fill="#15803d">• [μ-σ, μ+σ] : ~68%</text>
    <text x="10" y="64" fill="#d97706">• [μ-2σ, μ+2σ] : ~95%</text>
    <text x="10" y="84" fill="#b91c1c">• [μ-3σ, μ+3σ] : ~99,7%</text>
  </g>
</svg>""")

# Plan complexe de Gauss-Argand
save_and_verify("fig_55_plan_complexe.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 220" width="100%" height="220">
  <rect width="540" height="220" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>
  <g transform="translate(180, 120)">
    <!-- Axe Réel -->
    <line x1="-130" y1="0" x2="140" y2="0" stroke="#0f172a" stroke-width="2"/>
    <polygon points="145,0 135,-4 135,4" fill="#0f172a"/>
    <text x="135" y="18" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8">Axe Réel (Re)</text>
    
    <!-- Axe Imaginaire -->
    <line x1="0" y1="80" x2="0" y2="-100" stroke="#0f172a" stroke-width="2"/>
    <polygon points="0,-105 -4,-95 4,-95" fill="#0f172a"/>
    <text x="10" y="-95" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">Axe Imaginaire (Im)</text>
    
    <!-- Point M(z) : z = a + ib = r e^(iθ) -->
    <circle cx="80" cy="-60" r="5" fill="#b91c1c"/>
    <text x="95" y="-65" font-family="Liberation Sans" font-size="13" font-weight="bold" fill="#b91c1c">M (z = a + i b)</text>
    
    <!-- Module r -->
    <line x1="0" y1="0" x2="80" y2="-60" stroke="#b91c1c" stroke-width="3"/>
    <text x="35" y="-38" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">r = |z|</text>
    
    <!-- Projections a et b -->
    <line x1="80" y1="0" x2="80" y2="-60" stroke="#94a3b8" stroke-dasharray="3"/>
    <text x="80" y="18" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#1d4ed8" text-anchor="middle">a</text>
    <line x1="0" y1="-60" x2="80" y2="-60" stroke="#94a3b8" stroke-dasharray="3"/>
    <text x="-15" y="-56" font-family="Liberation Sans" font-size="12" font-weight="bold" fill="#b91c1c">i b</text>
    
    <!-- Argument θ -->
    <path d="M 30,0 A 30 30 0 0 0 24,-18" fill="none" stroke="#d97706" stroke-width="2"/>
    <text x="35" y="-8" font-family="Liberation Sans" font-size="11" font-weight="bold" fill="#d97706">θ</text>
  </g>
  <g transform="translate(370, 50)" font-family="Liberation Sans" font-size="12">
    <rect x="0" y="0" width="150" height="90" rx="6" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
    <text x="75" y="24" font-weight="bold" fill="#d97706" text-anchor="middle">Forme d'Euler :</text>
    <text x="12" y="48" font-weight="bold" fill="#0f172a">z = r · e^(i θ)</text>
    <text x="12" y="68" fill="#1d4ed8">r = √(a² + b²)</text>
    <text x="12" y="85" fill="#15803d">θ = arg(z)</text>
  </g>
</svg>""")

print("Volume VI: All SVG figures generated and verified successfully.")
