from langchain_google_vertexai import ChatVertexAI
from langchain.prompts import PromptTemplate

# 1. Create a prompt template with a variable
prompt = PromptTemplate.from_template("Give me 3 fun facts about {topic}")

# 2. Load the Gemini model from Vertex AI
llm = ChatVertexAI(
    model_name="gemini-2.0-flash-001",  # You can also try gemini-pro
    temperature=0.7
)

# 3. Create a chain using Runnable-style composition
chain = prompt | llm

# 4. Invoke the chain with structured input
response = chain.invoke({"topic": "How USA was formed?"})

# 5. Print the LLM response
print(response.content)  # .content because it's a ChatMessage
