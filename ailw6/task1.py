import numpy as np

def and_neuron(input1, input2):
    weights = np.array([1, 1])
    threshold = 1.5

    weighted_sum = np.sum(np.array([input1, input2]) * weights)

    if weighted_sum > threshold:
        return True
    else:
        return False

input1 = bool(input("1 значение \n"))
input2 = bool(input("2 значение \n"))
print(and_neuron(input1, input2))
