
"""HELLO GUYS This is a simple project that create a random password\
	Generator."""

#DOCUMENTATION:
	#first we are going to import random.
	#then we have the characters(lower, upper). we will also be using\
	#numbers  and symbols to make this random password generator

import random 

lower =  'abcdefghijklmnopqqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers ='0123456789'
symbols = '(){}[]#!$*_-|?/'

all = lower + upper + numbers + symbols
lenght = 10

password = "".join(random.sample(all,lenght))
print("your new password is :", password)
