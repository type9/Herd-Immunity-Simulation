from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation

test_virus = Virus("Ebola", 0.8, 0.5)
test_sim = Simulation(100, 0.5, test_virus)

test_sim.run()