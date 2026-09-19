[app]
title = Samundar AI
package.name = samundarai
package.domain = com.gurugskr.samundarai
source.dir =.
source.include_exts = py,png,jpg,kv
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
android.build_tools_version = 34.0.0
android.accept_sdk_license_agreements = True
android.permissions = INTERNET
p4a.bootstrap = sdl2
p4a.branch = develop
# add this line
android.accept_sdk_license_agreements = True

# and make sure these match
android.api = 33
android.minapi = 21
android.build_tools_version = 37.0.0
# or try 34.0.0 if 37 keeps failing
