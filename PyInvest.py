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