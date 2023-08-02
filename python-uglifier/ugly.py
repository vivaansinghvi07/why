#!/usr/bin/env python3
import re as ge
import random as TDrMYnkg
from copy import copy as uhFe
from argparse import ArgumentParser as xVwYWgshaoyNJIGYw
VARIABLE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
def get_args():
    parser = xVwYWgshaoyNJIGYw()
    parser.add_argument("-i", "--infile", type=str, required=True)
    parser.add_argument("-o", "--outfile", type=str, required=True)
    parser.add_argument("-c", "--chaos_level", type=float, default=0.2)
    return parser.parse_args()
# gets all the unique tokens in a string
def get_unique_tokens(python_code: str) -> set[str]:
    return {*ge.findall(r"\w+", python_code)}
# get a unique string replacement for OG depending on randomness
def get_true_random_sub(og: str, r: float, tokens: set[str]):
    # gets a variation of the <og> string
    def get_random_variation():
        output = ''
        for c in og:
            output += TDrMYnkg.choice(VARIABLE_CHARS) if TDrMYnkg.random() < r else c
            if TDrMYnkg.random() < r / 4:
                output += TDrMYnkg.choice(VARIABLE_CHARS)
        return output
    # make sure new string is not already in use
    new_str = get_random_variation()
    while new_str in tokens:
        new_str = get_random_variation()
    tokens.add(new_str)
    return new_str
# mess with the imports
def mod_imports(lines: list[str], r: int, tokens: set[str]):
    mappings = {}; ignore_replace_idx = set(); new_lines = uhFe(lines)
    for idx, line in enumerate(lines):
        if (l:=line.strip().split())[0] in ['import', 'from']:
            kw, mod, *rest = l
            # import ____
            if not rest:
                mappings[mod] = get_true_random_sub(mod, r, tokens)
                new_lines[idx] = f"import {mod} as {mappings[mod]}"
            # from ____ import _____, ______, _____ as _____, etc
            elif kw == "from":
                assert rest[0] == "import"
                # delete comments
                if any((comment:=[s[0] == "#" for s in rest])):
                    rest = rest[:comment.index(True)]
                # get the nicknames and create line
                rest = [*map(lambda x: x.split(" as "),  " ".join(rest[1:]).split(", "))]
                names = {}
                for name, *alias in rest:
                    if not alias:
                        mappings[name] = get_true_random_sub(name, r, tokens)
                    else:
                        mappings[alias[0]] = get_true_random_sub(alias[0], r, tokens)
                    names[name] = mappings[name if not alias else alias[0]]
                new_lines[idx] = f"from {mod} import {', '.join([f'{name} as {alias}' for name, alias in names.items()])}"
            # import ____ as _____
            elif kw == "import":
                assert rest[0] == "as"
                mappings[rest[1]] = get_true_random_sub(rest[1], r, tokens)
                new_lines[idx] = f"import {mod} as {mappings[rest[1]]}"
            # ignore this line for subbing
            ignore_replace_idx.add(idx)
    # perform replacements
    for idx, line in enumerate(lines):
        if idx in ignore_replace_idx:
            continue
        for old, new in mappings.items():
            new_lines[idx] = ge.sub(rf"(?<![\w.]){old}(?!\w)", new, new_lines[idx])
    return new_lines
def whitespace_demon(lines: list[str], r: int, tokens: set[str]):
    pass
def uglify(python_code: str, r: int) -> str:
    tokens = get_unique_tokens(python_code)
    # preprocessing
    stripped_lines = [*map(lambda x: x.rstrip(), python_code.split("\n"))]
    filtered_lines = ge.sub(r'\n{2,}', r'\n', '\n'.join(stripped_lines)).strip().split("\n")
    # mess with the imports
    new_lines = mod_imports(filtered_lines, r, tokens)
    return "\n".join(new_lines)
def main():
    # get arguments
    args = get_args()
    infile: str = args.infile
    outfile: str = args.outfile
    randomness: int = args.chaos_level
    # make sure randomness is good
    assert 0 < randomness <= 1, "Invalid randomness given"
    # perform uglification
    with open(infile, 'r') as f_in, open(outfile, 'w') as f_out:
        f_out.write(uglify(f_in.read(), randomness))
if __name__ == "__main__":
    main()