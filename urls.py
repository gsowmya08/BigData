import json
import re

def find_urls(text):
    """Extract URLs using a regular expression."""
    return re.findall(r'https?://\S+', text)

def extract_urls(input_file_path, tweet_field='full_text'):
    """Read tweets from a file and extract URLs."""
    all_urls = []
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                urls = find_urls(tweet.get(tweet_field, ''))
                all_urls.extend(urls)
            except json.JSONDecodeError:
                continue  # Skip invalid JSON lines
    return all_urls

def save_urls_to_file(urls, output_file_path):
    """Save extracted URLs to a file."""
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')

def main():
    input_file_path = r"C:\Users\LENOVO\Downloads\tweets.json (1)\out.json"
    output_file_path = r"C:\Users\LENOVO\Downloads\tweets.json (1)\output_urls.txt"
    urls = extract_urls(input_file_path)
    save_urls_to_file(urls, output_file_path)
    print(f"Extracted {len(urls)} URLs (including duplicates), saved to {output_file_path}")

if __name__ == "__main__":
    main()
