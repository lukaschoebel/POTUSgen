import json
import re
import sys


def beautify(name):
    ''' Loading, filtering and saving the JSON tweet file to a newly generated .txt file
    :type: name: String
    :rtype: output: .txt
    '''

    filename = name + '.json'
    output_name = name + "_filtered.txt"

    with open(filename, "r", encoding="utf-8") as input:
        with open(output_name, "w", encoding="utf-8") as output:
            document = json.load(input)
            
            # Filter only the messages that are not retweeted
            # >> Version i): for tweets from archive "master_XXXX.json" 
            # document = [x['full_text'] for x in document if x['user']['screen_name'] == 'realDonaldTrump' and 'full_text' in x]
            
            # >> Version ii): for self-scraped tweets via https://github.com/bpb27/twitter_scraping
            # document = [x['text'] for x in document if x['user']['screen_name'] == 'realDonaldTrump' and 'text' in x]

            # >> Version iii): Data set from https://github.com/MatthewWolff/MarkovTweets/
            document = [x['text'] for x in document]

            # Clean and only include not retweeted messages
            document = [deep_clean(x) for x in document if deep_clean(x) is not None]

            # Preventing unicode characters by ensuring false ascii encoding
            for _, value in enumerate(document):
                output.write(json.dumps(value, ensure_ascii=False) + "\n")
            # json.dump(document, output, ensure_ascii=False, indent=4)

    print(f">> Sucessfully cleaned {filename} and saved it to {output_name}")


def deep_clean(s):
    ''' Deep cleaning of filtered tweets. Replaces common symbols and kills quotation marks/apostrophes.
    :type: s: String
    :rtype: s: String
    '''

    # Return None if given tweet is a retweet
    if s[:2] == 'RT':
        return None

    # Delete all URLs because they don't make for interesting tweets.
    s = re.sub(r'http[\S]*', '', s)

    # Replace some common unicode symbols with raw character variants
    s = re.sub(r'\\u2026', '...', s)
    s = re.sub(r'…', '', s)
    s = re.sub(r'\\u2019', "'", s)
    s = re.sub(r'\\u2018', "'", s)
    s = re.sub(r"&amp;", r"&", s)
    s = re.sub(r'\\n', r"", s)

    # Delete emoji modifying characters
    s = re.sub(chr(127996), '', s)
    s = re.sub(chr(65039), '', s)

    # Kill apostrophes & punctuation because they confuse things.
    s = re.sub(r"'", r"", s)
    s = re.sub(r"“", r"", s)
    s = re.sub(r"”", r"", s)
    s = re.sub('[()]', r'', s)
    s = re.sub(r'"', r"", s)

    # Collapse multiples of certain chars
    s = re.sub('([.-])+', r'\1', s)
    
    # Pad sentence punctuation chars with whitespace
    s = re.sub('([^0-9])([.,!?])([^0-9])', r'\1 \2 \3', s)
    
    # Remove extra whitespace (incl. newlines)
    s = ' '.join(s.split()).lower()

    # Define emoji_pattern
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)

    s = emoji_pattern.sub(r'', s)

    # Care for a special case where the first char is a "."
    # return s[1:] if s[0] == "." else s
    if len(s):
        return s[1:] if s[0] == "." else s
    return None


if __name__ == "__main__":

    if len(sys.argv) - 1: beautify(sys.argv[1]) 