import numpy as np

class Layer:
    def __init__(self, p_neuron: int=1, c_neuron: int=1, p_layer: object=None, activation=np.vectorize(lambda z: max(0, z))):
        self.weight = np.random.rand(c_neuron, p_neuron)
        self.bias = np.random.rand(c_neuron, 1)
        self.size = c_neuron
        self.activation = activation
        self.z = np.array([])
        self.a = np.array([])
        self.next = None
        self.prev = p_layer
        print(self.weight)

    
    def forward(self, input):
        print(input)
        self.z = self.weight.dot(input) + self.bias
        self.a = self.activation(self.z)
        return self.a
        
    