# Fractional Brownian Motion Noise Generation

This python script uses fractional brownian motion to generate noise with a 
defined Hurst Parameter.

## Prerequisites 
The only prerequisite is the Python library, fbm. To install, run:
```bash
pip3 install fbm 
```

### How to run
The script takes in 3 arguments: the number of sample points, the Hurst 
parameter, and the length of time the signal runs for. To run, use the 
following command:

```bash
python3 fbm_generation.py [num samples] [Hurst parameter] [time length]

```  

For instance, if I wanted to generate a signal with 1024 sample points, a Hurst
parameter of 0.99, and a time length of 1 second, I would run:
```bash
python3 fbm_generation.py 1024 0.99 1
```

