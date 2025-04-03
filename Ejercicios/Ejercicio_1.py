def hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append(f"Mueve la piedra de {source} a {target}")
        return
    hanoi(n - 1, source, auxiliary, target, moves)
    moves.append(f"Mueve la piedra de {source} a {target}")
    hanoi(n - 1, auxiliary, target, source, moves)

def resolver_hanoi(n, imprimir_todo=True):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("El número de piedras debe ser un entero positivo.")
    moves = []
    hanoi(n, 'A', 'C', 'B', moves)
    print("\n".join(moves if imprimir_todo else moves[-100:]))
