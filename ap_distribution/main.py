from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationItem
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.utils.set_bars_colors import set_bars_colors
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.snackbar import MDSnackbar

from scan import QrScreen, QrDialog, ScanAnalyze
from login import LoginScreen
from branch import BranchScreen, BranchDetails
from home import HomeScreen
import models  

#from android.permissions import request_permissions, Permission

#request_permissions([Permission.CAMERA, Permission.INTERNET])


class Snack(MDSnackbar):
    pass

class BaseMDNavigationItem(MDNavigationItem):
    
    icon = StringProperty()
    text = StringProperty()
 

class RmScreenManager(MDScreenManager):
    
    def login_out(self, log, btns):
        
        if log.icon == 'account-circle-outline':
           
           self.current= 'loginscreen'
           
        else:
            
            try:
                
                self.user.logOut()
            
            except:
                
                self.go_snack('Error de conexión')
            
            self.current= 'loginscreen' 
            
            log.icon= 'account-circle-outline'
            
            for btn in btns:
                
                btn.disabled= True
                
    def go_snack(self, mnj):
        
        self.snack= Snack()
        
        self.snack.ids.snack_text.text= mnj
        
        self.snack.open()

    user= models.User()

class RoadMapsApp(MDApp):
    
    icon= 'truck.png'       
    
    store = JsonStore('load.json')
    
    
    def load_log(self,):
        
        try:
        
            self.user = self.store.get('log')['name']   
            
            self.passwd= self.store.get('log')['pswd']
            
            self.ip= self.store.get('log')['ip']
        
        except:
            
            self.user = ''   
            
            self.passwd= ''
            
            self.ip= ''
    
    def build(self):

        self.theme_cls.primary_palette = "Aliceblue"
        
        self.set_bars_colors()
       
        self.theme_cls.theme_style = "Dark"    
 
        self.theme_cls.primary_hue = "A700"
        
        self.load_log()

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
    
if __name__ == "__main__":
    
    RoadMapsApp().run()