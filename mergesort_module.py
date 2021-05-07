# mergesort module
def merge_lists(x, y, op):
    z = []
    i = 0
    j = 0
    while (i < len(x) and j < len(y)):
        if op(x[i], y[j]):
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    return z + x[i:] + y[j:]

def extract_runs(x, op):
    runs = []
    run = []
    for i in range(len(x[:-1])):
        if op(x[i], x[i+1]): run.append(x[i])
        else:
            run.append(x[i])
            runs.append(run)
            run = []
    if run:
        runs.append(run + x[-1:])
    else:
        runs.append(x[-1:])
    return runs

def merge_sort(x, op):
    runs = extract_runs(x, op)
    while len(runs) > 1:
        result = []
        for i in xrange(0, len(runs)-1, 2):
            result.append(merge_lists(runs[i], runs[i+1], op))
        if len(runs) % 2 != 0: result.append(runs[-1])
        runs = result
    return runs[0]

def is_sorted(ls, op):
    return all(op(ls[i], ls[i+1]) for i in xrange(len(ls)-1))
