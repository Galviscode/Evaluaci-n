lista_de_compras = []

while True:
    producto = input ("Ingrese el nombre del producto (o 'terminar' para finalizar): ").strip().lower()
    
    if producto == "terminar":
        break
    
    lista_de_compras.append(producto)
    
    print("Lista de compras:")
    for producto in lista_de_compras:
        print(producto)