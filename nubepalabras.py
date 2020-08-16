from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def generar_imagen(palabras , custom_mask, background = "black"):
    c_mask = np.array(Image.open(custom_mask))
    wc = WordCloud(background_color = background,  mask = c_mask)
    wc.generate(palabras)
    plt.imshow(wc, interpolation = "bilinear")
    plt.axis("off")
    plt.show()



