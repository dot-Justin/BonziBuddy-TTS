import requests
import simpleaudio as sa
import io
from urllib.parse import quote_plus

text = "T E T Y Y S is the best."

encoded_text = quote_plus(text)
tts_url = f"https://www.tetyys.com/SAPI4/SAPI4?text={encoded_text}&voice=Adult%20Male%20%232%2C%20American%20English%20(TruVoice)&pitch=140&speed=157"
response = requests.get(tts_url)
if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)

    wave_obj = sa.WaveObject.from_wave_file(io.BytesIO(response.content))
    
    play_obj = wave_obj.play()
    play_obj.wait_done()
else:
    print(f"Failed to fetch audio: {response.status_code}")