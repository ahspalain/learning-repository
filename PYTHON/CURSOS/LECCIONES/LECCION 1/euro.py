
precio_producto = (input("Introduce el precio en euros con dos decimales: "))

print(f'El precio del producto es de {precio_producto[:precio_producto.find(".")]} euros y {precio_producto[precio_producto.find(".")+1:]} centavos')