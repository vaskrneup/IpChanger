import requests
import time
from utils.proxy_manager import ProxyManager

req = ProxyManager(reset_after=40, password="test")

print("INITIAL: ", requests.get("http://httpbin.org/ip").text)
stat = {}

x = time.time()
d = req.get(
    "https://effigis.com/wp-content/uploads/2015/02/DigitalGlobe_WorldView2_50cm_8bit_Pansharpened_RGB_DRA_Rome_Italy_2009DEC10_8bits_sub_r_1.jpg"
)
print(time.time() - x)
with open("data.jpg", "wb") as f:
    f.write(d.content)
print(time.time() - x)
