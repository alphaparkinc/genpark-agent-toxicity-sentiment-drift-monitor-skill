from client import AgentToxicitySentimentDriftMonitorClient

def main():
    client = AgentToxicitySentimentDriftMonitorClient()
    res = client.monitor_stream_toxicity('Great job, thanks!')
    print('Toxicity & Sentiment Drift Monitor: ' + res['telemetry_id'] + ' (' + res['toxicity_level'] + ')')
    print('Toxicity Score: ' + str(res['toxicity_score']) + ' | Valence: ' + str(res['sentiment_valence']))
    print('Remedy: ' + res['recommended_remedy'])
    print('Feed URL: ' + res['telemetry_feed_url'])

if __name__ == '__main__':
    main()
