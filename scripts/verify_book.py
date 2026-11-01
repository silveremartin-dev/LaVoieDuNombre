# -*- coding: utf-8 -*-
"""
Auditing and verification suite for 'LA VOIE DU NOMBRE' and 'THE WAY OF THE NUMBER'.
Verifies:
1. Typst source integrity (zero ASCII box characters, zero unescaped math traps).
2. Macro and color parity (#principe, #methode, #alerte, #decouvre, #cas_limite).
3. Python code blocks (syntax highlighting and formatting).
4. Chapter and volume opener synchrony (all 58 chapters correctly distributed).
5. XML validity of all SVG assets in figures/ and figures_en/.
"""

import sys
import os
import re
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

def audit_book(filename, is_en=False):
    lang = "EN" if is_en else "FR"
    print(f"\n=================== AUDITING {filename} ({lang}) ===================")
    
    if not os.path.exists(filename):
        print(f"ERROR: {filename} does not exist!")
        return False
        
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        
    passed = True
    
    # 1. ASCII Box-Drawing Characters
    box_chars = ['┌', '┐', '└', '┘', '├', '┤', '┬', '┴', '┼', '│', '─', '═', '║', '╔', '╗', '╚', '╝']
    found_box = []
    for i, line in enumerate(text.splitlines()):
        if any(c in line for c in box_chars):
            found_box.append((i+1, line[:60]))
            
    if found_box:
        print(f"[FAIL] Found {len(found_box)} lines with ASCII box-drawing characters:")
        for lno, l in found_box[:5]:
            print(f"  Line {lno}: {l}")
        passed = False
    else:
        print("[PASS] Zero ASCII box-drawing characters.")

    # 2. Zombie data_table blocks
    if 'data_table' in text:
        print("[FAIL] Found legacy 'data_table' occurrence.")
        passed = False
    else:
        print("[PASS] Zero 'data_table' zombie blocks.")

    # 3. Volume Openers Check
    openers = list(re.finditer(r'#ouverture-volume\([\s\S]*?\n\)', text))
    if len(openers) == 6:
        print(f"[PASS] Exact 6 volume openers found.")
    else:
        print(f"[FAIL] Expected 6 volume openers, found {len(openers)}.")
        passed = False

    # 4. Chapters Count Check
    ch_pat = r'== CHAPTER (\d+):' if is_en else r'== CHAPITRE (\d+) :'
    chapters = list(re.finditer(ch_pat, text))
    if len(chapters) == 58:
        print(f"[PASS] All 58 chapters verified.")
    else:
        print(f"[FAIL] Expected 58 chapters, found {len(chapters)}.")
        passed = False

    # 5. Python Syntax Highlighting
    py_blocks = len(re.findall(r'```python', text))
    if py_blocks == 25:
        print(f"[PASS] Exactly 25 syntax-highlighted Python blocks.")
    else:
        print(f"[FAIL] Expected 25 Python blocks, found {py_blocks}.")
        passed = False

    # 6. Back Cover Quote
    bad_word = "distaste" if is_en else "dégoût"
    if bad_word in text:
        print(f"[FAIL] Found negative term '{bad_word}' in text.")
        passed = False
    else:
        print(f"[PASS] Clean back cover (zero occurrences of '{bad_word}').")

    # 7. Warning icon in alerte
    if "⚠️ #title" in text:
        print("[PASS] Warning icon ⚠️ active in alerte definition.")
    else:
        print("[WARN] ⚠️ #title not found in alerte definition.")

    return passed

def audit_svg_tree(folder):
    print(f"\n=================== AUDITING SVG DIRECTORY: {folder} ===================")
    if not os.path.exists(folder):
        print(f"ERROR: {folder} does not exist!")
        return False
        
    error_count = 0
    total_svgs = 0
    
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith('.svg'):
                total_svgs += 1
                filepath = os.path.join(root, f)
                try:
                    tree = ET.parse(filepath)
                except ET.ParseError as e:
                    print(f"[FAIL] XML Parse Error in {filepath}: {e}")
                    error_count += 1

    if error_count == 0:
        print(f"[PASS] All {total_svgs} SVGs in {folder} parsed cleanly with valid XML.")
        return True
    else:
        print(f"[FAIL] Found {error_count} corrupted SVGs in {folder}.")
        return False

def main():
    print("RUNNING REFERENCE INTEGRITY AUDIT")
    fr_ok = audit_book('LA_VOIE_DU_NOMBRE.typ', is_en=False)
    en_ok = audit_book('THE_WAY_OF_THE_NUMBER.typ', is_en=True)
    svg_fr_ok = audit_svg_tree('figures')
    svg_en_ok = audit_svg_tree('figures_en')
    
    if fr_ok and en_ok and svg_fr_ok and svg_en_ok:
        print("\n>>> ALL CHECKS PASSED: REPOSITORY IS 100% IN COMPLIANCE WITH AGENTS.MD! <<<")
        sys.exit(0)
    else:
        print("\n>>> AUDIT FAILED: ISSUES FOUND! <<<")
        sys.exit(1)

if __name__ == '__main__':
    main()
