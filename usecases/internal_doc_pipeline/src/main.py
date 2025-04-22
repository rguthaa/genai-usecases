# internal_doc_pipeline/main.py
from pipeline.document_pipeline import InternalDocPipeline
from pathlib import Path
import sys
import hashlib

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("❌ Usage: python main.py '<selection: [1] for build vector store and [2] for asking a question>' '<your question>'")
        sys.exit(1)

    selection = sys.argv[1]
    question = sys.argv[2]

    # Automatically find root of project relative to main.py
    project_root = Path(__file__).resolve().parents[3]
    data_dir = project_root / "data"

    doc_paths = []
    for folder in [data_dir / "confluence", data_dir / "proprofs"]:
        for ext in ("*.md", "*.html"):
            for path in folder.rglob(ext):
                doc_paths.append(str(path))

    pipeline = InternalDocPipeline(
        doc_paths=doc_paths,
        embedding_dir="/tmp/internal_doc_embeddings",
        model_type="openai"
    )

    if selection == '1':
        # Run only when needed
        try:
            pipeline.build_vectorstore()
        except ValueError as e:
            print(f"❌ Failed to build vectorstore: {e}")
            sys.exit(1)
    elif selection == '2':
        response = pipeline.query(question)
        print(response.content)
