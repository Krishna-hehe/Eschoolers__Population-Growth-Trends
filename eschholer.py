
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr

# Load datasets
population_data = pd.read_csv("global_population_urbanization_gdp.csv")
urbanization_data = pd.read_csv("global_population_urbanization_gdp.csv")       
gdp_data = pd.read_csv("global_population_urbanization_gdp.csv")                        


data = population_data.merge(urbanization_data, on=["Country", "Year"], how="inner")
data = data.merge(gdp_data, on=["Country", "Year"], how="inner")


data.rename(columns={
    "Population Growth (%)": "Population Growth",
    "Urbanization (%)": "Urbanization",
    "GDP (USD)": "GDP"
}, inplace=True)

print(data.head())
print("\nSummary Statistics:\n", data.describe())


plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x="Year", y="Population Growth", hue="Country")
plt.title("Population Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Population Growth (%)")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x="Year", y="Urbanization", hue="Country")
plt.title("Urbanization Over Time")
plt.xlabel("Year")
plt.ylabel("Urbanization (%)")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x="Year", y="GDP", hue="Country")
plt.title("GDP Over Time")
plt.xlabel("Year")
plt.ylabel("GDP (in USD)")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()


population_urban_corr, _ = pearsonr(data["Population Growth"], data["Urbanization"])
population_gdp_corr, _ = pearsonr(data["Population Growth"], data["GDP"])
urbanization_gdp_corr, _ = pearsonr(data["Urbanization"], data["GDP"])

print(f"\nCorrelation between Population Growth and Urbanization: {population_urban_corr:.2f}")
print(f"Correlation between Population Growth and GDP: {population_gdp_corr:.2f}")
print(f"Correlation between Urbanization and GDP: {urbanization_gdp_corr:.2f}")

plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Urbanization", y="Population Growth", hue="GDP", size="GDP", sizes=(20, 200), palette="viridis")
plt.title("Population Growth vs Urbanization")
plt.xlabel("Urbanization (%)")
plt.ylabel("Population Growth (%)")
plt.colorbar(label="GDP")
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="GDP", y="Population Growth", hue="Urbanization", size="Urbanization", sizes=(20, 200), palette="plasma")
plt.title("Population Growth vs GDP")
plt.xlabel("GDP (in USD)")
plt.ylabel("Population Growth (%)")
plt.colorbar(label="Urbanization")
plt.show()

file_path = 'global_population_urbanization_gdp.csv.csv'
data = pd.read_csv(file_path)

data.head()


spearman_corr, _ = spearmanr(data["Population Growth"], data["Urbanization"])
print(f"\nSpearman correlation between Population Growth and Urbanization: {spearman_corr:.2f}")

print("\nAnalysis complete. Review visualizations and correlations to interpret results.")
