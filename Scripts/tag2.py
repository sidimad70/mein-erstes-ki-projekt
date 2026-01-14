gehaelter = [2100, 3500, 4200, 1900, 5000]
bonus_gehaelter = []

for g in gehaelter:
    if g < 3000:
        neues_g = g * 1.1
        bonus_gehaelter.append(neues_g)
    else:
        bonus_gehaelter.append(g)

print("Alte Gehälter:", gehaelter)
print("Neue Gehälter:", bonus_gehaelter)


zahlen = [12, 55, 3, 89, 42, 100, 7]
gross = []

for z in zahlen:
    if z > 50:
        gross.append(z)

print(gross)

for i in range(10, 0, -3):
    print(i)
print("🚀 Start!")
