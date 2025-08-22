import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
df = pd.read_csv("data/omdb_top100_clean.csv")

print("✅ Data Loaded:", df.shape, "rows")
print(df.head())

# --- Numerical Insights ---
avg_rating = round(df['imdbRating'].mean(), 2)
highest_rating = df.loc[df['imdbRating'].idxmax(), ['Title','imdbRating']].to_dict()
lowest_rating = df.loc[df['imdbRating'].idxmin(), ['Title','imdbRating']].to_dict()
most_common_genre = df['MainGenre'].mode()[0]
avg_runtime = round(df['Runtime'].mean(), 1)
avg_boxoffice_m = round(df['BoxOffice'].mean(skipna=True) / 1_000_000, 2)

print("\n📊 Key Insights:")
print("- Average IMDb Rating:", avg_rating)
print("- Highest IMDb Rating Movie:", highest_rating)
print("- Lowest IMDb Rating Movie:", lowest_rating)
print("- Most Common Genre:", most_common_genre)
print("- Average Runtime:", avg_runtime, "minutes")
print("- Average Box Office (in $M):", avg_boxoffice_m)

# --- Export insights + summary stats to Excel ---
os.makedirs("reports", exist_ok=True)
output_file = "reports/imdb_analysis_summary.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    # Save raw data
    df.to_excel(writer, sheet_name="Data", index=False)

    # Save summary statistics
    summary_stats = df[["imdbRating", "Runtime", "BoxOffice"]].describe()
    summary_stats.to_excel(writer, sheet_name="Summary_Stats")

    # Save key insights
    insights = pd.DataFrame({
        "Metric": [
            "Average IMDb Rating",
            "Highest IMDb Rating Movie",
            "Lowest IMDb Rating Movie",
            "Most Common Genre",
            "Average Runtime (min)",
            "Average Box Office ($M)"
        ],
        "Value": [
            avg_rating,
            f"{highest_rating['Title']} ({highest_rating['imdbRating']})",
            f"{lowest_rating['Title']} ({lowest_rating['imdbRating']})",
            most_common_genre,
            avg_runtime,
            avg_boxoffice_m
        ]
    })
    insights.to_excel(writer, sheet_name="Insights", index=False)

print(f"\n✅ Analysis summary exported to {output_file}")

# --- Visuals (still shown for EDA) ---
# 1. IMDb Rating Distribution
plt.figure(figsize=(10,5))
sns.histplot(df["imdbRating"].dropna(), bins=15, kde=True)
plt.title("Distribution of IMDb Ratings (Top 100)")
plt.xlabel("IMDb Rating")
plt.ylabel("Count")
plt.show()

# 2. Top Genres
plt.figure(figsize=(12,6))
genre_counts = df["MainGenre"].value_counts().head(15)
sns.barplot(x=genre_counts.values, y=genre_counts.index, color="skyblue")
plt.title("Top Genres in IMDb Top 100")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

# 3. Box Office vs IMDb Rating
plt.figure(figsize=(10,6))
sns.scatterplot(x="imdbRating", y="BoxOffice", data=df)
plt.title("Box Office vs IMDb Rating")
plt.xlabel("IMDb Rating")
plt.ylabel("Box Office ($)")
plt.show()

# 4. Runtime Distribution
plt.figure(figsize=(10,5))
sns.histplot(df["Runtime"].dropna(), bins=15, kde=True, color="orange")
plt.title("Distribution of Movie Runtime (Top 100)")
plt.xlabel("Runtime (minutes)")
plt.ylabel("Count")
plt.show()

# 5. Average Rating by Decade
plt.figure(figsize=(12,6))
sns.barplot(x="Decade", y="imdbRating", data=df, errorbar=None, color="skyblue")
plt.title("Average IMDb Ratings by Decade (Top 100)")
plt.xlabel("Decade")
plt.ylabel("Average IMDb Rating")
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[["imdbRating", "Runtime", "BoxOffice", "Year"]].corr(),
            annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap")
plt.show()
