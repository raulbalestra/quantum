from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt

# Simulador
simulator = Aer.get_backend('aer_simulator')

def simulate_measurement_basis_y():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.sdg(0)
    qc.h(0)
    qc.sdg(1)
    qc.h(1)
    qc.measure([0, 1], [0, 1])
    job = simulator.run(qc, shots=1024)
    return job.result().get_counts()

def simulate_measurement_basis_x():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.h(0)
    qc.h(1)
    qc.measure([0, 1], [0, 1])
    job = simulator.run(qc, shots=1024)
    return job.result().get_counts()

# Resultados
results_y = simulate_measurement_basis_y()
results_x = simulate_measurement_basis_x()

print("Y-basis measurement:")
print(results_y)
print("\nX-basis measurement:")
print(results_x)
