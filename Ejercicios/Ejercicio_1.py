def hanoi(n, source, target, auxiliary):
    """
    Resuelve el problema de la Torre de Hanói.

    :param n: Número de piedras a mover.
    :param source: Nombre de la columna origen.
    :param target: Nombre de la columna destino.
    :param auxiliary: Nombre de la columna auxiliar.
    """
    if n == 1:
        print(f"Mueve la piedra de {source} a {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Mueve la piedra de {source} a {target}")
    hanoi(n - 1, auxiliary, target, source)