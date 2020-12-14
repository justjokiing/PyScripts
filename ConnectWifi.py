#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, subprocess, os.path, io

if os.geteuid() != 0:
	print("Run as Root.")
	exit()
CRED = '\33[91m'
CBLUE = '\33[34m'
CEND = '\33[0m'
subprocess.run("ifconfig", capture_output=True)
devsO = open("/proc/net/wireless",'r')
devOut = devsO.readlines()
out = []
for line in devOut:
	if ":" in line:
		out.append(line.split(":")[0])
devsO.close()
print("-WIRELESS DEVICES-")
for i in range(len(out)):
	print(CBLUE+str(i+1)+". "+CEND+out[i])
print()
dev = ''
while dev == '':
	try:	
		dev = out[int(input("Enter a device number: "))-1]
	except:
		print("Enter a correct device number.\n")
print("\n-NETWORKS-")
iwlist = subprocess.Popen(['iwlist',dev,'scan'],stdout=subprocess.PIPE, encoding='utf-8')
networks = []
ESSID=''
address=''
for i in iwlist.stdout:
	if 'Address' in i.strip():
		address = i.strip()[10:]
	elif 'ESSID' in i.strip():
		ESSID = i.strip().replace('"','')
		networks.append([ESSID,address])
for i in range(len(networks)):
	print(CBLUE+str(i+1)+". "+CEND+networks[i][0][:6]+CRED+networks[i][0][6:]+CEND+"\n   "+networks[i][1])
network = ''
while network=='':
	try:
		network = networks[int(input("Enter network number: "))-1][0][6:]
	except:
		print("Type a correct network number.")
password = input("Carefully type your password: ")

conf = open("/etc/wpa_supplicant.conf",'w',encoding='utf-8')
confNewL = "\n        "
if network == "":
	conf.write('network={'+confNewL+'ssid="HIDDEN"'+confNewL+'scan_ssid=1'+confNewL+'psk='+password+'\n'+'}\n')
else:
	conf.write('network={'+confNewL+'ssid="'+network+'"'+confNewL+'psk="'+password+'"\n'+'}\n')
conf.close()
print("Connecting.",end='')
subprocess.run(['killall','wpa_supplicant','NetworkManager'],stderr=subprocess.DEVNULL)
print('.',end='')
subprocess.Popen(['wpa_supplicant','-B','-i',dev,'-c','/etc/wpa_supplicant.conf'],stdout=subprocess.DEVNULL)
print('.')
subprocess.run(['dhclient',dev])
ifconfig = subprocess.Popen(['ifconfig',dev],stdout=subprocess.PIPE, encoding='utf-8')
NewIp = ''
for i in ifconfig.stdout:
	if 'inet6' in i:
		continue
	elif 'inet' in i:
		NewIP = i.strip().split()[1]
print('Connected! IP: '+CRED+NewIP+CEND)
