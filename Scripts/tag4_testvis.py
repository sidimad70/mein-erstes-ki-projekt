import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# 1. Daten vorbereiten
# -------------------------
daten = {
    'Jobtitel': [
        'Data Analyst',
        'Python Dev',
        'KI Spezialist',
        'Praktikant',
        'Senior Analyst'
    ],
    'Gehalt': [65000, 72000, 85000, 35000, 95000],
    'Stadt': ['Düsseldorf', 'Köln', 'Essen', 'Bonn', 'Düsseldorf']
}

df = pd.DataFrame(daten)

# -------------------------
# 2. Design setzen
# -------------------------
sns.set_theme(style="whitegrid")

# -------------------------
# 3. Diagramm erstellen
# -------------------------
plt.figure(figsize=(10, 6))

sns.barplot(
    x='Jobtitel',
    y='Gehalt',
    data=df,
    hue='Stadt'
)

# -------------------------
# 4. Beschriftung
# -------------------------
plt.title('Gehaltsvergleich nach Jobtitel und Stadt')
plt.xlabel('Beruf')
plt.ylabel('Jahresgehalt (€)')
plt.xticks(rotation=30)

# -------------------------
# 5. Speichern & Anzeigen
# -------------------------
plt.tight_layout()
plt.savefig('gehaltsgrafik.png')
plt.show()
