# Quantum Circuit Documentation

This document provides an explanation of the Quantum Circuit created using Qiskit. The circuit is designed to perform basic quantum operations, including quantum state preparation and a controlled-controlled-X (CCX) gate.

# Import necessary libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

## Quantum Registers and Classical Registers
# Create a quantum register with 3 qubits named 'q'
# Create a classical register with 1 classical bit named 'c'
- `QuantumRegister(3, 'q')`: Creates a quantum register named 'q' with 3 qubits.
- `ClassicalRegister(1, 'c')`: Creates a classical register named 'c' with 1 classical bit.
qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(1, 'c')

# Initialize a quantum circuit with the quantum and classical registers
- Initializes a quantum circuit with the previously created quantum and classical registers.
circuit = QuantumCircuit(qreg_q, creg_c)



## Quantum State Preparation
# Reset qubits 0, 1, and 2 to the |0⟩ state
- `circuit.reset(qreg_q[0])`: Initializes qubit 0 to the |0⟩ state.
- `circuit.reset(qreg_q[1])`: Initializes qubit 1 to the |0⟩ state.
- `circuit.reset(qreg_q[2])`: Initializes qubit 2 to the |0⟩ state.
circuit.reset(qreg_q[0])
circuit.reset(qreg_q[1])
circuit.reset(qreg_q[2])

# Apply a Hadamard gate to qubit 0, creating a superposition state
- `circuit.h(qreg_q[0])`: Applies a Hadamard gate to qubit 0, creating a superposition state.
circuit.h(qreg_q[0])

# Apply a Hadamard gate to qubit 1, creating a superposition state
- `circuit.h(qreg_q[1])`: Applies a Hadamard gate to qubit 1, creating a superposition state.
circuit.h(qreg_q[1])


## Controlled-Controlled-X (CCX) Gate
# Apply a Controlled-Controlled-X (Toffoli) gate to qubits 0, 1, and 2
This gate performs a controlled-X operation on qubit 2, controlled by qubits 0 and 1. The CCX gate flips the state of qubit 2 if and only if qubits 0 and 1 are both in the |1⟩ state.
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
 




# Import necessary libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

# Create a quantum register with 3 qubits named 'q'
qreg_q = QuantumRegister(3, 'q')

# Create a classical register with 1 classical bit named 'c'
creg_c = ClassicalRegister(1, 'c')

# Initialize a quantum circuit with the quantum and classical registers
circuit = QuantumCircuit(qreg_q, creg_c)
# Reset qubits 0, 1, and 2 to the |0⟩ state
circuit.reset(qreg_q[0])
circuit.reset(qreg_q[1])
circuit.reset(qreg_q[2])

# Apply a Hadamard gate to qubit 0, creating a superposition state
circuit.h(qreg_q[0])

# Apply a Hadamard gate to qubit 1, creating a superposition state
circuit.h(qreg_q[1])

# Apply a Controlled-Controlled-X (Toffoli) gate to qubits 0, 1, and 2
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
