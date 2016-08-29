from urllib import request
from bs4 import BeautifulSoup as bs
import lxml, subprocess

class Lyrics():
  def __init__(self):
    self.word = ""

  def getHTML(self, url):
    domain = url.split("/")[2]
    self.html = bs(request.urlopen(url), "lxml")

    return domain

  def parolesNet(self):
    lyrics = self.html.find("div", class_="song-text")
    lyrics.find("script").extract()
    lyrics = lyrics.get_text()
    
    return lyrics

  def metroLyricsCom(self):
    lyrics = self.html.find("div", class_="js-lyric-text")
    lyrics = lyrics.get_text()
    
    return lyrics

  def toWordsCSV(self, lyrics):
    words = lyrics.split()
    title = input("Please input the title:")

    subprocess.call(["mkdir", "-p", "result"])
    words_csv = open("result/"+title+".csv", "w", encoding="utf-8")
    for i in range(len(words)):
      words[i] = words[i].replace('"', "")
      words[i] = words[i].replace('(', "")
      words[i] = words[i].replace(')', "")
      words[i] = words[i].replace(',', "")
      words[i] = words[i].replace('.', "")
      words[i] = words[i].replace('!', "")
      words[i] = words[i].replace('?', "")
      words[i] = words[i].replace(":", "")
      words[i] = words[i].replace(";", "")
      words_csv.write(words[i]+"\n")
    words_csv.close()

def main():
  obj = Lyrics()

  url = input("Please input URL:\n")
  domain = obj.getHTML(url)

  if domain == "www.paroles.net":
    lyrics = obj.parolesNet()
  
  elif domain == "www.metrolyrics.com":
    lyrics = obj.metroLyricsCom()

  else:
    print("The website is not supported.")

  obj.toWordsCSV(lyrics)

if __name__ == "__main__":
  main()
