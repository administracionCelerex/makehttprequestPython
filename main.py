import json
import httplib2

def sendHttpRequest(url:str,method:str,body:dict)->str:
    print("Hi")
    http = httplib2.Http()
    try:
        response= http.request(url,method=method,body=json.dumps(body))
        print(response[1])
    except Exception as e:
        print("Error on the server")
        print(e)
    

sendHttpRequest("https://jsdhfjsdf",method="POST",body=23)


    


