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
        
    def get_url(self, id= ''):

        r= self.client.get( self.url + id)

        if r.status_code == 200:
            
            return r.json()
        
        else:
            return 'Error!'

    def patch_url(self, id, payload):
        
        self.url= self.url +  id +'/'
        
        p= self.client.get(self.url) 
        
        if 'csrftoken' in p.cookies:

            csrftoken = p.cookies['csrftoken']
            
            payload['csrfmiddlewaretoken']= csrftoken
            
            payload['next']= ''
            
            p= self.client.patch(self.url, data= payload, headers=dict(Referer= self.url))
        
        else:
            self.client.patch(self.url, data= payload)
   
    def post_url(self, payload):
        
        self.client.get(self.url) 
        
        if 'csrftoken' in self.client.cookies:

            csrftoken = self.client.cookies['csrftoken']
            
            payload['csrfmiddlewaretoken']= csrftoken
            
            payload['next']= ''
            
            p= self.client.post(self.url, data= payload, headers=dict(Referer= self.url))
        
            print(p)


class User(Route):
    
    def __init__(self,):
        
        self.id_user= {}
    
    def view_nodes(self,):
        
        self.url= self.url_origin
        
        get= self.get_url('')
        
        return get['results']
    
    def log(self, url, user, passwd):
        
        self.url=''
                
        self.url_route= url + 'api/api-route/'

        self.url_instance= url + 'api/api-instance/'

        self.url_id_user= url + 'api/api-user/'

        self.url_origin= url + 'api/api-origin/'    
   
        self.url_login= url + 'api-auth/login/'
        
        self.client = requests.session()
        
        self.client.get(self.url_login) 
        
        if 'csrftoken' in self.client.cookies:

            csrftoken = self.client.cookies['csrftoken']
            
            login_data = dict(username= user, password= passwd, csrfmiddlewaretoken=csrftoken, next='/api/api-user/')
            
            id = self.client.post(self.url_login, data=login_data, headers=dict(Referer= self.url_login))
        
            self.id_user= id.json()['results'][0]         

            self.nodes_origin= self.view_nodes()
                          
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
        

        
        
