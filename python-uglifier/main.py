#!/usr/bin/env python3

# TODO: find exact locations for performing replacements, then do those subs there

# challenge: convolute the code as much as possible while keeping
# every bit of the original functionality, including printing
# module imports, variable values, etc.

import regex as re
import math
import random
import tokenize
from copy import copy
from argparse import ArgumentParser

include_ranges = [
    ( 0x0021, 0x0021 ),
    ( 0x0023, 0x0026 ),
    ( 0x0028, 0x007E ),
    ( 0x00A1, 0x00AC ),
    ( 0x00AE, 0x00FF ),
    ( 0x0100, 0x017F ),
    ( 0x0180, 0x024F ),
    ( 0x2C60, 0x2C7F ),
    ( 0x16A0, 0x16F0 ),
    ( 0x0370, 0x0377 ),
    ( 0x037A, 0x037E ),
    ( 0x0384, 0x038A ),
    ( 0x038C, 0x038C ),
]

VARIABLE_CHARS = [
    chr(code_point) for current_range in include_ranges
        for code_point in range(current_range[0], current_range[1] + 1)
]

# convert str to list but with """ counting as a char
def __str_to_list(s: str) -> list[str]:
    changed_chars = []
    for a in map(lambda x: [*x], s.split('"""')):
        changed_chars += [*a, '"""']
    return changed_chars[:-1]

# find all the strings in order to preserve them
def __find_strings(s: str) -> list[str]:
    strings = []
    modified_code = __str_to_list(s)
    temp_inside, temp_index, in_string = "", 0, None
    for i, c in enumerate(modified_code):
        if in_string or c in ['"', "'", '"""']:
            temp_inside += c
        if c in ['"', "'", '"""'] and not in_string:
            while i > 0 and (mod:=modified_code[i-1]).lower() in 'frbu':
                temp_inside, i = mod + temp_inside, i - 1
            in_string = c
            temp_index = i
        elif c == in_string:
            strings.append((temp_inside, (temp_index, i + 1)))
            temp_inside, temp_index, in_string = "", None, 0
    return strings

# find all bracketed expressions within f_strings
def __inside_f_strings(s: str) -> list[str]:
    level = 0 
    inside_f_strings = []
    temp_inside = ""
    start_index = 0
    for i, c in enumerate(s):
        if level > 0 or c == "{":
            temp_inside += c
        if c == "{":
            level += 1
            if level == 1:
                start_index = i
        elif c == "}":
            level -= 1
            if not level:
                inside_f_strings.append((start_index, i + 1))
                temp_inside = ""
    return inside_f_strings

# update this to find strings, then find the f-string expressions WITHIN them
def remove_strings(code):

    # loop for replacing code and finding strings
    def generate_real_strings(code, layer):
        strings, real_strings = __find_strings(code), []
        code = __str_to_list(code)
        
        for s, (l, r) in strings:
            if not 'f' in s[:s.index(s[-1])]:
                real_strings.append((s, (l, r)))
                continue

            f_parts = __inside_f_strings(s)
            
            # determine the indeces of the f-strings
            left_indeces, right_indeces = [0], []
            for (ll, rr) in f_parts:
                left_indeces.append(rr)
                right_indeces.append(ll)
            right_indeces.append(len(s))
            
            # get the non-f-strings
            non_f_parts = []
            for fl, fr in zip(left_indeces, right_indeces):
                non_f_parts.append((s[fl:fr], (fl+l, fr+l)))
            real_strings.extend(non_f_parts)

        for s, (l, r) in reversed(real_strings):
            code[l:r] = f"__str{layer}__in__code__"
        return real_strings, "".join(code)
    
    # perform all replacements and find all strings
    strings, i = [], 0
    while True:
        part_strings, code = generate_real_strings(code, i)
        if not part_strings:
            break
        strings.append(part_strings)
        i += 1

    return code, strings

# replace the strings in the code
def replace_strings(code, strings):
    for i, level in reversed([*enumerate(strings)]):
        for s in level:
            code = code.replace(f"__str{i}__in__code__", s[0], 1)
    return code
    
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
            new_lines[idx] = re.sub(fr"(?<!(\w|\.\s*)){old}(?!\w)", new, new_lines[idx])
    
    return new_lines

def __get_random_tab_count(r: int, tab_size: int):
    return random.randint(
        max(1, tab_size - int(r * 3)), 
        tab_size + int(r * tab_size)
    )

def whitespace_demon(lines: list[str], r: int):

    # determine levels
    indent_schema = []
    for line in lines:
        line = line.replace('\t', '    ')
        indent_schema.append(len(line) - len(line.lstrip()))
    tab_size = math.gcd(*indent_schema)
    tab_schema = [t // tab_size for t in indent_schema]

    # add random tab counts
    tab_additions = []
    length_cache = [0] * (max(tab_schema) + 1)
    old_count = 0
    for n in tab_schema:
        if n > old_count:
            length_cache[n] = __get_random_tab_count(r, tab_size)
        old_count = n
        tab_additions.append(sum(length_cache[:n+1]))

    # add the tabs and also add the new lines
    random_tabs = []
    for line, tab_size in zip(lines, tab_additions):
        random_tabs.append(tab_size * " " + line.lstrip())
    return random_tabs

def change_variable_names(lines):
    
    # TODO: work on this regex 
    variables = re.compile(r"[A-Za-z_]\w*(?= *(: *[a-zA-Z_]\w*)? *=[^=])")
    functions = re.compile(r"def *[A-Za-z_]\w*")
    classes = re.compile(r"class *[A-Za-z_]\w*")

    print(variables.findall("\n".join(lines)))

def uglify(python_code: str, r: int) -> str:

    # conserve the strings
    unstrung, STRINGS = remove_strings(python_code)

    # get the unique tokens appearing in the thing
    tokens = get_unique_tokens(unstrung)
    
    # preprocessing
    stripped_lines = [*map(lambda x: x.rstrip(), python_code.split("\n"))]
    filtered_lines = re.sub(r'\n{2,}', r'\n', '\n'.join(stripped_lines)).strip().split("\n")

    # mess with the imports
    import_swapped = import_swapper(filtered_lines, r, tokens)

    # mess with whitespace
    whitespaced = whitespace_demon(import_swapped, r)

    change_variable_names(import_swapped)

    # replace strings 
    restrung = replace_strings("\n".join(whitespaced), STRINGS)
    return restrung

def main():

    # get arguments
    args = get_args()
    infile: str = args.infile
    outfile: str = args.outfile
    randomness: int = args.chaos_level

    # make sure randomness is good
    assert 0 < randomness < 1, "Invalid randomness given, must be between 0 and 1."

    # perform uglification but first remove all the comments
    with open(infile, 'rb') as f_in, open(outfile, 'w') as f_out:
        tokens = tokenize.tokenize(f_in.readline)
        uncommented_tokens = [t for t in tokens if t.type != tokenize.COMMENT]
        new_code = tokenize.untokenize(uncommented_tokens).decode()
        f_out.write(uglify(new_code, randomness))

if __name__ == "__main__":
    main()