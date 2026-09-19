[app]

# Title of your application
title = Samundar AI

# Package name
package.name = samundarai

# Package domain
package.domain = com.gurugskr.samundarai

# Source code where the main.py is
source.dir =.

# Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# Main file
source.main = main.py

# Version
version = 0.1
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py

# Requirements - YAHAN APNE APP KE HISAB SE CHANGE KARO
# agar tum kivymd, requests, google-generativeai use kar rahe ho to ye rakho
requirements = python3,kivy==2.3.0,kivymd,requests,urllib3,charset-normalizer,certifi,idna,pillow

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Android permissions -
