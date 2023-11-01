import pandas as pd
df = pd.read_csv("sample.csv")
df.head(10)

list  = []

for i in df["name"]:
    if i["name"] == "Adarsh":
        list.append(i)


def clean_text(text):
    # Remove punctuation
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])
    # Convert to lowercase
    text = text.lower()
    # Tokenize into words
    words = text.split()
    return words

# Sample text
sample_text = "This is an example text, with some punctuation marks and UPPERCASE words!"
cleaned_words = clean_text(sample_text)
print(cleaned_words)
