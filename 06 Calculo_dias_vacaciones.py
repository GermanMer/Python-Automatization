def es_fecha_valida(fecha):
    if len(fecha) != 8:
        return False
    try:
        dia = int(fecha[:2])
        mes = int(fecha[2:4])
        anio = int(fecha[4:])
        return 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= anio <= 9999
    except ValueError:
        return False


def sumar_dias(fecha, dias):
    from datetime import datetime, timedelta
    if es_fecha_valida(fecha):
        fecha_obj = datetime.strptime(fecha, "%d%m%Y")
        nueva_fecha = fecha_obj + timedelta(days=dias)
        return nueva_fecha.strftime("%d/%m/%Y")
    else:
        return None


def main():
    while True:
        fecha = input("Ingrese la fecha del primer día de vacaciones en formato DDMMAAAA (o 'salir' para terminar): ")
        if fecha.lower() == 'salir':
            break

        if not es_fecha_valida(fecha):
            print("La fecha ingresada no es válida.")
            continue

        dias = input("Ingrese la cantidad de días de vacaciones: ")
        try:
            dia = int(dias) #Para el día de reintegro al trabajo
            dias = int(dias) - 1 #Para el último día de vacaciones
            nueva_fecha = sumar_dias(fecha, dias)
            reintergro_fecha = sumar_dias(fecha, dia)
            if nueva_fecha:
                print("El último día de vacaciones es:", nueva_fecha, 'debiendo reintegrarse el', reintergro_fecha)
            else:
                print("Ha ocurrido un error al procesar la fecha.")
        except ValueError:
            print("La cantidad de días ingresada no es válida.")


if __name__ == "__main__":
    main()

