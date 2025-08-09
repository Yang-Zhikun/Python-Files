from kittentts import KittenTTS
m = KittenTTS("KittenML/kitten-tts-nano-0.1")

audio = m.generate("Whatsup man", voice='expr-voice-5-m' )

# available_voices : [  'expr-voice-2-m', 'expr-voice-2-f', 'expr-voice-3-m', 'expr-voice-3-f',  'expr-voice-4-m', 'expr-voice-4-f', 'expr-voice-5-m', 'expr-voice-5-f' ]

# Save the audio
import soundfile as sf
sf.write('output.mp3', audio, 24000)
