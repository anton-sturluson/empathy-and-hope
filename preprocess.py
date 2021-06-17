import re
import emoji

emojis_list = emoji.UNICODE_EMOJI["en"].keys()
remoji = re.compile('|'.join(re.escape(p) for p in emojis_list))

def preprocess(text):
    #lowercase
    text = text.lower()

    #remove url
    text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+~]|[!*\(\)]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub('http://', '', text)
    text = re.sub('https://', '', text)

    #remove tag
    text = re.sub('@(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\)]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '',text)
    text = re.sub('@', '',text)

    #remove hashtag
    text = re.sub('#(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\)]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '',text)

    #remove emoji
    text = remoji.sub(" ", text)

    #remove non-alphanumerical character
    text = re.sub("[^a-zA-Z0-9]", " ", text)

    #remove redundant space
    text = " ".join(text.split())

    return text
