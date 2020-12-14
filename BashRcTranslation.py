#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from LinColor import ColorDec

bashrc = open('/home/justjoking/.bashrc', 'r+')
Content = ''
for line in bashrc:
	Content += ColorDec(line,'1')

print(Content)
