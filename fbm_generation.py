"""
This is a script that creates noise from fractional brownian motion using the
Davies-Harte algorithm. It takes in 3 arguments, the number of sample points, 
the Hurst parameter, and the time length of the signal.

Prerequisites:
- Note that the fbm library is needed here! To install run: pip3 install fbm

- matplotlib is also needed. To install run: pip3 install matplotlib

To run, run the command: 
python3 fbm_generation.py num_samples hurst_parameter time_length

For example, if I wanted 1024 samples, with a Hurst parameter of 0.5, and a time
length of 1s, I would run:
python3 fbm_generation.py 1024 0.5 1

This script was created from the example in: https://pypi.org/project/fbm/
"""
from fbm import FBM
import matplotlib.pyplot as plt
import sys 

def main():
    
    #Take in command line arguments for the number of points, Hurst parameter, and 
    #time length:
    num_in=int(sys.argv[1])
    hurst_par_in=float(sys.argv[2])
    length_in=float(sys.argv[3])

    f = FBM(n=num_in, hurst=hurst_par_in, length=length_in, method='daviesharte')

    # Generate a fBm realization (fractional Brownian motion)
    fbm_sample = f.fbm()

    # Generate a fGn realization (fractional Gaussian noise)
    fgn_sample = f.fgn()

    # Get the times associated with the fBm
    t_values = f.times()

    #plot the noise signal:
    plt.plot(t_values[1:],fgn_sample)
    plt.show()

main()
