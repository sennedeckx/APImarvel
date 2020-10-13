import hashlib #voor de hash
import urllib.parse
import requests  #voor de requests
import datetime  #voor de timestamp


PUBLIC_KEY = "50296fea3dc827d0ac40dd44dfba8ee9"
PRIVATE_KEY = "d4d16c6676e3dc3ce61d9492afd7a21b4f2c62c2"
main_api = "https://gateway.marvel.com:443/v1/public/characters"
timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

#dit zorgt voor de hashes 
def hash_params():
 
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{PRIVATE_KEY}{PUBLIC_KEY}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


while True:   
    User = input("which hero/character do you want to know more about? " )
    params = {'name':  User, 'ts': timestamp,'apikey': PUBLIC_KEY, 'hash': hash_params()}
    request = requests.get(main_api,params=params)
    json_data = request.json()
    json_status = json_data["code"]

    
    #user kan afsluiten met q of quit
    if User == "quit" or User == "q":
        break

    #info printen over ingegeven hero/character
    if json_status == 200:
        print("------------------------------------------------------------------------------------------------------------")
        print("Name: " + (json_data["data"]["results"][0]["name"]))
        print("Description: " + (json_data["data"]["results"][0]["description"]))
        print("number of comics for this hero/character: " + str((json_data["data"]["results"][0]["comics"]["available"])))
        print("number of series for this hero/character: " + str((json_data["data"]["results"][0]["series"]["available"])) +"\n" )
        print("------------------------------------------------------------------------------------------------------------")
        
        

    #error afhandeling
    elif json_status == 400:
        print(str(json_status) + " bad request")
    elif json_status == 401:
        print(str(json_status) + " unauthorized")
    elif json_status == 403:
        print(str(json_status) + " Forbidden")
    elif json_status == 404:
        print(str(json_status) + " Not Found")
    elif json_status == 405:
        print(str(json_status) + " Method not allowed")
    elif json_status == 406:
        print(str(json_status) + " Not acceptable")