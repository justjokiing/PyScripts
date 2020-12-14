#!/usr/bin/env python3
# -*- coding: utf-8 -*-
colors = {"red":"1m","green":"2m","yellow":"3m","blue":"4m","violet":"5m","brown":"6m","grey":"0m"}

def Color(strng,color,background = 0,bright=1):
	i = ''
	global colors
	if background != 0:
		if bright != 1:
			i = '4'
		else:
			i = '10'
	else:
		if bright != 1:
			i = '3'
		else:
			i = '9'
	return "\33["+i+colors[color]+strng+"\33[0m"

colorsR = {}
for i in range(len(colors)):
	colorsR.update({list(colors.values())[i]:list(colors.keys())[i]})

def DeColor(strng, word = 0):
	end = ""
	color = ''
	h = 0
	for i in range(len(strng)):
		if i == len(strng)-1 and strng[i] != 'm':
			end += strng[i]
		elif strng[i] == "m" or '[':
			if word != 0:
				if strng[i] == 'm' and i not in [0,1]:
					end += "'"+Color(colorsR[strng[i-1:i+1]].upper(),colorsR[strng[i-1:i+1]])+"'"
				else:
					end += strng[i]
			else:
				if strng[i] == '[':
					for j in range(9):
						if strng[i+j+1] == 'm':
							color = '\33'+strng[i:i+j+2]
							end += color + strng[i:i+j+2] + '\33[0m' + strng[i+j+2]
							h = j+2
							break
				elif h != 0:
					h -= 1
				else:
					end += strng[i]
		elif strng[i+1] == "m":
			continue
		else:
			end += strng[i]
	return end

