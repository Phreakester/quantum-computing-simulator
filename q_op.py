import numpy as np

def set_superposition(obj, alpha = 1/(2**0.5)):
    obj.set_superposition(alpha)
    return False, obj.spin

def x_gate(obj):
    x_gate = np.array([[0,1],[1,0]])
    result = np.dot(obj.generate_vector(), x_gate)
    return False, result

def h_gate(obj):
    h_gate = np.multiply(1/(2**0.5), np.array([[1,1],[1,-1]]))
    obj.spin = -1
    try:
        result = np.dot(obj.generate_vector(), h_gate)
        return False, result
    except:
        print('Qubit does not yet have alpha/beta values')

def measure(obj):
    spin = obj.measure_spin()
    return True, spin
