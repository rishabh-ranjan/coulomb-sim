# Coulomb simulator
Simulates particles under inverse square law inter-particle forces.

Dependencies: python3, pygame  
`pip3 install pygame`

simulate.py - simulate the input as it would appear in linear flow of time.
trajectory.py - get more accurate trajectories without attempting time-based simulation.

Input can be provided through stdin or piped from an input file.
See demo/\*.in for examples of input files.
See docstring comment in input\_particles function of particle.py for input format.

Examples:
`./simulate.py < demo/sun.in`  
`./trajectory.py < demo/four.in`  
`python3 simulate.py < demo/test0.in`  
`python3 trajectory.py < demo/dual.in`

Settings can be tweaked from the config.py file or in the individual files.

