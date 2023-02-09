import requests

class TextToSpeechPostRequest:
    # initializing the general parameters from main cfg file
    def __init__(self, input_configs_json):
        self.configs = input_configs_json
        self.headers = self.get_headers()
        self.url = self.get_url()

    # get the header configs from main cfg file
    def get_headers(self):
        headers = {
            "content-type": self.configs["content-type"],
            "X-RapidAPI-Key": self.configs["X-RapidAPI-Key"],
            "X-RapidAPI-Host": self.configs["X-RapidAPI-Host"]
        }
        return headers
    
    # get the url from main cfg file
    def get_url(self):
        return self.configs["post_url"]
    
    # this is the first way to send post request, using payload structure
    def send_request_payload(self, api_key, src_text, content_language, speech_voice="", speech_rate="", audio_codec="", audio_format="", ssml="", out_str_format=""):
        payload = "key={}&src={}&hl={}&v={}&r={}&c={}&f={}&ssml={}&b64={}".format(api_key, src_text, content_language, speech_voice, speech_rate, audio_codec, audio_format, ssml, out_str_format)
        
        response = requests.post(self.url, headers=self.headers, data=payload)

        return response

    # this is the second way to send post request, using data structure
    def send_request_data(self, api_key, src_text, content_language, speech_voice="", speech_rate="", audio_codec="", audio_format="", ssml="", out_str_format=""):
        data = {
            "key": api_key,
            "src": src_text,
            "hl": content_language,
            "v": speech_voice,
            "r": speech_rate,
            "c": audio_codec,
            "f": audio_format,
            "ssml": ssml,
            "b64": out_str_format
        }
        
        response = requests.post(self.url, headers=self.headers, data=data)
        return response