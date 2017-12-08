# TMM_tunneling_in_stars

Newcastle University Physics stage 3 group project.

Utilising the transfer matrix method to approximate proton energy in stellar fusion.

# Requirements

Use spyder3 installed with all of its requirements (instructions https://pythonhosted.org/spyder/installation.html)
or 
Python3 and the packages:
scipy
numpy
mpmath
matplotlib
datetime (however will be replacing with timeit at some point)

# How to
Currently this is a very basic program built specifically for our group project, the 'main' script is a library of functions that currently;

Within the 'Tunneling' class, produce transmission and reflection graphs based upon the initial condions saved in the Dictionary file. You can easily add different potential barriers by adding the equation to the 'Potential_barriers' file as a function, and in turn add another function to the 'Tunneling' class for that potential. (this is cumbersome at the moment)

Within the 'Converge' class, this is used to decide upon the accuracy neccacary for reliable results, it produces data for increasing numbers of potential steps ('steps' function) and increasing number of incident energies ('E_res'), this outputs the probabilities for 50% transmission, the no. of steps/incident energies, and the time for each iteration to a file in the Data directory given the input string name.

There are also a couple of plotting functions within the 'converge' class, these read from the files saved, and plot corrispoiding graphs, you have to pass the name of the data file as a string for these at the minute.

# Licence 

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
