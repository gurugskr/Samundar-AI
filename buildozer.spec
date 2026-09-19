[app]
title = Samundar AI
package.name = samundarai
package.domain = com.gurugskr.samundarai
source.dir =.
source.include_exts = py,png,jpg,kv,json
version = 0.1
requirements = python3,kivy==2.2.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.accept_sdk_license_agreements = True
android.permissions = INTERNET
p4a.bootstrap = sdl2
android.archs = arm64-v8a, armeabi-v7a
