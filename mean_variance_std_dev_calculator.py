# Mean-Variance-Standard Deviation Calculator solution for freeCodeCamp Data Analysis with Python certification

import numpy as np

def calculate(a):
    calculations = {}
    if len(a) < 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(a).reshape((3, 3))

    arr_mean_0 = list(np.mean(arr, axis=0))
    arr_mean_1 = list(np.mean(arr, axis=1))
    arr_mean_f = np.mean(arr.flatten())
    calculations["mean"] = [arr_mean_0, arr_mean_1, arr_mean_f]

    arr_var_0 = list(np.var(arr, axis=0))
    arr_var_1 = list(np.var(arr, axis=1))
    arr_var_f = np.var(arr.flatten())
    calculations["variance"] = [arr_var_0, arr_var_1, arr_var_f]

    arr_std_0 = list(np.std(arr, axis=0))
    arr_std_1 = list(np.std(arr, axis=1))
    arr_std_f = np.std(arr.flatten())
    calculations["standard deviation"] = [arr_std_0, arr_std_1, arr_std_f]

    arr_max_0 = list(np.max(arr, axis=0))
    arr_max_1 = list(np.max(arr, axis=1))
    arr_max_f = np.max(arr.flatten())
    calculations["max"] = [arr_max_0, arr_max_1, arr_max_f]

    arr_min_0 = list(np.min(arr, axis=0))
    arr_min_1 = list(np.min(arr, axis=1))
    arr_min_f = np.min(arr.flatten())
    calculations["min"] = [arr_min_0, arr_min_1, arr_min_f]

    arr_sum_0 = list(np.sum(arr, axis=0))
    arr_sum_1 = list(np.sum(arr, axis=1))
    arr_sum_f = np.sum(arr.flatten())
    calculations["sum"] = [arr_sum_0, arr_sum_1, arr_sum_f]

    return calculations
