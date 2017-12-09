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
import mpmath as mp




def TMM(v_r,c,v):
    E_range = np.linspace(v.get('E_min'),v.get('E_max'),v.get('E_divs'))
    TR = np.zeros(shape=(v.get('E_divs'),2))
    for j in range(0,v.get('E_divs')) :
       
        mid = np.zeros(v.get('divs'))
        Height = np.zeros(v.get('divs')+2)
            
        #The width of each potential barrier.
        width = (v.get('r_start')-v.get('r_end'))/(v.get('divs')) 
        #This for loop produces a vector of Height used in the next sections.
        for i in range(0,v.get('divs')) : 
            x_1 = v.get('r_start') - (i)*width        
            x_2 = v.get('r_start') - (i+1)*width      
            mid[i] = (x_1+x_2)/2
            Height[i+1] = v_r(mid[i],c,v)
        
        
        ###############################################################################
        """
        Next, with the same theme, an array this time for the wave-vector k. One for 
        each step plus two, one for before the potential barrier and one after.
        """
        
        
        #Set up the array
        k = np.zeros(len(Height),dtype=complex)
        
        #Will need a for loop to work out the k value for all steps.
        for i in range(0,len(Height)):
            k[i] = mp.sqrt(2*c.get('m')*(E_range[j]-Height[i]))/c.get('hbar')
        
        ###############################################################################
        """
        We now need to produce the Scattering matrix D, very similar process, except 
        this time D depends on both the current potential step and the one previous,
        this means that we have divs-1 number of value of D.
        """
        
        #Set up the matricies.
        D = np.zeros((2,2,len(Height)-1),dtype=complex)
        
        #For loop for working out D.
        for i in range(1,len(Height)):
            top1 = np.array([(1+(k[i]/k[i-1])),(1-(k[i]/k[i-1]))])
            bottom1 = np.array([(1-(k[i]/k[i-1])),(1+(k[i]/k[i-1]))])
            D[:,:,i-1] = 0.5*np.array([top1,bottom1])
        
        ###############################################################################
        """
        Almost there, we now need to sort out the Propagation matrix, again done in a 
        very similar way, this time, for the propagation matrix, we need divs -1 total 
        values minus the first P value (before the wavefunction has encountered the potential)
        """
        #Set up the values.
        P = np.zeros((2,2,len(Height)-2),dtype=complex)
        
        #Now a for loop.
        for i in range(1,len(Height)-1):
            top2 = np.array([mp.exp(-1j*k[i]*width),0])
            bottom2 = np.array([0,mp.exp(1j*k[i]*width)])
            P[:,:,i-1] = np.array([top2,bottom2])
        
        ###############################################################################
        """
        Now we combine both of the D_i and P_i matricies, producting them in 
        sequence ( D_i @ P_i ) @ D_divs-1
        """
        
        Q = np.zeros(shape=(2,2),dtype=complex)   
        Q = D[:,:,0]
        for i in range(0,len(Height)-2) :
            Q = Q @ P[:,:,i]
            Q = Q @ D[:,:,i+1]
        
        ###############################################################################
        """
        Lastly the Q[0,0] and Q[1,0] values are used to calculate the Transmission and 
        Reflection coefficients.
        """
        
        T = 1/((mp.norm(Q[0,0]))**2)
        R = ((mp.norm(Q[1,0]))**2)/((mp.norm(Q[0,0]))**2)
        
        
        TR[j] = np.array([T,R])
        
    return {'TR':TR, 'mid':mid ,'E_range':E_range, 'Height':Height, 'x_2':x_2}


#####################################################################################################


