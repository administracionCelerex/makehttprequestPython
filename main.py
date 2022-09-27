from email import message
import json
import httplib2

def sendHttpRequest(url:str,method:str,body:dict)->dict:
    print("Hi")
    http = httplib2.Http()
    headers = {
        "content-type":"application/json"
    }
    try:
        response= http.request(url,method=method,body=json.dumps(body),headers=headers)
        #print(response[1])
        statusCode = response[0].status
        message = response[1]
        
        return {
            "statusCode":statusCode,
            "msg":message
        }
       
        
    except Exception as e:
        
        print("Error on the server")
        print(e)
        return {
            "statusCode":500,
            "msg":"Something fails criticaly"
        }
        
        
### probando la funcion
    
mybody = {
            "extraccion_id":"Teresaochoa_SMNYL_2022-08-24_21:01:58.960466",
            "table":"polizas"
        }

g = sendHttpRequest("URL",method="POST",body=mybody)

print(g)

    


