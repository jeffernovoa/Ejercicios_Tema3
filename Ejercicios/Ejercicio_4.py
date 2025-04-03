class Polinomio:
    def __init__(self, terminos=None):
        """
        Inicializa un polinomio con una lista de términos.
        Cada término es una tupla (coeficiente, exponente).
        """
        self.terminos = sorted((t for t in terminos if t[0] != 0), key=lambda t: t[1], reverse=True) if terminos else []

    def __str__(self):
        """
        Representación en cadena del polinomio.
        """
        if not self.terminos:
            return "0"
        return " + ".join(
            f"{coef}x^{exp}" if exp != 0 else f"{coef}" for coef, exp in self.terminos
        )

    def restar(self, otro):
        """
        Resta otro polinomio de este polinomio.
        """
        resultado = {exp: coef for coef, exp in self.terminos}
        for coef, exp in otro.terminos:
            resultado[exp] = resultado.get(exp, 0) - coef
        return Polinomio([(coef, exp) for exp, coef in resultado.items() if coef != 0])

    def dividir(self, otro):
        """
        Divide este polinomio por otro polinomio.
        Retorna el cociente y el residuo como dos polinomios.
        """
        if not otro.terminos:
            raise ValueError("No se puede dividir por un polinomio vacío.")
        
        cociente = []
        residuo = self.terminos[:]

        while residuo and residuo[0][1] >= otro.terminos[0][1]:
            coef_div = residuo[0][0] / otro.terminos[0][0]
            exp_div = residuo[0][1] - otro.terminos[0][1]
            termino_div = (coef_div, exp_div)
            cociente.append(termino_div)

            pol_div = Polinomio([termino_div])
            residuo = Polinomio(residuo).restar(pol_div.multiplicar(otro)).terminos

        return Polinomio(cociente), Polinomio(residuo)

    def eliminar_termino(self, exponente):
        """
        Elimina un término con un exponente específico del polinomio.
        """
        self.terminos = [(coef, exp) for coef, exp in self.terminos if exp != exponente]

    def existe_termino(self, exponente):
        """
        Determina si un término con un exponente específico existe en el polinomio.
        """
        return any(exp == exponente for _, exp in self.terminos)

    def multiplicar(self, otro):
        """
        Multiplica este polinomio por otro polinomio.
        """
        resultado = {}
        for coef1, exp1 in self.terminos:
            for coef2, exp2 in otro.terminos:
                exp = exp1 + exp2
                resultado[exp] = resultado.get(exp, 0) + coef1 * coef2
        return Polinomio([(coef, exp) for exp, coef in resultado.items() if coef != 0])
