from kivymd.uix.screen import MDScreen
from datetime import datetime
import time
from kivymd.uix.snackbar import MDSnackbar

class HomeSnack(MDSnackbar):
    pass

            
class HomeScreen(MDScreen):
    
    def count_routes(self,):

        self.ids.text_home.text= 'Hola '+ self.parent.user.id_user['username'] 
        
        snack= HomeSnack()
        
        snack.ids.snack_text.text='Actualizado: ' +  time.strftime("%H:%M:%S", time.localtime()) + ' ' + datetime.today().strftime('%d-%m-%Y')

        snack.open()
        
        prepared= self.parent.user.view_road('?p=p!all')
        
        if prepared['count'] != 0:
            
            self.ids.badge_prep.text= str(prepared['count'])
        
        self.ids.text_prepared.text='Tienes '+ str(prepared['count']) + ' pedidos para retirar'
        
        
        on_road= self.parent.user.view_road('?c=c!all')
        
        if on_road['count'] != 0:
            
            self.ids.badge_onroad.text= str(on_road['count'])
        
        self.ids.text_onroad.text='Tienes '+ str(on_road['count']) + ' pedidos para entregar'
        



