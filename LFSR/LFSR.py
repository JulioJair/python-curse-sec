from pylfsr import LFSR

# Initial state of LFSR.
state = 'random'

# Feedback polynomial, it has to be primitive polynomial
fpoly = [4, 1]

L = LFSR(fpoly=fpoly, initstate=state, verbose=True)

# check if -degree of feedback polynomial <= length of LFSR >=1 -given intistate of LFSR is correct
L.check()

# display the information about LFSR with current state of variables
L.info()

# run full cycle ( = 2^M-1)
# L.runFullCycle()
