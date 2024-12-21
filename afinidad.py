
def calcular_afinidad(parametros, df_herramientas):
    """
    Calcula la afinidad entre los parámetros seleccionados y las herramientas disponibles.
    """
    # Pesos de los parámetros
    pesos = {
        "proposito": 50,
        "movimiento_estetico": 30,
        "plano_fotografico": 10,
        "iluminacion": 10
    }

    # Función para buscar coincidencias parciales
    def tiene_coincidencia(valor, categoria):
        return valor.lower() in categoria.lower()

    afinidades = []
    for _, row in df_herramientas.iterrows():
        puntuacion = 0

        if tiene_coincidencia(parametros["proposito"], row["Usos_Enriquecidos"]):
            puntuacion += pesos["proposito"]
        if tiene_coincidencia(parametros["movimiento_estetico"], row["Estilos_Enriquecidos"]):
            puntuacion += pesos["movimiento_estetico"]
        if tiene_coincidencia(parametros["plano_fotografico"], row["categoria"]):
            puntuacion += pesos["plano_fotografico"]
        if tiene_coincidencia(parametros["iluminacion"], row["categoria"]):
            puntuacion += pesos["iluminacion"]

        if puntuacion > 0:
            afinidades.append({
                "nombre": row["herramienta"],
                "descripcion": row["categoria"],
                "url": row["url"],
                "puntuacion": puntuacion
            })

    return sorted(afinidades, key=lambda x: x["puntuacion"], reverse=True)
