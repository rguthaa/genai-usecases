# loader/document_loader.py
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter, HTMLHeaderTextSplitter
from langchain.schema import Document

class DocumentLoader:
    def __init__(self, markdown_cleaner):
        self.markdown_cleaner = markdown_cleaner
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    def load_markdown_file(self, file_path: str) -> List[Document]:
        with open(file_path, 'r') as file:
            raw_text = file.read()
        cleaned_text = self.markdown_cleaner.clean(raw_text)
        docs = self.splitter.create_documents([cleaned_text], metadatas=[{"source": file_path}])
        return docs

    def load_html_file(self, file_path: str) -> List[Document]:
        with open(file_path, 'r') as file:
            raw_html = file.read()
        headers_to_split_on = [("h1", "Section"), ("h2", "Subsection"), ("h3", "Detail")]
        html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
        return html_splitter.split_text(raw_html)
