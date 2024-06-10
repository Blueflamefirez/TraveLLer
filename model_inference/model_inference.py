import wikivoyage
import re

def remove_URL(text):
    """
    Remove URLs from a text string
    """
    return re.sub(r"\(http\S+", "", text)

res = wikivoyage.get("https://en.wikivoyage.org/wiki/Albania")

for i in res.sections:
    print(i.title, "\n")
    print(remove_URL(i.content))
