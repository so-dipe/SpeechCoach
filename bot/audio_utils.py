from pydub import AudioSegment
from io import BytesIO

def convert_ogg_to_wav(ogg_data: bytes) -> BytesIO:
    try:
        # Create an in-memory buffer for the WAV data
        wav_buffer = BytesIO()

        # Load the OGG data from the input bytes
        oga_file = AudioSegment.from_file(BytesIO(ogg_data), format="ogg")

        # Export the OGG data as WAV format into the in-memory buffer
        oga_file.export(wav_buffer, format="wav")

        # Reset the buffer's position to the beginning
        wav_buffer.seek(0)

        return wav_buffer

    except Exception as e:
        # Handle any exceptions that may occur during the conversion
        print(f"Error converting OGG to WAV: {e}")
        return None
