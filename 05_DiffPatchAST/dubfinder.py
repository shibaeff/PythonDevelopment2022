import argparse
import importlib
import inspect
import sys
import textwrap
import ast
import difflib
from collections import defaultdict

functions = dict()
diffb = defaultdict()


def get_functions(pkg, prefix_line):
    for name, value in inspect.getmembers(pkg):
        if inspect.isclass(value) and name.startswith("__"):
            continue
        if inspect.isfunction(value):
            full_func_name = prefix_line + '.' + name
            functions[full_func_name] = value
        elif inspect.ismodule(value) and name in cmd_args or inspect.isclass(value):
            get_functions(value, prefix_line + '.' + name)


def read_args():
    return sys.argv[1:]


def find_similar():
    global body
    current_keys = list(diffb.keys())
    found = False
    for i, body in enumerate(current_keys):
        if difflib.SequenceMatcher(None, body, f_body).ratio() > THRESHOLD:
            diffb.setdefault(body, []).append(f_name)
            found = True
    if not found:
        # new body appear:
        diffb.setdefault(f_body, []).append(f_name)


def output():
    global body
    out = list()
    for body, f_names in diffb.items():
        if len(f_names) > 1:
            list.sort(f_names)
            out.append(f_names[0] + ' ' + f_names[1])
    list.sort(out)
    for line in out:
        print(line)


if __name__ == "__main__":
    global cmd_args
    cmd_args = read_args()

    for m in cmd_args:
        pkg = importlib.import_module(m)
        get_functions(pkg, m)

    for f_name, pointer in functions.items():
        text = textwrap.dedent(inspect.getsource(pointer))
        tree = ast.parse(text)
        for item in ast.walk(tree):
            for var_id in ['name', 'id', 'arg', 'attr']:
                if var_id in dir(item):
                    setattr(item, var_id, "_")

        functions[f_name] = ast.unparse(tree)
    THRESHOLD = 0.95
    for f_name, f_body in functions.items():
        find_similar()

    output()
