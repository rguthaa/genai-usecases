# GenAI Use Cases

This repository contains practical Generative AI (GenAI) projects and pipelines for real-world use cases.

- Each folder in `/usecases` is a standalone use case, complete with code, setup instructions, and documentation.
- The `/examples` folder contains sample programs I created to learn and experiment with technologies like LangChain.

## 1. Project Overview

This repository showcases multiple Generative AI use cases.

**Current example:**
- **Internal Documentation RAG Pipeline:**
  - Ingests and cleans Markdown/HTML documentation
  - Generates text embeddings (OpenAI or HuggingFace)
  - Stores and searches embeddings in ChromaDB
  - Retrieves and summarizes content with LLMs using LangChain

More use cases will be added over time.

## 2. How to Run the Internal Doc Jupyter Notebook

### A. Clone the Repository
```bash
git clone https://github.com/rguthaa/genai-usecases.git
cd genai-usecases/usecases/internal_doc_pipeline
```

### B. Launch Jupyter Notebook
```bash
cd notebooks
jupyter notebook
```

### C. Environment Setup

- The first cell in each notebook runs the setup script for you.
- If you run it manually, you must specify the model provider (`OpenAI`, `VertexAI`, etc):

```bash
# For OpenAI
bash setup.sh OpenAI

# For Google Vertex AI
bash setup.sh VertexAI
```

- The setup script will automatically call the appropriate provider-specific setup (like `vertex_ai_setup.sh`) based on the argument you provide.

### D. Follow the Notebook
Step through the cells to load data, clean, embed, search, and generate LLM-based answers.

## 3. How to Run the Internal Doc Pipeline as a Python Project

### A. Clone the Repository (if not already done)
```bash
git clone https://github.com/rguthaa/genai-usecases.git
cd genai-usecases/usecases/internal_doc_pipeline
```

### B. Setup Environment
```bash
bash setup.sh OpenAI      # or VertexAI, depending on your provider
```

### C. (Optional) Google Vertex AI Setup
If you use Vertex AI, the setup script will handle this step for you.

### D. Run the Pipeline
```bash
cd src
python main.py
```
The script will process the docs, create embeddings, run retrieval, and summarize with your chosen LLM.

## Environment Variables

You must configure environment variables for API keys and service credentials.
A `.env.example` file is provided in the repo root.

### To use it:

1. **Copy `.env.example` to `.env`** in the root directory:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env`** and fill in your actual keys/paths, for example:
   ```
   OPENAI_API_KEY=your-openai-api-key
   ```

3. **Do NOT commit your `.env` file to git.**
   `.gitignore` includes `.env` for your safety.

## Directory Structure

usecases/
  internal_doc_pipeline/
    notebooks/         # Jupyter notebooks for experimentation
    src/               # Core Python source code for the pipeline
    setup.sh           # Main setup script (pass model provider as argument)
    vertex_ai_setup.sh # GCP/Vertex AI setup (called as needed)
  examples/
    ...                # Sample programs, LangChain experiments, etc.
  # Other usecase folders may be added in the future

## Requirements

- Python 3.9+
- (Optional) Google Cloud CLI for Vertex AI workflows
- OpenAI API key and/or HuggingFace token (for embeddings)
- `.env` file with your API keys and credentials (see above)

## More Information

- [Related Medium Article: RAG Pipeline for Summarizing Internal Documentation](https://medium.com/@rgutha/rag-pipeline-for-summarizing-internal-documentation-using-langchain-303159300e63)

## Contributing and Questions

Questions, issues, and pull requests are welcome.
If you are experimenting with similar GenAI pipelines, feel free to fork, extend, or reach out via the Issues tab.
