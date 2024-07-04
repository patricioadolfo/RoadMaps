from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationItem
from kivymd.uix.screen import MDScreen
from scan import QrScreen, QrCard, ScanAnalyze
from login import LoginScreen, LogOutScreen
from branch import BranchScreen, BranchDetails
from home import HomeScreen
import models   
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.utils.set_bars_colors import set_bars_colors


#from android.permissions import request_permissions, Permission

#request_permissions([Permission.CAMERA, Permission.INTERNET])

class BaseMDNavigationItem(MDNavigationItem):
    
    icon = StringProperty()
    text = StringProperty()
 

class RmScreenManager(MDScreenManager):
    
    def login_out(self, log, btns):
        
        if log.icon == 'account-circle-outline':
           
           self.current= 'loginscreen'
           
        else:
            self.user.logOut()
            
            self.current= 'logoutscreen' 
            
            log.icon= 'account-circle-outline'
            
            for btn in btns:
                
                btn.disabled= True

    user= models.User()

class RoadMapsApp(MDApp):
               
    
    def build(self):

        self.theme_cls.primary_palette = "Skyblue"
        
        self.set_bars_colors()
       
        self.theme_cls.theme_style = "Light"    
 
        self.theme_cls.primary_hue = "A700"
        
        print(self.theme_cls.primaryColor)
           
        return Builder.load_file('home.kv')
    
    def switch_theme_style(self):
        
        if self.theme_cls.theme_style == "Dark":
            
             self.theme_cls.theme_style= 'Light'
             self.root.ids.title_ap.md_bg_color=  [0.047058823529411764, 0.403921568627451, 0.5019607843137255, 1.0]
        
        else:
            self.theme_cls.theme_style = "Dark"
            self.root.ids.title_ap.md_bg_color=  [0.047058823529411764, 0.403921568627451, 0.5019607843137255, 1.0]
        
    
    def set_bars_colors(self):
        
        set_bars_colors(
            self.theme_cls.primaryColor,  # status bar color
            self.theme_cls.primaryColor,  # navigation bar color
            "Dark",      # icons color of status bar
        )
    

RoadMapsApp().run()