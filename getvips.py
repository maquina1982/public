import requests
import json
import logging

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from getpass import getpass

username = input ("Enter username:")
password = getpass ("Enter password:")


f5_list = [
    "127.0.0.1:5556",
]

for f5 in f5_list:
    try:

        test_vips = [
"vip1",
]
        for vip in test_vips:
            vip_call = requests.get("https://" + f5 + "/mgmt/tm/ltm/virtual/~Common~" + vip, auth=(username, password),
                                    verify=False)
            response_json = vip_call.json()

            vip_dict = response_json
        
            
            try:
                

                rules = vip_dict["rules"]
                
                
                print(vip, rules)
                        


                    
                    

            
            except Exception as e:


                print(f"key error no {e}, on vip {vip}") 



 
    except Exception as e:
        error = e, f5
        
        print(error)
        continue
       

                

                

                
                

                    

                





            
       

        



      
              




