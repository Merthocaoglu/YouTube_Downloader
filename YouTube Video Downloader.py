# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:41:37 2023

@author: MertHocaoglu
"""

from pytube import YouTube

link= input('Video link:')

yt= YouTube(link)

yr= yt.streams.get_highest_resolution()

print('Video Downloading')

yr.download('C:\YouTube')
print('Video Downloaded')
