import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- 1. Data Generation ---
# Create realistic synthetic data for customer support response times.
# We'll simulate data for three different support channels.
np.random.seed(42) # for reproducibility
data = {
    'Channel': np.repeat(['Email', 'Live Chat', 'Phone Call'], 200),
    'Response_Time_Mins': np.concatenate([
        np.random.normal(loc=120, scale=30, size=200), # Email: Slower, higher variability
        np.random.normal(loc=5, scale=2, size=200),    # Chat: Fast, low variability
        np.random.normal(loc=15, scale=5, size=200)    # Phone: Medium speed and variability
    ])
}
df = pd.DataFrame(data)
# Ensure no negative response times
df['Response_Time_Mins'] = df['Response_Time_Mins'].clip(lower=1)

# --- 2. Professional Styling ---
# Set a professional style for the plot.
sns.set_style("whitegrid")
sns.set_context("talk") # "talk" context makes labels larger for presentations

# --- 3. Create Violin Plot ---
# Set the figure size to 8x8 inches. With a DPI of 64, this will produce a 512x512 pixel image.
plt.figure(figsize=(8, 8))

# Create the violin plot
ax = sns.violinplot(
    x='Channel',
    y='Response_Time_Mins',
    data=df,
    palette='viridis', # Use a visually appealing color palette
    inner='quartile',  # Show quartiles inside the violins
    linewidth=2
)

# --- 4. Customize Chart ---
# Add meaningful titles and labels for a professional report.
ax.set_title('Distribution of Customer Support Response Times', fontsize=20, pad=20)
ax.set_xlabel('Support Channel', fontsize=16)
ax.set_ylabel('Response Time (Minutes)', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# --- 5. Export Chart ---
# Save the chart as a PNG file with the exact required dimensions.
# Do NOT use bbox_inches='tight' or layout adjustments, as they can change pixel size.
# figsize=(8, 8) and dpi=64 results in 8*64 x 8*64 = 512x512 pixels.
plt.savefig('chart.png', dpi=64)

print("Successfully generated and saved chart.png (512x512 pixels).")

