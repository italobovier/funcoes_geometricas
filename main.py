def mostrar_menu():
    print('1 - Calcular quadrilátero.')
    print('2 - Calcular triângulo.')
    print('3 - Calcular círculo.')
    print('4 - Sair do programa.')

def calcular_quadrilatero(b, h):
    return b * h

def calcular_triangulo(b, h):
    return (b * h) / 2

def calcular_circulo(r):
    return 3.14 * (r ** 2)

# Programa principal
while True:
    mostrar_menu()
    opcao = input("Opção desejada: ")
    
    match opcao:
        case '1':
            b = float(input('Informe o valor da base: ').replace(',', '.'))
            h = float(input('Informe o valor da altura: ').replace(',', '.'))
            print(f'Área do quadrilátero: {calcular_quadrilatero(b, h)}.')
        
        case '2':
            b = float(input('Informe o valor da base: ').replace(',', '.'))
            h = float(input('Informe o valor da altura: ').replace(',', '.'))
            print(f'Área do triângulo: {calcular_triangulo(b, h)}.')
        
        case '3':
            r = float(input('Informe o valor do raio: ').replace(',', '.'))
            print(f'Área do círculo: {calcular_circulo(r)}.')
        
        case '4':
            print("Saindo do programa.")
            break
        
        case _:
            print("Opção inválida.")
