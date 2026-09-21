# Sistema de Classificação do Consumo de Água 
# Autora: Emanuelly Nicolly

# ENTRADA DE DADOS
# Indique o imóvel e o consumom mensal:
tipo_imovel = input("Olá, qual é o tipo de imóvel?").lower().strip()
consumo = float(input("E qual é o consumo mensal de água em m³?"))

#PROCESSAMENTO
# Verifique o tipo de imóvel e o consumo de água para apresentar a classificação adequada:
if tipo_imovel == "comercial":
    classificacao = "Tarifa comercial aplicada - consulte o plano corporativo."

else:
    if tipo_imovel == "apartamento" and consumo < 10:
        classificacao = "Consumo econômico - excenlente controle de água."

    else:
        if (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
            classificacao = "Consumo moderado - dentro do padrão residencial."

        else:
            classificacao = "Consumo execessivo - adote medidas de economia e verifique vazamentos."

# SAÍDA DE DADOS
print()
print("SISTEMA DE CONSUMO DE ÁGUA")
print(f"Aqui está o valor do consumo de água do imóvel {tipo_imovel}:")
print(f"Consumo água: {consumo} m³")
print(f"Classificação: {classificacao}")
print()
print("Obrigado por utilizar nosso Sistema!")