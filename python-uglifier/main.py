#!/usr/bin/env python3

# challenge: convolute the code as much as possible while keeping
# every bit of the original functionality, including printing
# module imports, variable values, etc.

import regex as re
import random
from copy import copy
from argparse import ArgumentParser

VARIABLE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"


# update this to find strings, then find the f-string expressions WITHIN them
def remove_strings(func):
    F_BEGIN    =  r'fr?{}[\s\S]*?[^{]*?{'
    F_END      =  r'(?<=fr?{}[^{}]*?{[\s\S]*?)}[^}]*?{}'
    F_BETWEEN  =  r'(?<=fr?{}[\s\S]*?})[\s\S]*?(?={[\s\S]*?{})'

    patterns = {
        "f_begin": {
            "single": re.compile(F_BEGIN.replace("{}", "'")),
            "double": re.compile(F_BEGIN.replace("{}", '"')),
            "triple": re.compile(F_BEGIN.replace("{}", '"""'))
        },
        "f_end": {
            "single": re.compile(F_END.replace("{}", "'")),
            "double": re.compile(F_END.replace("{}", '"')),
            "triple": re.compile(F_END.replace("{}", '"""'))
        },
        "f_between": {
            "single": re.compile(F_BETWEEN.replace("{}", "'")),
            "double": re.compile(F_BETWEEN.replace("{}", '"')),
            "triple": re.compile(F_BETWEEN.replace("{}", '"""'))
        }
    }
    stored_f_strings = copy(patterns)
    normal_strings = {
        "single": None,
        "double": None,
        "triple": None
    }

    def inner(code, *args):

        # replace all strings
        for quote, q in zip(['single', 'double', 'triple'], ["'", '"', '"""']):
            normal_strings[quote] = re.findall(r"(?<![fF])[rRbB]+{}[\s\S]*?{}".replace('{}', q), code)
            for s in normal_strings[quote]:
                code = code.replace(s, f'__normal__{quote}__')

        # get f strings
        for type, d in patterns.items():
            for quote, p in d.items():
                stored_f_strings[type][quote] = re.findall(p, code)

        # replace all f strings
        for type, d in stored_f_strings.items():
            for quote, strings in d.items():
                for s in strings:
                    code = code.replace(s, f"__{type}__{quote}__", 1)

        # perform all operations
        new_code: str = func(code, *args)

        # replace all f strings again
        for type, d in stored_f_strings.items():
            for quote, strings in d.items():
                for s in strings:
                    new_code = new_code.replace(f"__{type}__{quote}__", s, 1)

        # replace all strings 
        for quote in normal_strings:
            for s in normal_strings[quote]:
                new_code = new_code.replace(f"__normal__{quote}__", s, 1)

        return new_code
    
    return inner 

def get_args():
    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", type=str, required=True)
    parser.add_argument("-o", "--outfile", type=str, required=True)
    parser.add_argument("-c", "--chaos_level", type=float, default=0.2)
    return parser.parse_args()

# gets all the unique tokens in a string
def get_unique_tokens(python_code: str) -> set[str]:
    return {*re.findall(r"\w+", python_code)}

# get a unique string replacement for OG depending on randomness
def get_true_random_sub(og: str, r: float, tokens: set[str]):

    # gets a variation of the <og> string
    def get_random_variation():
        output = ''
        for c in og:
            output += random.choice(VARIABLE_CHARS) if random.random() < r else c
            if random.random() < r / 4:
                output += random.choice(VARIABLE_CHARS)
        return output
    
    # make sure new string is not already in use
    new_str = get_random_variation()
    while new_str in tokens:
        new_str = get_random_variation()
    tokens.add(new_str)
    return new_str

# mess with the imports
def import_swapper(lines: list[str], r: int, tokens: set[str]):
    mappings = {}; ignore_replace_idx = set(); new_lines = copy(lines)
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
            new_lines[idx] = re.sub(fr"(?<![\w.]){old}(?!\w)", new, new_lines[idx])
    
    return new_lines

def uncommentator(lines: list[str]):
    new_lines = copy(lines)
    for idx, line in enumerate(new_lines):
        pass

def whitespace_demon(lines: list[str], r: int, tokens: set[str]):
    pass

@remove_strings
def uglify(python_code: str, r: int) -> str:

    # remove strings from the code (including saving f-strings)


    tokens = get_unique_tokens(python_code)
    
    # preprocessing
    stripped_lines = [*map(lambda x: x.rstrip(), python_code.split("\n"))]
    filtered_lines = re.sub(r'\n{2,}', r'\n', '\n'.join(stripped_lines)).strip().split("\n")

    # mess with the imports
    import_swapped = import_swapper(filtered_lines, r, tokens)

    return "\n".join(import_swapped)

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