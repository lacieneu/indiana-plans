import pandas as pd
import matplotlib.pyplot as plt

# Load Marketplace health plan data
plans = pd.read_excel("individual_market_medical.xlsx")

# Keep only Indiana plans
indiana_plans = plans[plans["State Code"] == "IN"]

# Select the premium and deductible columns
premium = "Premium Adult Individual Age 21"
deductible = "Medical Deductible - Individual - Standard"

# Convert the columns to numbers
indiana_plans[premium] = pd.to_numeric(
    indiana_plans[premium], errors="coerce"
)

indiana_plans[deductible] = pd.to_numeric(
    indiana_plans[deductible], errors="coerce"
)

# Make the scatter plot
plt.scatter(
    indiana_plans[premium],
    indiana_plans[deductible]
)

plt.xlabel("Monthly Premium ($)")
plt.ylabel("Deductible ($)")
plt.title("Indiana Marketplace Health Plans: Premium vs. Deductible")

# Save the graph as a PNG
plt.savefig(
    "indiana_premium_vs_deductible.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# Print the number of Indiana plans
print("Number of Indiana plans:", len(indiana_plans))
