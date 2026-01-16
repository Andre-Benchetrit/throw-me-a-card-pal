import os
import re
import json
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash-lite")

def safe_parse_scores(text):
    match = re.search(r"\[[\d\.,\s]+\]", text)
    if not match:
        raise ValueError("Nenhum array encontrado")
    return json.loads(match.group(0).replace(",", ","))


def rerank(query: str, candidates: list[dict]) -> list[dict]:
    if not candidates:
        return candidates

    prompt = f"""
Você é um sistema de busca semântica.

Avalie o quão relevante cada trecho é para a consulta do usuário.
Dê uma nota de 0.0 a 1.0 para cada trecho, na MESMA ordem.

Consulta:
{query}

Trechos:
""" + "\n".join(
        f"{i+1}. {c['text'][:300]}"
        for i, c in enumerate(candidates)
    ) + """

Responda APENAS com um array JSON válido.
Não escreva texto antes ou depois.
Não use explicações.
Somente números.

Formato exato esperado:
[0.1, 0.9, 0.3]
"""

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.0,
            "max_output_tokens": 200,
        }
    )


    try:
        scores = safe_parse_scores(response.text)
    except Exception:
        # fallback: não rerankeia
        return candidates

    for c, score in zip(candidates, scores):
        c["rerank_score"] = float(score)

    return sorted(candidates, key=lambda x: x["rerank_score"], reverse=True)
