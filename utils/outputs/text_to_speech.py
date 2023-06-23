import dataclasses
import io
from pathlib import Path

from gtts import gTTS


@dataclasses.dataclass
class TextToSpeechConfig:
    text: str
    output: str | io.BytesIO | Path
    tld: str = 'com'
    lang: str = "en"
    slow: bool = True
    format: str = "audio/mp3"


def text_to_speech(config: TextToSpeechConfig):
    tts = gTTS(text=config.text,
               lang=config.lang,
               slow=config.slow,
               tld=config.tld, )
    tts.save(config.output)