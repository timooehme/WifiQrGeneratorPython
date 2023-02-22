import qrcode as qr
import subprocess
from sys import platform
import getpass

#Function to import Wifi SSID of current Connection on MacOS
def net_mac():
    #grab the wifi Informations through subprocesses
    process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-I'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    #convert the wifi information to a dictionary for easy access
    wifi_info = {}
    for line in out.decode("utf-8").split("\n"):
        if ": " in line:
            key, val = line.split(": ")
            key = key.replace(" ", "")
            val = val.strip()
            wifi_info[key] = val
    return wifi_info

#In Future there should be the function to import Wifi SSID of current Connection on Linux
def net_lin():
    print('Linux is not supported yet for automatic ssid indentification')
    wifi_info = {'ssid' : ''}
    return wifi_info
    
#In Future there should be the function to import Wifi SSID of current Connection on Windows
def net_win(): 
    print('Windows is not supported yet for automatic ssid indentification')
    wifi_info = {'ssid' : ''}
    return wifi_info
   
#Check for OS for future use // Only MacOS supported so far
if platform == "linux" or platform == "linux2":
    wifi = net_lin()
elif platform == "darwin":
    wifi = net_mac()
elif platform == "win32":
    wifi = net_win()

#grab the SSID of connected Wifi
ssid = wifi['SSID']

#set ssid if a different connection than current should be used:
ssid = ''

#If no ssid is given or read, use console to set it
if ssid == '':
    ssid = input('Geben sie die SSID (Name) des Netzwerks ein:')
#Setting the Wifi as not hidden
hidden = 'false'
#Setting the Authentication Methode to WPA everything else to this day is unacceptable 
authentication = 'WPA'
#Setting the password for the Wifi if not there read it from console
password = ''
if password == '':
    password = getpass.getpass(f"Geben sie das Passwort für das WLAN: {ssid} ein:")
#Construction of Wifi String for QR Usage
string = f'WIFI:T:{authentication};S:{ssid};P:{password};H:{hidden};;'
#Creating the QR-Code and saving it to current directory
img = qr.make(string).get_image()
img.save(f'./Wifi_QR_Project/WIFI_QR_{ssid}.png')
