import subprocess
import sys, os

"""
This file intends to import all modules needed for any tools in the Deakin Detonator Toolkit.

You can use the commented out code to import your module, changing MODULE_NAME to the name of the desired module.

Alternatively, you can call os.system('COMMAND') and replace COMMAND with the command to import.
"""
# Xterm for Payload Maker

os.system('apt-get update')                                                                                                                                                                                                                 
os.system('apt-get install python3-pip')


# PySimpleGUI
subprocess.check_call([sys.executable, "-m", "pip", "install", 'PySimpleGUI'])

# python-crontab for Cron tool
subprocess.check_call([sys.executable, "-m", "pip", "install", 'python-crontab'])

# Xterm for Payload Maker
os.system('apt-get install xterm')

# install zenity GUI
subprocess.check_call([sys.executable, "-m", "pip", "install", 'zenity'])
# subprocess.check_call([sys.executable, "-m", "pip", "install", 'MODULE_NAME'])
# os.system('COMMAND')


subprocess.check_call([sys.executable, "-m", "pip", "install", 'tkcalendar'])

subprocess.check_call([sys.executable, "-m", "pip", "install", 'pymetasploit3'])

subprocess.check_call([sys.executable, "-m", "pip", "install", 'Pillow'])

subprocess.check_call([sys.executable, "-m", "pip", "install", 'msgpack'])

subprocess.check_call([sys.executable, "-m", "pip", "install", 'ffmpeg'])

subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyglet '])