import pandas as pd
from klaten_selenium import covid
import openpyxl


covid.lodp_aktif
a =sum(covid.lodp_aktif)

covid.lodp_meninggal
b =sum(covid.lodp_meninggal)

covid.lodp_sembuh
c = sum(covid.lodp_sembuh)

covid.lpdp_aktif
d = sum(covid.lpdp_aktif)

covid.lpdp_meninggal
e = sum(covid.lpdp_meninggal)

covid.lpdp_sembuh
f = sum(covid.lpdp_sembuh)

covid.lpositif_aktif
g = sum(covid.lpositif_aktif)

covid.lpositif_meninggal
h = sum(covid.lpositif_meninggal)

covid.lpositif_sembuh
i = sum(covid.lpositif_sembuh)
#"""""
rekapan_df = pd.DataFrame(columns=list('ABCDEFGHI'))
rekapan_df.loc[0] = [a,b,c,d,e,f,g,h,i]

#"""""
print(a,b,c,d,e,f,g,h)
print(rekapan_df)

rekapan_df.to_excel('output_klaten.xlsx')