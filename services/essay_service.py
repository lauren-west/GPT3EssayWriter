import os
import openai

# authentication
openai.organization = "org-4NKqHPrsBbd1Yi3HVZP1cZr2"
openai.api_key = os.getenv("OPENAI_API_KEY")

essay_engine_id = 'text-davinci-002'

prompt = input("Prompt for the essay, with desired length and outline specified:\n")

result = openai.Completion.create(
  engine=essay_engine_id,
  prompt=prompt,
  max_tokens=200
)

essay = result["choices"][0]["text"]

prompt2 = "What letter grade do you think this essay will get?\n" + essay

result = openai.Completion.create(
  engine=essay_engine_id,
  prompt=prompt2,
  max_tokens=200
)
print(result["choices"][0]["text"])
print()
print(essay)







