class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __repr__(self):
        return (f"NaveEspacial(nombre='{self.nombre}', longitud={self.longitud}, "
                f"tripulantes={self.tripulantes}, pasajeros={self.pasajeros})")

def ordenar_naves_por_nombre_y_longitud(naves):
    return sorted(naves, key=lambda nave: (nave.nombre, -nave.longitud))

def obtener_info_naves_por_nombre(naves, nombres):
    nombres_set = set(nombres)
    return [nave for nave in naves if nave.nombre in nombres_set]

def obtener_cinco_mayores_pasajeros(naves):
    return sorted(naves, key=lambda nave: nave.pasajeros, reverse=True)[:5]

def obtener_nave_mayor_tripulacion(naves):
    if not naves:
        raise ValueError("La lista de naves está vacía.")
    return max(naves, key=lambda nave: nave.tripulantes)

def obtener_naves_con_nombre_gx(naves):
    return [nave for nave in naves if nave.nombre.startswith("GX")]

def obtener_naves_con_seis_o_mas_pasajeros(naves):
    if not naves:
        raise ValueError("La lista de naves está vacía.")
    naves_con_seis_o_mas_pasajeros = [nave for nave in naves if nave.pasajeros >= 6]
    if not naves_con_seis_o_mas_pasajeros:
        return [], None, None
    return (
        naves_con_seis_o_mas_pasajeros,
        min(naves_con_seis_o_mas_pasajeros, key=lambda nave: nave.longitud),
        max(naves_con_seis_o_mas_pasajeros, key=lambda nave: nave.longitud),
    )