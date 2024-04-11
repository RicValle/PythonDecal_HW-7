
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

planets_df = sns.load_dataset('planets')

planets_df.dropna(subset=['year', 'method'], inplace=True)

# Plot 1: 

plt.figure(figsize=(10, 6))
sns.scatterplot(x='orbital_period', y='mass', hue='method', data=planets_df, palette='Set2')
plt.xscale('log')
plt.yscale('log')
plt.title('Orbital Period vs Mass of Exoplanets by Discovery Method')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Mass (Jupiter Mass)')
plt.legend(title='Discovery Method')
plt.grid(True)
plt.savefig("Plot 1: (Orbital period vs exoplanets)")
plt.show()


#Plot 2: 

plt.figure(figsize=(12, 6))
sns.countplot(x='year', hue='method', data=planets_df, palette='Set2', edgecolor='black')
plt.title('Exoplanet Discoveries by Year and Method')
plt.xlabel('Year')
plt.ylabel('Number of Exoplanets Discovered')
plt.legend(title='Discovery Method', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Plot 2: (Exoplanets discovered by year)")
plt.show()

