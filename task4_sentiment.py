import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("reviews.csv")

print("===== SENTIMENT ANALYSIS =====")
print("\nReviews:")
print(df)

# Count sentiments
sentiment_counts = df["Sentiment"].value_counts()

print("\nSentiment Counts:")
print(sentiment_counts)

# Find most common sentiment
most_common = sentiment_counts.idxmax()
print("\nMost Common Sentiment:", most_common)

# Visualization
plt.figure(figsize=(7, 5))
plt.bar(sentiment_counts.index, sentiment_counts.values)
plt.title("Sentiment Analysis of Customer Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.savefig("chart5_sentiment.png")
plt.close()

print("\nSentiment chart created successfully!")