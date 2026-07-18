import anthropic
from dotenv import load_dotenv
import os
import sqlite3
conn = sqlite3.connect("pipeline_results.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM expression_results")
results = str(cursor.fetchall())

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=api_key)

response_agent1 = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Analyze these gene exprtession results: " + results}
    ]
)

agent1answer = (response_agent1.content[0].text)

response_agent2 = client.messages.create(
    model = "claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role":"user", "content": "write a 1 paragraph report on the data from the infomration" + agent1answer}
    ]
)
print(response_agent2.content[0].text)