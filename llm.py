"""
Local AI Interface using Ollama + Mistral
Now with RAG (Retrieval Augmented Generation)
"""

import ollama
from typing import Optional


def ask_ai(question: str, context: Optional[str] = None) -> str:
    if context:
        full_prompt = f"""You are a helpful medical assistant.
Use ONLY the context below to answer the question.
If the answer is not in the context, say "Information not available in my database."
Do NOT make up information.

Context:
{context}

Question: {question}

Answer:"""
    else:
        full_prompt = question

    try:
        response = ollama.chat(
            model='mistral',
            messages=[{'role': 'user', 'content': full_prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("🤖 Testing Local AI...\n")

    print("=" * 60)
    print("Test 1: Simple Question")
    print("=" * 60)
    answer = ask_ai("What is AI in one sentence?")
    print(f"A: {answer}\n")

    print("=" * 60)
    print("Test 2: With Context")
    print("=" * 60)
    context = "Paracetamol 500mg is used for fever. Price: Rs 10. Brand: Crocin."
    answer = ask_ai("What is paracetamol used for?", context=context)
    print(f"A: {answer}")