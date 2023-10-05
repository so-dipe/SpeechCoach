from io import BytesIO
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler
from telegram.ext.filters import AUDIO, COMMAND, TEXT
from .speech_recognition import transcribe_ogg
from .feedback import critic_speech
import tempfile

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # update.message.voice.get_file()
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    voice_message = update.message.voice

    if voice_message:
        try:
            # Usage of async functions within an async context
            voice_file = await update.message.voice.get_file()

            # Download the voice message and save as a temporary file
            with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as temp_ogg_file:
                await voice_file.download_to_drive(custom_path=temp_ogg_file.name)

                # Transcribe the OGG audio from the temporary file using Whisper
                transcript = transcribe_ogg(temp_ogg_file)

            if transcript:
                # Provide the transcription as a response
                await update.message.reply_text(f"Transcription: {transcript}")
            else:
                await update.message.reply_text("Error occurred during transcription.")
        except Exception as e:
            print(f"Error in reply: {e}")

    # Provide a response
    response = critic_speech(transcript=transcript)
    await update.message.reply_text(response)

hello_command = CommandHandler("hello", hello)
reply_command = MessageHandler(~COMMAND, reply)
# reply_command = MessageHandler(AUDIO | TEXT, reply)


# app.add_handler(CommandHandler("hello", hello))

# app.add_handler(MessageHandler(AUDIO, reply))