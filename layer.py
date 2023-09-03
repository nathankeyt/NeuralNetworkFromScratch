import numpy as np

class Layer:
    def __init__(self, p_neuron: int=1, c_neuron: int=1, p_layer: object=None, activation = lambda z: max(0, z)):
        self.weight = np.random.rand(p_neuron, c_neuron)
        self.bias = np.random.rand(c_neuron)
        self.size = c_neuron
        self.activation = activation
        self.z = np.array()
        self.a = np.array()
        self.next = None
        self.prev = p_layer

    
    def forward(self, input):
        self.z = self.weights.dot(input) + self.biases
        self.a = self.activation(self.z)
        return self.a
        
    