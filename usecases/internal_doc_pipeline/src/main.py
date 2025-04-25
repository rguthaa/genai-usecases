# internal_doc_pipeline/main.py
from pipeline.document_pipeline import InternalDocPipeline
from pathlib import Path
import sys
import os

ALLOWED_MODELS = ["openai", "huggingface"]

def get_project_root():
    return Path(__file__).resolve().parents[3]

def embeddings_exist(model):
    return os.path.exists(f"/tmp/{model}_embeddings") and len(os.listdir(f"/tmp/{model}_embeddings")) > 0

if __name__ == "__main__":
    print("Select an operation:")
    print("[1] Build vector store")
    print("[2] Query")

    selection = input("Enter 1 or 2: ").strip()

    if selection not in ("1", "2"):
        print("❌ Invalid selection. Please enter 1 or 2.")
        sys.exit(1)

    # Automatically find root of project relative to main.py
    project_root = get_project_root()
    data_dir = project_root / "data"

    doc_paths = []
    for folder in [data_dir / "confluence", data_dir / "proprofs"]:
        for ext in ("*.md", "*.html"):
            for path in folder.rglob(ext):
                doc_paths.append(str(path))

    if selection == '1':
        print("Choose embedding model:")
        print(" - openai")
        print(" - huggingface")
        model = input("Enter embedding model (openai/huggingface): ").strip().lower()
        if model not in ALLOWED_MODELS:
            print(f"❌ Invalid embedding model. Allowed: {ALLOWED_MODELS}")
            sys.exit(1)
        embedding_dir = f"/tmp/{model}_embeddings"
        pipeline = InternalDocPipeline(
            doc_paths=doc_paths,
            embedding_dir=embedding_dir,
            embedding_model_type=model
        )
        try:
            pipeline.build_vectorstore()
            print("✅ Vector store built successfully.")
        except ValueError as e:
            print(f"❌ Failed to build vectorstore: {e}")
            sys.exit(1)

    elif selection == '2':
        question = input("Enter your question: ").strip()

        # Check if any embedding model's vector store exists
        existing_models = [m for m in ALLOWED_MODELS if embeddings_exist(m)]
        if existing_models:
            # Use the first found embedding model/vector store
            model = existing_models[0]
            print(f"Auto-detected existing embedding model: {model}")
        else:
            print("No existing vector store found. Please build one first.")
            sys.exit(1)

        embedding_dir = f"/tmp/{model}_embeddings"
        pipeline = InternalDocPipeline(
            doc_paths=doc_paths,
            embedding_dir=embedding_dir,
            embedding_model_type=model,
            llm_model_type="openai"  # Or make this configurable if you wish
        )
        response = pipeline.query(question)
        print("\n=== GenAI Response ===")
        print(response.content)
