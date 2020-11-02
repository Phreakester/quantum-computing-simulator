import random
import numpy as np
import q_op as qop

zero_vector = np.array([1,0])
one_vector = np.array([0,1])

x_gate = np.array([[0,1],[1,0]])
h_gate = np.multiply(1/(2**0.5), np.array([[1,1],[1,-1]]))

class Qubit:
    """Keeps track of all data for each qubit"""
    def __init__(self, alpha = 1): #Default Initializes qubit as |0>
        self.alpha = alpha
        self.beta = (1 - alpha**2)**0.5 #By Born Rule |alpha|^2+|beta|^2=1
        self.vector = np.array([self.alpha * zero_vector]) + np.array([self.beta * one_vector]) #|u> = a|0> + B|1>
        self.spin = None #Qubit not measured yet

    def apply_gate(self, gate):
        """Applies given gate to qubit, updates and returns self.vector"""
        self.vector = np.dot(self.vector, gate)
        self.update_from_vector()
        return self.vector

    def measure_spin(self):
        """Returns qubit spin, and determines spin if in superposition, also sets self.spin to result"""
        if random.random() < self.alpha**2:
            self.spin = 0
        else:
            self.spin = 1
        return self.spin

    def update_from_vector(self):
        """After vector is changed ex: applied gate usew this to update alpha, beta, and spin"""
        self.alpha = self.vector[0,0]
        self.beta = (1 - self.alpha**2)**0.5 #By Born Rule |alpha|^2+|beta|^2=1
        self.spin = None

total_one = 0
total_zero = 0

# given_operations = ['h_gate', 'measure']
#
# #LIMITATIONS
# #Runs operation on all qubits, cannot work with entangled / multi gates
# #Cant use if statements or other logic thingies
# qubits = {}
# toutput = []
# for num in range(0, 2048): #Initializes all qubit objects
#     qubits[num] = Qubit()
# for operation in given_operations: #Goes through each operation given
#     for qubit in qubits.values():
#         is_output, output = operations[operation](qubit)
#         if is_output: #If output is important, it is recorded
#             toutput.append(output)
#
# #Parse data given to toutput
# for value in toutput:
#     if value == 1:
#         total_one += 1
#     else:
#         total_zero += 1
#
# print(total_one)
# print(total_zero)

qubits = {}
for num in range(0,1024):
    qubits[num] = Qubit()
for qubit in qubits.values():
    qubit.apply_gate(h_gate)
    print(qubit.vector)
    qubit.measure_spin()
    # print(qubit.measure_spin())
    if qubit.spin == 1:
        total_one += 1
    else:
        total_zero += 1

print(total_one)
print(total_zero)
