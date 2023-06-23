# Witterungsbereinigung Nebenrechnung für Vojens Fernwärmenetz Wärmeabsatz und EE Anteil
# Quelle: https://ec.europa.eu/eurostat/de/web/main/search/-/search/estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J?p_auth=8m0lNu54&text=Heizgradtage+und+K%C3%BChlgradtage+nach+Land+-+j%C3%A4hrliche+Daten&_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_collection=&_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_theme=

# Betrachtete Zeitperiode
Jahre = [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003]

# Jährliche Heizgradtage in Kd/a für Dänemark von 2022 bis 2003
HGT = [3019.14 , 3263.77, 2920.71, 3026.80, 3048.54, 3112.11, 3141.46,	3114.15, 2834.98, 3396.28, 3424.15, 3148.45, 3982.16, 3230.76, 3019.35, 3000.97, 3084.26, 3261.34, 3309.22, 3325.61]

# Durschnitts Heizgradtage in Zeitperiode
periode = len(Jahre)
hgt_avg = sum(HGT)/len(HGT)
print('Betrachtete Jahre:\n',Jahre)
print('Heizgradtage in den Jahren\n:', HGT)
print('Durschnitts Heizgradtage in der genannten Periode:', hgt_avg)

# Berechnung Korrekturfaktor k 
# HGT eines Jahres geteilt durch Durschnitts-HGT einer Periode
k = []
for idx, hgt in enumerate(HGT):
	k.append(hgt/hgt_avg)

# Anteil der Erneuerbaren in den Jahren 2022, 2021, 2020 in Prozent
EE_gegeben = [62.76, 58.00, 42.00]
EE_bereinigt = []
# Berechnung: Anteil der Erneuerbaren in Prozent, witterungsbereinigt
# Annahme: EE-Anteil absolut gleich, Gesamtverbrauch mit Korrekturfaktor 
# Bsp: 42 % von 100 % -> 42 von k*100 -> 42/k % von 100 %
for idx, EE in enumerate(EE_gegeben):
	EE_bereinigt.append(EE/k[idx])
	print(f'Jahr: {Jahre[idx]:2} 	EE = {EE:2f} % 	k = {k[idx]:2f}	EE(witterungsbereinigt) = {EE_bereinigt[idx]:2f}')
