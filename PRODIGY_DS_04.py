import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
import re

# Create a sample dataset
data = {
    'text': [
        "I love the new iPhone! It's amazing!",
        "The customer service of XYZ company is terrible.",
        "Just had a great meal at the new restaurant downtown.",
        "I'm so disappointed with the quality of this product.",
        "Amazing experience with the customer support team!",
        "The traffic today is unbearable.",
        "I can't wait to try out the new features of the app!",
        "Such a beautiful sunset!",
        "This movie was a complete waste of time.",
        "The weather today is perfect for a picnic."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Preprocess the text data
def preprocess_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

df['text'] = df['text'].apply(preprocess_text)

# Perform sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    # Return sentiment polarity
    return analysis.sentiment.polarity

df['sentiment'] = df['text'].apply(get_sentiment)

# Visualize sentiment distribution
plt.hist(df['sentiment'], bins=20, color='skyblue', edgecolor='black')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.show()

# Visualize word cloud of positive and negative sentiments
positive_tweets = ' '.join(df[df['sentiment'] > 0]['text'])
negative_tweets = ' '.join(df[df['sentiment'] < 0]['text'])

wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(positive_tweets)
wordcloud_negative = WordCloud(width=800, height=400, background_color='white').generate(negative_tweets)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.title('Positive Sentiment Word Cloud')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.title('Negative Sentiment Word Cloud')
plt.axis('off')

plt.show()

