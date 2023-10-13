from bs4 import BeautifulSoup
import csv

# Parsing the HTML content
with open("/Users/wang/click_more/douying/comments/comments.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extracting data based on the updated elements for author name and comment
final_combined_data_updated = []

# Iterating over each <div> element with class CDx534Ub
for div in soup.find_all('div', class_='CDx534Ub'):
    
    comment_data = {}
    
    # Extracting comment content
    comment_span = div.find('span', class_='VD5Aa1A1')
    if comment_span:
        nested_comment_span = comment_span.find('span', class_='Nu66P_ba')
        if nested_comment_span:
            comment_data["comment"] = nested_comment_span.get_text(strip=True)
    
    # Extracting likes
    like_p = div.find('p', class_='eJuDTubq')
    if like_p:
        comment_data["likes"] = like_p.find('span').get_text(strip=True)
    
    # Extracting replies
    reply_div = div.find('div', class_='SIAdR40d')
    if reply_div:
        comment_data["replies"] = reply_div.find('span').get_text(strip=True).replace("展开", "").replace("条回复", "")
    
    # Extracting location
    location_div = div.find('div', class_='L4ozKLf7')
    if location_div:
        location_span = location_div.find('span')
        if location_span:
            # Splitting the text on the · character and taking the last part
            location_text = location_span.get_text(strip=True).split('·')[-1]
            comment_data["location"] = location_text


    # Extracting image URL
    image_div = div.find('div', class_='dZNywHd7')
    if image_div and image_div.find('img'):
        comment_data["image_url"] = image_div.find('img')['src']

    
    final_combined_data_updated.append(comment_data)

# Writing the extracted data to a CSV file
csv_file_path = "/Users/wang/click_more/douying/comments/extracted_data.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ["comment", "likes", "replies", "location","image_url"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in final_combined_data_updated:
        writer.writerow(data)
