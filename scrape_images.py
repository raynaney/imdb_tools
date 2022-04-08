import sys
import re
import requests 
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 

def createHTMLFile(body):
    # to open/create a new html file in the write mode
    f = open('shoplinks.html', 'w')
    
    # the html code which will go in the file GFG.html
    html_open = """
    <!doctype html>
    <html lang="en">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

        <html>
        <head>
            <title>ShopLinks</title>
            <meta name="place to store products, prices, in visually pleasing way" content="images and links">
            <meta name="Rayna Ney">
            <link rel="icon" href="/favicon.ico">
            <link rel="icon" href="/favicon.svg" type="image/svg+xml">
            <link rel="apple-touch-icon" href="/apple-touch-icon.png">
            <link rel="stylesheet" href="css/reset.css">
            <link rel="stylesheet" href="css/styles.css?v=1.0">
            
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Shrikhand&display=swap');  
                @import url('https://fonts.googleapis.com/css2?family=Chivo:ital,wght@0,300;0,400;0,700;1,300;1,400&display=swap');
            </style>

        </head>
    """
    html_body_open = """
     <body>
        <h1>ShopLinks</h1>
        <div class="gallery-images-container"> 
            <h3 id = "directions"> Choose an image for the link thumbnail</h3>
         """
    
    html_body_close = """</div></body>"""

    html_close = """ 
        <footer></footer> </html>
        """

    # writing the code into the file
    f.write(html_open+html_body_open+body+html_body_close+html_close) #todo replace by a list and join 
    
    # close the file
    f.close()

def main():
# Make sure a URL is passed through the command line
    image_url_list = []
    if len(sys.argv) == 1:
        print("USAGE:", sys.argv[0], "[www.SomeLink.com]")
        sys.exit(1)
    if "http" in str(sys.argv[1]):


        url = sys.argv[1]
        string_array = url.split('/')
        product_id = string_array[-1]
        htmldata = getdata(url) 
        soup = BeautifulSoup(htmldata, 'html.parser') 


        for item in soup.findAll('img',{"src":True}): #for all images on webpage
            if(product_id in item['src'] and not (".png" in item['src'])): #if the source contains the product ID, (which is found at the end of the URL), add these to the HTML
                image_url_list.append(""" <div class="gallery-image item"> """ + """ <img src= """ + item['src'] + """></div> """)

        if len(image_url_list) == 0: #if there are no matches for a product ID, then add all images
            for item in soup.findAll('img',{"src":True}):
                if not ".png" in item['src']:
                    image_url_list.append(""" <div class="gallery-image item"> """ + """ <img src= """ + item['src'] + """></div> """)

        if len(image_url_list) == 0: #if the list is still empty, allow .png file types
            for item in soup.findAll('img',{"src":True}):
                image_url_list.append(""" <div class="gallery-image item"> """ + """ <img src= """ + item['src'] + """></div> """)

        ##TODO: weed out any image sources that include the words 'logo'

        body = ''.join(image_url_list)

    else:
        print("malformed URL: "+url)
    createHTMLFile(body)

if __name__ == "__main__":
    main()