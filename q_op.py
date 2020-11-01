def set_superposition(obj, alpha = 1/(2**0.5)):
    obj.set_superposition(alpha)
    return False, obj.spin

def x_gate(obj):
    x_gate = np.array([[0,1],[1,0]])
    result = np.dot(obj.generate_vector(), x_gate)
    return False, result

def measure(obj):
    spin = obj.measure_spin()
    return True, spin