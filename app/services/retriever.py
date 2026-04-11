from app.services.embeddings import load_data, build_index, retrieve


# Initialize on first import
def initialize():
    """Load data and build search index"""
    load_data()
    build_index()
    print("✅ Retriever ready!")


def get_context(query, top_k=3):
    """
    Takes user question → returns relevant context string
    This context will be fed to Mistral
    """
    results = retrieve(query, top_k)

    if not results:
        return "No relevant information found."

    # Join results into one context block
    context = "\n".join(results)
    return context


# === QUICK TEST ===
if __name__ == "__main__":
    initialize()

    print("\n" + "=" * 50)
    query = "What medicine for fever?"
    print(f"❓ Query: {query}")
    print(f"📄 Context:\n{get_context(query)}")

    print("\n" + "=" * 50)
    query = "Which is the cheapest medicine?"
    print(f"❓ Query: {query}")
    print(f"📄 Context:\n{get_context(query)}")

    print("\n" + "=" * 50)
    query = "medicine for diabetes"
    print(f"❓ Query: {query}")
    print(f"📄 Context:\n{get_context(query)}")