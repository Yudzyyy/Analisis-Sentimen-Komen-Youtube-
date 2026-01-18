import pandas as pd
import matplotlib.pyplot as plt

# Load data hasil sentimen
df = pd.read_csv("data/comments_sentiment.csv")

# Hitung jumlah tiap sentimen
sentiment_counts = df["sentiment"].value_counts()

# ===== PIE CHART =====
plt.figure()
plt.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribusi Sentimen Komentar YouTube")
plt.show()

# ===== BAR CHART =====
plt.figure()
sentiment_counts.plot(kind="bar")
plt.title("Jumlah Komentar per Sentimen")
plt.xlabel("Sentimen")
plt.ylabel("Jumlah Komentar")
plt.show()
