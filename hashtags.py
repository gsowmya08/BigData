import json
import re

class TweetHashtagExtractor:
    def __init__(self, input_file_path, tweet_field='full_text'):
        self.input_file_path = input_file_path
        self.tweet_field = tweet_field

    def find_hashtags(self, text):
        """Extract hashtags using a regular expression."""
        return re.findall(r'#\w+', text)
    
    def read_tweets(self):
        """Yield tweets as dictionaries from a file."""
        with open(self.input_file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON line at {line_number}.")
    
    def extract_hashtags(self):
        """Aggregate all hashtags from tweets, including duplicates."""
        tweets = self.read_tweets()
        all_hashtags = []  # Changed from set to list to keep duplicates
        for tweet in tweets:
            hashtags = self.find_hashtags(tweet.get(self.tweet_field, ''))
            all_hashtags.extend(hashtags)  # Extending the list with all found hashtags
        return all_hashtags

    def save_hashtags_to_file(self, hashtags, output_file_path):
        """Save all extracted hashtags to a file."""
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for hashtag in hashtags:  # No sorting, to keep the original order
                file.write(hashtag + '\n')

def main():
    input_file_path = r"C:\Users\LENOVO\Downloads\tweets.json (1)\out.json"  # Adjust this to your actual file path
    output_file_path = r"C:\Users\LENOVO\Downloads\tweets.json (1)\output_hashtags.txt"  # Adjust to where you want to save hashtags
    tweet_field = 'full_text'  # Change this if your tweets use a different field for text
    extractor = TweetHashtagExtractor(input_file_path, tweet_field=tweet_field)
    hashtags = extractor.extract_hashtags()
    extractor.save_hashtags_to_file(hashtags, output_file_path)
    print(f"Extracted {len(hashtags)} hashtags (including duplicates), saved to {output_file_path}")

if __name__ == "__main__":
    main()
