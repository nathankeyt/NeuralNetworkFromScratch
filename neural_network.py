import numpy as np
from layer import Layer 

class NeuralNetwork:
    def __init__(self, num_inputs: int=1, hidden_layers: list=[1], num_outputs: list=1, activation=lambda z: max(0, z)):
        # Init input to first hidden layer from a_0 -> a_1
        self.layers = [Layer(num_inputs, hidden_layers[0], activation)]
        # Init all layers from a_i-1 -> a_i
        for i in range(len(hidden_layers) - 1):
            self.layers.append(Layer(hidden_layers[i], hidden_layers[i + 1], activation))
        # Init last hidden layer to output layer from a_n-1 -> a_n
        self.layers.append(Layer(hidden_layers[-1], num_outputs, activation))
    
    def train(self, input_data: list, labels: list, epochs: int, learning_rate: float, batch_size: int):
        print("train")

    def forward_prop():
        print("forward")

    def test(self, input_data: list, labels: list):
        print("test")