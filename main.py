from neural_network import NeuralNetwork 
from layer import Layer
import numpy as np

def main():
    layer = Layer(2, 3)
    print(layer.forward(np.transpose(np.array([[2,3]]))))
    neural_network = NeuralNetwork(2, [2, 3], 2)
    print(neural_network.train(np.array([[2,3]]), [0, 1]))

if __name__=="__main__":
    main()