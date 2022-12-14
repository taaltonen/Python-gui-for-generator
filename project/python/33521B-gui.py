import tkinter as tk
import pyvisa as visa

rm = visa.ResourceManager()
v33521B = rm.open_resource('USB0::0x0957::0x2B07::MY57700923::0::INSTR')
root = tk.Tk()

selectedWaveform = ""

# Initialize all used labels and input fields
freqInput = tk.Entry()
amplitudeInput = tk.Entry()
offsetInput = tk.Entry()
DCycleInput = tk.Entry()
symmetryInput = tk.Entry()
phaseInput = tk.Entry()
transLeadingInput = tk.Entry()
transTrailingInput = tk.Entry()
sampleRateInput = tk.Entry()
bandwidthInput = tk.Entry()
bitrateInput = tk.Entry()
edgetimeInput = tk.Entry()

freqLabel = tk.Label(text="Frequency (1μHz - 30MHz)")
amplitudeLabel = tk.Label(text="Amplitude (1μVpp - 10Vpp)")
offsetLabel = tk.Label(text="Offset (-5V - 5V)")
DCycleLabel = tk.Label(text="Duty cycle (0% - 100%)")
symmetryLabel = tk.Label(text="Symmetry (0% - 100%)")
phaseLabel = tk.Label(text="Phase (-360° - 360°)")
transLeadingLabel = tk.Label(text="Transition leading (8.4ns - 1μs)")
transTrailingLabel = tk.Label(text="Transition trailing (8.4ns - 1μs)")
sampleRateLabel = tk.Label(text="Sample rate (1 μsa/s - 250 Msa/s)")
bandwidthLabel = tk.Label(text="Bandwidth (1mHz - 30MHz)")
bitrateLabel = tk.Label(text="Bit rate (1mbps - 50Mbps)")
edgetimeLabel = tk.Label(text="Edge time (8.4ns - 1μs)")
transInstructionLabel = tk.Label(text="(Enter transision times in nanoseconds)")
edgetimeInstructionLabel = tk.Label(text="(Enter edge time in nanoseconds)")

# Initialize dropdown for Arb name selection
optionsArb = [
    "CARDIAC.arb",
    "D_LORENTZ.arb",
    "EXP_FALL.arb",
    "EXP_RISE.arb",
    "GAUSSIAN.arb",
    "HAVERSINE.arb",
    "LORENTZ.arb",
    "NEG_RAMP.arb",
    "SINC.arb"
]
clickedArb = tk.StringVar()
clickedArb.set( "EXP_RISE.arb" )
dropArb = tk.OptionMenu( root , clickedArb , *optionsArb )

# Initialize dropdown for PRBS Data selection
optionsPrbs = [
    "PN7",
    "PN9",
    "PN11",
    "PN15",
    "PN20",
    "PN23"
]
clickedPrbs = tk.StringVar()
clickedPrbs.set( "PN7" )
dropPrbs = tk.OptionMenu( root , clickedPrbs , *optionsPrbs )

def commonInputs():
    freqLabel.pack(padx=10)
    freqInput.pack()
    amplitudeLabel.pack()
    amplitudeInput.pack()
    offsetLabel.pack()
    offsetInput.pack()
    phaseLabel.pack()
    phaseInput.pack()

def clearWidgets():
    freqLabel.forget()
    freqInput.forget()
    amplitudeLabel.forget()
    amplitudeInput.forget()
    offsetLabel.forget()
    offsetInput.forget()
    DCycleLabel.forget()
    DCycleInput.forget()
    phaseLabel.forget()
    phaseInput.forget()
    transLeadingLabel.forget()
    transLeadingInput.forget()
    transTrailingLabel.forget()
    transTrailingInput.forget()
    transInstructionLabel.forget()
    symmetryLabel.forget()
    symmetryInput.forget()
    sampleRateLabel.forget()
    sampleRateInput.forget()
    bandwidthLabel.forget()
    bandwidthInput.forget()
    bitrateLabel.forget()
    bitrateInput.forget()
    edgetimeLabel.forget()
    edgetimeInput.forget()
    edgetimeInstructionLabel.forget()
    dropArb.forget()
    dropPrbs.forget()

