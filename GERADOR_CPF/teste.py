import random

def generate_random_cpf(estado="SP"):
    # Dicionário com os dígitos iniciais de cada estado
    estados = {
        "AC": "01", "AL": "02", "AP": "03", "AM": "04", "BA": "05", "CE": "06",
        "DF": "07", "ES": "08", "GO": "09", "MA": "10", "MT": "11", "MS": "12",
        "MG": "13", "PA": "14", "PB": "15", "PR": "16", "PE": "17", "PI": "18",
        "RJ": "19", "RN": "20", "RS": "21", "RO": "22", "RR": "23", "SC": "24",
        "SP": "25", "SE": "26", "TO": "27"
    }

    if estado not in estados:
        raise ValueError("Estado inválido. Escolha um estado válido de duas letras (exemplo: SP, RJ, MG, etc.).")

    # Gerar 9 dígitos aleatórios
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Inserir os dígitos iniciais do estado escolhido
    cpf[:2] = [int(digito) for digito in estados[estado]]

    # Calcular os dígitos verificadores
    def calculate_digit(cpf):
        total = 0
        count = 10 if len(cpf) == 9 else 11
        for i in range(len(cpf)):
            total += int(cpf[i]) * count
            count -= 1
        remainder = total % 11
        return 0 if remainder in [0, 1] else 11 - remainder

    digit1 = calculate_digit(cpf)
    cpf.append(digit1)
    digit2 = calculate_digit(cpf)
    cpf.append(digit2)

    return "".join(map(str, cpf))

# Teste de geração de CPF fictício com estado definido
if __name__ == "__main__":
    estado_escolhido = "PE"  # Substitua por outro estado válido de duas letras, se desejar
    cpf_gerado = generate_random_cpf(estado_escolhido)
    print(f"CPF Gerado: {cpf_gerado}")
