[app]
title = Samundar AI
package.name = samundarai
package.domain = com.gurugskr.samundarai

source.dir =.
source.include_exts = py,png,jpg,kv,json
source.include_patterns = assets/*,images/*
version = 0.1

requirements = python3,kivy

orientation = portrait

# App ka icon agar ho to
#icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2

# --- Android Settings - Ye Sab Fix Hai ---
[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.ant = auto
p4a.bootstrap = sdl2
p4a.port = auto

# Permission
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
