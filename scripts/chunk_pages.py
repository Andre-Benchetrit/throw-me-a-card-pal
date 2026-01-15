import json
from pathlib import Path

PAGES_PATH = Path("data/pages.json")
CHUNKS_PATH = Path("data/chunks.json")

CHUNK_SIZE = 500
OVERLAP = 100

def chunk_text(text):
    chunks = []
    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start += CHUNK_SIZE - OVERLAP

    return chunks

def build_chunks():
    with open(PAGES_PATH, encoding="utf-8") as f:
        pages = json.load(f)

    all_chunks = []
    chunk_id = 0

    for page in pages:
        page_num = page["page"]
        text = page["text"]

        for chunk in chunk_text(text):
            if len(chunk.strip()) < 100:
                continue

            chunk_id += 1
            all_chunks.append({
                "id": chunk_id,
                "page": page_num,
                "text": chunk.strip()
            })

    CHUNKS_PATH.parent.mkdir(exist_ok=True)
    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    print(f"Gerados {len(all_chunks)} chunks em {CHUNKS_PATH}")

if __name__ == "__main__":
    build_chunks()
