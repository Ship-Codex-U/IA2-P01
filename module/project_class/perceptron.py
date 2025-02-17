class Perceptron:
    def __init__(self, w1, w2, b):
        self.weights = [w1, w2]
        self.bias = b

    def activation(self, net):
        return 1 if net >= 0 else 0

    def predict(self, x, y):
        net = x*self.weights[0] + y*self.weights[1] + self.bias

        return self.activation(net)
    
    def get_MB_equation_line(self):
        if self.weights[1]:
            m = -(self.weights[0] / self.weights[1])
            c = -(self.bias / self.weights[1])

            return (m,c)
        
        else:
            return None