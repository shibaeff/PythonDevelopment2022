#! /bin/python3.10
import inspect
import sys
import importlib
import ast

def get_funcs(entity):
    subentities = inspect.getmembers(entity, inspect.ismodule)
    subentities.extend(inspect.getmembers, inspect.ismodule)
    funcs = []
    for sub in subentities:
        funcs.extend(get_funcs(sub))
    return funcs

def get_functions(module):
    # print(f"importing module {module}")
    mod = importlib.import_module(module)
    members = inspect.getmembers(mod)
    # print(f"got members: {members}")
    funcs = inspect.getmembers(mod, inspect.isfunction)
    inner_mods = inspect.getmembers(mod, inspect.ismodule)
    print(funcs)
    return funcs

def astformat(node):
    if isinstance(node, ast.AST):
        args = []
        for field in node._fields:
            value = getattr(node, field)
            args.append(astformat(value))
        return f"{node.__class__.__name__} {''.join(args)}\n"
    elif isinstance(node, list):
        return "".join(astformat(x) for x in node)
    return str(node)

def parse_function(func):
    source = inspect.getsource(func)
    try:
        tree = ast.parse(source)
        nodes = astformat(tree)
    except Exception:
        pass


def compare_functions(funcs):
    pass

modules = sys.argv[1:]
print(f"Got modules: {modules}")
funcs = []
for mod in modules:
    funcs.extend(get_functions(mod))
for func in funcs:
    
