import pdm


print(pdm.people)

print(pdm.people["Dimitri"])
print(pdm.people["Roland"])

print(pdm.people["Dimitri"]["name"])
print(pdm.people["Dimitri"]["age"])
print(pdm.people["Dimitri"]["gewicht"])

print(pdm.people["Roland"].items())
print(pdm.people["Roland"].keys())
print(pdm.people["Roland"].values())

print(pdm.people["Igor"].items())
print(pdm.people["Igor"].keys())
print(pdm.people["Igor"].values())
