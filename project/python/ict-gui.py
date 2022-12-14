# NOTE: the default pyvisa import works well for Python 3.6+
# if you are working with python version lower than 3.6, use 'import visa' instead of import pyvisa as visa

# =============================================================================
# import pyvisa as visa
# import time
# # start of Untitled
# 
# rm = visa.ResourceManager()
# v33521B = rm.open_resource('USB0::0x0957::0x2B07::MY57700923::0::INSTR')
# v33521B.write(':DISPlay:TEXT "%s"' % ('testi'))
# time.sleep(5)
# v33521B.write(':DISPlay:TEXT:CLEar')
# v33521B.write(':SOURce1:FREQuency %G' % (100000.0))
# v33521B.close()
# rm.close()
# 
# =============================================================================
from tkinter import *
import pyvisa as visa
import time
rm = visa.ResourceManager()
v33521B = rm.open_resource('USB0::0x0957::0x2B07::MY57700923::0::INSTR')

def myClick():
    #v33521B.write(':DISPlay:TEXT "%s"' % ('testi'))
    v33521B.write(':SOURce1:FREQuency %G' % (int(freqInput.get())))
    

def myClick2():
    v33521B.write(':SOURce1:VOLTage:OFFSet %G' % (float(offsetInput.get())))
    #v33521B.write(':DISPlay:TEXT:CLEar')
    
    

root = Tk()

freqInput = Entry(root)
freqInput.pack()

freqButton = Button(root, text="Frequency", command=myClick)
freqButton.pack()

offsetInput = Entry(root)
offsetInput.pack()

offsetButton = Button(root, text="Offset", command=myClick2)
offsetButton.pack()

root.mainloop()
