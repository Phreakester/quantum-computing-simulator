import random
import numpy as np
import q_op as qop

zero_vector = np.array([1,0])
one_vector = np.array([0,1])

operations = {
    'x_gate' : qop.x_gate,
    'h_gate' : qop.set_superposition,
    'measure' : qop.measure
}

class Qubit:
    """Keeps track of all data for each qubit"""
    def __init__(self, initial = 0):
        self.spin = initial
        self.alpha = None
        self.beta = None

    def set_spin(self, spin):
        """Sets qubit spin when given a spin"""
        if spin in [0,1]:
            self.spin = spin
        else:
            print(f'Cannot set spin as {spin} is not a valid spin')

    def set_superposition(self, alpha = 1/(2**0.5)):
        """Sets qubit into superposition when given an alpha value (beta is determined)"""
        self.spin = -1
        self.alpha = alpha
        self.beta = (1 - alpha**2)**0.5 #By Born Rule |alpha|^2+|beta|^2=1

    def measure_spin(self):
        """Returns qubit spin, and determines spin if in superposition, also sets self.spin to result"""
        if self.spin == -1:
            if random.random() < self.alpha**2:
                self.spin = 0
            else:
                self.spin = 1
        return self.spin

    def generate_vector(self):
        """Generates and returns qubit's vectors"""
        if self.spin == 1:
            vector = one_vector #0 vector |0>
        elif self.spin == 0:
            vector = zero_vector #1 vector |1>
        elif self.spin == -1:
            vector = np.array([self.alpha * zero_vector, self.beta * one_vector]) #|u> = a|0> + B|1>
        return vector

total_one = 0
total_zero = 0


given_operations = ['h_gate', 'measure']

qubits = {}
toutput = []
for num in range(0, 1024): #Initializes all qubit objects
    qubits[num] = Qubit()
for operation in given_operations: #Goes through each operation given
    for qubit in qubits.values():
        is_output, output = operations[operation](qubit)
        if is_output: #If output is important, it is recorded
            toutput.append(output)

for value in toutput:
    if value == 1:
        total_one += 1
    else:
        total_zero += 1

print(total_one)
print(total_zero)
print(toutput)