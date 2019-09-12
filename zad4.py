
osnovica = 40000
jan = 0.17
feb = 1.9
mar = 0.13
apr = 1.02
may = 0.78
jun = 0.67
july = 0.67
august = 0.35
september = 1.18
october = 0.2
november = 0.66
december = 1
janToJun = jan + feb + mar + apr + may + jun
julyToDec = july + august + september + october + november + december
total = janToJun + julyToDec


print("Polugodisnji koeficijent je: " + str(janToJun))
print("Ukupan koeficijent je: " + str(total))


total = janToJun + julyToDec

bonus = osnovica * total * 0.1

print("Bonus je: " + str(bonus))
