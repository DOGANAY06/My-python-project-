# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:42:36 2019

@author: Doğan AY
"""

from pytube import YouTube
YouTube("https://youtu.be/xl_DxXhyaac").streams.first().download()
