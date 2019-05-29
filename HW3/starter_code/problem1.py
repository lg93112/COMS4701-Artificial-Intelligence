import numpy as np
import sys
import pandas as pd
from visualize import visualize_scatter

def perceptron(weights, x):
    if np.dot(weights, x[:-1]) > 0:
        return 1
    else:
        return -1

def main(input_f, output_f):
    # Import input1.csv, without headers for easier indexing
    raw_d = pd.read_csv(input_f, header=None)
    data = np.insert(raw_d.as_matrix(), 2, 1, axis = 1)
    weights = np.array([0, 0, 0])
    output_w = []

    while 1:
        error = False
        output_w.append(weights)
        for x in data:
            if x[-1]*perceptron(weights,x) <= 0:
                weights = weights + x[-1]*x[:-1]
                error = True
        if not error:
            break

    output_w = np.matrix(output_w)
    pd.DataFrame(output_w).to_csv(output_f, header=False, index=False)
    visualize_scatter(raw_d, weights=[float(w) for w in weights])

if __name__ == '__main__':
    input_f = sys.argv[1]
    output_f = sys.argv[2]
    main(input_f, output_f)

