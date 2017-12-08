#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General TMM and analysis
Copyright (C) 2017  Christian Johnson-Richards

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import numpy as np
import TMM

import matplotlib.patches as mpatches
from matplotlib import pyplot as plt
import datetime as time 


def TRplot(keyword,data,c,v):
        
    """
    This function is used to plot the results of the TMM function above. 
    Eventualy this will be generalised to plot any data.
    
    This first section produces a figure for the tunneling and reflection probability.
    """
  
    #setting up the first figure.    
    f, ax = plt.subplots(1,figsize=(10,4))
    plt.xlabel('Incident energy / MeV', fontsize=15)
    plt.ylabel('Probability', fontsize=15)
    
    #Ledgend
    Blue_Patch = mpatches.Patch( label='Tunneling Probability')
    Green_Patch = mpatches.Patch(color='green', label='Reflection Probability')
    plt.legend(handles=[Blue_Patch,Green_Patch],fontsize=8)
    
    #Plot both data sets.
    ax.plot(data.get('E_range')/(c.get('e')*1e6),data.get('TR')[:,1],color='green',linewidth=2)
    ax.plot(data.get('E_range')/(c.get('e')*1e6),data.get('TR')[:,0],linewidth=2)
    
    #Save the figure into its own directory, with a keyword and the settings it 
    #was produced with.
    filenameA =  "_" + str(keyword) + "_" + str(v.get('barrier')) + "_divs_" + str(v.get('divs')) + "_E_divs_" + str(v.get('E_divs'))
    plt.savefig("Figures/Transmission_Reflection/" + filenameA + ".eps", format='eps', dpi=600)

###############################################################################
    """
    The second figure is for producing a representation of the barrier approximation.
    """
    #Import data from the dictionary created by the TMM function.
    mid = data.get('mid')
    #This bit adds extra zero values in order to make the figure more readable. 
    mid = np.insert(mid,[0,len(mid)],[0,mid[len(mid)-1]])
    
    #Setting up and plotting the second figure.
    f, bx = plt.subplots(1,figsize=(10,4))
    plt.xlabel('Distance / fm ', fontsize=15)
    plt.ylabel('Potential Height / MeV  ', fontsize=15)
    bx.plot(mid/(1e-15),data.get('Height')/(c.get('e')*1e6),drawstyle='steps-pre')
    plt.show()
    
    #Saves the figure again with a keyword.
    filenameB =  str(keyword) + "_" + str(v.get('barrier')) + "_divs_" + str(v.get('divs'))
    plt.savefig("Figures/Barrier_width/" + filenameB + ".eps", format='eps', dpi=600)

    return 

#####################################################################################################


def converge_steps(v_r,c,a,keyword):
    divs_range = np.linspace(a.get('divs_min'),a.get('divs_max'),a.get('rpts'))
    divs_range = divs_range.astype(int)
    E = np.zeros((a.get('rpts')))   
    t = np.zeros((a.get('rpts')))   

    for i in range(0,a.get('rpts')):
        t1 = time.datetime.now()
        a["divs"] = divs_range[i]
        print(str(np.around((divs_range[i]/a.get('divs_max'))*100,1)) + "%")
        data = TMM.TMM(v_r,c,a)
        T = np.argmin(abs(data.get('TR')[:,0] - (0.5)*np.ones(len(data.get('TR')))))        
        E[i] = data.get('E_range')[T]
        
        t2 = time.datetime.now() - t1
        t[i] = t2.total_seconds() 
        
    filenameC =  str(keyword)+ "_" + str(a.get('divs_min')) + "to" + str(a.get('divs_max')) + "_rpts_" + str(a.get('rpts'))
    np.save("Data/Divs_convergence/" + filenameC, (divs_range, E,t)) 
    return 

#####################################################################################################



def converge_E(v_r,c,v,a,keyword):
    
    E_divs_range = np.linspace(a.get('divs_min'),a.get('divs_max'),a.get('rpts'))
    E_divs_range = E_divs_range.astype(int)
    E = np.zeros((a.get('rpts')))
    t = np.zeros((a.get('rpts')))   

    for i in range(0,a.get('rpts')):
        t1 = time.datetime.now()
        print(str(np.around((E_divs_range[i]/a.get('divs_max'))*100,1)) + "%")
        v["E_divs"] = E_divs_range[i]
        data = TMM(v_r,c,v)
        T = np.argmin(abs(data.get('TR')[:,0] - (0.5)))        
        E[i] = data.get('E_range')[T]
        
        t2 = time.datetime.now() - t1
        t[i] = t2.total_seconds() 
        
    filenameD =  str(keyword) + "_" + str(a.get('divs_min')) + "to" + str(a.get('divs_max')) + "_rpts_" + str(a.get('rpts'))
    np.save("Data/E_Divs_convergence/" + filenameD, (E_divs_range, E,t))    
    return 

#####################################################################################################




def steps_plot(filename,c):
    
    (divs_range,E,t) = np.load("Data/Divs_convergence/" + filename + ".npy")
    
    
    f, ax = plt.subplots(1)
    plt.xlabel('No. of Potential steps', fontsize=13)
    plt.ylabel('KE where 50% of collisions would fuse / MeV', fontsize=13)
    ax.plot(divs_range,E/(c.get('e')*1e6),'x')     
    #ax.plot(divs_range, np.polyval(p1,divs_range),color='green',linewidth=2) 
    ax.plot(divs_range, max(E)*np.ones(len(divs_range))/(c.get('e')*1e6))
    
    f, bx = plt.subplots(1)
    bx.plot(divs_range,t/60,'x')  
    plt.ylabel('time taken for simulation / minutes', fontsize=13)
    plt.xlabel('No. of Potential steps', fontsize=13)

        
    #filenameC =  str(keyword)+ "_" + str(a.get('divs_min')) + "to" + str(a.get('divs_max')) + "_rpts_" + str(a.get('rpts'))
    #plt.savefig("Figures/Potential_steps_Convergence/" + filenameC + ".eps", format='eps', dpi=600)
    return

def E_plot(filename,c): 
    
    (divs_range,E,t) = np.load("Data/E_Divs_convergence/" + filename + ".npy")
    
    #p2 = np.polyfit(divs_range,E/(c.get('e')*1e6),4,cov=False)

    f, ax = plt.subplots(1)
    plt.xlabel('Resolution of incident energies', fontsize=13)
    plt.ylabel('KE where 50% of collisions would fuse / MeV', fontsize=13)
    ax.plot(divs_range,E/(c.get('e')*1e6),'x')    
    #dx.plot(divs_range, np.polyval(p2,divs_range),color='green',linewidth=2)
    
    f, bx = plt.subplots(1)
    bx.plot(divs_range,t/60,'x')  
    plt.ylabel('time taken for simulation / seconds', fontsize=13)
    plt.xlabel('Resolution of incident energies', fontsize=13)


#    filenameD =  str(keyword) + "_" + str(a.get('divs_min')) + "to" + str(a.get('divs_max')) + "_rpts_" + str(a.get('rpts'))
#    plt.savefig("Figures/E_Res_Convergence/" + filenameD + ".eps", format='eps', dpi=600)  