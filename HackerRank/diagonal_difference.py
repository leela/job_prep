def diagonal_difference(arr):
    """input: square matrix
    """
    noof_rows = len(arr)
    LR_diagonal_values = [arr[i][i] for i in range(noof_rows) ]
    RL_diagonal_values = [arr[i][noof_rows-i-1] for i in range(noof_rows)]
    return abs(sum(LR_diagonal_values)-sum(RL_diagonal_values))