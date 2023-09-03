import numpy as np

class Layer:
    def __init__(self, p_neuron: int=1, c_neuron: int=1, activation = lambda z: max(0, z)):
        self.weights = np.random.rand(p_neuron, c_neuron)
        self.bias = np.random.rand(c_neuron)
        
        print("layer")
        