from repustate import Client

repustate_client = Client(api_key='0acfbe5d0224e513e3afed3cdcb49ffbb900ceb1', version='v3')

def strip_non_ascii(text):
	new_text = [c for c in text if ord(c) < 128]
	return ''.join(new_text)

def get_sentiment(text):
    return repustate_client.sentiment(strip_non_ascii(text))['score']
