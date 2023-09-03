import numpy as np
from layer import Layer 

class NeuralNetwork:
    def __init__(self, num_inputs: int=1, hidden_layers: list=[1], num_ouputs: list=1):
        np.array([1,2,3,4,5])
        Layer(2, 3)
        print("constructor")
    
    def train(self, input_data: list, labels: list, epochs: int, learning_rate: float, batch_size: int):
        print("train")

    def test(self, input_data: list, labels: list):
        print("test")