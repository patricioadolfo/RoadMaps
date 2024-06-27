from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    
    def login(self,url, username, password):
               
        try:
            url= url._get_text()
            
            username= username._get_text()
            
            password= password._get_text()

            self.parent.user.log(url, username, password)
            
            self.parent.current= 'homescreen'
            
            self.parent.parent.children[-1].children[0].icon= 'logout'    
            
            self.parent.parent.ids.qr_btn.disabled= False
            
            self.parent.parent.ids.branch_btn.disabled= False   
            
            self.parent.parent.ids.home_btn.disabled= False           

        except:
            
            self.children[-1].text= 'Login Incorrecto'
        

    def logout(self, home_btn, qr_btn, branch_btn, btn, screen_manager):
        
        screen_manager.user.logOut()
        
        btn.icon= 'account'
        
        home_btn.disabled= True
            
        qr_btn.disabled= True   
            
        branch_btn.disabled= True  
        

        
        
 
class LogOutScreen(MDScreen):
    
    pass      
        
        
