import random
import math


def sigmoid(x):
    return 1/(math.exp(-x)+1)


class NodeGene:
    def __init__(self, activation_function, input_nodes, input_connections, id):
        self.activation_function = activation_function
        self.input_nodes = input_nodes
        self.input_connections = input_connections
        self.input_connected = False
        for i in self.input_connections:
            if not i.disabled:
                self.input_connected = True
                break

        self.id = id

    def calculate(self):
        if not self.input_connected:
            return 0

        total = 0
        for i, c in zip(self.input_nodes, self.input_connections):
            if not c.disabled:
                total += i.calculate() * c.weight

        return self.activation_function(total)

    def add_node(self, node):
        pass



class NeuralNetwork:
    pass