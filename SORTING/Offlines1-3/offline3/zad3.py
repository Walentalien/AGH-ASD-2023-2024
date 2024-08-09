from zad3testy import runtests



def fenwick_update(bit, idx, value, n):
    while idx <= n:
        bit[idx] += value
        idx += idx & -idx

def fenwick_query(bit, idx):
    sum_ = 0
    while idx > 0:
        sum_ += bit[idx]
        idx -= idx & -idx
    return sum_

def dominance(P):
    n = len(P)
    
    # Sort points by x coordinate
    P.sort(key=lambda p: p[0])
    
    # Initialize Fenwick Tree (BIT) for y-coordinates
    bit = [0] * (n + 1)
    
    max_strength = 0
    # Traverse points
    for x, y in P:
        # Query the number of points with y' < y
        strength = fenwick_query(bit, y - 1)
        # Update the maximum strength
        max_strength = max(max_strength, strength)
        # Update BIT with current y-coordinate
        fenwick_update(bit, y, 1, n)
    
    return max_strength


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
