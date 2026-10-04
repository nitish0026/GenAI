import requests
from bs4 import BeautifulSoup

def fetch_and_clean_flipkart_page():
    # Step 1: Download the HTML page
    url = "https://www.flipkart.com/"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Step 2: Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove CSS, JavaScript, and Images
        for script in soup(["script", "style", "img"]):
            script.decompose()  # Remove the tag from the tree
        
        # Get cleaned text
        cleaned_text = soup.get_text(separator='\n').strip()

        # Step 3: Save the remaining text content
        with open("cleaned_flipkart_content.txt", "w", encoding="utf-8") as file:
            file.write(cleaned_text)

        print("Text content cleaned and saved to cleaned_flipkart_content.txt")
    else:
        print("Failed to retrieve the webpage, status code:", response.status_code)

# Execute the function
fetch_and_clean_flipkart_page()

# Return the signal to terminate
""