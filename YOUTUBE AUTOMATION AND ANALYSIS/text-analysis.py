import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
import re
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob  # Import TextBlob for sentiment analysis

# Download necessary NLTK data (you only need to run this once)
nltk.download('punkt')
nltk.download('stopwords')

def perform_text_analysis(content):
    # Tokenize the text (split into words)
    words = word_tokenize(content.lower())

    # Remove punctuation and stopwords
    table = str.maketrans('', '', string.punctuation)
    words = [word.translate(table) for word in words]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # Perform frequency distribution analysis
    freq_dist = FreqDist(words)

    # Get the most common words
    most_common_words = [word for word, freq in freq_dist.most_common(10)]

    # Perform sentiment analysis
    blob = TextBlob(content)
    polarity_scores = [sentence.sentiment.polarity for sentence in blob.sentences]

    avg_polarity = sum(polarity_scores) / len(polarity_scores)

    if avg_polarity > 0.05:
        sentiment = "Positive"
    elif avg_polarity < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    most_positive_comment = blob.sentences[polarity_scores.index(max(polarity_scores))].raw
    most_negative_comment = blob.sentences[polarity_scores.index(min(polarity_scores))].raw

    # Other text analysis metrics
    total_words = len(words)
    total_sentences = len(sent_tokenize(content))
    avg_sentence_length = total_words / total_sentences

    complex_words = [word for word in words if len(word) > 2]
    percentage_complex_words = len(complex_words) / total_words
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

    complex_word_count = len(complex_words)
    word_count = total_words

    vowels = "aeiouy"
    syllable_per_word = sum([len(re.findall(r'[aeiouy]+', word)) for word in words])

    personal_pronouns = len(re.findall(r'\b(?:I|we|my|ours|us)\b', content, re.IGNORECASE))

    total_characters = sum(len(word) for word in words)
    avg_word_length = total_characters / total_words

    freq_dist_results = {
        "MOST_COMMON_WORDS": most_common_words,
        "AVG_SENTENCE_LENGTH": avg_sentence_length,
        "PERCENTAGE_OF_COMPLEX_WORDS": percentage_complex_words,
        "FOG_INDEX": fog_index,
        "AVG_NUMBER_OF_WORDS_PER_SENTENCE": total_words / total_sentences,
        "COMPLEX_WORD_COUNT": complex_word_count,
        "WORD_COUNT": word_count,
        "SYLLABLE_PER_WORD": syllable_per_word,
        "PERSONAL_PRONOUNS": personal_pronouns,
        "AVG_WORD_LENGTH": avg_word_length,
    }

    sentiment_results = {
        "AVG_POLARITY": avg_polarity,
        "polarity_scores": polarity_scores,  # Include the polarity scores in the results
        "SENTIMENT": sentiment,
        "MOST_POSITIVE_COMMENT": most_positive_comment,
        "MOST_NEGATIVE_COMMENT": most_negative_comment,
    }

    return {**freq_dist_results, **sentiment_results}

def read_content_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def plot_analysis_results(analysis_results, title):
    plt.figure(figsize=(10, 6))
    numeric_metrics = {metric: value for metric, value in analysis_results.items() if isinstance(value, (int, float))}
    mean_values = {metric: np.mean(value) for metric, value in numeric_metrics.items()}
    plt.bar(mean_values.keys(), mean_values.values(), color='blue')
    plt.title(title)
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    transcript_file_path = 'transcript.txt'
    comments_file_path = 'comments.txt'

    # Analyze Transcript
    transcript_content = read_content_from_file(transcript_file_path)
    if transcript_content:
        print("\nText Analysis on Transcript:")
        transcript_analysis_results = perform_text_analysis(transcript_content)
        print(transcript_analysis_results)

        transcript_df = pd.DataFrame([transcript_analysis_results])
        transcript_output_excel_path = 'transcript_analysis_results.xlsx'
        transcript_df.to_excel(transcript_output_excel_path, sheet_name='Transcript Analysis', index=False)
        print(f"Transcript analysis results exported to: {transcript_output_excel_path}")

        plot_analysis_results(transcript_analysis_results, 'Transcript Analysis')

    # Analyze Comments
    comments_content = read_content_from_file(comments_file_path)
    if comments_content:
        print("\nText Analysis on Comments:")
        comments_analysis_results = perform_text_analysis(comments_content)
        print(comments_analysis_results)

        comments_df = pd.DataFrame([comments_analysis_results])
        comments_output_excel_path = 'comments_analysis_results.xlsx'
        comments_df.to_excel(comments_output_excel_path, sheet_name='Comments Analysis', index=False)
        print(f"Comments analysis results exported to: {comments_output_excel_path}")

        plot_analysis_results(comments_analysis_results, 'Comments Analysis')

        # Sentiment Analysis Visualization (Bar Chart)
        plt.figure(figsize=(10, 6))
        sentiment_counts = {
            "Positive": sum(1 for score in comments_analysis_results["polarity_scores"] if score > 0.05),
            "Negative": sum(1 for score in comments_analysis_results["polarity_scores"] if score < -0.05),
            "Neutral": sum(1 for score in comments_analysis_results["polarity_scores"] if -0.05 <= score <= 0.05),
        }
        plt.bar(sentiment_counts.keys(), sentiment_counts.values(), color=['blue', 'red', 'grey'])
        plt.title('Sentiment Analysis of Comments')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.show()

        # Sentiment Analysis Visualization (Pie Chart)
        plt.figure(figsize=(10, 6))
        plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct='%1.1f%%', colors=['blue', 'red', 'grey'])
        plt.title('Sentiment Analysis of Comments')
        plt.show()

if __name__ == "__main__":
    main()
