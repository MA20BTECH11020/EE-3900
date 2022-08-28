import soundfile as sf
import matplotlib .pyplot as plt
from scipy import signal
from scipy import vectorize as vec
import numpy as np

input_signal ,fs = sf.read('codes/Sound_Noise.wav')

sampl_freq = fs
order= 7
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/sampl_freq
b,a = signal.butter(order,Wn,'low')
r,p,k = signal.residuez(b,a)

sz = 50
sz_lin = np.arange(sz)

def rp(x):
    return r@(p**x).T

rp_vec = vec(rp,otypes = ['double'])

h1 = rp_vec(sz_lin)
k_add = np.pad(k,(0,sz-len(k)),'constant',constant_values = (0,0))
h = h1 + k_add
plt.stem(sz_lin,h)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()