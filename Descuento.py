def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento basado en el monto total y el porcentaje de descuento.

    Parámetros:
    - monto_total: El monto total de la compra.
    - porcentaje_descuento: El porcentaje de descuento a aplicar (predeterminado es 10).

    Retorna:
    - El monto final a pagar después de aplicar el descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return monto_final


def main():
    # Solicitar el monto total de la compra al usuario
    try:
        monto_total = float(input("Ingrese el monto total de la compra: "))
        # Solicitar el porcentaje de descuento (opcional)
        porcentaje_descuento = input("Ingrese el porcentaje de descuento (presione Enter para 10%): ")

        if porcentaje_descuento:
            porcentaje_descuento = float(porcentaje_descuento)
        else:
            porcentaje_descuento = 10  # Valor predeterminado

        # Calcular el monto final
        monto_final = calcular_descuento(monto_total, porcentaje_descuento)

        # Mostrar el resultado
        print(f"El monto final a pagar es: ${monto_final:.2f}")

    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")


if __name__ == "__main__":
    main()
