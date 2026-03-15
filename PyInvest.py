import math
import random
import datetime
import statistics as st
import locale
locale.setlocale(locale.LC_ALL, "pt_br.UTF-8")

#inputs

capitalI = float(input("Digite o capital inicial: R$"))
aporteM = float(input("Digite o aporte mensal: R$"))
mesesI = int(input("Prazo do investimento (meses): "))
cdiA = float(input("Valor do CDI anual: %"))
percCdi = float(input("Percentual do CDI aplicado ao CDB: %"))
percLci = float(input("Percentual do CDI aplicado a LCI/LCA: %"))
rentFii = float(input("Rentabilidade mensal esperada do FII: %"))
metaI = float(input("Meta final desejada: R$"))

#calculos dos inputs

cdiM = (1+cdiA/100)**(1/12)-1
totalInv = capitalI + (aporteM*mesesI)
taxCdb = cdiM * (percCdi/100)
taxLci = cdiM * (percLci/100)
taxFii = (rentFii/100)
taxPoup = (0.5/100)

#calculo cdb
montanteCdb = (capitalI * math.pow(1+taxCdb, mesesI)) + (aporteM * mesesI)
lucroCdb = montanteCdb - totalInv
montanteCdbF = totalInv + (lucroCdb * 0.85)

#calculo lci
montanteLci = (capitalI * math.pow(1+taxLci, mesesI)) + (aporteM * mesesI)

#calculo poupança
montantePoup = (capitalI * math.pow(1+taxPoup, mesesI)) + (aporteM * mesesI)

#calculo FII
montanteIFii = (capitalI * math.pow(1+taxFii, mesesI)) + (aporteM * mesesI)
val1 = montanteIFii + random.uniform(-0.03, 0.03) * montanteIFii
val2 = montanteIFii + random.uniform(-0.03, 0.03) * montanteIFii
val3 = montanteIFii + random.uniform(-0.03, 0.03) * montanteIFii
val4 = montanteIFii + random.uniform(-0.03, 0.03) * montanteIFii
val5 = montanteIFii + random.uniform(-0.03, 0.03) * montanteIFii

mediaFii = st.mean((val1, val2, val3, val4, val5))
medianaFii = st.median((val1, val2, val3, val4, val5))
desvioFii = st.stdev((val1, val2, val3, val4, val5))

#datas
datahojeI = datetime.datetime.now()
dataresF = datahojeI + datetime.timedelta(days= mesesI * 30)

#barras para o grafico
barraCdb = int(montanteCdbF/1000)
barraLci = int(montanteLci/1000)
barraPoup = int(montantePoup/1000)
barraFii = int(mediaFii/1000)

#outputs

print(f"{"SIMULADOR PYINVEST":^60}")

print(f"Data da simulação: {datahojeI.strftime("%d/%m/%Y")}")
print(f"Data estimada de resgate: {dataresF.strftime("%d/%m/%Y")}")

print("="*60)

print(f"Total investido: {locale.currency(totalInv, grouping=True)}")

print(f"{"RESULTADOS":^20}")

print(f"CDB: {locale.currency(montanteCdbF, grouping=True)}")
print(f"█"*barraCdb)

print(f"LCI/LCA: {locale.currency(montanteLci, grouping=True)}")
print(f"█"*barraLci)

print(f"Poupança: {locale.currency(montantePoup, grouping=True)}")
print(f"█"*barraPoup)

print(f"FII (média): {locale.currency(mediaFii, grouping=True)}")
print(f"█"*barraFii)

print(f"{"ESTATISTICAS FII":^20}")
print(f"Mediana: {locale.currency(medianaFii, grouping=True)}")
print(f"Desvio padrão: {locale.currency(desvioFii, grouping=True)}")
#verificar se a meta inicial foi atingida
metaF = max(montanteCdbF, montanteLci, montantePoup, mediaFii) >= metaI
print(f"Meta atingida? {metaF}")
print("="*60)

#referencias:
#PDF Aula 1, pag. 68 e 71
#https://docs.python.org/3/library/datetime.html#examples-of-usage-date
#https://docs.python.org/3/library/functions.html#max


