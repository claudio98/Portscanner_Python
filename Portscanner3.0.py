# Dieser Portscaner kann lokale und öffentliche IP Adressen oder Domain Namen auf Offene Ports scannen
# Autor: Claudio Dos Santos
import os
import socket
import sys
from datetime import datetime
import time

# Clear screen (Nur im Konsolenprogramm möglich)
clear = lambda: os.system("cls")

# IP + Range Input
host = input("Gib die IP/Domain an, die gescannt werden soll > ")
hostIP = socket.gethostbyname(host)
sport = input("Von Port > ")
eport = input("Bis Port > ")
clear()

# Gibt aus das gescannt wird
print("-" * 60)
print("Bitt warte während der Host '" + hostIP + "' gescannt wird...")
print("-" * 60)


def pscann():
    # Versucht (try) die Ports der angegebenen Range zu scannen
    for port in range(int(sport), int(eport) + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect = sock.connect_ex((host, port))
            if connect == 0:
                print("[+] Port " + str(port) + " = [Offen]")
            else:
                print("[-] Port " + str(port) + " = [Geschlossen]")
                sock.close()
        except:
            print("[!] Port " + str(port) + " = [ERROR] (Es konnte keine Verbindung aufgebaut werden)")


# TODO Zeit in Stunde:Minute:Sekunde
# Überprüft die zeit vom Start des scans
z1 = datetime.now()

# Scann wird gestartet
pscann()

# Überprüft die Zeit nach dem scannen
z2 = datetime.now()

# Differenz zwischen startzeit und endzeit
ztotal = z2 - z1

# Scanninformationen
print("\nScann abgeschlossen!\n")
time.sleep(2)
print("Der Scann dauerte: " + str(ztotal))


newscan = input("\nWollen Sie einen neuen Scann durchführen? [y/n] > ")
if str(newscan) == str("y"):
    clear()
    # Startet das Programm neu (Nur in Konsole möglich)
    restart = sys.executable
    os.execl(restart, restart, * sys.argv)
else:
    print("\nDas Programm wird geschlossen...")
    time.sleep(4)
    sys.exit(0)
