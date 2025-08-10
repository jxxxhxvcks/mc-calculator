cores = {
    'azulclaro':'\033[36m', # overworld
    'vermelho':'\033[31m',  # nether & erro
    'verde':'\033[32m',     # coordenada x
    'amarelo': '\033[33m',  # coordenada z
    'azul':'\033[34m',      # encerrado
    'negrito':'\033[1m',    # texto com negrito
    'reset':'\033[m'        # nulo
    }

print(f"""{cores['negrito']}Você deseja calcular as coordenadas de qual mundo?{cores['reset']}
{cores['negrito']} [ 0 ] {cores['negrito']} {cores['vermelho']}NETHER{cores['reset']} para o {cores['azulclaro']}OVERWORLD{cores['reset']}
{cores['negrito']} [ 1 ] {cores['reset']} {cores['azulclaro']}OVERWORLD{cores['reset']} para o {cores['vermelho']}NETHER{cores['reset']}""")
opcao = int(input(f"{cores['negrito']}>> Faça sua escolha: "))

while opcao not in [0, 1]:
    print(f"{cores['vermelho']}  {opcao} não é uma opção viável.\n     {cores['reset']}Use 0 para calcular do {cores['vermelho']}Nether{cores['reset']} para o {cores['azulclaro']}Overworld{cores['reset']}\n     Use 1 para calcular do {cores['azulclaro']}Overworld{cores['reset']} para o {cores['vermelho']}Nether{cores['reset']}")
    opcao = int(input(f"{cores['negrito']}>> Faça sua escolha: (correta dessa vez) {cores['reset']}"))

while True:
    if opcao == 0:
        print(f"  Ok. Vamos calcular as coordenadas do {cores['vermelho']}Nether{cores['reset']} para o {cores['azulclaro']}Overworld{cores['reset']}")
        try:
            n1 = int(input(f"{cores['negrito']}Digite a primeira coordenada: {cores['verde']}(X){cores['reset']} "))
            n2 = int(input(f"{cores['negrito']}Digite a segunda coordenada: {cores['amarelo']}(Z){cores['reset']} "))
            x = n1 * 8
            z = n2 * 8
            print(f"{cores['verde']}X: {x:,}{cores['reset']}".replace(",", "."))
            print(f"{cores['amarelo']}Z: {z:,}{cores['reset']}".replace(",", "."))
        except ValueError:
            print(f"{cores['vermelho']}Entrada inválida! Por favor, digite números inteiros.{cores['reset']}")
            continue  # volta ao início do while para tentar de novo
        leave = str(input(f"{cores['negrito']}Deseja fazer outro cálculo? [Sim/Não] {cores['reset']}")).upper()[0].strip()
        while leave not in ['S', 'N']:
            leave = str(input(f"{cores['negrito']}Deseja fazer outro cálculo? [Sim/Não] {cores['reset']}")).upper()[0].strip()
        if leave == 'N':
            break
        else:
            print(f"""\n{cores['negrito']} [ 0 ] {cores['negrito']} {cores['vermelho']}NETHER{cores['reset']} para o {cores['azulclaro']}OVERWORLD{cores['reset']}
{cores['negrito']} [ 1 ] {cores['reset']} {cores['azulclaro']}OVERWORLD{cores['reset']} para o {cores['vermelho']}NETHER{cores['reset']}""")
            opcao = int(input(f"{cores['negrito']}>> Faça sua escolha: "))
            while opcao not in [0, 1]:
                print(f"{cores['vermelho']}  {opcao} não é uma opção viável.\n     {cores['reset']}Use 0 para calcular do {cores['vermelho']}Nether{cores['reset']} para o {cores['azulclaro']}Overworld{cores['reset']}\n     Use 1 para calcular do {cores['azulclaro']}Overworld{cores['reset']} para o {cores['vermelho']}Nether{cores['reset']}")
                opcao = int(input(f"{cores['negrito']}>> Faça sua escolha: (correta dessa vez) {cores['reset']}"))

    elif opcao == 1:
        print(f"  Ok. Vamos calcular as coordenadas do {cores['azulclaro']}Overworld{cores['reset']} para o {cores['vermelho']}Nether{cores['reset']}")
        try:
            n1 = int(input(f"{cores['negrito']}Digite a primeira coordenada: {cores['verde']}(X){cores['reset']} "))
            n2 = int(input(f"{cores['negrito']}Digite a segunda coordenada: {cores['amarelo']}(Z){cores['reset']} "))
            x = n1 // 8
            z = n2 // 8
            print(f"{cores['verde']}X: {x:,}{cores['reset']}".replace(",", "."))
            print(f"{cores['amarelo']}Z: {z:,}{cores['reset']}".replace(",", "."))
        except ValueError:
            print(f"{cores['vermelho']}Entrada inválida! Por favor, digite apenas números inteiros.{cores['reset']}")
            continue  # volta ao início do while para tentar de novo
        leave = str(input(f"{cores['negrito']}Deseja fazer outro cálculo? [Sim/Não] {cores['reset']}")).upper()[0].strip()
        while leave not in ['S', 'N']:
            leave = str(input(f"{cores['negrito']}Deseja fazer outro cálculo? [Sim/Não] {cores['reset']}")).upper()[0].strip()
        if leave == 'N':
            break
        else:
            print(f"""\n{cores['negrito']} [ 0 ] {cores['negrito']} {cores['vermelho']}NETHER{cores['reset']} para o {cores['azulclaro']}OVERWORLD{cores['reset']}
{cores['negrito']} [ 1 ] {cores['reset']} {cores['azulclaro']}OVERWORLD{cores['reset']} para o {cores['vermelho']}NETHER{cores['reset']}""")
            opcao = int(input(f"{cores['negrito']}>> Faça sua escolha: "))
            while opcao not in [0, 1]:
                print(f"{cores['vermelho']}  {opcao} não é uma opção viável.\n     {cores['reset']}Use 0 para calcular do {cores['vermelho']}Nether{cores['reset']} para o {cores['azulclaro']}Overworld{cores['reset']}\n     Use 1 para calcular do {cores['azulclaro']}Overworld{cores['reset']} para o {cores['vermelho']}Nether{cores['reset']}")
                opcao = int(input(f"{cores['negrito']}>> Faça sua escolha: (correta dessa vez) {cores['reset']}"))
print(f"{cores['azul']}Programa encerrado.{cores['reset']}")
