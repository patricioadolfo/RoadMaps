from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen
from scan import ScanAnalyze
from scan import QrCard
from login import Login
from branch import Branch, BranchDetails
import models


#from android.permissions import request_permissions, Permission

#request_permissions([Permission.CAMERA, Permission.INTERNET])

class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class BaseScreen(MDScreen):
    pass
    #image_size = StringProperty()
        

class RoadMapsApp(MDApp):
    
    def on_switch_tabs(self, bar: MDNavigationBar, item: MDNavigationItem, item_icon: str, item_text: str,):
        
        self.root.ids.screen_manager.current = item_text
              
    
    def build(self):
        
        self.user= models.User()  
        
        self.cam= ScanAnalyze()
        
        self.branch= Branch()
        
        self.cam.user = self.user
        
        self.branch.user = self.user  

        self.theme_cls.primary_palette = "Lightsteelblue"
       
        self.theme_cls.theme_style = "Light"    
 
        self.theme_cls.primary_hue = "A700"
        
        
        return Builder.load_file('home.kv')
    

RoadMapsApp().run()