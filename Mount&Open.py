#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, subprocess, io, os.path

if os.geteuid() != 0:
	print("Run as Root.")
	exit()
#MOUNTDRIVES
try:
	def lineB():
		print(u'\u2500'*25)

	lsblk = subprocess.Popen(['lsblk','-i'], stdout=subprocess.PIPE)
	devs = []
	parts = []
	for line in io.TextIOWrapper(lsblk.stdout, encoding="utf-8"):
		if line.split()[0].isupper():
			continue
		elif line[0].isalnum():
			devs.append([line.split()[0],line.split()[3]])
		else:
			line = line.replace("-","")
			line = line.replace("`","")
			line = line.replace("|","")
			parts.append([line.split()[0],line.split()[3]])
	devs = sorted(devs)
	CRED = '\33[91m'
	CBLUE = '\33[94m'
	CPURP = '\33[95m'
	CEND = '\033[0m'
	lineB()
	for i in range(len(devs)):
		print((CRED+str(i+1)+CEND)+"  /dev/"+(CPURP+devs[i][0]+CEND)+":"+(" "*(9-len(devs[i][0])))+(CBLUE+devs[i][1]+CEND))
	lineB()
	drive = ""
	while drive == "":
		try:
			enterNum = int(input("\nEnter disk number: "))-1
			if enterNum < 0:
				raise Exception
			drive = devs[enterNum][0]
			print()
		except KeyboardInterrupt:
			raise KeyboardInterrupt
		except:
			print("\nType a correct disk number.")

	partitions = []
	for i in parts:
		if drive in i[0]:
			partitions.append(i)
	parts = sorted(parts)
	lineB()
	for i in range(len(partitions)):
		print((CRED+str(i+1)+CEND)+"  /dev/"+(CPURP+partitions[i][0]+CEND)+":  "+(CBLUE+partitions[i][1]+CEND))
	lineB()
	MountDev = ""
	while MountDev == "":
		try:
			enterNum = int(input("\nEnter partition number: "))-1
			if enterNum < 0:
				raise Exception
			MountDev = "/dev/"+partitions[enterNum][0]
		except KeyboardInterrupt:
			raise KeyboardInterrupt
		except:
			print("Enter a correct partition number.")
	
	if os.path.ismount('/mnt'):
		try:
			os.mkdir('/media/mount')
		except:
			pass
		defaultMount = '/media/mount'
	else:
		defaultMount = '/mnt'
	mountpoint = input("\nEnter an absolute mount point or press enter for default path["+CRED+defaultMount+CEND+"]: ")
	while mountpoint != "" and (os.path.exists(mountpoint) == False or os.listdir(mountpoint) != []):
		if os.path.exists(mountpoint) == False:
			temp = input("\nPath does not exist. Would you like to make this directory?"+"\""+CRED+mountpoint+CEND+"\" [y/n] ")
			if temp == "y" or "Y":
				os.mkdir(mountpoint)
			else:
				mountpoint = input("\nEnter an absolute mount point or press enter for default path["+CRED+defaultMount+CEND+"]: ")
		if os.listdir(mountpoint) != []:
			mountpoint = input("\nThe path has contents.\nEnter an absolute mount point or press enter for default path["+CRED+defaultMount+CEND+"]: ")
	if mountpoint == "":
		mountpoint = defaultMount
	try:
		subprocess.run(['mount',MountDev,mountpoint],text=True, check=True)
		print("\nYour device has been mounted to "+mountpoint+".")
	except subprocess.CalledProcessError:
		pass
except KeyboardInterrupt:
	print()
	pass
#OPEN PROGRAMS
LoggedInUser = os.getlogin()
Programs = ["FireFox","Pluma","Geany","Exit"]
	
def FireFox():
	subprocess.run(['su',LoggedInUser,'-c','firefox '+"&"])
def Pluma():
	subprocess.run(['su',LoggedInUser,"-c",'pluma '+"&"])
def Geany():
	subprocess.run(['su',LoggedInUser,"-c",'geany '+"&"])
def Exit():
	exit()
print()
for i in range(len(Programs)):
	print(CBLUE+str(i+1)+CEND+". "+Programs[i])

while True:
	try:
		for num in input("Enter program number(s): "):
			try:	
				eval(Programs[int(num)-1]+"()")
			except KeyboardInterrupt:
				exit()
			except IndexError:
				print("Enter a valid number.")
	except ValueError:
		quit()
