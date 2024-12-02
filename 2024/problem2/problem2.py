import numpy as np

file = 'example.txt'
file = 'puzzle.txt'

def report2array(report: str) -> np.ndarray:
    return np.array(list(report.rstrip().replace(' ', ''))).astype(int)

def is_safe(report: np.ndarray) -> bool:
    diff = np.diff(report)
    safe = True
    print(diff)
    if np.any(np.sign(diff) != np.sign(diff[0])):
        safe = False
    elif np.any(np.abs(diff) < 1) or np.any(np.abs(diff) > 3):
        safe = False
    return safe
    



if __name__ == '__main__':
    with open(file, 'r') as f:
        reports = f.readlines()
    
    safe_reports = 0
    for report in reports:
        safe_reports += is_safe(report2array(report))
        print(is_safe(report2array(report)))

    print(safe_reports)