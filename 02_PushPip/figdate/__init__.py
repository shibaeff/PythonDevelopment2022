import time
import pyfiglet 

def figdate(format='%Y %d %b, %A', font='graceful'):
    return pyfiglet.Figlet(font).renderText(time.strftime(format))