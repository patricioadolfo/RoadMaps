from kivymd.uix.screen import MDScreen

class HomeScreen(MDScreen):
    
    def count_routes(self,):
        
        self.ids.text_home.text= 'Hola '+ self.parent.user.id_user['username'] + '!!!'
        
        prepared= self.parent.user.view_road('?p=p!all')
        
        self.ids.prepared.text='Tienes '+ str(prepared['count']) + ' pedidos para retirar'
     
        on_road= self.parent.user.view_road('?c=c!all')
        
        self.ids.on_road.text='Tienes '+ str(on_road['count']) + ' pedidos entrgar'
    