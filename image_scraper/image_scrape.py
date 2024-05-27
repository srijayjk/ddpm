import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# Make directory for the images if it doesn't already exist
image_directory = "downloaded_images"
if not os.path.exists(image_directory):
    os.makedirs(image_directory)


# URL of the webpage to scrape
urls = [
    "https://www.bluestone.com/jewellery/plain+gold-earrings.html",
    "https://www.bluestone.com/jewellery/jhumka-earrings.html",
    "https://www.bluestone.com/jewellery/chand+bali.html",
    "https://www.bluestone.com/jewellery/filter/front+back.html",
    "https://www.bluestone.com/jewellery/hoops-earrings.html",
    "https://www.tanishq.co.in/shop/jhumka-earrings?lang=en_IN",
    "https://www.bluestone.com/jewellery/rings.html",
    "https://www.tanishq.co.in/shop/earring?lang=en_IN",
    "https://www.caratlane.com/jewellery/gold-earrings.html",
    "https://www.caratlane.com/jewellery/jhumkas-earrings.html",
    "https://www.caratlane.com/jewellery/chand+bali-earrings.html",
    "https://www.kalyanjewellers.net/Jewellery/Earrings/",
    "https://www.malabargoldanddiamonds.com/gold-jewellery/earring.html"
    "https://www.candere.com/jewellery/stud-earrings.html",
    "https://www.candere.com/jewellery/gemstone-navratna-earrings.html",
    
    ]

img_id = 0

for url in urls:
    # Fetch the content of the webpage
    response = requests.get(url)
    webpage = response.content

    # Parse the webpage content
    soup = BeautifulSoup(webpage, "html.parser")

    # Look for image tags - this may vary based on the web page's structure and may need tweaking
    # If the script doesn't work, inspect the webpage and adjust the selection criteria accordingly.
    images = soup.find_all("img", class_="hc img-responsive center-block")  # Adjust class_ if needed hc img-responsive center-block , 

    # Loop through the found images, download them, and resize them
    for idx, img_tag in enumerate(images):
        # Get the image URL
        img_url = img_tag["src"]
        if not img_url.startswith("http"):
            img_url = f"https:{img_url}"  # Handling relative URLs if needed

        # Download the image
        img_resp = requests.get(img_url, stream=True)
        img_resp.raw.decode_content = True
        img = Image.open(img_resp.raw)

        # Convert the image to PNG if it's GIF, take first frame if GIF is animated
        if img.format == 'GIF':
            img = img.convert('RGBA')
            img = Image.new('RGBA', img.size)
            img.paste(img)

        # Resize the image
        img = img.resize((512, 512), Image.ANTIALIAS)

        img_id += 1
        # Save the image as PNG
        img_path = os.path.join(image_directory, f"image_{img_id:03}.png")
        img.save(img_path, format="PNG")

        print(f"Downloaded and converted image {img_id}.png")


print("All images have been downloaded, converted, and resized.")
