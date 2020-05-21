from lxml import html, etree
import requests

page = requests.get("http://www.howtowebscrape.com/examples/simplescrape1.html")

extractedHtml = html.fromstring(page.content)
bookTitle = extractedHtml.xpath("/html/body/center/h1")
print(bookTitle[0].text)

author = extractedHtml.xpath("//span[@id='author']")
print(author[0].text)

image = extractedHtml.xpath("//img/@src")
print(image)

bookData = extractedHtml.xpath("//*/td[2]/p[1]/font")
print(bookData[0].text)
