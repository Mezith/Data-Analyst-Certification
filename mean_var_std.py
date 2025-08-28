import numpy as np

def calculate(list):
    if not len(list) == 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3, 3)
    funcs = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }

    calculations = {
        name: [func(arr, axis=0).tolist(), func(arr, axis=1).tolist(), func(arr).item()] for name, func in funcs.items()
    }

    return calculations