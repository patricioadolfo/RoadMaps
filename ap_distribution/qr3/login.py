from kivymd.uix.screen import MDScreen


class Login(MDScreen):
    
    def login(self,url, username, password, app):
               
        try:
            url= url._get_text()
            
            username= username._get_text()
            
            password= password._get_text()

            app.log(url, username, password)
            
            self.parent.current= 'Home'
            
            self.parent.parent.children[-1].children[0].icon= 'logout'    
            
            self.parent.parent.ids.qr_btn.disabled= False
            
            self.parent.parent.ids.branch_btn.disabled= False   
            
            self.parent.parent.ids.home_btn.disabled= False           

        except:
            
            self.children[-1].text= 'Login Incorrecto'
        

    def logout(self, app, home_btn, qr_btn, branch_btn, btn):
    
        app.logOut()
        
        btn.icon= 'account'
        
        home_btn.disabled= True
            
        qr_btn.disabled= True   
            
        branch_btn.disabled= True   
        
        
        
