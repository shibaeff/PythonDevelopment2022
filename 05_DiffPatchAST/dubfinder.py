#! /bin/python3.10
import inspect
import sys
import importlib
import textwrap
import ast

def get_funcs(entity):
    print(entity)
    subentities = inspect.getmembers(entity, inspect.ismodule)
    subentities.extend(inspect.getmembers(entity, inspect.isclass))
    funcs = []
    for sub in subentities:
        funcs.extend(get_funcs(sub))
    return funcs

def get_functions(module, name):
    members = inspect.getmembers(module)
    functions = []
    for elem in members:
        if inspect.isfunction(elem[1]):
            functions += [(f"{name}.{elem[0]}", elem[1]), ]  # такая схема - чтобы сохранить путь к функции
        elif inspect.isclass(elem[1]):
            if not elem[0].startswith('__'):
                functions += get_functions(elem[1], f"{name}.{elem[0]}")
    return functions

def parse(fun):
    code = textwrap.dedent(inspect.getsource(fun[1]))
    tree = ast.parse(code)
    nodes = ast.walk(tree)
    for node in nodes:
        if hasattr(node, "id"):
            node.id = "_"
        elif hasattr(node, "name"):
            node.name = "_"
        elif hasattr(node, "arg"):
            node.arg = "_"
        elif hasattr(node, "attr"):
            node.attr = "_"
    return fun[0], ast.unparse(tree)


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
print(funcs)

    
