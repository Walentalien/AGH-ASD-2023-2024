from zad3testy import runtests


#O(n^2)
def dominance1(P):
    n = len(P)
    max_strength = 0

    for i in range(n):
        x_i, y_i = P[i]
        current_strength = 0
        
        for j in range(n):
            if i != j:
                x_j, y_j = P[j]
                if x_i > x_j and y_i > y_j:
                    current_strength += 1
        
        max_strength = max(max_strength, current_strength)

    return max_strength


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
