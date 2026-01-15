import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer
from core.config import STOPWORDS

DB_PATH = "data/embeddings.db"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def search_vector(query_embedding, top_k=8):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT text, page, embedding FROM chunks")
    rows = cursor.fetchall()
    conn.close()

    results = []
    for text, page, emb_blob in rows:
        emb = np.frombuffer(emb_blob, dtype=np.float32)
        score = cosine_similarity(query_embedding, emb)
        results.append({
            "text": text,
            "page": page,
            "score": float(score)
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]


def search_keywords(keywords, limit_per_word=2):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    results = []

    for word in keywords:
        word = word.lower().strip()

        if len(word) < 3:
            continue

        if word in STOPWORDS:
            continue

        cursor.execute(
            "SELECT text, page FROM chunks WHERE lower(text) LIKE ? LIMIT ?",
            (f"%{word}%", limit_per_word)
        )

        for text, page in cursor.fetchall():
            results.append({
                "text": text,
                "page": page,
                "score": 0.15
            })

    conn.close()
    return results



def search(query, top_k=8):
    query_embedding = model.encode(query)

    vector_results = search_vector(query_embedding, top_k)
    keywords = query.lower().split()
    keyword_results = search_keywords(keywords)

    combined = {}

    for r in vector_results:
        combined[r["text"]] = r

    for r in keyword_results:
        if r["text"] not in combined:
            combined[r["text"]] = r
        else:
            combined[r["text"]]["score"] += r["score"]

    final_results = list(combined.values())
    final_results.sort(key=lambda x: x["score"], reverse=True)

    return final_results[:top_k]
