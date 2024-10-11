import math

def calcular_trigonometria():
    print("Bem-vindo ao Calculador de Trigonometria!")
    print("Escolha uma opção:")
    print("1. Calcular seno, cosseno e tangente de um ângulo")
    print("2. Resolver um triângulo retângulo")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        angulo = float(input("Digite o ângulo em graus: "))
        angulo_rad = math.radians(angulo)
        seno = math.sin(angulo_rad)
        cosseno = math.cos(angulo_rad)
        tangente = math.tan(angulo_rad)
        
        print(f"Seno({angulo}°) = {seno}")
        print(f"Cosseno({angulo}°) = {cosseno}")
        print(f"Tangente({angulo}°) = {tangente}")

    elif opcao == 2:
        print("Escolha os dados que você tem:")
        print("1. Cateto adjacente e oposto")
        print("2. Cateto adjacente e hipotenusa")
        print("3. Cateto oposto e hipotenusa")

        escolha = int(input("Digite o número da escolha: "))

        if escolha == 1:
            cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
            cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
            hipotenusa = math.sqrt(cateto_adjacente**2 + cateto_oposto**2)
            angulo = math.degrees(math.atan(cateto_oposto / cateto_adjacente))
            
            print(f"Hipotenusa = {hipotenusa}")
            print(f"Ângulo = {angulo}°")

        elif escolha == 2:
            cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
            hipotenusa = float(input("Digite o comprimento da hipotenusa: "))
            cateto_oposto = math.sqrt(hipotenusa**2 - cateto_adjacente**2)
            angulo = math.degrees(math.acos(cateto_adjacente / hipotenusa))
            
            print(f"Cateto oposto = {cateto_oposto}")
            print(f"Ângulo = {angulo}°")

        elif escolha == 3:
            cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
            hipotenusa = float(input("Digite o comprimento da hipotenusa: "))
            cateto_adjacente = math.sqrt(hipotenusa**2 - cateto_oposto**2)
            angulo = math.degrees(math.asin(cateto_oposto / hipotenusa))
            
            print(f"Cateto adjacente = {cateto_adjacente}")
            print(f"Ângulo = {angulo}°")

        else:
            print("Opção inválida!")

    else:
        print("Opção inválida!")

if __name__ == "__main__":
    calcular_trigonometria()