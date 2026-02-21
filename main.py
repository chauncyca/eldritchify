
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

import eldritchify

def getTextFromWeb(url:str):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    outStr = eldritchify.curseText(''.join(getTextFromWeb(sys.argv[1])))
    print(''.join(outStr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
