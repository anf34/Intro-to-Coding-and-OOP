import random

def sign(n):
    if n < 0:
        return -1
    return 1


class Perceptron:

    #Constructor
    def __init__(self):
        self.weight = []
        i = 0
        while i < 2:
            self.weight.append(random.uniform(-1, 1))
            i += 1
        self.bias = random.uniform(-1, 1)


    #Getter methods
    def get_weight(self):
        return self.weight

    def get_bias(self):
        return self.bias

    #Setter methods
    def set_weight(self, weight):
        self.weight = weight

    def set_bias(self, bias):
        self.bias = bias

    #Perceptron's methods
    def guess(self, input):
        output = self.bias
        i = 0
        while i < len(input):
            output += self.weight[i] * input[i]
            i += 1
        return sign(output)

    def adjust_perceptron(self):
        pass

percy = Perceptron()

print("Weights: [{:.2f}, {:.2f}] ".format(percy.get_weight()[0], percy.get_weight()[1]))
print("Bias: {:.2f}".format(percy.get_bias()))
print("Guess: {:.0f}".format(percy.guess([100, 1])))
