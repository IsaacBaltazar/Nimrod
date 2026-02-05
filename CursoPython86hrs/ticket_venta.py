print('*** Generación Ticket de Venta ***')

precio_leche = float(input('Precio de la leche: '))
precio_pan = float(input('Precio del pan: '))
precio_lechuga = float(input('Precio de la lechuga: '))
precio_platanos = float(input('Precio de los plátanos: '))
descuento_porcentaje = int(input('Aplicar descuento (%)? '))

# Cálculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Descuento
descuento = subtotal * (descuento_porcentaje/100)
# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento
# Cálculo de impuestos (16%)
impuesto = subtotal_con_descuento * 0.16


# Cálculo total de la compra con impuestos
costo_total_compra = subtotal_con_descuento + impuesto
print(f'''
Subtotal: ${subtotal:.2f}
Descuento: ${descuento:.2f} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento}
Impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}
    ''')