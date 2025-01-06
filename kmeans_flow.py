# Import library yang diperlukan
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Membaca file chat
file_path = "_chat.txt"
with open(file_path, "r", encoding="utf-8") as file:
    chat_data = file.readlines()

# Fungsi untuk membersihkan data
def clean_chat_data(chat_lines):
    cleaned_data = []
    regex_pattern = r"^\[(.*?)\] (.*?): (.*)$"  # Pola: [timestamp] sender: message
    for line in chat_lines:
        match = re.match(regex_pattern, line)
        if match:
            timestamp, sender, message = match.groups()
            cleaned_data.append({
                "Timestamp": timestamp,
                "Sender": sender.strip(),
                "Message": message.strip()
            })
    return cleaned_data

# Membersihkan data
cleaned_chat = clean_chat_data(chat_data)
df_chat = pd.DataFrame(cleaned_chat)

# Memfilter pesan relevan
def filter_relevant_messages(df):
    system_messages_keywords = ["created this group", "added", "removed", "Messages and calls are end-to-end encrypted"]
    return df[~df["Message"].str.contains("|".join(system_messages_keywords), na=False)]

df_filtered_chat = filter_relevant_messages(df_chat)

# Menyimpan data ke CSV
df_filtered_chat.to_csv("data_group.csv", index=False, encoding="utf-8")

# Clustering dengan kMeans
# Menggunakan TF-IDF untuk mengubah teks menjadi fitur numerik
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df_filtered_chat["Message"])

# Menjalankan kMeans untuk 3 hingga 5 cluster
clusters_range = [3, 4, 5]
results = {}

for n_clusters in clusters_range:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)
    labels = kmeans.labels_
    df_filtered_chat[f"Cluster_{n_clusters}"] = labels
    results[n_clusters] = kmeans

# Menampilkan 3 kata teratas untuk setiap cluster
for n_clusters in clusters_range:
    print(f"\nTop terms per cluster (k={n_clusters}):")
    order_centroids = results[n_clusters].cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()
    for i in range(n_clusters):
        print(f"Cluster {i}: ", end="")
        print(", ".join(terms[ind] for ind in order_centroids[i, :3]))

# Menyimpan hasil clustering ke file CSV
df_filtered_chat.to_csv("data_group_with_clusters.csv", index=False, encoding="utf-8")

# Visualisasi (contoh dengan k=3)
kmeans_3 = results[3]
plt.scatter(X.toarray()[:, 0], X.toarray()[:, 1], c=kmeans_3.labels_, cmap="viridis")
plt.title("Clustering Visualization (k=3)")
plt.show()