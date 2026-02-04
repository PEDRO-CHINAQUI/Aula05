quant = int(input("Escolha a quantidade de teste:"))
for i in range(1,quant + 1):
    print(f"{i}º Aluno: \n")
    nome = input("Nome: ")
    p1 = float(input("Prova 01:"))
    p2 = float(input("Prova 02:"))
    p3 = float(input("Prova 03:"))
    md = (p1+p2+p3)/3
    if md >= 7:
        resultado = "Aprovado"
    elif md >= 5:
        resultado = "Recuperação"
    else:
        resultado = "Reprovado"
    print(f"\n{i}º Nome: {nome}")
    print(f"Prova 01: {p1}")
    print(f"Prova 02: {p2}")
    print(f"Prova 03: {p3}")
    print(f"Prova 01: {p1}")
    print(f"Média:  {md:.1f}")
    print(f"Resultado: {resultado}")