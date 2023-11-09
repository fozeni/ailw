import numpy as np

def threshold_activation(x):
    if x >= 0:
        return 1
    else:
        return 0

def or_perceptron(input1, input2):
    weights = np.array([1, 1])
    bias = -0.5
    weighted_sum = np.sum(np.array([input1, input2]) * weights) + bias
    return threshold_activation(weighted_sum)

def xor_perceptron(input1, input2):
    or_result = or_perceptron(input1, input2)
    and_result = and_perceptron(input1, input2)
    nand_result = and_perceptron(input1, input2)
    result = and_perceptron(or_result, nand_result)
    return result

print(xor_perceptron(False, False))  # False
print(xor_perceptron(False, True))   # True
print(xor_perceptron(True, False))   # True
print(xor_perceptron(True, True))    # False


