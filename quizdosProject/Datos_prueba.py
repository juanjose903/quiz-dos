#calculamos liquidacion
def calcularliquidacion(nombre, dias, salario):
    prima = salario * dias / 360
    cesantias = salario * dias / 360
    intereses_cesantias = cesantias * 0.12 / dias
    vacaciones = salario * dias / 720
    liquidacion_total = prima + cesantias + intereses_cesantias + vacaciones

    return prima, cesantias, intereses_cesantias, vacaciones, liquidacion_total

if __name__ == "__main__":
    nombre = ("Luis Vejarano")
    dias = int("7")
    salario = float("785000 ")

    prima, cesantias, intereses_cesantias, vacaciones, liquidacion_total = calcularliquidacion(nombre, dias, salario)

    print(f"Señor {nombre} para los {dias} días laborados y salario ${salario:.2f}, su liquidación se compone así:")
    print(f"Prima: ${prima:.2f}")
    print(f"Cesantía: ${cesantias:.2f}")
    print(f"Intereses cesantías: ${intereses_cesantias:.2f}")
    print(f"Vacaciones: ${vacaciones:.2f}")
    print(f"Liquidación: ${liquidacion_total:.2f}")










