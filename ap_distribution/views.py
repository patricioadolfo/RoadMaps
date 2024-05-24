import models
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from cam import CamBox


class Main(Screen):
    

    def go_cam(self, body):
                
        self.cam= CamBox(sm.user)
        
        body.add_widget(self.cam)
        
        Clock.schedule_interval(self.cam.update, 1.0/30) 

    def logOut(self, body):
        
        sm.user.logOut()
        
        self.cam.stop_stream()
        
        body.clear_widgets()
        
        sm.current= "login"

    def view_list(self,box, node):
        
        list= sm.user.view_list(node)
        
        for x in list:
              
            x= Label(text= 'Id: ' + str(x['id']) + 'Origen : '+ str(x['origin_name']))
            
            box.add_widget(x)

    def view_nodes(self, drop, btn):
            
        for node in sm.user.origin:
            print(node)
            node= Button(text= node['name'])
            
            drop.add_widget(node)
 


        
class Login(Screen):
    
    def invalidLogin(self,):
    
        pop = Popup(title='Login incorrecto',
                    content=Label(text='Usuario o contraseña incorrecto.'),
                    size_hint=(None, None), size=(300, 200))
        pop.open()
       

    def login(self, username, password):
        
        try:
        
            username= username._get_text()
            
            password= password._get_text()
            
            sm.user.log(username, password)
            
            sm.current="main"
            
            
        except:
            
            self.invalidLogin()


class WindowManager(ScreenManager):

    user= models.User()

kv = Builder.load_file('views.kv')
sm = WindowManager()

screens = [Login(name="login"),Main(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class UserAp(App):       
    
    def build(self,):
        return sm

UserAp().run()