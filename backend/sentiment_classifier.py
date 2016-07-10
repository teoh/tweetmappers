from repustate import Client

repustate_client = Client(api_key='61f177d260b047b2626537561dc9920c305cb242', version='v3')

def strip_non_ascii(text):
	new_text = [c for c in text if ord(c) < 128]
	return ''.join(new_text)

def get_sentiment(text):
    return repustate_client.sentiment(strip_non_ascii(text))['score']
