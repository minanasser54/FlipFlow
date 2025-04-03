import os
import webbrowser
import socket
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)
webbrowser.open("http://{}:8000".format(IPAddr))
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)
print("Current working directory:", os.getcwd())

os.system('cmd /k "cd FlipFlow  & cd Scripts & activate & cd.. & cd Project & python manage.py runserver {}:8000"'.format(IPAddr))
