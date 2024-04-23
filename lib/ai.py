from g4f.client import Client
import g4f
import re

url_pattern = re.compile(r'https?://\S+|www\.\S+')

#Get response from GPT4
def gpt(input):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "You are a virtual workshop assistant called JARVIS, behave like the JARVIS from the iron man movies", "content": input }],
        provider = g4f.Provider.Bing
    )
    text = response.choices[0].message.content
    text = url_pattern.sub(" ", text.replace("*", ""))
    return text