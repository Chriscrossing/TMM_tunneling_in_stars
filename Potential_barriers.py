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


def elect(r,c,v) :
    return (c.get('e')**2)/(4*c.get('pi')*c.get('e_0')*r)


def linear(r,c,v) :
    return linear_vars.get('grad')*r + linear_vars.get('y-intercept')

def square(r,c,v):
    return v.get('Height')