[app]
title = Cooler Control
package.name = coolercontrol
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 1.0.0
requirements = python3,kivy==2.2.0,kivymd==1.2.0,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.allow_backup = False
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
