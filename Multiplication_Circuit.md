## The Code for the Original Ciruit that runs the Multiplication Function
```python
from ibm_quantum_widgets import CircuitComposer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q0 = QuantumRegister(3, 'q0')
creg_c0 = ClassicalRegister(1, 'c0')
circuit = QuantumCircuit(qreg_q0, creg_c0)

circuit.reset(qreg_q0[0])
circuit.reset(qreg_q0[1])
circuit.reset(qreg_q0[2])
circuit.h(qreg_q0[0])
circuit.h(qreg_q0[1])
circuit.ccx(qreg_q0[0], qreg_q0[1], qreg_q0[2])
circuit.measure(qreg_q0[2], creg_c0[0])


editor = CircuitComposer(circuit=circuit)
editor
```

## The Circuit On IBM Composer


![original-circuit-2](https://github.com/ubsuny/23-Homework1G4/assets/38404107/d12fc316-2b82-4859-ab99-64e5113c176f)


## The Truth Table, Probabilities and results are included in another Markdown

  


