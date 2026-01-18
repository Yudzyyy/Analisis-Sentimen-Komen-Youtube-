import pandas as pd
import re

# Load data
df = pd.read_csv("data/comments.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)       # hapus URL
    text = re.sub(r"[^a-zA-Z\s]", "", text)   # hapus simbol & angka
    text = re.sub(r"\s+", " ", text).strip() # rapikan spasi
    return text

df["clean_comment"] = df["comment"].apply(clean_text)

# Simpan hasil
df.to_csv("data/comments_clean.csv", index=False)

print("Preprocessing selesai! File comments_clean.csv dibuat.")
