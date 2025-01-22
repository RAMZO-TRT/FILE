import os,platform
os.system('git pull')
Ramzo=platform.architecture()[0]
if Ramzo=="32bit":print('32 Bit Upload Soon')
elif Ramzo=="64bit":__import__("File_Making")
