import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def findones(a):
    isone = np.concatenate(([0], a, [0]))
    absdiff = np.abs(np.diff(isone))
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return np.clip(ranges, 0, len(a) - 1)

def plotbooleans(ax, dictofbool):
    ax.set_ylim([-1, len(dictofbool)])
    ax.set_yticks(np.arange(len(dictofbool.keys())))
    ax.set_yticklabels(dictofbool.keys())

    for i, (key, value) in enumerate(dictofbool.items()):
        indexes = findones(value)
        for idx in indexes:
            if idx[0] == idx[1]:
                idx[1] = idx[1]+1
            ax.hlines(y=i, xmin=idx[0], xmax=idx[1], linewidth=10, colors='r')
    return ax

testbool = {}

df = pd.read_csv('locomotion.csv')

#df = df.iloc[0:300,]


testbool['lf_contact'] = df.lf_contact
testbool['lm_contact'] = df.lm_contact
testbool['lr_contact'] = df.lr_contact
testbool['rf_contact'] = df.rf_contact
testbool['rm_contact'] = df.rm_contact
testbool['rr_contact'] = df.rr_contact

fig, ax = plt.subplots(3)
ax[0] = plotbooleans(ax[0], testbool)


testbool = {}
testbool['lf_forward'] = df.lf_forward
testbool['lm_forward'] = df.lm_forward
testbool['lr_forward'] = df.lr_forward
testbool['rf_forward'] = df.rf_forward
testbool['rm_forward'] = df.rm_forward
testbool['rr_forward'] = df.rr_forward
ax[1] = plotbooleans(ax[1], testbool)


testbool = {}

a = np.zeros(len(df.lf_contact))

for idx, n in enumerate(df.lf_contact):
	if df.lf_contact[idx] == 0 and df.lf_forward[idx] == 1:
		a[idx] = 1
	else:
		a[idx] = 0

testbool['lf_swing'] = a

a = np.zeros(len(df.lm_contact))

for idx, n in enumerate(df.lm_contact):
        if df.lm_contact[idx] == 0 and df.lm_forward[idx] == 1:
                a[idx] = 1
        else:
                a[idx] = 0

testbool['lm_swing'] = a

a = np.zeros(len(df.lr_contact))

for idx, n in enumerate(df.lr_contact):
        if df.lr_contact[idx] == 0 and df.lr_forward[idx] == 1:
                a[idx] = 1
        else:
                a[idx] = 0

testbool['lr_swing'] = a

a = np.zeros(len(df.rf_contact))

for idx, n in enumerate(df.rf_contact):
        if df.rf_contact[idx] == 0 and df.rf_forward[idx] == 1:
                a[idx] = 1
        else:
                a[idx] = 0

testbool['rf_swing'] = a

a = np.zeros(len(df.rm_contact))

for idx, n in enumerate(df.rm_contact):
        if df.rm_contact[idx] == 0 and df.rm_forward[idx] == 1:
                a[idx] = 1
        else:
                a[idx] = 0

testbool['rm_swing'] = a

a = np.zeros(len(df.rr_contact))

for idx, n in enumerate(df.rr_contact):
        if df.rr_contact[idx] == 0 and df.rr_forward[idx] == 1:
                a[idx] = 1
        else:
                a[idx] = 0

testbool['rr_swing'] = a



ax[2] = plotbooleans(ax[2], testbool)

plt.grid()
plt.subplots_adjust(bottom=0.2)
plt.show()

