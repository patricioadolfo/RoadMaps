from kivymd.uix.screen import MDScreen
from datetime import datetime
import time
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.badge import MDBadge
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText, MDListItemTrailingIcon
from kivymd.uix.divider import MDDivider


class HomeSnack(MDSnackbar):
    pass

            
class HomeScreen(MDScreen):
    
    def order_item(self, order, list):
           
        item= MDListItem(
                        MDListItemLeadingIcon(
                            icon='package-variant-plus',
                                ),
                        MDListItemTertiaryText(
                            text= str(order['id'])+' Para '+ order['destination_name'] + ', preparado el '+ order['preparation_date']
                        ),
                        ids= order,

                    )
        list.add_widget(item)
            
    def order_list(self,):

        
        self.ids.text_home.text= 'Hola '+ self.parent.user.id_user['username'] 
        
        snack= HomeSnack()
        
        snack.ids.snack_text.text='Actualizado: ' +  time.strftime("%H:%M:%S", time.localtime()) + ' ' + datetime.today().strftime('%d-%m-%Y')

        snack.open()
       
        self.ids.mdlist.clear_widgets(self.ids.mdlist.children)
        
        if self.parent.user.id_user != {}:
            
            on_road= self.parent.user.view_road('?q='+ str({"status":"c", "origin": self.parent.user.perfil}).replace("'",'"').replace(' ',''))
                       
            self.ids.mdlist.add_widget(
                MDListItem(
                    MDListItemHeadlineText(
                        text= 'Mis pedidos EN CAMINO',
                        halign= "center"
                        
                        ), 
                    MDListItemTrailingIcon(
                        MDBadge(
                          text= str(on_road['count'])  
                        ),
                        icon= 'information-variant',
                    )
                )
            )
            
            self.ids.mdlist.add_widget(MDDivider())
            
            for order in on_road['results']:

                self.order_item(order, self.ids.mdlist)
            
            receiver= self.parent.user.view_road('?q='+ str({"status":"p", "origin": self.parent.user.perfil}).replace("'",'"').replace(' ',''))
            
            self.ids.mdlist.add_widget(
                MDListItem(
                    MDListItemHeadlineText(
                        text= 'Mis pedidos PREPARADOS',
                        halign= "center"
                        ), 
                    MDListItemTrailingIcon(
                        MDBadge(
                          text= str(receiver['count'])  
                        ),
                        icon= 'information-variant',
                    )
                )
            )
            
            self.ids.mdlist.add_widget(MDDivider())
            
            for order in receiver['results']:

                self.order_item(order, self.ids.mdlist)
    
    def count_routes(self,):

        self.ids.text_home.text= 'Hola '+ self.parent.user.id_user['username'] 
        
        snack= HomeSnack()
        
        snack.ids.snack_text.text='Actualizado: ' +  time.strftime("%H:%M:%S", time.localtime()) + ' ' + datetime.today().strftime('%d-%m-%Y')

        snack.open()
        
        prepared= self.parent.user.view_road('?q='+ str({"status":"p", "origin": self.parent.user.perfil}).replace("'",'"').replace(' ',''))
        
        badge= MDBadge()
        
        badge.text= str(prepared['count'] )
        
        self.ids.icon_prep.add_widget(badge)    
        
        self.ids.text_prepared.text='Mis pedidos PREPARADOS'
        
        on_road= self.parent.user.view_road('?q='+ str({"status":"c", "origin": self.parent.user.perfil}).replace("'",'"').replace(' ',''))
        
        badge_p= MDBadge()
        
        badge_p.text= str(on_road['count'] )
        
        self.ids.icon_onroad.add_widget(badge_p)
        
        self.ids.text_onroad.text='Mis pedidos EN CAMINO'
        

        



