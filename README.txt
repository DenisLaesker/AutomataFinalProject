#####################################
#	COT4210 - Final Project			#
#	Instructor: 					#
#	Group Members: Patricia Wilthew	#
#				   Griffin Hocker	#
#				   Denis Laesker	#
#####################################
#  NFA-DFA Conversion Instructions  #
#####################################

###############
# Input File: #
#############################################################
# A file named input.txt has been provided to serve as model
# The format is as follows:
# State,  a,      b
# q0,     qi      qi									
# q1,     qi,     qi																		  
# qn,     qi,     qi																		  
# 																							  
# States are represented with numbers 0 through 9											  
# qi can be any state from 0 to n 															  
# The final state/s must be followed by an "*"												  
# If no transition exists, an "e" must be included											  
# If a state, given some input, transitions to more 
# than one state, separate them using a "-" 
#
# Example:
# State,  a,      b
# 0,      0-1,    0
# 1,      e,      2-1
# 2*,     1,      e
############################################################

##########################
# How to run the script: #
################################################################
# 
# Python 3 must be installed
# 
# The script takes a command line argument (argv[1])
# In the Terminal, type: python NFAtoDFA.py <name of your file>
#
# 	Example: python NFAtoDFA input.txt
#
################################################################
