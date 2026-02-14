def solution(ineq, eq, n, m):
    if ineq == ">" and eq == "=":
        return 1 if n >= m else 0
    if ineq == "<" and eq == "=":
        return 1 if n <= m else 0
    if ineq == ">" and eq == "!":
        return 1 if n > m else 0
    # ineq == "<" and eq == "!"
    return 1 if n < m else 0
