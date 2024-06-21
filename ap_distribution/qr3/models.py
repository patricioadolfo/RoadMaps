import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import time


"""
http://127.0.0.1:8000/api/api-route/?q=c filtro en camino
http://127.0.0.1:8000/api/api-route/?q=p filtro preparado
http://127.0.0.1:8000/api/api-route/?q=r filtro recibido
http://192.168.0.5:8080/api/api-route/?q=p!5 filtro estado preparado, origen 5

"""


class Route:
    
    def __init__(self,):    
        
        pass
        
    def get_url(self, id):
        
        r= requests.get( self.url + id, auth= self.auth)

        if r.status_code == 200:
            
            return r.json()
        
        else:
            return 'Error!'

    def patch_url(self, id, payload):
        
        p= requests.patch(self.url + id + '/' , json= payload, auth= self.auth)
        
        return p.json()
    
    def post_url(self, payload):
        
        p= requests.post(self.url, json= payload, auth= self.auth)
        
        return p.text

class User(Route):
    
    def __init__(self,):
        
        self.id_user= {}
    
    def view_nodes(self,):
        
        self.url= self.url_origin
        
        get= self.get_url('')
        
        return get['results']
    
    def log(self, url, user, passwd):
        
        self.url=''
                
        self.url_base= url

        self.url_route= self.url_base + 'api-route/'

        self.url_instance= self.url_base + 'api-instance/'

        self.url_id_user= self.url_base + 'api-user/'

        self.url_origin= self.url_base + 'api-origin/'    
   
        
        self.auth=  HTTPBasicAuth(user, passwd)
        
        id= requests.get( self.url_id_user, auth= self.auth)
        
        self.nodes_origin= self.view_nodes()
        
        self.id_user= id.json()['results'][0]
                
    def logOut(self,):
        
        self.auth= HTTPBasicAuth('','')
        
        self.id_user= {}
    
    def on_road(self, id_route):
        
        self.url= self.url_route
     
        payload= {"status":"c"}
    
        patch= self.patch_url(id_route, payload)
        
        payload={
            "route_id": id_route,
            "status": 'c',
            "instance_date":  datetime.today().strftime("%Y-%m-%d"),
            "instance_time": time.strftime("%H:%M:%S", time.localtime()),
            "user": self.id_user['id'],
            "route": id_route
        }
        
        self.url= self.url_instance

        self.post_url(payload)        
        
        return patch

    def view_list(self, arg):
        
        self.url= self.url_route
        
        get= self.get_url(arg)
        
        return get['results']

    def view_road(self, query):
        
        self.url= self.url_route
        
        route= self.get_url(query)
        
        return route
        

        
        
