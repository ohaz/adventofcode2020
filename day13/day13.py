from file_reader import get_file_entries
import numpy as np
from sympy import *
from scipy.optimize import nnls

def sub1():
    data = get_file_entries('day13/input.txt')
    starttime = int(data[0])
    bustimes = [int(x) for x in data[1].split(',') if x != 'x']
    current_time = starttime
    while True:
        for x in bustimes:
            if current_time % x == 0:
                print(x * (current_time - starttime))
                return
        current_time += 1

def sub2():
    data = get_file_entries('day13/input.txt')
    starttime = int(data[0])
    bustimes = [x for x in data[1].split(',')]
    for index in range(len(bustimes)):
        if bustimes[index].isnumeric():
            bustimes[index] = int(bustimes[index])
    equations = [x for x in bustimes if x != 'x']

    #exes = symbols(' '.join([f'x{i}' for i in range(len(equations))])+' t')
    #eqs = []
    #for index, eq in enumerate(equations):
    #    e = Eq(eq*exes[index]-exes[-1], -bustimes.index(eq))
    #    eqs.append(e)
    #print(solve(eqs, exes[:-1]))

    x = []
    t = []
    for eq_i, e in enumerate(equations):
        index = bustimes.index(e)
        t.append(-index)
        arr = [0 for x in range(eq_i)]
        arr.append(e)
        arr.extend([0 for x in range(eq_i+1, len(equations))])
        arr.append(-1)
        x.append(arr)
    sol, rnorm = nnls(np.array(x), np.array(t))
    #sol = np.linalg.lstsq(np.array(x), np.array(t), rcond=None)
    print(sol, rnorm)
