from bardapi import Bard
import os

os.environ['_BARD_API_KEY'] = "fAj2B1hbkVjk9Go5UpcpDeKOzUd7psxijqjKVd1M0PJgWl5VE9LlZs1XmzJSNORl5iTIXw."

input_text = "Qual o melhor modelo LLM do mercado? Bard ou ChatGPT?"


bard_output = Bard().get_answer(input_text)['content']
print(bard_output)
