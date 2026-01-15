from core.vector_search import search
from core.gemini import client, model

SYSTEM_PROMPT = """
Você é um assistente cowboy que responde dúvidas sobre regras do RPG Sacramento.
Responda APENAS com base no contexto fornecido, mas explicando a regra e condições.
Responda com um sotaque de cowboy.
Se a resposta não estiver no contexto, diga que não encontrou no livro.
Sempre cite o número da página ao final. Seja educado.
"""

def answer_question(question):
    results = search(question)

    if not results:
        return "Não encontrei essa regra no livro."

    context = ""
    for r in results:
        context += f"[Página {r['page']}]: {r['text']}\n\n"

    prompt = f"""
{SYSTEM_PROMPT}

Contexto:
{context}

Pergunta: {question}

Resposta:
"""

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text.strip()
