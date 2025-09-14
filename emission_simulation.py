import pandas as pd
import matplotlib.pyplot as plt

MAX_SUPPLY = 21_000_000
BLOCK_REWARD = 50
BLOCK_TIME = 10  # minutos
BLOCKS_PER_YEAR = int((365*24*60) / BLOCK_TIME)
HALVING_INTERVAL = 210_000

supply = 0
reward = BLOCK_REWARD
blocks_mined = 0

data = []
for year in range(2025, 2141):
    blocks_this_year = 0
    emitted_this_year = 0
    while blocks_this_year < BLOCKS_PER_YEAR and supply < MAX_SUPPLY:
        blocks_this_year += 1
        blocks_mined += 1
        emitted_this_year += reward
        supply += reward
        if blocks_mined % HALVING_INTERVAL == 0:
            reward /= 2
    data.append([year, blocks_this_year, emitted_this_year, supply])

df = pd.DataFrame(data, columns=["Year", "Blocks_Mined", "Emitted_in_Year", "Cumulative_End_Year"])
df.to_csv("nbg_emission_full_2025_2140.csv", index=False)

plt.bar(df["Year"], df["Emitted_in_Year"])
plt.xlabel("Ano")
plt.ylabel("Moedas emitidas")
plt.title("Emissão Anual NBG (2025–2140)")
plt.savefig("nbg_emission_full_bar.png", dpi=300)
plt.close()

plt.plot(df["Year"], df["Cumulative_End_Year"])
plt.xlabel("Ano")
plt.ylabel("Supply acumulado")
plt.title("Supply acumulado NBG (2025–2140)")
plt.savefig("nbg_emission_full_cumulative.png", dpi=300)
plt.close()

print("Simulação concluída! Arquivos salvos:")
print(" - nbg_emission_full_2025_2140.csv")
print(" - nbg_emission_full_bar.png")
print(" - nbg_emission_full_cumulative.png")
