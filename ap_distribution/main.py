from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationItem
from kivymd.uix.screen import MDScreen
from scan import QrScreen, QrDialog, ScanAnalyze
from login import LoginScreen
from branch import BranchScreen, BranchDetails
from home import HomeScreen, HomeSnack
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
            
            self.current= 'loginscreen' 
            
            log.icon= 'account-circle-outline'
            
            for btn in btns:
                
                btn.disabled= True

    user= models.User()

class RoadMapsApp(MDApp):
               
    
    def build(self):

        self.theme_cls.primary_palette = "Blue"
        
        self.set_bars_colors()
       
        self.theme_cls.theme_style = "Dark"    
        
        print(self.theme_cls.primaryColor)
 
        self.theme_cls.primary_hue = "A700"
           
        return Builder.load_file('kv.kv')
    
    def switch_theme_style(self):
        
        if self.theme_cls.theme_style == "Dark":
            
            self.theme_cls.theme_style= 'Light'
            self.root.ids.title_ap.md_bg_color=  [0.047058823529411764, 0.403921568627451, 0.5019607843137255, 1.0]
        
        else:
            self.theme_cls.theme_style = "Dark"
            self.root.ids.title_ap.md_bg_color=  [0.047058823529411764, 0.403921568627451, 0.5019607843137255, 1.0]
           
    def set_bars_colors(self):
        
        set_bars_colors(
            [0.047058823529411764, 0.403921568627451, 0.5019607843137255, 1.0],  # status bar color
            [0.047058823529411764, 0.403921568627451, 0.5019607843137255, 1.0],  # navigation bar color
            "Dark",      # icons color of status bar
        )
    


RoadMapsApp().run()