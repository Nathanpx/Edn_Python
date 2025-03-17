def classificar_idade(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

# Solicita a idade do usuário
try:
    idade = int(input("Digite sua idade: "))
    categoria = classificar_idade(idade)
    print(f"Você é classificado como: {categoria}")
except ValueError:
    print("Por favor, digite um número válido.")
