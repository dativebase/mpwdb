"""
https://github.com/hbenbel/French-Dictionary

(venv) Joels-MacBook-Pro-2:french joeldunham$ cat French-Dictionary/decoder.txt 
1sg  -> 1ere personne singulier
1pl  -> 1ere personne pluriel
1isg -> 3e personne singulier
mas  -> masculin
fem  -> féminin
ipre -> indicatif présent
iimp -> indicatif imparfait
ipsi -> indicatif passé simple
ifut -> indicatif futur
     -> indicatif passé composé
     -> indicatif plus-que-parfait
     -> indicatif passé antérieur
     -> indicatif futur antérieur
spre -> subjonctif présent
simp -> subjonctif imparfait
     -> subjonctif plus-que-parfait
     -> subjonctif passé
cond -> conditionnel présent
     -> conditionnel passé
impe -> impératif présent
     -> impératif passé
infi -> infinitif présent
     -> infinitif passé
ppre -> participe présent
     -> paricipe passé composé
ppas -> participe passé

.
├── French-Dictionary
│   ├── LICENSE
│   ├── README
│   ├── decoder.txt
│   └── dictionary
│       ├── adjectives.txt
│       ├── adverbs.txt
│       ├── conjunctions.txt
│       ├── determiners.txt
│       ├── dictionary.txt
│       ├── nouns.txt
│       ├── prepositions.txt
│       ├── pronouns.txt
│       └── verbs.txt
└── analyze.py

bienpensante;fem;sg
bienpensantes;fem;pl
bienpensant;mas;sg
bienpensants;mas;pl
inplano;epi;sg
inplanos;epi;pl
nonpareille;fem;sg
nonpareilles;fem;pl
nonpareil;mas;sg
nonpareils;mas;pl
synpériplanaire;epi;sg
synpériplanaires;epi;pl

, ', -, ;, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, â, æ, ç, è, é, ê, ë, î, ï, ô, û, ü, œ


"""

import os
import re


FD_DIR = 'French-Dictionary'
DICT_DIR = 'dictionary'
ADJ_FNAME = 'adjectives.txt'
ADJ_FPATH = os.path.join(FD_DIR, DICT_DIR, ADJ_FNAME)

VOWELS_REGEX = (
    '(a|e|i|o|u|â|æ|ç|è|é|ê|ë|î|ï|ô|û|ü|œ)')
VOWELS_PATT = re.compile(VOWELS_REGEX)
CONSONANTS_REGEX = (
    '(b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z)')
CONSONANTS_PATT = re.compile(CONSONANTS_REGEX)

# labial consonants
LAB_C_REGEX = (
    '(b|m|p|w)')
#    '(b|f|m|p|v|w)')

# non-labial consonants
N_LAB_C_REGEX = (
    '(c|d|g|h|j|k|l|n|q|r|s|t|x|y|z)')
#    '(c|d|f|g|h|j|k|l|n|q|r|s|t|v|x|y|z)')

# prefixes ending in labial or alveolar nasal
PFX_END_NAS_REGEX = (
    '^('
    'i[mn]'
    '|'
    'no[mn]'
    '|'
    'sy[mn]'
    '|'
    'bie[mn]'
    ')'
)

# prefixes ending in labial nasal
PFX_END_LAB_REGEX = (
    '^('
    'im'
    '|'
    'nom'
    '|'
    'sym'
    '|'
    'biem'
    ')'
)

# prefixes ending in alveolar nasal
PFX_END_ALV_REGEX = (
    '^('
    'in'
    '|'
    'non'
    '|'
    'syn'
    '|'
    'bien'
    ')'
)

# Matches specific adj prefixes that end in [nm] followed by a consonant. Our widest net.
PATT = re.compile(
    f'{PFX_END_NAS_REGEX}'
    f'{CONSONANTS_REGEX}'
)

# Subnet that matches <LABIAL, LABIAL> sequences like "mp"
LAB_LAB_PATT = re.compile(
    f'{PFX_END_LAB_REGEX}'
    f'{LAB_C_REGEX}'
)

# Subnet that matches <NON-LABIAL, LABIAL> sequences like "np"
N_LAB_LAB_PATT = re.compile(
    f'{PFX_END_ALV_REGEX}'
    f'{LAB_C_REGEX}'
)

# Subnet that matches <LABIAL, NON-LABIAL> sequences like "mt"
LAB_N_LAB_PATT = re.compile(
    f'{PFX_END_LAB_REGEX}'
    f'{N_LAB_C_REGEX}'
)

# Subnet that matches <NON-LABIAL, NON-LABIAL> sequences like "nt"
N_LAB_N_LAB_PATT = re.compile(
    f'{PFX_END_ALV_REGEX}'
    f'{N_LAB_C_REGEX}'
)

def extract_adjs(fh):
    ret = {
        'chars': set(),
        'all': [],
        'lab_lab': [],
        'non_lab_lab': [],
        'lab_non_lab': [],
        'non_lab_non_lab': [],
    }
    for line in fh:
        line = line.strip()
        for c in line:
            ret['chars'].add(c)
        if PATT.search(line):
            if 'nomp' in line:
                print(line)

            ret['all'].append(line)

            if LAB_LAB_PATT.search(line):
                ret['lab_lab'].append(line)

            if N_LAB_LAB_PATT.search(line):
                ret['non_lab_lab'].append(line)

            if LAB_N_LAB_PATT.search(line):
                ret['lab_non_lab'].append(line)

            if N_LAB_N_LAB_PATT.search(line):
                ret['non_lab_non_lab'].append(line)
    for attr in (
            'lab_lab',
            'non_lab_lab',
            'lab_non_lab',
            'non_lab_non_lab'):
        v = ret[attr]
        print(attr)
        print(len(v))
        d = '\n  '
        if v:
            print(f'  {d.join(v)}')
        print('\n')

    print(', '.join(sorted(ret['chars'])))


with open(ADJ_FPATH, 'r', encoding='utf8') as fh:
    extract_adjs(fh)


