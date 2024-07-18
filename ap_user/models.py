import requests
from datetime import datetime
import time
import socket

"""
http://127.0.0.1:8000/api/api-route/?q=c filtro en camino
http://127.0.0.1:8000/api/api-route/?q=p filtro preparado
http://127.0.0.1:8000/api/api-route/?q=r filtro recibido
http://192.168.0.5:8080/api/api-route/?q=p!5 filtro estado preparado, origen 5

"""

class Client():
    
    def conect(self, ip, port):
                
        port = int(port)
        
        self.client_p= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.client_p.connect((ip, port))

    def send(self, msj):
        
        self.client_p.send(msj.encode())
        
    def disconnect(self,):
        
        self.client_p.close()

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
        
        self.client.get(self.url)   

        if 'csrftoken' in self.client.cookies:
            
            csrftoken = self.client.cookies['csrftoken']
        
            self.client.patch(self.url, data= payload, headers={'X-CSRFTOKEN': csrftoken})
                        
    def post_url(self, payload):
        
        self.client.get(self.url) 
        
        if 'csrftoken' in self.client.cookies:

            csrftoken = self.client.cookies['csrftoken']
            
            payload['csrfmiddlewaretoken']= csrftoken
            
            payload['next']= ''
            
            self.client.post(self.url, data= payload, headers=dict(Referer= self.url))
        


class User(Route, Client):
    
    def __init__(self,):
        
        self.id_user= {}
    
    def view_nodes(self,):
        
        self.url= self.url_origin
        
        get= self.get_url('')
        
        return get['results']
    
    def log(self, url, user, passwd):
        
        url= 'http://' + url 
        
        self.url=''
                
        self.url_route= url + '/api/api-route/'

        self.url_instance= url + '/api/api-instance/'

        self.url_id_user= url + '/api/api-user/'

        self.url_origin= url + '/api/api-origin/'    
   
        self.url_login= url + '/api-auth/login/'
        
        self.url_logout= url + '/api-auth/logout/'
        
        self.url_perfil= url + '/api/api-perfil/'
        
        self.client = requests.session()
        
        self.client.get(self.url_login) 
        
        if 'csrftoken' in self.client.cookies:

            csrftoken = self.client.cookies['csrftoken']
            
            login_data = dict(username= user, password= passwd, csrfmiddlewaretoken=csrftoken, next='/api/api-user/')
            
            id = self.client.post(self.url_login, data=login_data, headers=dict(Referer= self.url_login))
        
            self.id_user= id.json()['results'][0]         

            self.nodes_origin= self.view_nodes()
            
            self.url= self.url_perfil
            
            perfil = self.get_url(id= '?q='+ str(self.id_user['id']))
            
            self.perfil= perfil['results'][0]['nodo']
                          
    def logOut(self,):

        self.id_user= {}
        
        if 'csrftoken' in self.client.cookies:

            csrftoken = self.client.cookies['csrftoken']
       
            self.client.post(self.url_logout, data=dict(csrfmiddlewaretoken=csrftoken, next=''), headers=dict(Referer= self.url_logout))
    
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
        
    def view_orders(self, query):
        
        self.url= self.url_route
        
        route= self.get_url(query)
        
        return route
        
        
