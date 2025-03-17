def converter_temperatura(temperatura, origem, destino):
    origem = origem.lower()
    destino = destino.lower()
    
    if origem == destino:
        return temperatura
    
    if origem == "celsius":
        if destino == "fahrenheit":
            return (temperatura * 9/5) + 32
        elif destino == "kelvin":
            return temperatura + 273.15
    elif origem == "fahrenheit":
        if destino == "celsius":
            return (temperatura - 32) * 5/9
        elif destino == "kelvin":
            return (temperatura - 32) * 5/9 + 273.15
    elif origem == "kelvin":
        if destino == "celsius":
            return temperatura - 273.15
        elif destino == "fahrenheit":
            return (temperatura - 273.15) * 9/5 + 32
    
    return "Unidade inválida"

# Solicita entrada do usuário
try:
    temperatura = float(input("Digite a temperatura: "))
    origem = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ")
    destino = input("Digite a unidade de destino (Celsius, Fahrenheit, Kelvin): ")
    resultado = converter_temperatura(temperatura, origem, destino)
    print(f"A temperatura convertida é: {resultado} {destino.capitalize()}")
except ValueError:
    print("Por favor, digite um valor numérico válido.")