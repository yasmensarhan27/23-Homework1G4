```python
from ibm_quantum_widgets import CircuitComposer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(7, 'q')
creg_c0 = ClassicalRegister(1, 'c0')
circuit = QuantumCircuit(qreg_q, creg_c0)

circuit.x(qreg_q[1])
circuit.rz(pi / 2, qreg_q[3])
circuit.sx(qreg_q[3])
circuit.rz(pi / 2, qreg_q[3])
circuit.cx(qreg_q[1], qreg_q[3])
circuit.rz(-pi / 4, qreg_q[3])
circuit.cx(qreg_q[5], qreg_q[3])
circuit.rz(pi / 4, qreg_q[3])
circuit.cx(qreg_q[1], qreg_q[3])
circuit.rz(pi / 4, qreg_q[1])
circuit.rz(3 * pi / 4, qreg_q[3])
circuit.sx(qreg_q[3])
circuit.rz(-3 * pi / 2, qreg_q[3])
circuit.sx(qreg_q[5])
circuit.cx(qreg_q[3], qreg_q[5])
circuit.sx(qreg_q[3])
circuit.rz(pi / 2, qreg_q[5])
circuit.cx(qreg_q[3], qreg_q[5])
circuit.rz(-pi, qreg_q[3])
circuit.sx(qreg_q[3])
circuit.rz(-pi / 4, qreg_q[3])
circuit.cx(qreg_q[3], qreg_q[1])
circuit.rz(-pi / 4, qreg_q[1])
circuit.cx(qreg_q[3], qreg_q[1])
circuit.rz(3 * pi / 4, qreg_q[5])
circuit.sx(qreg_q[5])
circuit.rz(-pi / 2, qreg_q[5])
circuit.barrier(qreg_q[3], qreg_q[1], qreg_q[5])
circuit.measure(qreg_q[5], creg_c0[0])


editor = CircuitComposer(circuit=circuit)
editor
```




    CircuitComposer(circuit=<qiskit.circuit.quantumcircuit.QuantumCircuit object at 0x7faefa72e4a0>)




```python

```
