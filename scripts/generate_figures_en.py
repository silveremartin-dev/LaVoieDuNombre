import os, re, shutil, json, sys
sys.stdout.reconfigure(encoding='utf-8')

translations = {}
for fn in ['master_svg_translations.json', 'complete_fr_to_en_svg.json', 'exact_226.json', 'exact_final_12.json']:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            translations.update(json.load(f))

# Also add uppercase keys
for k, v in list(translations.items()):
    translations[k.upper()] = v.upper()

sorted_phrases = sorted(translations.keys(), key=lambda x: len(x), reverse=True)

src_dir = 'figures'
dst_dir = 'figures_en'

if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)

shutil.copytree(src_dir, dst_dir)
print(f"Copied {src_dir} to {dst_dir}")

word_replacements = [
    (r'\b[Dd]izaines?\b', 'Tens'),
    (r'\b[Uu]nit[eé]s?\b', 'Units'),
    (r'\b[Cc]entaines?\b', 'Hundreds'),
    (r'\b[Mm]illiers?\b', 'Thousands'),
    (r'\b[Ss]ommet\b', 'Vertex'),
    (r'\b[Ss]ommets\b', 'Vertices'),
    (r'\b[Pp]ente\b', 'Slope'),
    (r'\b[Aa]bscisses?\b', 'Abscissa'),
    (r'\b[Oo]rdonn[eé]es?\b', 'Ordinate'),
    (r'\b[Dd][eé]riv[eé]e\b', 'Derivative'),
    (r'\b[Tt]angente\b', 'Tangent'),
    (r'\b[Aa]ire\b', 'Area'),
    (r'\b[Pp][eé]rim[eè]tre\b', 'Perimeter'),
    (r'\b[Hh]auteur\b', 'Height'),
    (r'\b[Ll]ongueur\b', 'Length'),
    (r'\b[Ll]argeur\b', 'Width'),
    (r'\b[Rr]ayon\b', 'Radius'),
    (r'\b[Dd]iam[eè]tre\b', 'Diameter'),
    (r'\b[Cc]ercle\b', 'Circle'),
    (r'\b[Dd]isque\b', 'Disk'),
    (r'\b[Cc]arr[eé]\b', 'Square'),
    (r'\b[Rr]ectangle\b', 'Rectangle'),
    (r'\b[Tt]riangle\b', 'Triangle'),
    (r'\b[Dd]roite\b', 'Line'),
    (r'\b[Vv]ecteur\b', 'Vector'),
    (r'\b[Pp]roduit\b', 'Product'),
    (r'\b[Ss]omme\b', 'Sum'),
    (r'\b[Dd]iff[eé]rence\b', 'Difference'),
    (r'\b[Qq]uotient\b', 'Quotient'),
    (r'\b[Rr]este\b', 'Remainder'),
    (r'\b[Ff]raction\b', 'Fraction'),
    (r'\b[Nn]ombre\b', 'Number'),
    (r'\b[Nn]ombres\b', 'Numbers'),
    (r'\b[Cc]hiffre\b', 'Digit'),
    (r'\b[Cc]hiffres\b', 'Digits'),
    (r'\b[Éé]galit[eé]\b', 'Equality'),
    (r'\b[Éé]quilibre\b', 'Balance'),
    (r'\b[Éé]change\b', 'Trade'),
    (r'\b[Dd][eé]part\b', 'Start'),
    (r'\b[Aa]rriv[eé]e\b', 'Finish'),
    (r'\b[Mm]ilieu\b', 'Midpoint'),
    (r'\b[Oo]rigine\b', 'Origin'),
    (r'\b[Aa]xe\b', 'Axis'),
    (r'\b[Cc]entre\b', 'Center'),
    (r'\b[Mm]iroir\b', 'Mirror'),
    (r'\b[Pp]liage\b', 'Folding'),
    (r'\b[Ee]ntr[eé]e\b', 'Input'),
    (r'\b[Ss]ortie\b', 'Output'),
    (r'\b[Mm]achine\b', 'Machine'),
    (r'\b[Aa]ngle\s+droit\b', 'Right angle'),
    (r'\b[Aa]ngle\s+aigu\b', 'Acute angle'),
    (r'\b[Aa]ngle\s+obtus\b', 'Obtuse angle'),
    (r'\b[Aa]ngle\s+plat\b', 'Straight angle'),
    (r'\b[Hh]orizontale?\b', 'Horizontal'),
    (r'\b[Vv]erticale?\b', 'Vertical'),
    (r'\b[Pp]arall[eè]les?\b', 'Parallel'),
    (r'\b[Pp]erpendiculaires?\b', 'Perpendicular'),
    (r'\b[Pp]ositi[fv]es?\b', 'Positive'),
    (r'\b[Nn][eé]gati[fv]es?\b', 'Negative'),
    (r'\b[Cc]roissante?\b', 'Increasing'),
    (r'\b[Dd][eé]croissante?\b', 'Decreasing'),
    (r'\b[Pp]aire\b', 'Even'),
    (r'\b[Ii]mpaire?\b', 'Odd'),
    (r'\b[Mm]aximum\b', 'Maximum'),
    (r'\b[Mm]inimum\b', 'Minimum'),
    (r'\b[Mm][eé]diane\b', 'Median'),
    (r'\b[Qq]uartiles?\b', 'Quartiles'),
    (r'\b[Éé]cart-type\b', 'Standard deviation'),
    (r'\b[Ee]sp[eé]rance\b', 'Expected value'),
    (r'\b[Pp]robabilit[eé]\b', 'Probability'),
    (r'\b[Pp]robabilit[eé]s\b', 'Probabilities'),
    (r'\b[Ss]ucc[eè]s\b', 'Success'),
    (r'\b[Éé]chec\b', 'Failure'),
    (r'\b[Éé]preuve\b', 'Trial'),
    (r'\b[Éé]preuves\b', 'Trials'),
    (r'\b[Éé]v[eé]nement\b', 'Event'),
    (r'\b[Éé]v[eé]nements\b', 'Events'),
    (r'\b[Cc]onditionnelle?\b', 'Conditional'),
    (r'\b[Dd][eé]cision\b', 'Decision'),
    (r'\b[Tt]h[eé]or[eè]me\b', 'Theorem'),
    (r'\b[Rr][eè]gle\b', 'Rule'),
    (r'\b[Pp]ropri[eé]t[eé]\b', 'Property'),
    (r'\b[Dd][eé]monstration\b', 'Proof'),
    (r'\b[Dd][eé]finition\b', 'Definition'),
    (r'\b[Ee]xemple\b', 'Example'),
    (r'\b[Mm][eé]thode\b', 'Method'),
    (r'\b[Ee]nsemble\b', 'Set'),
    (r'\b[Ee]nsembles\b', 'Sets'),
    (r'\b[Ii]ntersection\b', 'Intersection'),
    (r'\b[Rr][eé]union\b', 'Union'),
    (r'\b[Cc]ompl[eé]mentaire\b', 'Complement'),
    (r'\b[Cc]ontinuit[eé]\b', 'Continuity'),
    (r'\b[Cc]onvexit[eé]\b', 'Convexity'),
    (r'\b[Cc]oncavit[eé]\b', 'Concavity'),
    (r'\b[Ii]nflexion\b', 'Inflection'),
    (r'\b[Aa]symptote\b', 'Asymptote'),
    (r'\b[Ii]nt[eé]grale\b', 'Integral'),
    (r'\b[Rr][eé]currence\b', 'Induction'),
    (r'\b[Mm]atrice\b', 'Matrix'),
    (r'\b[Mm]atrices\b', 'Matrices'),
    (r'\b[Gg]raphe\b', 'Graph'),
    (r'\b[Gg]raphes\b', 'Graphs'),
    (r'\b[Cc]omplexe\b', 'Complex'),
    (r'\b[Cc]omplexes\b', 'Complex'),
    (r'\b[Mm]odule\b', 'Modulus'),
    (r'\b[Aa]rgument\b', 'Argument'),
    (r'\b[Pp]ar paquets de 5\b', 'in tallies of 5'),
    (r'\b[Pp]ar paquets de 10\b', 'in bundles of 10'),
    (r'\bvers la droite\b', 'to the right'),
    (r'\bvers la gauche\b', 'to the left'),
    (r'\bplus grand que\b', 'greater than'),
    (r'\bplus petit que\b', 'less than'),
    (r'\b[Cc]e qui reste\b', 'What remains'),
    (r'\b[Qq]uantit[eé] initiale\b', 'Initial quantity'),
    (r'\b[Pp]art de chacun\b', "Each person's share"),
    (r'\b[Cc]e que l\'on partage\b', 'What is being shared'),
    (r'\b[Cc]hemin\b', 'Path'),
    (r'\b[Cc]hemins\b', 'Paths'),
    (r'\b[Cc]hoix\b', 'Choice'),
    (r'\b[Aa]rrangements?\b', 'Permutations'),
    (r'\b[Cc]ombinaisons?\b', 'Combinations'),
    (r'\b[Pp]ermutations?\b', 'Permutations'),
    (r'\bavec\b', 'with'),
    (r'\b[Dd]ans\b', 'In'),
    (r'\b[Pp]our\b', 'For'),
    (r'\b[Ss]ur\b', 'on'),
    (r'\b[Ss]ous\b', 'under'),
    (r'\b[Dd]e\b', 'of'),
    (r'\b[Dd]u\b', 'of the'),
    (r'\b[Dd]es\b', 'of the'),
    (r'\b[Ll]e\b', 'The'),
    (r'\b[Ll]a\b', 'The'),
    (r'\b[Ll]es\b', 'The'),
    (r'\b[Uu]n\b', 'A'),
    (r'\b[Uu]ne\b', 'A')
]

