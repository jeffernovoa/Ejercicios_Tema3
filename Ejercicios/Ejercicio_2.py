def determinante_recursivo(matriz):
    """
    Calcula el determinante de una matriz cuadrada usando un método recursivo.
    """
    if not matriz or any(len(fila) != len(matriz) for fila in matriz):
        raise ValueError("La matriz debe ser cuadrada y no vacía.")
    
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    if n == 2:
        # Caso base: matriz 2x2
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    determinante = 0
    for i in range(n):
        submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
        determinante += ((-1) ** i) * matriz[0][i] * determinante_recursivo(submatriz)
    return determinante


def determinante_iterativo(matriz):
    """
    Calcula el determinante de una matriz 3x3 usando un método iterativo.
    """
    if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
        raise ValueError("La matriz debe ser de 3x3.")
    
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    
    # Fórmula para el determinante de una matriz 3x3
    return (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)