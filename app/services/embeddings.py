from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model (runs locally, no API needed)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Storage
chunks = []
index = None


def load_data(file_path="data/med_data.txt"):
    """Read text file and split into chunks (each line = 1 chunk)"""
    global chunks
    with open(file_path, "r") as f:
        chunks = [line.strip() for line in f.readlines() if line.strip()]
    print(f"✅ Loaded {len(chunks)} chunks")
    return chunks


def build_index():
    """Convert chunks to embeddings and store in FAISS"""
    global index
    if not chunks:
        print("❌ No chunks loaded. Run load_data() first.")
        return

    # Convert text to embeddings
    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    print(f"✅ FAISS index built with {index.ntotal} vectors")


def retrieve(query, top_k=3):
    """Search FAISS index and return top matching chunks"""
    if index is None:
        print("❌ Index not built. Run build_index() first.")
        return []

    # Convert query to embedding
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # Search
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(chunks):
            results.append(chunks[idx])

    return results


# === QUICK TEST ===
if __name__ == "__main__":
    load_data()
    build_index()

    print("\n🔍 Testing: 'fever medicine'")
    results = retrieve("fever medicine")
    for r in results:
        print(f"  → {r}")

    print("\n🔍 Testing: 'cheapest medicine'")
    results = retrieve("cheapest medicine")
    for r in results:
        print(f"  → {r}")

    print("\n🔍 Testing: 'antibiotic for infection'")
    results = retrieve("antibiotic for infection")
    for r in results:
        print(f"  → {r}")