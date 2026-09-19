[app]
title = Samundar AI
package.name = samundarai
package.domain = org.gurugskr.samundarai

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 0.1
requirements = python3,kivy,requests,urllib3,certifi,charset-normalizer,idna
orientation = portrait

# Samundar AI ke liye jaruri permission
android.permissions = INTERNET

# Arch - Isse build fast aur stable hota hai
android.archs = arm64-v8a, armeabi-v7a

# Android API
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2
warn_on_root = 1