def printInputFields(waveform):
    global selectedWaveform
    selectedWaveform = waveform
    
    clearWidgets()
    
    if waveform == "Sine":
        # Print common input fields
        commonInputs()
        
    elif waveform == "Square":
        commonInputs()
         
        # Print waveform specific input fields
        DCycleLabel.pack()
        DCycleInput.pack()
        
    elif waveform == "Ramp":
        commonInputs()
         
        symmetryLabel.pack()
        symmetryInput.pack()

    elif waveform == "Pulse":
        commonInputs()
         
        DCycleLabel.pack()
        DCycleInput.pack()
        transLeadingLabel.pack()
        transLeadingInput.pack()
        transTrailingLabel.pack()
        transTrailingInput.pack()
        transInstructionLabel.pack(padx=5)
        
    elif waveform == "Arb":
        sampleRateLabel.pack(padx=10)
        sampleRateInput.pack()
        amplitudeLabel.pack()
        amplitudeInput.pack()
        offsetLabel.pack()
        offsetInput.pack()
        dropArb.pack()
    
    elif waveform == "Triangle":
        commonInputs()
        
    elif waveform == "Noise":
        bandwidthLabel.pack(padx=10)
        bandwidthInput.pack()
        amplitudeLabel.pack()
        amplitudeInput.pack()
        offsetLabel.pack()
        offsetInput.pack()
        
    elif waveform == "PRBS":
        bitrateLabel.pack()
        bitrateInput.pack()
        amplitudeLabel.pack()
        amplitudeInput.pack()
        offsetLabel.pack()
        offsetInput.pack()
        edgetimeLabel.pack()
        edgetimeInput.pack()
        edgetimeInstructionLabel.pack(padx=5)
        dropPrbs.pack()

    elif waveform == "DC":
        offsetLabel.pack()
        offsetInput.pack(padx=10)

def applySettings():
    if selectedWaveform == "Sine":
        v33521B.write(':SOURce:APPLy:SINusoid %G,%G,%G' % (float(freqInput.get()), float(amplitudeInput.get()), float(offsetInput.get())))
        v33521B.write(':SOURce:PHASe:ADJust %G' %  float(phaseInput.get()))
    elif selectedWaveform == "Square":
        v33521B.write(':SOURce:APPLy:SQUare %G,%G,%G' % (float(freqInput.get()),  float(amplitudeInput.get()), float(offsetInput.get())))
        v33521B.write(':SOURce:FUNCtion:SQUare:DCYCle %G' % float(DCycleInput.get()))
    elif selectedWaveform == "Ramp":
        v33521B.write(':SOURce:APPLy:RAMP %G,%G,%G' % (float(freqInput.get()), float(amplitudeInput.get()), float(offsetInput.get())))
        v33521B.write(':SOURce:PHASe:ADJust %G' %  float(phaseInput.get()))
        v33521B.write(':SOURce:FUNCtion:RAMP:SYMMetry %G' % float(symmetryInput.get()))
    elif selectedWaveform == "Pulse":
        v33521B.write(':SOURce:APPLy:PULSe %G,%G,%G' % (float(freqInput.get()),  float(amplitudeInput.get()), float(offsetInput.get())))
        v33521B.write(':SOURce:FUNCtion:PULSe:DCYCle %G' % float(DCycleInput.get()))
        v33521B.write(':SOURce:PHASe:ADJust %G' %  float(phaseInput.get()))
        v33521B.write(':SOURce:FUNCtion:PULSe:TRANsition:LEADing %G' % (float(transLeadingInput.get()) * 0.000000001))
        v33521B.write(':SOURce:FUNCtion:PULSe:TRANsition:TRAiling %G' % (float(transTrailingInput.get()) * 0.000000001))
    elif selectedWaveform == "Arb":
        v33521B.write(':SOURce:DATA:VOLatile:CLEar')
        v33521B.write(':MMEMory:LOAD:DATA "%s"' % ('Int:\\Builtin\\' + clickedArb.get()))
        v33521B.write(':SOURce:FUNCtion:ARBitrary "%s"' % ('Int:\\Builtin\\' + clickedArb.get()))
        v33521B.write(':SOURce:APPLy:ARBitrary %G,%G,%G' % (float(sampleRateInput.get()), float(amplitudeInput.get()), float(offsetInput.get())))
    elif selectedWaveform == "Triangle":
        v33521B.write(':SOURce:APPLy:TRIangle %G,%G,%G' % (float(freqInput.get()), float(amplitudeInput.get()), float(offsetInput.get())))
        v33521B.write(':SOURce:PHASe:ADJust %G' %  float(phaseInput.get()))
    elif selectedWaveform == "Noise":
        v33521B.write(':SOURce:APPLy:NOISe %G,%G,%G' % (float(bandwidthInput.get()), float(amplitudeInput.get()), float(offsetInput.get())))
        v33521B.write(':SOURce:FUNCtion:NOISe:BANDwidth %G' % float(bandwidthInput.get()))
    elif selectedWaveform == "PRBS":
        v33521B.write(':SOURce:FUNCtion:PRBS:DATA %s' % (clickedPrbs.get()))
        v33521B.write(':SOURce:APPLy:PRBS %G,%G,%G' % (float(bitrateInput.get()), float(amplitudeInput.get()), float(offsetInput.get())))
        v33521B.write(':SOURce:FUNCtion:PRBS:TRANsition:BOTH %G' % (float(edgetimeInput.get()) * 0.000000001))
    elif selectedWaveform == "DC":
        v33521B.write(':SOURce:APPLy:DC %G,%G,%G' % (float(offsetInput.get()), float(offsetInput.get()), float(offsetInput.get())))

