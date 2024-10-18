# pip install speedtest-cli
# pip install pillow
# pip install pyqrcode

import speedtest
wifi=speedtest.Speedtest()
download=wifi.download()
upload=wifi.upload()
print("download speed id = ", download/1024,"Kbps")
print("upload speed is =", upload/1024 ,"Kbps")