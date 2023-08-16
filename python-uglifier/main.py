#!/usr/bin/env python3

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
    # ( 0x0021, 0x0021 ),
    # ( 0x0023, 0x0026 ),
    ( 0x0041, 0x005a ),     # uppercase
    ( 0x0061, 0x007a ),     # lowercase
    ( 0x0675, 0x06d0 ),     # arabic
    # ( 0x00A1, 0x00AC ),
    # ( 0x00AE, 0x00FF ),
    # ( 0x0100, 0x017F ),
    # ( 0x0180, 0x024F ),
    # ( 0x2C60, 0x2C7F ),
    # ( 0x16A0, 0x16F0 ),
    # ( 0x0370, 0x0377 ),
    # ( 0x037A, 0x037E ),
    # ( 0x0384, 0x038A ),
    # ( 0x038C, 0x038C ),
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
def import_swapper(lines: list[str], r: float, tokens: set[str]):
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

def __get_random_tab_count(r: float, tab_size: int):
    return random.randint(
        max(1, tab_size - int(r * 3)), 
        tab_size + int(r * tab_size)
    )

def __get_indent_schema(lines: list[str]):
    indent_schema = []
    for line in lines:
        line = line.replace('\t', '    ')
        indent_schema.append(len(line) - len(line.lstrip()))
    tab_size = math.gcd(*indent_schema)
    return [t // tab_size for t in indent_schema], tab_size

def whitespace_demon(lines: list[str], r: float):

    # add random tab counts
    tab_additions = []
    tab_schema, tab_size = __get_indent_schema(lines)
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

    # adds spaces whenever can
    code = "\n".join(random_tabs)
    available_idx = [0] * len(code)
    for paren in re.finditer(r"\(.*?\)", code):
        bounds = paren.span()
        available_idx[bounds[0]:bounds[1]] = [1] * (bounds[1] - bounds[0])
    for f_string in re.finditer(r"(?<=\_\_str0\_\_in\_\_code\_\_)\{[\s\S]*?\}(?=\_\_str0\_\_in\_\_code\_\_)", code, overlapped=True):
        fbounds = f_string.span()
        available_idx[fbounds[0]:fbounds[1]] = [0] * (fbounds[1] - fbounds[0])

    # find all commas, check if position is legit
    code_list = list(code)
    for comma in reversed([*re.finditer(",", code)]):
        if available_idx[(s:=comma.span()[0])]:

            # generate the random spaces
            space_addition = "" if random.random() < r else ","
            if not space_addition:
                for i in range((n:=__get_random_tab_count(r, 4))):
                    if random.random() < r / 4:
                        space_addition += "\n"
                    space_addition += " "
                    if i == n // 2:
                        space_addition += ","
            code_list[s:s+1] = [*space_addition]

    # return as list of lines
    return ''.join(code_list).split('\n')

def change_variable_names(lines: list[str], r: float, tokens: set[str]):
    
    # regex patterns
    variables = re.compile(r"(?<![:\(\.].*)[A-Za-z_]\w*(?= *(: *[a-zA-Z_]\w*)? *=[^=])")
    functions = re.compile(r"(?<=def *)[A-Za-z_]\w*")
    classes = re.compile(r"(?<=class *)[A-Za-z_]\w*")
    func_heads = re.compile(r"(?<=def *[A-Za-z_]\w*)\([\s\S]*?\)")

    # gets all the variables, in a set
    code = "\n".join(lines)
    var_names = {*map(lambda x: x.group(), variables.finditer(code))}
    class_names = {*classes.findall(code)}
    func_names = {*functions.findall(code)}

    # replace all the function heads 
    tab_schema, _ = __get_indent_schema(lines)
    for func in func_heads.finditer(code):

        # determine replacements for each variable in the header
        func_inside = func.group()[1:-1]
        no_special_types = re.sub(r"\[.*\]", "", func_inside)
        func_vars = map(lambda x: re.sub(r"\=.*", "", re.sub(r":.*", "", x)).strip(), no_special_types.split(','))

        # determine how long the function spans
        header_line = code[:func.span()[0]].count("\n")
        header_tab = tab_schema[header_line]
        func_span = header_line,
        for i in range(header_line+1, len(lines)):
            if header_tab == tab_schema[i]:
                func_span += i,
                break

        # determine mappings for the function variables
        mappings = {}
        for name in filter(lambda x: bool(x), func_vars):
            mappings[name] = get_true_random_sub(name, r, tokens)

        # replace everything in the function body in the range
        for i in range(*func_span):
            for old, new in mappings.items():
                lines[i] = re.sub(fr"(?<!(\w|\.\s*)){old}(?!\w)", new, lines[i])

    # generate mappings
    mappings = {}
    for name in filter(lambda x: not (x.startswith('__') and x.endswith('__')),[*(var_names | class_names | func_names)]):
        mappings[name] = get_true_random_sub(name, r, tokens)
    
    # do replacements
    for idx, line in enumerate(lines):
        for old, new in mappings.items():
            line = re.sub(fr"(?<!(\w|\.\s*)){old}(?!\w)", new, line)
        lines[idx] = line

    # replace function variables
    return lines

# add random comments everywhere
def commentate(lines: list[str], r: float):
    for idx, line in enumerate(lines):
        if random.random() < r:
            line += f"{' ' * random.randint(0, 10)}#{''.join(random.choices(VARIABLE_CHARS, k=__get_random_tab_count(r, 40)))}"
            lines[idx] = line
    return lines

def uglify(python_code: str, r: float) -> str:

    # conserve the strings
    unstrung, STRINGS = remove_strings(python_code)

    # get the unique tokens appearing in the thing
    tokens = get_unique_tokens(unstrung)
    
    # preprocessing
    stripped_lines = [*map(lambda x: x.rstrip(), unstrung.split("\n"))]
    filtered_lines = re.sub(r'\n{2,}', r'\n', '\n'.join(stripped_lines)).strip().split("\n")

    # mess with the imports
    import_swapped = import_swapper(filtered_lines, r, tokens)

    # change the variable names
    changed_vars = change_variable_names(import_swapped, r, tokens)

    # mess with whitespace
    whitespaced = whitespace_demon(changed_vars, r)

    # add random comments
    commentated = commentate(whitespaced, r)

    # replace strings 
    restrung = replace_strings("\n".join(commentated), STRINGS)
    return restrung

def get_args():
    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", type=str, required=True)
    parser.add_argument("-o", "--outfile", type=str, required=True)
    parser.add_argument("-c", "--chaos_level", type=float, default=0.2)
    return parser.parse_args()

def main():

    # get arguments
    args = get_args()
    infile: str = args.infile
    outfile: str = args.outfile
    randomness: float = args.chaos_level

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