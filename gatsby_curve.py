import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
# Use standard fonts for international academic submission
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def generate_gatsby_curve():
    # Simulated data based on typical OECD and Miles Corak findings
    # x-axis: Gini Coefficient (Measure of Inequality)
    # y-axis: Intergenerational Income Elasticity (Higher = Lower Mobility)
    data = {
        'Country': ['Denmark', 'Norway', 'Finland', 'Sweden', 'Germany', 'France', 'UK', 'USA', 'China', 'Brazil'],
        'Gini': [25, 26, 27, 28, 30, 33, 35, 41, 46, 53],
        'Elasticity': [0.15, 0.17, 0.18, 0.27, 0.32, 0.41, 0.50, 0.47, 0.60, 0.66]
    }
    
    df = pd.DataFrame(data)

    # Initialize the figure
    plt.figure(figsize=(10, 7))
    
    # Draw scatter plot
    sns.scatterplot(data=df, x='Gini', y='Elasticity', s=120, color='darkred', edgecolor='black', zorder=5)
    
    # Draw trend line (regression line)
    sns.regplot(data=df, x='Gini', y='Elasticity', scatter=False, color='gray', 
                line_kws={"linestyle": "--", "alpha": 0.6, "linewidth": 2})

    # Add country labels to each point
    for i in range(df.shape[0]):
        plt.text(df.Gini[i] + 0.8, df.Elasticity[i], df.Country[i], 
                 fontsize=11, verticalalignment='center')

    # Set title and axis labels in English
    plt.title('The Great Gatsby Curve: Inequality vs. Social Mobility', fontsize=15, fontweight='bold', pad=20)
    plt.xlabel('Income Inequality (Gini Coefficient)', fontsize=12)
    plt.ylabel('Intergenerational Income Elasticity (Higher = Lower Mobility)', fontsize=12)

    # Add quadrant annotations
    plt.text(25, 0.65, 'High Mobility / Low Inequality\n(Shallow Social Ladder)', color='green', fontsize=10, 
             fontweight='bold', bbox=dict(facecolor='white', alpha=0.7, edgecolor='green'))
    plt.text(42, 0.2, 'Low Mobility / High Inequality\n(Class Stratification)', color='red', fontsize=10, 
             fontweight='bold', bbox=dict(facecolor='white', alpha=0.7, edgecolor='red'))

    # Optimize layout
    plt.tight_layout()
    
    # Save the file
    file_path = 'gatsby_curve_en.png'
    plt.savefig(file_path, dpi=300)
    print(f"Success! Plot saved to: {file_path}")
    
    # Display the plot
    plt.show()
    plt.close()

if __name__ == "__main__":
    generate_git commit -m "Initialize Econ-AI-Research\gatsby_curve.py“       ()
