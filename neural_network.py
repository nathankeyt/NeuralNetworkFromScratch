import numpy as np
from layer import Layer 

class NeuralNetwork:
    def __init__(self, num_inputs: int=1, hidden_layers: list=[1], num_outputs: list=1, activation=np.vectorize(lambda z: max(0, z))):
        self.head = Layer(num_inputs, hidden_layers[0], activation=activation) # First Hidden Layer, NOT Imput Layer
        prev = self.head
        for num in hidden_layers + [num_outputs]:
            temp = Layer(prev.size, num, prev, activation)
            prev.next = temp
            prev = temp


        # Init input to first hidden layer from a_0 -> a_1
        #self.layers = [Layer(num_inputs, hidden_layers[0], activation)]
        # Init all layers from a_i-1 -> a_i
        #for i in range(len(hidden_layers) - 1):
        #    self.layers.append(Layer(hidden_layers[i], hidden_layers[i + 1], activation))
        # Init last hidden layer to output layer from a_n-1 -> a_n
        #self.layers.append(Layer(hidden_layers[-1], num_outputs, activation))
    
    def train(self, input, labels: list, epochs: int=10, learning_rate: float=0.1, batch_size: int=3):
        return self.forward_prop(np.transpose(input))
        print("train")

    def forward_prop(self, input: list):
        prevLayer = self.head
        prevLayer.forward(input)
        while (prevLayer.next != None):
            currLayer = prevLayer.next
            currLayer.forward(prevLayer.a)
            prevLayer = currLayer
        return prevLayer.a
            
            

    def test(self, input_data: list, labels: list):
        print("test")