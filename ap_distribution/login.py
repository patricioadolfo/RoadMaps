from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    
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

        except:
            
            self.children[-1].text= 'Login Incorrecto'
        
     
 
class LogOutScreen(MDScreen):
    
    pass
        
        
