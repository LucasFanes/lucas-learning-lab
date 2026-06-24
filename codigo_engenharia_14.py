NumeroDecimal = int(input("Digite um número decimal: "))
NumeroDecimal1 = NumeroDecimal
NumeroDecimal2 = NumeroDecimal 

print("Número Binário: ", end="")
if NumeroDecimal1 == 0:
    print(0)
else:
    binary_result_str = ""
    while NumeroDecimal1 > 0:
        NumeroBinario = NumeroDecimal1 % 2
        binary_result_str = str(NumeroBinario) + binary_result_str
        NumeroDecimal1 = NumeroDecimal1 // 2
    print(binary_result_str)

resposta_hex = input("Deseja converter para número hexadecimal? (sim/não): ").lower()
if resposta_hex == "sim":
    if NumeroDecimal2 == 0:
        NumeroHexadecimal = "0"
    else:
        hex_result_str = ""
        hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        temp_num = NumeroDecimal2 
        while temp_num > 0:
            remainder = temp_num % 16
            if remainder < 10:
                hex_char = str(remainder)
            else:
                hex_char = hex_map[remainder]
            hex_result_str = hex_char + hex_result_str 
            temp_num //= 16 
        NumeroHexadecimal = hex_result_str
    print(f"Seu número hexadecimal é: {NumeroHexadecimal}")