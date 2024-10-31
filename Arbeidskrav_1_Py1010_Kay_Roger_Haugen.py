'''
Arbeidskrav 1 i Py1010

Samanlikning av aarlege kostnadar med elbil vs bensinbil

Laga av: Kay Roger Haugen - kay.roger.haugen@gmail.com

Sist oppdatert: 2024-10-31
'''

Km = 10000  # Årleg køyrelengde [km/år]
Fs_El = 5000  # Forsikring elbil [kr/år]
Fs_B = 7500  # Forsikring bensinbil [kr/år]
Tfs = 8.38  # Trafikkforsikringsavgift [kr/dag]
Dsf_El = 0.2  # Drivstoffbruk elbil [kWh/km]
Dsf_B = 1.0  # Drivstoffbruk bensin [kr/km]
Straum = 2.00  # Straumpris [kr/kWh]
Bom_El = 0.1  # Bomavgift elbil [kr/km]
Bom_B = 0.3  # Bomavgift bensin [kr/km]

# Utrekning av årleg totalkostnad for elbil
# Forsikring + trafikkforsikring + drivstoff + bomavgift
Tot_El = Fs_El + 365*Tfs + Dsf_El*Km*Straum + Bom_El*Km

# Utrekning av årleg totalkostnad for bensinbil
# Forsikring + trafikkforsikring + drivstoff + bomavgift
Tot_B = Fs_B + 365*Tfs + Dsf_B*Km + Bom_B*Km

# Utrekning av årleg kostnadsdifferanse mellom elbil og bensinbil
Tot_diff = Tot_El - Tot_B

# Utskrift av årleg totalkostnad for elbil og bensinbil, samt differansen
print('Årleg totalkostnad for elbil: kr.', Tot_El)
print('Årleg totalkostnad for bensinbil: kr.', Tot_B)
print('Årleg kostnadsdifferanse mellom elbil og bensinbil: kr.', Tot_diff)
