[app]
title = Samundar AI
package.name = samundarai
package.domain = com.gurugskr.samundarai

source.dir =.
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreements = True

[buildozer]
log_level = 2
warn_on_root = 1
p4a.branch = master
p4a.bootstrap = sdl2
android.archs = arm64-v8a
android.build_tools_version = 34.0.0
android.api = 33
requirements = python3,kivy==2.3.0
p4a.branch = master