selectWaveformLabel = tk.Label(text="Select waveform")
selectWaveformLabel.pack()

buttonFrame1 = tk.Frame(root)
buttonFrame1.pack()
buttonFrame2 = tk.Frame(root)
buttonFrame2.pack()
buttonFrame3 = tk.Frame(root)
buttonFrame3.pack()

# Buttons for selecting the waveform in use
sineButton = tk.Button(buttonFrame1, text="Sine", command=lambda : printInputFields("Sine"))
sineButton.pack( side=tk.LEFT, padx=(5,0))
squareButton = tk.Button(buttonFrame1, text="Square", command=lambda : printInputFields("Square"))
squareButton.pack( side=tk.LEFT, padx=2, pady=2)
rampButton = tk.Button(buttonFrame1, text="Ramp", command=lambda : printInputFields("Ramp"))
rampButton.pack( side=tk.LEFT, padx=(0,5))
pulseButton = tk.Button(buttonFrame2, text="Pulse", command=lambda : printInputFields("Pulse"))
pulseButton.pack( side=tk.LEFT, padx=(5,0))
arbButton = tk.Button(buttonFrame2, text="Arb", command=lambda : printInputFields("Arb"))
arbButton.pack( side=tk.LEFT, padx=2, pady=2)
trangleButton = tk.Button(buttonFrame2, text="Triangle", command=lambda : printInputFields("Triangle"))
trangleButton.pack( side=tk.LEFT, padx=(0,5))
noiseButton = tk.Button(buttonFrame3, text="Noise", command=lambda : printInputFields("Noise"))
noiseButton.pack( side=tk.LEFT, padx=(5,0))
arbButton = tk.Button(buttonFrame3, text="PRBS", command=lambda : printInputFields("PRBS"))
arbButton.pack( side=tk.LEFT, padx=2, pady=2)
dcButton = tk.Button(buttonFrame3, text="DC", command=lambda : printInputFields("DC"))
dcButton.pack( side=tk.LEFT, padx=(0,5))

applyButton = tk.Button(root, text="Apply setting", command=applySettings)
applyButton.pack( side=tk.BOTTOM, pady=5 )


root.mainloop()
