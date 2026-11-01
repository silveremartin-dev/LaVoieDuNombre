import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

french_words = ['le', 'la', 'les', 'un', 'une', 'des', 'du', 'dans', 'pour', 'avec', 'sur', 'par', 'sans', 'sous', 'sommet', 'abscisse', 'ordonnée', 'croissante', 'décroissante', 'droite', 'gauche', 'dizaine', 'dizaines', 'centaine', 'centaines', 'caillou', 'cailloux', 'flèche', 'côté', 'côtés', 'moitié', 'partage', 'festin', 'bâton', 'renard', 'poisson', 'poissons', 'galette', 'potence', 'marmite']

residual = []

for root, dirs, files in os.walk('figures_en'):
    for f in sorted(files):
        if f.endswith('.svg'):
            p = os.path.join(root, f)
            c = open(p, 'r', encoding='utf-8', errors='ignore').read()
            # find text tags
            texts = re.findall(r'<text\b[^>]*>(.*?)</text>', c, re.DOTALL)
            for t in texts:
                clean = re.sub(r'<[^>]+>', ' ', t).strip()
                words = [w.lower() for w in re.findall(r'[a-zA-ZÀ-ÿ]{2,}', clean)]
                for fw in french_words:
                    if fw in words:
                        residual.append((f, fw, clean))

print(f"Residual French check in figures_en: {len(residual)} matches found.")
for f, fw, clean in residual[:30]:
    print(f"  {f} [{fw}]: {clean}")
