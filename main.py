from utils import *
import fade, os, ctypes

ct = ctypes.windll.kernel32.SetConsoleTitleW
ct("TITLEHERE")