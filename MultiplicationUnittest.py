import qiskit as qk
from qiskit import QuantumCircuit, Aer, transpile
def quantum_multiply(x, y):
    # Convert input numbers to binary strings
    bin_x = format(x, 'b')
    bin_y = format(y, 'b')
    result_length = len(bin_x) + len(bin_y)
    qc = QuantumCircuit(result_length, result_length)
    x_reg = qc.register(result_length, "x")
    y_reg = qc.register(result_length, "y")
    result_reg = qc.register(result_length, "result")
    for i, bit in enumerate(bin_x[::-1]):
        if bit == '1':
            qc.x(x_reg[i])
    for i, bit in enumerate(bin_y[::-1]):
        if bit == '1':
            qc.x(y_reg[i])
    for i in range(len(bin_x)):
        for j in range(len(bin_y)):
            if bin_x[i] == '1' and bin_y[j] == '1':
                qc.cx(x_reg[i], result_reg[i + j])
    qc.measure(result_reg, result_reg)
    simulator = Aer.get_backend('qasm_simulator')
    transpiled_circuit = transpile(qc, simulator)
    result = simulator.run(transpiled_circuit).result()
    counts = result.get_counts(qc)
    decimal_result = int(list(counts.keys())[0], 2)

    return decimal_result

    result = quantum_multiply(3, 5)
    print(f"Result: {result}")
