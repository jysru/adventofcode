import numpy as np

file = 'example.txt'
# file = 'puzzle.txt'

def report2array(report: str) -> np.ndarray:
    return np.array(report.rstrip().split(' ')).astype(int)

def is_safe(report: np.ndarray) -> bool:
    diff = np.diff(report)
    safe = True
    ref_sign = np.sign(diff[0]) if np.sign(diff[0]) != 0 else 1
    if np.any(np.sign(diff) != ref_sign):
        safe = False
    elif np.any(np.abs(diff) < 1):
        safe = False
    elif np.any(np.abs(diff) > 3):
        safe = False
    print(diff, safe)
    return safe
    

def is_dampened_safe(report: np.ndarray) -> bool:
    diff = np.diff(report)
    safe = True

    ref_sign = np.sign(diff[0]) if np.sign(diff[0]) != 0 else 1
    signs = np.sign(diff) != ref_sign
    down_levels = np.abs(diff) < 1
    up_levels = np.abs(diff) > 3
    sum_checks = np.logical_or(np.logical_or(signs, down_levels), up_levels)
    print(np.sum(sum_checks))
    
    if np.sum(sum_checks) > 1:
        safe = False
    print(diff, safe)
    return safe


if __name__ == '__main__':
    with open(file, 'r') as f:
        reports = f.readlines()
    
    safe_reports = 0
    for report in reports:
        safe_reports += is_dampened_safe(report2array(report))

    print(safe_reports)