# LangChain Python Examples

This project contains simple Python examples for working with LangChain using either OpenAI or Google Vertex AI.

---

## Setup Steps

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-python-examples.git
cd langchain-python-examples
```

### 2. Create a .env file

```bash
cp .env.example .env
```

Edit the `.env` file and fill in your OpenAI API key or Google credentials.

### 3. Run the setup script

Choose which provider you want to use:

```bash
./setup.sh OpenAI
# or
./setup.sh VertexAI
```

If you're using a business-managed Google account, the script will prompt you to sign in with your Google credentials automatically.

---

## Running Examples

You can run Python examples like this:

```bash
python python-examples/decorator_example.py
python scripts/01-basic-llm/simple_llm_chain.py
```

---

## Notes

- Don’t share your `.env` file or service account key files.
- The `.env.example` file is provided so others can easily get started.
- Scripts automatically load the `.env` file if it exists.

---

## License

MIT License.
