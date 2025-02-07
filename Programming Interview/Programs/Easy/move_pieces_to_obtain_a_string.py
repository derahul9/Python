import re

start = "R_L_", target = "__LR"

def canChange(start: str, target: str) -> bool:
    start = re.sub(r'_+L', 'L', start)
    start = re.sub(r'R_+', 'R', start)
    target = re.sub(r'_+L', 'L', target)
    target = re.sub(r'R_+', 'R', target)
    return start == target

print (canChange(start, target))