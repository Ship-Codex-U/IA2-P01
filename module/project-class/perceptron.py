class Perceptron:
    def __init__(self, w1, w2, b):
        self.weights = [w1, w2]
        self.bias = b

    def activation(self, net):
        return 1 if net >= 0 else 0

    def train(self):
        ANDInputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
        ANDResults = [0, 0, 0, 1]

        expectedResults = [0, 0, 0, 0]
        errors = [-1, -1, -1, -1]

        cont = 0

        while not arrays_equal(errors, expectedResults):
            for i in range(4):
                y = 0

                net = ANDInputs[i][0]*self.weights[0] + ANDInputs[i][1]*self.weights[1] + self.bias

                print(f"Net: {net}")

                y = self.activation(net)
                
                print(f"y: {y}")

                errors[i] = ANDResults[i] - y

                print(f"Error: {errors[i]}")


                if(errors[i] != 0):
                    self.weights[0] = self.weights[0] + errors[i]*ANDInputs[i][0]
                    self.weights[1] = self.weights[1] + errors[i]*ANDInputs[i][1]
                    self.bias = self.bias + errors[i]

                    print(f"New weights: {self.weights}, new bias: {self.bias}")
            
            cont += 1

            print(f"Epoch {cont}")
            print("------------------------------")
            print(f"Errors = {errors}")
            print(f"Array equal: {arrays_equal(errors, expectedResults)}")
            print("------------------------------")

            input("End cicle while...")
        
        print(f"weights: {self.weights}")
        print(f"bias: {self.bias}")
        print(f"errors: {errors}")
        print(f"cont: {cont}")

            
        
        if arrays_equal(errors, expectedResults):
            print("Training finished successfully")
        else:
            print("Training finished unsuccessfully")
        
        print("------------------------------")
        print(f"Weights: {self.weights}")
        print(f"Bias: {self.bias}")
        print(f"Iterations: {cont}")
        print("------------------------------\n\n")

    def predict(self, x, y):
        net = x*self.weights[0] + y*self.weights[1] + self.bias

        return 1 if net >= 0 else 0
      
def arrays_equal(arr1, arr2):
    print(f"arr1 - Errors: {arr1}, arr2 - ExpectedResults: {arr2}")
    print(f"len(arr1): {len(arr1)}, len(arr2): {len(arr2)}")
    if len(arr1) != len(arr2):
        print("Arrays are not equal in length")
        return False
    
    for a, b in zip(arr1, arr2):
        print(f"a: {a}, b: {b}")
        if a != b:
            print("Arrays are not equal in values")
            return False
            
        
    return True

# Diseña un menu pinteractivo para el usuario con las siguientes opciones:
# 1. Entrenar el perceptrón AND
# 2. Probar el perceptrón AND
# 3. Salir

def menu():
    option = ""

    while option != "3":

        print("Perceptrón AND")
        print("1. Entrenar el perceptrón AND")
        print("2. Probar el perceptrón AND")
        print("3. Salir")
        print("------------------------------")
        
        option = input("Seleccione una opción: ")
        
        if option == "1":
            w1 = int(input("Ingrese el valor de w1: "))
            w2 = int(input("Ingrese el valor de w2: "))
            b = int(input("Ingrese el valor de b: "))
            epochs = int(input("Ingrese el número de épocas: "))

            perceptron = PerceptronAND(w1, w2, b, epochs)
            perceptron.train()

        elif option == "2":
            x = int(input("Ingrese el valor de x: "))
            y = int(input("Ingrese el valor de y: "))
            perceptron.predict(x, y)
            print(f"Predicción: {perceptron.predict(x, y)}")

        elif option == "3":
            print("Hasta luego")
        else:
            print("Opción no válida")


menu()
