#! /bin/python3.10
import inspect
import sys
import importlib

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

def parse_function(func):
    pass

def compare_functions(funcs):
    pass

modules = sys.argv[1:]
print(f"Got modules: {modules}")
funcs = []
for mod in modules:
    funcs.extend(get_functions(mod))
print(funcs)
