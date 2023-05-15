valores = [23, 56, 101, 19, 87, 98, 65, 45, 56, 59, 88, 13]

pct_manual = 0.05
pct_maquina = 0.15

colheita_ano = 0
projecao_desperdicio_manual = 0
projecao_desperdicio_maquina = 0

cont = 1
for valor in valores:

    perda_manual = (valor * pct_manual).__round__(2)
    perda_maquina = (valor * pct_maquina).__round__(2)

    print(f"""
    Perda manual.....: {perda_manual:.2f}
    Perda máquina.....: {perda_maquina:.2f}
    """)

    colheita_ano += valor
    projecao_desperdicio_manual += perda_manual
    projecao_desperdicio_maquina += perda_maquina

    cont += 1

print(f"""
RELATÓRIO CONSOLIDADO

Colheita do ano....: {colheita_ano:.2f} Toneladas

Projeção de desperdício

Manual....: {projecao_desperdicio_manual:.2f}
Máquina....: {projecao_desperdicio_maquina:.2f}

""")