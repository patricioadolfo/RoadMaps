from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText, MDListItemTrailingIcon
from kivymd.uix.badge import MDBadge
from kivymd.uix.divider import MDDivider
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.menu import MDDropdownMenu

class OrderSnack(MDSnackbar):
    pass

class OrdersScreen(MDScreen):
    
    
    def order_item(self, order, list):
           
        item= MDListItem(
                        MDListItemLeadingIcon(
                            icon='package-variant-plus',
                                ),
                        MDListItemSupportingText(
                            text= '## '+ str(order['id']),
                        ),
                        MDListItemTertiaryText(
                            text= 'De '+ order['origin_name'] + ', preparado el '+ order['preparation_date']
                        ),
                        ids= order,
                    )
        list.add_widget(item)
            
    def order_list(self,):
       
        self.ids.mdlist.clear_widgets(self.ids.mdlist.children)
        
        if self.parent.user.id_user != {}:
            
            on_road= self.parent.user.view_road('?q='+ str({"status":"c", "destination": self.parent.user.perfil}).replace("'",'"').replace(' ',''))
            
            if on_road['count'] != 0:
                
                text_headeer= 'Tienes '+ str(on_road['count']) + ' pedidos en camino para recibir'
            
            else:
                
                text_headeer= 'No tienes pedidos en camino para recibir'
                       
            self.ids.mdlist.add_widget(
                MDListItem(
                    MDListItemHeadlineText(
                        text= text_headeer,
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
            
            receiver= self.parent.user.view_road('?q='+ str({"status":"p", "destination": self.parent.user.perfil}).replace("'",'"').replace(' ',''))
            
            if receiver['count'] != 0:
                text_headeer= 'Tienes '+ str(receiver['count']) + ' pedidos preprados para recibir'
            else:
                text_headeer= 'No tienes pedidos a preparados para recibir'
            
            self.ids.mdlist.add_widget(
                MDListItem(
                    MDListItemHeadlineText(
                        text= text_headeer,
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
                
                                
class OrderCreate(MDScreen):
    
    def create_order(self,):
        
        snack =OrderSnack()
        
        try: 
            create = self.parent.user.route_create(self.ids.text_detail.text, self.ids.drop_text.ids)

            if create == 400:
                
                snack.ids.order_snack_text.text= 'Complete los campos'
                
            else:
                
                snack.ids.order_snack_text.text= 'Envio creado'
                
                self.ids.drop_text.text= 'Destino'
                
                self.ids.text_detail.text= ''
            
            snack.open()
        
        except:
            snack.ids.order_snack_text.text= 'Complete los campos'           
            snack.open()
     
    def open_menu(self, item):
        
        menu_items= []
        
        for i in self.parent.user.nodes_destin:
            
            menu_items.append(
                {        
                "text": i['name'],
                'ids': i,
                "on_release": lambda x= i: self.menu_callback(x) 
                }
            )

        MDDropdownMenu(caller=item, items=menu_items).open()

    def menu_callback(self, text_item):
        
        self.ids.drop_text.text = text_item['name']
        
        self.ids.drop_text.ids= text_item
        