"""
Local AI Interface using Ollama + Mistral
"""

import ollama
from typing import Optional


def ask_ai(question: str, context: Optional[str] = None) -> str:
    if context:
        full_prompt = f"""Context: {context}

Question: {question}

Answer based on the context provided:"""
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
    context = "MedSave helps users save money on medicines."
    answer = ask_ai("What does MedSave do?", context=context)
    print(f"A: {answer}")
