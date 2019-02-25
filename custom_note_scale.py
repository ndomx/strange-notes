import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

N = int(sys.argv[1])

original = np.exp2(np.arange(0, 12) / 12)
custom = np.exp2(np.arange(0, N) / N)

# Plot custom scale note and original note scale
plt.figure()
plt.scatter(original, 0.4 * np.ones(np.shape(original)))
plt.scatter(custom, 0.6 * np.ones(np.shape(custom)))

plt.title('12 note scale & {0} note scale'.format(N))
plt.legend(['12 note scale', str(N) + ' note scale'])

for k in range(12):
    plt.text(original[k], 0.41, str(k+1), fontsize=8, horizontalalignment='center')

for k in range(N):
    plt.text(custom[k], 0.59, str(k+1), fontsize=8, horizontalalignment='center')

plt.show()

# Test the custom note scale
F0 = 440

Fs = 8192
Ts = 1/Fs
t = np.arange(0, 0.5, Ts) # Play the note for 0.5 seconds

for k in range(N+1):
    f = F0 * np.exp2(k/N)
    x = np.cos(2*np.pi*f*t)
    sd.play(x, Fs)

    time.sleep(1)


