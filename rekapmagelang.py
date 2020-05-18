import pandas as pd
from kab_magelang import covid_magelang
import openpyxl


covid.lodp_aktif
a =sum(covid_magelang.lodp_aktif)

magelang.lodp_meninggal
b =sum(covid_magelang.lodp_meninggal)

magelang.lodp_sembuh
c = sum(covid_magelang.lodp_sembuh)

magelang.lpdp_aktif
d = sum(covid_magelang.lpdp_aktif)

magelang.lpdp_meninggal
e = sum(covid_magelang.lpdp_meninggal)

magelang.lpdp_sembuh
f = sum(covid_magelang.lpdp_sembuh)

magelang.lpositif_aktif
g = sum(covid_magelang.lpositif_aktif)

magelang.lpositif_meninggal
h = sum(covid_magelang.lpositif_meninggal)

magelang.lpositif_sembuh
i = sum(covid_magelang.lpositif_sembuh)
#"""""
rekapan_df = pd.DataFrame(columns=list('ABCDEFGHI'))
rekapan_df.loc[0] = [a,b,c,d,e,f,g,h,i]

#"""""
print(a,b,c,d,e,f,g,h)
print(rekapan_df)

rekapan_df.to_excel('output_magelang.xlsx')