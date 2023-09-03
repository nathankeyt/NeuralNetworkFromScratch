import numpy as np

class Layer:
    def __init__(self, p_neuron: int=1, c_neuron: int=1, activation: function=lambda z: max(0, z)):
        print("layer")