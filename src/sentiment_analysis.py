import pandas as pd
from transformers import pipeline

# Load data hasil preprocessing
df = pd.read_csv("data/comments_clean.csv")

# Load model sentiment Bahasa Indonesia
sentiment_model = pipeline(
    "sentiment-analysis",
    model="w11wo/indonesian-roberta-base-sentiment-classifier"
)

# Fungsi analisis sentimen
def analyze_sentiment(text):
    try:
        result = sentiment_model(text[:512])[0]  # batasi panjang teks
        return result["label"]
    except:
        return "ERROR"

# Terapkan ke data
df["sentiment"] = df["clean_comment"].apply(analyze_sentiment)

# Simpan hasil
df.to_csv("data/comments_sentiment.csv", index=False)

print("Analisis sentimen selesai! File comments_sentiment.csv dibuat.")
