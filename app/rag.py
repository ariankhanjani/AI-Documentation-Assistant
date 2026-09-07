from app.llm import create_llm


def generate_answer(llm, question, context):
    prompt = f"""
You are a technical documentation assistant.

Use ONLY the information in the context below.

If the answer is explicitly present in the context, answer with the relevant
information only.

If the answer is not present in the context, reply exactly:
I don't know based on the provided documentation.

Do not add information from your general knowledge.
Do not invent steps, commands, URLs, or instructions.
Keep the answer concise.

Context:
{context}

Question:
{question}

Answer:
"""

    return llm.invoke(prompt)
