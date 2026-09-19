[app]
title = Samundar AI
package.name = samundarai
package.domain = com.samundar.ai

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
# p4a.port =

[app]

# (str) Title of your application
# title = My Application

# (str) Package name
# package.name = myapp

# (str) Package domain (needed for android/ios packaging)
# package.domain = org.test

# (str) Source code where the main.py live
# source.dir =.

# (list) Source files to include (let empty to include all the files)
# source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*,images/*

# (list) Source files to exclude (let empty to not exclude anything)
# source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
# source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
# source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
# version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"]([^'"]*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy =../../kivy

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of sensort, sensorLandscape, portrait, landscape)
# landscape, sensorLandscape, portrait, sensorPortrait or all
# orientation = portrait

# (list) List
