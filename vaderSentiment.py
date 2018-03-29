from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import rhymz
analyzer = SentimentIntensityAnalyzer()

# Assuming we have a list of lyrics sorted chronologically
# Returns a dictionary of Lyrics and their sentiment weights
def getSentimentScores(lyrics):
    sentimentScores = {}
    for song in lyrics:
        # puts the song as key and the sentiment score as value
        sentimentScores[song] = analyzer.polarity_scores(song)

    return sentimentScores


