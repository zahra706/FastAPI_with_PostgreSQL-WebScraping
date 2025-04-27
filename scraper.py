import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    url = "https://news.ycombinator.com/item?id=42919502"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    # find all elements with class="ind" and indent level = 0
    elements = soup.find_all(class_="ind", indent=0)
    # for each of these elements, find the next element (comment)
    comments = [e.find_next(class_="comment") for e in elements]

    # Map of technologies keyword to search for and their occurrence initialized at 0
    keywords = {"python": 0, "javascript": 0, "typescript": 0, "go": 0, "c#": 0, "java": 0, "rust": 0}

    # Process each comment (job post)
    for comment in comments:
        # get the comment text and lower case it
        comment_text = comment.get_text().lower()

        # split comment by space to create an array of words
        words = comment_text.split(" ")

        # Use the string strip function and place all the characters we want to strip away
        words = {w.strip(".,/:;!@") for w in words}  # Use a set to ensure unique words

        # search for k in keywords, if the key is in the words set, we add 1 to the keywords score
        for k in keywords:
            if k in words:
                keywords[k] += 1

    # Print the collected keyword counts
    print(keywords)

    # Plot a bar graph
    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")
    plt.show()

if __name__ == "__main__":
    main()
