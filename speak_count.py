#!/usr/bin/env python3
'''
## License
The MIT License (MIT)
GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
#Program to Count Numbers 
# This is an example program to show how to generate speech with the Raspberry Pi.  
# You can see the full written tutorial here:  http://www.dexterindustries.com/howto/make-your-raspberry-pi-speak/
#This program makes the Pi count numbers down from the number entered by the user till zero.

from num2words import num2words
from subprocess import call

cmd_beg= 'espeak '
cmd_end= ' 2>/dev/null' # To dump the std errors to /dev/null


x = int(input("Enter a number: "))
count = num2words(x)+' Count Down Starts'
print(count)

#Replacing ' ' with '_' to identify words in the text entered
count = count.replace(' ', '_')
#Calls the Espeak TTS Engine to read aloud a Text
call([cmd_beg+count+cmd_end], shell=True)

#To do a Count Down
for i in range(x,-1,-1): # To count numbers down from the entered number till zero
	cmd=num2words(i) #To convert the Numbers to Text
	print(i)
    #Calls the Espeak TTS Engine to read aloud the Numbers
	call([cmd_beg+cmd+cmd_end], shell=True)
