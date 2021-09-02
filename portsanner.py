import socket
import optparse
import threading
from colorama import Fore, Style,init
from pyfiglet import Figlet
from termcolor import colored
f=Figlet(font="standard")
print(Fore.YELLOW,"-"*70)
print(colored(f.renderText(f'Port Scanner'), "red"))
print(Fore.YELLOW,"-"*70)
parser = optparse.OptionParser()
parser.add_option("-s","--sport",dest="sport",help="Add starting port number to scan")
parser.add_option("-e","--eport",dest="eport",help="Add endingport number to scan")
parser.add_option("-i","--host",dest="host",help="Add host")
parser.add_option("-p","--port",dest="port",help="Add single port number to scan")
(options,arguments)=parser.parse_args()
if not options.host:
    parser.error(Fore.RED+"[-] Please Enter hostname or ip address")
elif options.port:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if not (s.connect_ex((options.host,int(options.port)))):
		print(Fore.GREEN,"Port ",options.port,"is open")
	else:
		print(Fore.BLUE,"Port ",options.port,"is closed")
	s.close()
	exit()
	
if not (options.sport and options.eport):
	options.sport=0 if  not (options.sport) else options.sport
	options.eport=1024 if not (options.eport) else options.eport
if (options.sport>options.eport):
	raise ValueError(Fore.RED,"Starting port number cannot be less than ending port number")
	exit()


try:
	sport=int(options.sport)
	eport=int(options.eport)
except:
	print(Fore.RED+"[-] Please Enter the correct port number")
	exit()
if options.port:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if not (s.connect_ex((host,options.port))):
		print(Fore.GREEN,"Port ",options.port,"is open")
	s.close()
	
try:
	host=socket.gethostbyname(options.host)
except:
	print(Fore.RED,"[-] Please Enter the correct hostname or ip-address")
	exit()

def loo():
    for i in range(sport,eport):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not (s.connect_ex((host,i))):
            print("Port ",i,"is open")
        s.close()
        

threading.Thread(target=loo).start()
init(autoreset=True)	



    
