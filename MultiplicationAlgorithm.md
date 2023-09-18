# Algorithm for the Multiplication using Quantum Computers:

## How the Multiplication function works on Classical Computers:
### for Classical Multiplication on Classical Computers:
let's say I'd Multiply 2*2, first this 2 in Binary will be 1 0; hence, the multiplication of 1 0 * 1 0 = 1 0 0 which equals 4.

**So for the classical multiplications on a QC:
if i have a state |0> and a state |1> multiplied it will reflect |010>
  |1> and a state |1> multiplied will return: |111>
  while |1> and |0> = |100>
  and |0> and |0> = |000>**

 ### The Algorithm For Mutliplication:
  1-Create 3 register: q0, q1 and q3 (q1 and q2 will contain the multiplier and multiplicand  while q3 will return the product)
  2- Assign the 3 registers to a Zero State
  3- Apply Hadamard gate for q0 and q1; This will let the register iterate between 0 and 1 state.
  4- leave the 3rd register q2 at zero state.
  5- Apply the Teffoli gate. The Toffoli gate is a CCX controlled-controlled-X gate, which means that it flips the state of the third qubit if the first two qubits are both in the state |1>.
The Truth Table of Teffoli or CCX gate will be as follows:

<img width="748" alt="Screen Shot 2023-09-15 at 11 32 37 PM" src="https://github.com/yasmensarhan27/23-Homework1G4/assets/38404107/495c7846-d70e-4f60-91e9-25b8a5feb4fe">


  6- The third register q3 will reflect the Multiplication of q0 and q1 as shown in the table above.
  7- The circuit will also has one classical bit, which is used to measure the state of the third qubit at the end of the circuit.


## For the unit test:
1- 3 register q0,q1 and q3
2- assign 0 state for q0,q1 and q3.
3- apply Not gate to q1 to change its state to 1 instead of 0.
4- apply Teffoli gate and a measure tool at q3 to check the result.
![original-circuit](https://github.com/yasmensarhan27/23-Homework1G4/assets/38404107/2e259c91-5875-4ea9-8b10-2ad396971c08)


** Find the truth table and implementation below: **

<img width="790" alt="Screen Shot 2023-09-15 at 11 41 54 PM" src="https://github.com/yasmensarhan27/23-Homework1G4/assets/38404107/14298cdc-1cf9-4979-a3bb-e2fa0c9bf7e8"><img width="1115" alt="Screen Shot 2023-09-15 at 11 42 48 PM" src="https://github.com/yasmensarhan27/23-Homework1G4/assets/38404107/dd668dc2-e041-450e-a7a5-8d29b53949a0">




  
