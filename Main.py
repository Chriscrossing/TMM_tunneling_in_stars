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

import Dictionaries 
import Potential_barriers 
import TMM 
import Analysis 


class tunneling:
    
    def electropotential(keyword):
        data = TMM.TMM(Potential_barriers.elect,Dictionaries.constants,Dictionaries.elect_vars)
        Analysis.TRplot(keyword,data,Dictionaries.constants,Dictionaries.elect_vars)
        return 
    
    def square(keyword):
        data = TMM.TMM(Potential_barriers.square,Dictionaries.constants,Dictionaries.square_vars)
        Analysis.TRplot(keyword,data,Dictionaries.constants,Dictionaries.square_vars)
        return
    
    def linear(keyword): 
        data = TMM.TMM(Potential_barriers.linear,Dictionaries.constants,Dictionaries.linear_vars)
        Analysis.TRplot(keyword,data,Dictionaries.constants,Dictionaries.linear_vars)
        return  
 

class converge:
    
    def steps(keyword):
        Analysis.converge_steps(Potential_barriers.elect,Dictionaries.constants,Dictionaries.steps_vars,keyword)
        return 
    
    def E_res(keyword):
        Analysis.converge_E(Potential_barriers.elect,Dictionaries.constants,Dictionaries.E_vars,keyword)       
        return 
    
    def Both(keyword):
        return
        
#    def square():
#        return converge(square,constants,square_vars,analysis_vars)
        
    def step_plot(filename,keyword):
        Analysis.steps_plot(filename,Dictionaries.constants,keyword)
        return 
   
    def E_res_plot(filename,keyword):
        Analysis.E_plot(filename,Dictionaries.constants,keyword)
        return
    
