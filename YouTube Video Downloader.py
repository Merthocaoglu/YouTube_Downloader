# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:41:37 2023

@author: efeho
"""

from pytube import YouTube

link= input('Video link:')

yt= YouTube(link)

yr= yt.streams.get_highest_resolution()

print('Video indiriliyor')

yr.download('C:\YouTube')
print('video indirildi')
