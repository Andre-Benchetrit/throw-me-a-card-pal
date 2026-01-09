import re
import random
from core.config import MAX_DICE, MAX_FACES

TERM_PATTERN = re.compile(r"[+-]?\s*[^+-]+")

DICE_TERM_PATTERN = re.compile(
    r"""
    (\d+)              
    d
    (\d+)              
    \s*
    (k[hl](\d+)?)?     
    """,
    re.VERBOSE | re.IGNORECASE
)

async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if not content.startswith("!"):
        return

    expr = content[1:].strip()

    terms = TERM_PATTERN.findall(expr)
    if not terms:
        return

    total = 0
    detalhes = []

    for term in terms:
        term = term.strip()

        sign = -1 if term.startswith("-") else 1

        clean = term.lstrip("+-").strip()

        match = DICE_TERM_PATTERN.fullmatch(clean)

        if match:
            qtd, faces, keep_raw, keep_n = match.groups()
            qtd = int(qtd)
            faces = int(faces)

            if qtd > MAX_DICE:
                await message.reply(
                    f"⚠️ Máximo de dados permitido: {MAX_DICE}",
                    mention_author=False
                )
                return

            if faces > MAX_FACES:
                await message.reply(
                    f"⚠️ Máximo de faces permitido: {MAX_FACES}",
                    mention_author=False
                )
                return

            resultados = [random.randint(1, faces) for _ in range(qtd)]
            usados = resultados.copy()

            if keep_raw:
                keep_type = keep_raw[:2]  # kh ou kl
                keep_count = int(keep_n) if keep_n else 1

                if keep_count > qtd:
                    await message.reply(
                        "⚠️ Não dá pra manter mais dados do que foram rolados.",
                        mention_author=False
                    )
                    return

                resultados_ordenados = sorted(
                    resultados,
                    reverse=(keep_type == "kh")
                )

                usados = resultados_ordenados[:keep_count]

            subtotal = sum(usados) * sign
            total += subtotal

            detalhes.append(
                f"{term} → {resultados} → {subtotal}"
            )

        else:
            try:
                valor = int(clean) * sign
            except ValueError:
                return

            total += valor
            detalhes.append(f"{term} → {valor}")

    await message.reply(
        "🎲 **Rolagem de dados**\n"
        + "\n".join(detalhes)
        + f"\n\n**Total: {total}**",
        mention_author=False
    )
