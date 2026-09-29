[app]
title = EMA Assistant
package.name = emaassistant
package.domain = org.ema
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,gtts,playsound,SpeechRecognition,pyaudio,requests,setuptools
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 20
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
