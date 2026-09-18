[app]
title = Samundar AI
package.name = samundarai
package.domain = com.gurugskr.samundarai
source.dir =.
version = 0.1
requirements = python3,kivy==2.2.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.permissions = INTERNET
p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2
