import sys
import locale
from figdate import figdate

if __name__ == '__main__':
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    if len(sys.argv) == 3:
        print(figdate(sys.argv[1], sys.argv[2]))
    elif len(sys.argv) == 2:
        print(figdate(format=sys.argv[1]))
    else:
        raise AttributeError()