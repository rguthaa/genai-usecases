import re

class MarkdownPreprocessor:
    def clean(self, text: str) -> str:
        text = re.sub(r'^#+\\s*', 'Section: ', text, flags=re.MULTILINE)
        text = re.sub(r'[*_`]+', '', text)
        text = re.sub(r'\\[(.*?)\\]\\(.*?\\)', r'\\1', text)
        text = re.sub(r'^\\s*[-*+]\\s+', '- ', text, flags=re.MULTILINE)
        text = re.sub(r'^\\s*\\d+\\.\\s+', '- ', text, flags=re.MULTILINE)
        text = re.sub(r'\\n{2,}', '\\n\\n', text)
        return text.strip()