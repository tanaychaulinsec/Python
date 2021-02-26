import requests
api_url="https://ifsc.razorpay.com/"
ifsc_code="SBIN0000300"
req = requests.get(api_url+ifsc_code)
data=req.json()
#iterate data dic
for key , val in data.items():
    print(key +" : "+str(val))
