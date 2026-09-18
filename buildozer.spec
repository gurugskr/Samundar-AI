[app]
title = Samundar AI
package.name = samundarai
package.domain = com.gurugskr.samundarai
source.dir =.
source.include_exts = py,png,jpg,kv,json
version = 0.1
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True
android.permissions = INTERNET
p4a.bootstrap = sdl2
p4a.branch = develop
android.archs = arm64-v8a, armeabi-v7a
