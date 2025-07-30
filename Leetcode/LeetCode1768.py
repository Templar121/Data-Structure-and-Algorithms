def merge(w1, w2):
    a, b = len(w1), len(w2)
    n = max(a, b)
    sol = []
    for i in range(n):
        if i < a:
            sol.append(w1[i])
        if i < b:
            sol.append(w2[i])
            
    return ("".join(sol))