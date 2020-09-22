# Developed for converting binary code to the sinusoidal signal.

import matplotlib.pyplot as plt
import numpy as np
import math

# The software will continue to ask for inputs
# until they are given in true format.
ask_again= True

while ask_again:

    checkBC = True

    # taking the line code as an input
    # it should be given as polar or on-off
    LC = input("Line Code = ")
    LC = LC.replace(" ","").lower()
    LC = LC[0]

    # taking the "Rb" value as an input
    # the input should be an integer
    # and shouldn't have any non-numeric character
    Rb = input("Bit Rate = ")
    Rb = Rb.strip()

    # taking the binary code as an input
    # the input shouldn't have any non-numeric character
    BC = input("Binary Code = ")
    BC = BC.replace(" ","")

    # checking the binary code
    for i in BC:
        if i != "0" and i != "1":
            checkBC=False

    # checking the inputs
    if (LC == "p" or LC == "o") and Rb.isdecimal() and checkBC:
        ask_again=False

# calculating the "Tb"
Tb = 1 / int(Rb)

# creating a figure for plotting
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

signal = []
time = []

# taking each bit from binary code
for count,bit in enumerate(BC):

    # ranging the x-axis regarding to the Tb value
    for t in  np.arange(Tb*count, Tb*(count+1), 0.00001).tolist():

        time.append(t)

        if bit == "1":
            signal_point = 10 * np.cos(1000* math.pi * t)
            signal.append(signal_point)

        # for the polar signaling
        elif bit =="0" and LC == "p":
            signal_point = -10 * np.cos(1000 * math.pi * t)
            signal.append(signal_point)

        # for the on-off signaling
        elif bit =="0" and LC == "o":
            signal.append(0)

    # plotting signal with red color
    ax1.plot(time, signal,c="crimson")

Text_Tb = "Tb = " + str(Tb)

# to locate the text box on the upper side of the graph
upper = 9.6
# to locate the text box at the right side of the graph
right_side = Tb*len(BC)*0.82

ax1.text(right_side, upper, Text_Tb , style='italic',
         bbox={'facecolor': 'green', 'alpha': 0.8, 'pad': 6})
ax1.set(xlabel="t")
plt.show()

