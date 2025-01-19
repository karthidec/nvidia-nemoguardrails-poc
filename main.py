from nemoguardrails import RailsConfig
from nemoguardrails import LLMRails
from langchain_huggingface import HuggingFaceEndpoint

config = RailsConfig.from_path("./config")

rails = LLMRails(config)

response = rails.generate(messages=[{
    "role": "user",
    "content": "learn llm"
}])

print(response)
