#-*-coding:utf-8-*-

#Sorgu işleminde kullanılacak modüller:
#(eğer modüller yüklü değil ise komut sistemine "pip install requests" komutunu kullanarak yükleyebilirsiniz)
import requests, json

#Sorgu sonucu listelenecek başlıklar:
print ("IP","Ülke","İl","İlçe","Enlem","Boylam")

#Sorgulanacak ip lere ait liste:
ip = ["176.220.33.233"]
APIKEY = "81ac0d765ed9122937ae64cbae0c1e80"
#ip listesinin teker teker web servis üzerinden sorgulanması:
for x in ip:
  #Bu kısımda yer alan API_KEY'i https://ipstack.com/ adresine üye olarak temin edebilirsiniz.
  serviceURL = "http://api.ipapi.com/"+x+"?access_key="+APIKEY+"&output=json"  
  r = requests.get(serviceURL)
  y = json.loads(r.text)
  print(y)
  #print(y["ip"],y["country_name"],y["region_name"],y["city"],y["latitude"],y["longitude"])  