#  TEXT SUMMARIZATION TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: Mohith B

*INTERN ID*: CT06WRL

*DOMAIN*: Artificial intelligence 

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

TASK 1

#OBJECTIVE

The goal of Task 1 was to build a Text Summarization Tool using Natural Language Processing (NLP) techniques. The tool should be able to analyze a long piece of text and return a concise, meaningful summary — similar to how a human might condense a paragraph or an article into a few lines.

#WHAT IS THE TOOL WE CREATED?

We developed an AI-powered text summarizer using a pre-trained transformer model from Hugging Face's transformers library.

🔹 Functionality:
Takes a long-form article or paragraph as input.

Uses a pre-trained model to identify important context.

Returns a shortened version while preserving the original meaning.

🔹 Model Used:
We used the BART model (facebook/bart-large-cnn), a state-of-the-art model specifically fine-tuned for text summarization tasks. BART is known for its fluency and accuracy in generating human-like summaries.

🔹 Key Features:
Minimal code, powerful results (thanks to Hugging Face pipelines).

Works on a wide range of texts: news, essays, technical content.

Easily extendable to take input from files or a UI.

# Platform & Technology Stack

*Component	Details

Language:	Python

Libraries:	transformers (by Hugging Face), torch

Model:	facebook/bart-large-cnn (BART - Bidirectional and Auto-Regressive Transformer)

Execution:	Command-line script / Python environment

Runtime:	CPU or GPU (if available)

Development:	VS Code / Any Python IDE

# How the Tool Works (Behind the Scenes)
 
Input Handling: The tool accepts a paragraph of text from the user.

Text Preprocessing: Internally handled by the pipeline — tokenization, embedding, etc.

Model Inference: The BART model processes the input and identifies the most relevant parts of the text.

Text Generation: The model constructs a summary using natural-sounding language.

Output Display: The summary is printed to the screen (or optionally saved).
