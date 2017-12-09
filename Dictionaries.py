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


import scipy.constants as const

###############################################################################
#Constants
constants = {
        'hbar': const.hbar,
        'pi': const.pi,
        'e_0': const.epsilon_0,
        'e': const.e,
        'r_strong': 0.7*10**(-15),
        'm': const.proton_mass*10,
        'divs': 50,
        'E_divs': 100
        }
###############################################################################
#Variables


elect_vars = {
        'barrier': "electropotential",
        'divs': constants.get('divs'), 
        'E_divs': constants.get('E_divs'), 
        'E_min': constants.get('e')/10,
        'E_max': 3e6*constants.get('e'),                 
        'r_start': 1e-12,                           #RHS of the barrier. 
        'r_end': constants.get('r_strong')             #LHS of the barrier. 
}


steps_vars = {
        'rpts': 3,
        'divs_max': 1000,
        'divs_min': 10,
        'divs': constants.get('divs'), 
        'E_divs': constants.get('E_divs'), 
        'E_min': constants.get('e')/10,
        'E_max': 10000000*constants.get('e'),                 
        'r_start':100**(-9), #8.7e-16,                 #RHS of the barrier. 
        'r_end': constants.get('r_strong')             #LHS of the barrier. 
}

E_vars = {
        'rpts': 500,
        'divs_max': 5000,
        'divs_min': 10,
        'divs': constants.get('divs'), 
        'E_divs': constants.get('E_divs'), 
        'E_min': constants.get('e')/10,
        'E_max': 10000000*constants.get('e'),                 
        'r_start':100**(-9), #8.7e-16,                 #RHS of the barrier. 
        'r_end': constants.get('r_strong')             #LHS of the barrier. 
}

square_vars = {
        'barrier': "square",
        'divs': constants.get('divs'), 
        'E_divs': constants.get('E_divs'),  
        'E_min': constants.get('e'),
        'E_max': 100*constants.get('e'),                 
        'r_start':1e-9,
        'r_end': 0,
        'Height': 10*constants.get('e')
}

linear_vars = {
        'barrier': "linear",
        'divs': constants.get('divs'), 
        'E_divs': constants.get('E_divs'), 
        'E_min': 0,
        'E_max': 2*constants.get('e'),                 
        'r_start':constants.get('r_strong'), #8.7e-16,                 #RHS of the barrier. 
        'r_end': 0,             #LHS of the barrier. 
        'y-intercept': 2e6*constants.get('e'),
        'grad': -1    
}





elect_vars_2 = {
        'divs': constants.get('divs'), 
        'E_divs': constants.get('E_divs'), 
        'E_min': constants.get('e'),
        'E_max': 1e-14,                 
        'r_start':constants.get('r_strong') + 1e-9,    #RHS of the barrier. 
        'r_end': constants.get('r_strong')             #LHS of the barrier. 
}
###############################################################################