translated_svg_count = 0

for root, dirs, files in os.walk(dst_dir):
    for f in sorted(files):
        if f.endswith('.svg'):
            p = os.path.join(root, f)
            content = open(p, 'r', encoding='utf-8', errors='ignore').read()
            original = content
            
            # Step 1: Replace exact master phrases
            for fr_phrase in sorted_phrases:
                en_phrase = translations[fr_phrase]
                if fr_phrase in content:
                    content = content.replace(fr_phrase, en_phrase)
            
            # Step 2: Apply word-level regexes on remaining <text> and <tspan> tags
            def repl_tag(m):
                tag_start = m.group(1)
                text_inner = m.group(2)
                tag_end = m.group(3)
                for pat, rep in word_replacements:
                    text_inner = re.sub(pat, rep, text_inner)
                return f"{tag_start}{text_inner}{tag_end}"
            
            content = re.sub(r'(<text\b[^>]*>)(.*?)(</text>)', repl_tag, content, flags=re.DOTALL)
            content = re.sub(r'(<tspan\b[^>]*>)(.*?)(</tspan>)', repl_tag, content, flags=re.DOTALL)
            
            if content != original:
                translated_svg_count += 1
                with open(p, 'w', encoding='utf-8') as out:
                    out.write(content)

print(f"Successfully translated {translated_svg_count} SVGs in {dst_dir}!")
