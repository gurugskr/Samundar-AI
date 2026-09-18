name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install JAVA and Deps
        run: |
          sudo apt update
          sudo apt install -y openjdk-17-jdk zip unzip git python3-pip libffi-dev libssl-dev
          sudo update-alternatives --set java /usr/lib/jvm/java-17-openjdk-amd64/bin/java
          pip install --upgrade pip
          pip install https://github.com/kivy/buildozer/archive/master.zip
          pip install cython==0.29.36
          # Buildozer ke andar ka purana rasta naya kar do
          SITE=$(pip show buildozer | grep Location | awk '{print $2}')
          echo $SITE
          sed -i 's|tools/bin/sdkmanager|cmdline-tools/latest/bin/sdkmanager|g' $SITE/buildozer/targets/android.py || true
          sed -i 's|android-sdk/tools|android-sdk/cmdline-tools/latest/bin|g' $SITE/buildozer/targets/android.py || true

      - name: Install Android SDK
        run: |
          export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
          export PATH=$JAVA_HOME/bin:$PATH
          mkdir -p ~/.android && touch ~/.android/repositories.cfg
          rm -rf $HOME/android_sdk
          mkdir -p $HOME/android_sdk/cmdline-tools
          wget -q https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O cmd.zip
          unzip -q cmd.zip -d /tmp/
          mkdir -p $HOME/android_sdk/cmdline-tools/latest
          mv /tmp/cmdline-tools/* $HOME/android_sdk/cmdline-tools/latest/
          export ANDROID_HOME=$HOME/android_sdk
          export ANDROID_SDK_ROOT=$HOME/android_sdk
          export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
          mkdir -p $ANDROID_HOME/licenses
          echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > $ANDROID_HOME/licenses/android-sdk-license
          echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> $ANDROID_HOME/licenses/android-sdk-license
          echo "24333f8a63b6825ea9c5514f83c1059b8ea4b9ac" >> $ANDROID_HOME/licenses/android-sdk-license
          yes | sdkmanager --licenses || true
          sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"

      - name: Build APK
        env:
          JAVA_HOME: /usr/lib/jvm/java-17-openjdk-amd64
          ANDROID_HOME: /home/runner/android_sdk
          ANDROID_SDK_ROOT: /home/runner/android_sdk
        run: |
          export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
          export PATH=$JAVA_HOME/bin:$HOME/android_sdk/cmdline-tools/latest/bin:$HOME/.local/bin:$PATH
          # SDK ko Buildozer ke folder me copy karo taaki wo download na kare
          mkdir -p $HOME/.buildozer/android/platform/
          rm -rf $HOME/.buildozer/android/platform/android-sdk
          cp -r $HOME/android_sdk $HOME/.buildozer/android/platform/android-sdk
          mkdir -p $HOME/.buildozer/android/platform/android-sdk/tools/bin
          echo '#!/bin/bash' > $HOME/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager
          echo 'exec $HOME/android_sdk/cmdline-tools/latest/bin/sdkmanager "$@"' >> $HOME/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager
          chmod +x $HOME/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Samundar-AI-APK
          path: bin/*.apk
