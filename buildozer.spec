[app]
title = CoolerControl
package.name = coolercontrol
package.domain = org.skksqw3

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 0.1
requirements = python3==3.11.9,kivy==2.3.0,kivymd==1.2.0,pyjnius,requests,urllib3,certifi,idna,chardet,filetype

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png

android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 33.0.2
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.debug_artifact = debug

[buildozer]
log_level = 2
warn_on_root = 1
