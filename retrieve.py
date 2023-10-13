from bs4 import BeautifulSoup
import csv

# Load the content from the uploaded HTML file
with open("/Users/wang/click_more/video.html", "r", encoding="utf-8") as file:
    content = file.read()

# Parse the content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all comments
comments = soup.find_all('ytd-comment-renderer', {'id': 'comment'})

# List to store extracted data
extracted_data = []

# Loop through each comment to extract details
for comment in comments:
    # Extract comment text
    comment_text = comment.find('yt-formatted-string', {'class': 'style-scope ytd-comment-renderer'}).text
    
    # Extract number of likes
    likes = comment.find('span', {'id': 'vote-count-left'}).text.strip() if comment.find('span', {'id': 'vote-count-left'}) else "0"
    
    # Searching for the associated replies section for the comment
    replies_section = comment.find_next_sibling('div', {'id': 'replies'})
    if replies_section:
        replies_span = replies_section.find('span', {'class': 'yt-core-attributed-string'})
        replies_text = replies_span.text.replace("条回复", "").strip() if replies_span else "0"
    else:
        replies_text = "0"
    
    # Append extracted data to the list
    extracted_data.append({
        'comment': comment_text,
        'likes': likes,
        'replies': replies_text
    })

# Save the extracted data to a CSV file
csv_file = "comments_data.csv"
with open(csv_file, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['comment', 'likes', 'replies'])
    writer.writeheader()
    writer.writerows(extracted_data)

print(f"Data saved to {csv_file}")
