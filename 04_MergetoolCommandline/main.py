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

    def do_generate(selfself, args):