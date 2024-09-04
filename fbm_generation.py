from fbm import FBM
import matplotlib.pyplot as plt

f = FBM(n=1024, hurst=0.75, length=1, method='daviesharte')
# or
f = FBM(1024, 0.75)

# Generate a fBm realization
fbm_sample = f.fbm()

# Generate a fGn realization
fgn_sample = f.fgn()

# Get the times associated with the fBm
t_values = f.times()

#plot the noise signal:
plt.plot(t_values[1:],fgn_sample)
plt.show()
