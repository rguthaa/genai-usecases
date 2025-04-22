# summarizer/search_and_summarize.py
from typing import List
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class DocumentSearchSummarizer:
    def __init__(self, embedding_manager):
        self.embedding_manager = embedding_manager
        self.llm = ChatOpenAI(temperature=0.2)

    def summarize(self, query: str, context_docs: List[Document]) -> str:
        unique_docs = []
        for doc in context_docs:
            unique_docs.append(doc)
                
        context = "\n".join([doc.page_content for doc in unique_docs])

        #print('context', context)

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are an AI assistant summarizing internal documentation as points, just summarize based on the context provided. If the context is empty then return string Nothing found"),
            ("human", "Context:\n{context}"),
            ("human", "Question: {question}")
        ])
        chain = prompt_template | self.llm
        return chain.invoke({"context": context, "question": query})
