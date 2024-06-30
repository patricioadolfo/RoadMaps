from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationItem
from kivymd.uix.screen import MDScreen
from scan import QrScreen, QrCard, ScanAnalyze
from login import LoginScreen, LogOutScreen
from branch import BranchScreen, BranchDetails
import models   
from kivymd.uix.screenmanager import MDScreenManager


#from android.permissions import request_permissions, Permission

#request_permissions([Permission.CAMERA, Permission.INTERNET])

class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()

class HomeScreen(MDScreen):
    
    pass


class RmScreenManager(MDScreenManager):
    
    def login_out(self, log, btns):
        
        if log.icon == 'account':
           
           self.current= 'loginscreen'
           
        else:
            self.user.logOut()
            
            self.current= 'logoutscreen' 
            
            log.icon= 'account'
            
            for btn in btns:
                
                btn.disabled= True

    user= models.User()

class RoadMapsApp(MDApp):
               
    
    def build(self):

        self.theme_cls.primary_palette = "Lightsteelblue"
       
        self.theme_cls.theme_style = "Light"    
 
        self.theme_cls.primary_hue = "A700"
           
        return Builder.load_file('home.kv')
    

RoadMapsApp().run()