from googleapiclient.discovery import build
import pandas as pd

# API key kamu
API_KEY = "AIzaSyCTkAQo6hWmQet27SN82Zhx_L4tVN64eDI"

# Video ID dari link kamu
VIDEO_ID = "PxSBNOLJzL8"

youtube = build("youtube", "v3", developerKey=API_KEY)

comments = []
next_page_token = None

while True:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=VIDEO_ID,
        maxResults=100,
        textFormat="plainText",
        pageToken=next_page_token
    )
    response = request.execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    next_page_token = response.get("nextPageToken")
    if not next_page_token:
        break

df = pd.DataFrame(comments, columns=["comment"])
df.to_csv("data/comments.csv", index=False)

print(f"Selesai! Total komentar diambil: {len(comments)}")
