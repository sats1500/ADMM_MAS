import numpy as np
##	        bus_i   type    Pd      Qd      Gs  Bs  area	Vm  Va  baseKV	zone	Vmax	Vmin
bus=np.array([[1,    3,      1.20,   0.10,   0,  0,  1,      1,  0,  230,    1,      1.1,    0.9],
              [2,    2,      1.80,   0.8861, 0,  0,	1,      1,	0,	230,    1,	    1.1,	0.9]])

#	            bus Pg      Qg	Qmax    Qmin	Vg	mBase	status	Pmax	Pmin	Pc1	Pc2	Qc1min	Qc1max	Qc2min	Qc2max	ramp_agc	ramp_10	ramp_30	ramp_q	apf
gen =np.array([[ 1,  0.40,   0,  0.3,    -0.30,  1,  100,    1,      2.00,   0,      0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
               [ 2,	1.70,   0,  1.275,	-1.275,	1,	100,    1,      2.50,   0,      0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]])

#                fbus    tbus       r           x       b       rateA   rateB   rateC   ratio   angle   status  angmin  angmax
branch =np.array([[	1,      2,      0.00281,	0.0281, 0.00,	400,    400,    400,    0,      0,      1,      -360,   360]])

#           1   startup shutdown    n   x1  y1  ... xn  yn
#           2   startup shutdown    n   c(n - 1)    ... c0
gencost = np.array([[2,  0,  0,  3,  0.10,   10, 0],
           [2,  0,  0,  3,  0.20,   20, 0]])
