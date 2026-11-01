import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('all_fr_block_actions.json', 'r', encoding='utf-8') as f:
    fr_actions = json.load(f)

with open('callout_titles_en.json', 'r', encoding='utf-8') as f:
    titles_en = json.load(f)

with open('svg_captions_en.json', 'r', encoding='utf-8') as f:
    svg_captions_en = json.load(f)

# Table translations
table_fr_to_en = {
    "[*Angle Aigu*], [*Angle Droit*], [*Angle Obtus*]": "[*Acute Angle*], [*Right Angle*], [*Obtuse Angle*]",
    "[Plus fermé que l'équerre], [Épouse exactement l'équerre], [Plus ouvert que l'équerre]": "[More closed than square], [Fits square exactly], [More open than square]",
    "[Ouverture $< 90 degree$], [Ouverture $= 90 degree$], [Ouverture $> 90 degree$]": "[Aperture $< 90 degree$], [Aperture $= 90 degree$], [Aperture $> 90 degree$]",
    "[*Noyau*], [*Atome*], [*Humain*], [*Terre*], [*Système Solaire*], [*Galaxie*]": "[*Nucleus*], [*Atom*], [*Human*], [*Earth*], [*Solar System*], [*Galaxy*]",
    "[*1. Diagramme en bâtons*], [*2. Histogramme (classes)*], [*3. Diagramme circulaire*]": "[*1. Bar Chart*], [*2. Histogram (bins)*], [*3. Pie Chart*]",
    "[Valeurs discrètes isolées], [Intervalles continus accolés], [Parts proportionnelles à $360 degree$]": "[Isolated discrete values], [Adjacent continuous intervals], [Slices proportional to $360 degree$]",
    "[Hauteur proportionnelle à l'effectif], [Aire du rectangle proportionnelle à l'effectif], [Angle proportionnel à la fréquence (%)]": "[Height proportional to count], [Area proportional to count], [Angle proportional to frequency (%)]",
    "Somme $2^n$": "Sum $2^n$",
    "Prix (€)": "Price ($)",
    "Poids (kg)": "Weight (kg)",
    "Distance (km)": "Distance (km)",
    "Temps (h)": "Time (h)",
    "Fréquence": "Frequency",
    "Effectif": "Count / Frequency"
}

en_action_map = {}
for a in fr_actions:
    v = a['vol']
    ch = a['chapter']
    ch_num = int(re.search(r'Chapitre_(\d+)', ch).group(1))
    b_idx = a['block_idx']
    r_fr = a['res_fr']
    
    key = (v, ch_num, b_idx)
    
    # SVG check
    m_svg = re.search(r'!\[(.*?)\]\((figures/[^)]+\.svg)\)', r_fr)
    if m_svg:
        fig_path = m_svg.group(2)
        if fig_path in svg_captions_en:
            cap_en, new_path = svg_captions_en[fig_path]
            en_action_map[key] = ("SVG", cap_en, new_path)
        else:
            en_action_map[key] = ("SVG", m_svg.group(1), fig_path.replace("figures/", "figures_en/"))
        continue
        
    # Callout check
    m_cal = re.search(r'> \*\*([^*]+)\*\*', r_fr)
    if m_cal:
        tit_fr = m_cal.group(1).strip()
        tit_en = titles_en.get(tit_fr, tit_fr)
        en_action_map[key] = ("CALLOUT", tit_en)
        continue
        
    # Calc op check
    if 'calc_op' in r_fr:
        en_action_map[key] = ("CALC_OP",)
        continue
        
    # Table check
    if 'data_table' in r_fr:
        if '#table(' in r_fr:
            # translate table contents
            t_content = r_fr
            for k, val in table_fr_to_en.items():
                t_content = t_content.replace(k, val)
            en_action_map[key] = ("TABLE", t_content)
        else:
            en_action_map[key] = ("DATA_TABLE_RAW",)
        continue
        
    en_action_map[key] = ("RAW", r_fr)

print(f"Total mapped actions: {len(en_action_map)}")
with open('en_action_map.json', 'w', encoding='utf-8') as out:
    # serializable keys
    ser = {f"{k[0]}|{k[1]}|{k[2]}": v for k, v in en_action_map.items()}
    json.dump(ser, out, ensure_ascii=False, indent=2)
print("Saved en_action_map.json")
