name: build
on:
  push:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'
      - name: Install Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y zip unzip openjdk-17-jdk libffi-dev libssl-dev
          pip install --upgrade pip
          pip install cython==0.29.36 buildozer
      - name: Build APK
        run: |
          rm -rf .buildozer bin
          buildozer -v android debug
