def converterIdade(dias_totais):
    anos = dias_totais // 365
    meses = dias_totais // 30
    dias = dias_totais

    return anos, meses, dias

# Entrada do usuário
idade_em_dias = int(input("Digite a idade em dias: "))

# Conversão
anos, meses, dias = converterIdade(idade_em_dias)

# Saída
print(f"A idade corresponde a {anos} anos, {meses} meses e {dias} dias.")
