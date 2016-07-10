from repustate import Client

repustate_client = Client(api_key='0acfbe5d0224e513e3afed3cdcb49ffbb900ceb1', version='v3')

def get_sentiment(text):
    return repustate_client.sentiment(text)['score']