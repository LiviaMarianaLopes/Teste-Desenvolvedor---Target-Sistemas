def inverter_string(string):
    """Função que retorna uma string invertida"""
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

texto = input("Texto: ")
print(f"Texto invertido: {inverter_string(texto)}")
