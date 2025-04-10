
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

input_text = """
Artificial Intelligence (AI) is rapidly transforming the landscape of education...
"""

summary = summarizer(input_text, max_length=80, min_length=30, do_sample=False)

print("\n🔹 Original Text:\n", input_text)
print("\n🔹 Summary:\n", summary[0]['summary_text'])
