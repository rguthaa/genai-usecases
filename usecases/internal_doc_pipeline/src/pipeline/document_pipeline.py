# pipeline/document_pipeline.py
import hashlib
from preprocessing.markdown_cleaner import MarkdownPreprocessor
from loader.document_loader import DocumentLoader
from embedding.embedding_manager import EmbeddingManager
from summarizer.search_and_summarize import DocumentSearchSummarizer

class InternalDocPipeline:
    def __init__(self, doc_paths, embedding_dir, embedding_model_type: str ="openai", llm_model_type="openai"):
        self.doc_paths = doc_paths
        self.embedding_dir = embedding_dir
        self.markdown_cleaner = MarkdownPreprocessor()
        self.loader = DocumentLoader(self.markdown_cleaner)
        self.embedder = EmbeddingManager(model_type=embedding_model_type)
        self.summarizer = DocumentSearchSummarizer(self.embedder)

    def _hash_content(self, content: str) -> str:
        return hashlib.md5(content.encode("utf-8")).hexdigest()

    def build_vectorstore(self):
        all_docs = []
        seen_hashes = set()

        for path in self.doc_paths:
            try:
                if path.endswith(".md"):
                    docs = self.loader.load_markdown_file(path)
                elif path.endswith(".html"):
                    docs = self.loader.load_html_file(path)
                else:
                    continue

                for doc in docs:
                    content = doc.page_content.strip()
                    if not content:
                        print(f"Skipped empty document from: {doc.metadata.get('source')}")
                        continue

                    content_hash = self._hash_content(content)
                    if content_hash not in seen_hashes:
                        seen_hashes.add(content_hash)
                        all_docs.append(doc)
            except Exception as e:
                print(f"Skipped {path}: {e}")

        if not all_docs:
            raise ValueError("No valid, unique documents to embed.")

        self.embedder.save_embeddings(all_docs, self.embedding_dir)

    def query(self, question: str) -> str:
        self.embedder.load_vectorstore(self.embedding_dir)

        docs = self.embedder.similarity_search(question)
        seen_sources = set()
        unique_docs = []

        for doc in docs:
            source = doc.metadata.get("source")
            if source and source not in seen_sources:
                seen_sources.add(source)
                unique_docs.append(doc)

        return self.summarizer.summarize(question, unique_docs)
