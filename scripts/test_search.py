import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.vector_search import search

query = "Como sei quantas ações de combate tenho?"
results = search(query)

for r in results:
    print("\nPágina:", r["page"])
    print("Score:", round(r["score"], 3))
    print(r["text"][:300], "...")
