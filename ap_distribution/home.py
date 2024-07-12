from kivymd.uix.screen import MDScreen
from datetime import datetime
import time
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.badge import MDBadge

class HomeSnack(MDSnackbar):
    pass

            
class HomeScreen(MDScreen):
    
    def count_routes(self,):

        self.ids.text_home.text= 'Hola '+ self.parent.user.id_user['username'] 
        
        snack= HomeSnack()
        
        snack.ids.snack_text.text='Actualizado: ' +  time.strftime("%H:%M:%S", time.localtime()) + ' ' + datetime.today().strftime('%d-%m-%Y')

        snack.open()
        
        prepared= self.parent.user.view_road('?p=p!all')
        
        badge= MDBadge()
        
        badge.text= str(prepared['count'] )
        
        if prepared['count'] != 0:
            
            if self.ids.icon_prep.children == []:

                self.ids.icon_prep.add_widget(badge)                
        
            self.ids.text_prepared.text='Tienes '+ str(prepared['count']) + ' pedidos preparados para retirar'
        
        else: 
            
            if self.ids.icon_prep.children != []:
                
                self.ids.icon_prep.clear_widgets(self.ids.icon_prep.children)
                
            self.ids.text_prepared.text='No tienes pedidos preparados para retirar' 

        
        on_road= self.parent.user.view_road('?c=c!all')
        
        badge_p= MDBadge()
        
        badge_p.text= str(on_road['count'] )
        
        if on_road['count'] != 0:
            
            if self.ids.icon_onroad.children == []:
                
                self.ids.icon_onroad.add_widget(badge_p)
   
            self.ids.text_onroad.text='Tienes '+ str(on_road['count']) + ' pedidos en camino para entregar'
        
        else: 
            
            if self.ids.icon_onroad.children != []:
                
                self.ids.icon_onroad.clear_widgets(self.ids.icon_onroad.children)
                
            self.ids.text_onroad.text='No tienes pedidos en camino para entregar' 
        



