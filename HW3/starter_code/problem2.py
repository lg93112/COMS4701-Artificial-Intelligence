import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from visualize import visualize_3d

alphas = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]
fig1 = plt.figure(num=1, figsize=(10,8))

def loss(beta, X, y, n):
    return (1.0/2*n) * np.sum(np.square(X.dot(beta)-y))

def plot(fig, i, loss_l, alpha, iters):
    ax = fig.add_subplot(5, 2, i+1)
    ax.plot(range(iters), loss_l, '-')
    ax.set_xlabel('iterations', fontsize=12)
    ax.set_ylabel('MSE loss', fontsize=12)
    ax.set_title('alpha %s' % str(alpha), fontsize=14)

def GD(i, alpha, iters, X, y, n, output):
    beta = np.zeros(3)
    loss_l = list()
    for ite in range(iters):
        beta = beta - alpha*(1.0/n)*np.transpose(X).dot(X.dot(beta)-y)
        loss_l.append(loss(beta, X, y, n))
    plot(fig1, i, loss_l, alpha, iters)
    output.append([alpha, iters, f"{beta[0]:0.8f}", f"{beta[1]:0.8f}", f"{beta[2]:0.8f}"])
    return beta

def main(input_f, output_f):
    # Import input1.csv, without headers for easier indexing
    raw_d = pd.read_csv('input2.csv', header=None)

    # Normalization
    for i in range(2):
        raw_d[i] = (raw_d[i] - np.mean(raw_d[i]))/np.std(raw_d[i])

    X = np.insert(raw_d.as_matrix(columns=raw_d.columns[0:2]), 0, 1, axis = 1)
    y = raw_d.as_matrix(columns=raw_d.columns[2:]).flatten()
    n = len(X)

    output = []

    for i, alpha in enumerate(alphas):
        GD(i, alpha, 100, X, y, n, output)

    beta_o = GD(9, 0.6, 80, X, y, n, output)
    pd.DataFrame(output).to_csv('output2.csv', header=False, index=False)

    plt.tight_layout()
    plt.show()

    visualize_3d(raw_d, lin_reg_weights=beta_o, alpha=0.6)

if __name__ == '__main__':
    input_f = sys.argv[1]
    output_f = sys.argv[2]
    main(input_f, output_f)
