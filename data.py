import matplotlib
import matplotlib.pyplot as plt

incarceration = {
    "Louisiana": 0.85, "Delaware": 0.76, "Mississippi": 0.73, "Oklahoma": 0.71, "Alaska": 0.69,
    "Alabama": 0.67, "Texas": 0.63, "Arizona": 0.62, "Arkansas": 0.58, "Georgia": 0.54,
    "Florida": 0.53, "Missouri": 0.52, "Connecticut": 0.49, "Kentucky": 0.48, "Nevada": 0.47,
    "Idaho": 0.47, "South Carolina": 0.46, "Indiana": 0.46, "Virginia": 0.45, "Ohio": 0.45,
    "Michigan": 0.44, "Tennessee": 0.44, "South Dakota": 0.43, "Hawaii": 0.40, "Wyoming": 0.40,
    "Colorado": 0.39, "Oregon": 0.39, "Wisconsin": 0.39, "Pennsylvania": 0.39, "Illinois": 0.38,
    "North Carolina": 0.37, "West Virginia": 0.37, "Maryland": 0.36, "Montana": 0.36, "California": 0.35,
    "Kansas": 0.34, "Vermont": 0.33, "New Mexico": 0.33, "Rhode Island": 0.32, "Iowa": 0.28,
    "New York": 0.27, "Nebraska": 0.27, "Washington": 0.26, "New Jersey": 0.25, "Utah": 0.24,
    "New Hampshire": 0.23, "North Dakota": 0.21, "Minnesota": 0.19, "Maine": 0.16, "Massachusetts": 0.16,
}

bachelors = {
    "Louisiana": 21.7, "Delaware": 31.0, "Mississippi": 21.8, "Oklahoma": 24.4, "Alaska": 29.4,
    "Alabama": 25.0, "Texas": 31.7, "Arizona": 29.2, "Arkansas": 24.0, "Georgia": 32.1,
    "Florida": 31.1, "Missouri": 31.7, "Connecticut": 40.0, "Kentucky": 24.0, "Nevada": 24.0,
    "Idaho": 26.0, "South Carolina": 29.0, "Indiana": 27.0, "Virginia": 39.6, "Ohio": 31.0,
    "Michigan": 31.1, "Tennessee": 30.5, "South Dakota": 29.0, "Hawaii": 34.0, "Wyoming": 27.0,
    "Colorado": 42.0, "Oregon": 34.7, "Wisconsin": 32.2, "Pennsylvania": 32.9, "Illinois": 36.3,
    "North Carolina": 33.0, "West Virginia": 20.0, "Maryland": 40.9, "Montana": 33.0, "California": 35.0,
    "Kansas": 34.0, "Vermont": 38.0, "New Mexico": 27.0, "Rhode Island": 34.2, "Iowa": 29.1,
    "New York": 38.0, "Nebraska": 32.6, "Washington": 36.3, "New Jersey": 40.7, "Utah": 34.7,
    "New Hampshire": 37.0, "North Dakota": 31.0, "Minnesota": 36.5, "Maine": 33.4, "Massachusetts": 44.2,
}

states = list(incarceration.keys())
x = [bachelors[state] for state in states]
y = [incarceration[state] for state in states]

fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(x, y, alpha=0.8, color="steelblue", edgecolors="black", s=80)

for state, xi, yi in zip(states, x, y):
    ax.annotate(state, (xi, yi), textcoords="offset points", xytext=(4, 4), fontsize=8)

ax.set_title("Incarceration Rate vs. Bachelor's Degree Rate by State")
ax.set_xlabel("Percent with Bachelor's Degree or Higher")
ax.set_ylabel("Incarceration Rate (%)")
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xlim(18, 46)
ax.set_ylim(0.15, 0.90)

plt.tight_layout()

plt.savefig("state_incarceration_vs_bachelors.png", dpi=300)
print("Graph saved: state_incarceration_vs_bachelors.png")

plt.show()

plt.close(fig)