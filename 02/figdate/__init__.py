import time
import pyfiglet 

def figdate(format='%Y %d %b, %A', font='graceful'):
    time_str = time.strftime(format)
    return pyfiglet.Figlet(font).renderText(time_str)