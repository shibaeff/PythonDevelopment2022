import readline
import shlex
import cmd
import importlib
from pynames import GENDER, LANGUAGE


class Generator(cmd.Cmd):
    lang = LANGUAGE.EN

    def do_language(self, args):
        if args == 'RU':
            self.lang = LANGUAGE.RU
        elif args == 'EN':
            self.lang = LANGUAGE.EN
        elif args == 'NATIVE':
            self.lang = LANGUAGE.NATIVE

    def do_info(self, args):
        arguments = shlex.split(args)
        i = importlib.import_module('pynames.generators.' + arguments[0])
        generator_objects = [s for s in dir(i) if s.endswith('NamesGenerator')]
        match arguments:
            case [_, 'language']:
                for object_name in generator_objects:
                    cls = eval(f'i.{object_name}')()
                    print(f'class {object_name} has {cls.languages} languages')
            case [_, _]:
                for object_name in generator_objects:
                    cls = eval(f'i.{object_name}')()
                    match arguments[-1]:
                        case 'male':
                            print(f'class {object_name} has {cls.get_names_number(GENDER.MALE)} male names')
                        case 'female':
                            print(f'class {object_name} has {cls.get_names_number(GENDER.FEMALE)} female names')
            case [_]:
                for object_name in generator_objects:
                    cls = eval(f'i.{object_name}')()
                    print(f'class {object_name} has {cls.get_names_number()} names')