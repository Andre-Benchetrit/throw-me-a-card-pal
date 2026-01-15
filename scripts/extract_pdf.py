import fitz
import json
from pathlib import Path
from tqdm import tqdm
import re

PDF_PATH = Path("data/Sacramento-RPG-Livro-Basico.pdf")
OUTPUT_PATH = Path("data/pages.json")

def remove_duplicate_chars(text):
    return re.sub(r'(.)\1+', r'\1', text)

def extract_pages():
    doc = fitz.open(PDF_PATH)
    pages_data = []

    for page_num in tqdm(range(len(doc)), desc="Extraindo páginas"):
        page = doc.load_page(page_num)
        text = page.get_text("text")

        text = text.replace("\n", " ")
        text = remove_duplicate_chars(text)
        text = re.sub(r'\s+', ' ', text).strip()

        if len(text) < 50:
            continue

        pages_data.append({
            "page": page_num + 1,
            "text": text
        })

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, ensure_ascii=False, indent=2)

    print(f"\nExtraídas {len(pages_data)} páginas para {OUTPUT_PATH}")

if __name__ == "__main__":
    extract_pages()
