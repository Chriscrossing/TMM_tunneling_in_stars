#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:49:13 2017

@author: chriscrossing
"""
from matplotlib import pyplot as plt

def plot(data):
    f, ax = plt.subplots(1,figsize=(10,3))
    #plt.ylim([-0.1,1.1])
    #plt.xlim([v.get('E_min'),v.get('E_max')])
    ax.plot(data.get('E_range'),data.get('TR'))
    
    #Height = np.insert(Height,[0,len(k)-2],[0,0])
    #x_2 = np.insert(x_2,[0,len(x_2)-2],[x_2[0],x_2[len(x_2)-3]])
    
    f, bx = plt.subplots(1,figsize=(10,3))
    #plt.xlim([v.get('r_end'),v.get('r_start')])
    bx.plot(data.get('x_2'),data.get('Height'),drawstyle='steps-pre')
    plt.show()
    return 