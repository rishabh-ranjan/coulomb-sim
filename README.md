# Coulomb simulator
Simulates particles under inverse square law inter-particle forces.

Dependencies: pygame  
`pip3 install pygame`

Example run: `python3 sim.py < demo/sun.in`

or `./sim.py < demo/grid.in`

The code has been refactored. The new input files are of the form demo/n\*.in.
New testfiles work with simulate.py and trajectory.py.

simulate.py - simulate the input as it would appear in linear flow of time.
trajectory.py - get more accurate trajectories without attempting time-based simulation.

