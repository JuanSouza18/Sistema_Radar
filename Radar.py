#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO , SE FOR MAIOR QUE 80 VAI TER UMA MULTA POR CADA KM A RODADO
limite = 50
valor_multa_por_km = 7

for i in range(2):
    velocidade = float(input(f"Digite a velocidade do veículo {i + 1}: "))
    
    if velocidade > limite:
        excesso = velocidade - limite
        multa = excesso * valor_multa_por_km
        print(f"Veículo {i + 1}: Excedeu o limite em {excesso:.1f} km/h.")
        print(f"Multa: R$ {multa:.2f}\n")
    else:
        print(f"Veículo {i + 1}: Dentro do limite. Sem multa.\n")
