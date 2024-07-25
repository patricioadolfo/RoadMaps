from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore

class LoginScreen(MDScreen):
    
    store = JsonStore('load.json')
        
    def login(self,url, username, password):
               
        try:
            url= url._get_text()
            
            username= username._get_text()
            
            password= password._get_text()

            self.parent.user.log(url, username, password)
            
            self.parent.current= 'homescreen'
            
            self.parent.parent.ids.btn_log.icon= 'logout'    
            
            self.parent.parent.ids.qr_btn.disabled= False
            
            self.parent.parent.ids.branch_btn.disabled= False   
            
            self.parent.parent.ids.home_btn.disabled= False    
            
            self.parent.parent.ids.home_screen.count_routes() 
            
            self.save_log(username, password, url)

        except:
            
            self.children[-1].text= 'Login Incorrecto'
      
    def save_log(self, username, password, url):
        
        try:

            self.store.put('log', name= username, pswd= password, ip= url)
        
        except:
            
            pass
        
