# Nube de palabras

import wikipedia
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def plotCloud(wordCloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordCloud)
    plt.axis("off")


if __name__ == '__main__':
    print("ingrese el titulo del articulo de wikipedia del que desea obterner el resultado")
    word = input()
    if (word == ""):
        word = "GNU/Linux"
    else:
        pass

    wiki = wikipedia.page(word)
    text = wiki.content
    # cleaning...
    text = re.sub(r'==.*?==+', '', text)
    text = text.replace('\n', '')

    wordCloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
    plotCloud(wordCloud)
    wordCloud.to_file("wordcloud.png")
