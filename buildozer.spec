[app]
title = Samundar-AI
package.name = samundarai
package.domain = com.samundar.ai
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2
p4a.branch = develop
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET
