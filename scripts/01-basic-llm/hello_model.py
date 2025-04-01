from langchain_google_vertexai import ChatVertexAI
from langchain.prompts import PromptTemplate
#from langchain.output_parsers import StrOutputParser

# 1. Create prompt
prompt = PromptTemplate.from_template("Hi Gemini !!!")

# 2. Use Gemini Vertex AI Model (Automatically uses ADC credentials if available)
llm = ChatVertexAI(
    model_name="gemini-2.0-flash-001",
    temperature=1
)

response = llm.invoke(prompt.format())
print(response.content)