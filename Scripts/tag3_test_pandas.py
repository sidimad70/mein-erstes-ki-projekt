import pandas as pd

df = pd.read_csv("data/tiere.csv")

print(df)
print(df.columns)
print(df.shape)

print(df.describe())


schwere_tiere = df[df["Gewicht"] > 80]
print(schwere_tiere)
gesund = df[df["Gesund"] == True]
print(gesund)
kandidaten = df[(df["Gewicht"] > 80) & (df["Gesund"] == True)]
print(kandidaten)

df["Gewichtsklasse"] = df["Gewicht"].apply(
    lambda g: "schwer" if g > 80 else "normal"
)

print(df)
df.to_csv("data/tiere_analysiert.csv", index=False)
