import json
import sqlite3
from pathlib import Path
from sentence_transformers import SentenceTransformer
import numpy as np
from tqdm import tqdm

CHUNKS_PATH = Path("data/chunks.json")
DB_PATH = Path("data/embeddings.db")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def build_database():
    print("Carregando modelo de embeddings...")
    model = SentenceTransformer(MODEL_NAME)

    print("Carregando chunks...")
    with open(CHUNKS_PATH, encoding="utf-8") as f:
        chunks = json.load(f)

    print("Criando banco SQLite...")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY,
            page INTEGER,
            text TEXT,
            embedding BLOB
        )
    """)

    print("Gerando embeddings...")
    for chunk in tqdm(chunks, desc="Processando chunks"):
        text = chunk["text"]
        embedding = model.encode(text)

        embedding_blob = embedding.astype(np.float32).tobytes()

        cur.execute(
            "INSERT INTO chunks (id, page, text, embedding) VALUES (?, ?, ?, ?)",
            (chunk["id"], chunk["page"], text, embedding_blob)
        )

    conn.commit()
    conn.close()
    print(f"\nBanco criado em {DB_PATH}")

if __name__ == "__main__":
    build_database()
