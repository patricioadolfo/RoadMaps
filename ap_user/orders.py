from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText, MDListItemTrailingIcon
from kivymd.uix.badge import MDBadge

class OrdersScreen(MDScreen):
    
    def node_details(self, instance, *args):

        prepared= self.screen_manager.user.view_road('?p=p!'+ str(instance.ids['id']))
        
        on_road= self.screen_manager.user.view_road('?c=c!'+ str(instance.ids['id']))
             
        self.branch_details.ids.branch_details_lb.text= instance.ids['name']
        
        for item in prepared['results']:
            
            self.branch_details.ids.branch_details_p.add_widget(MDListItem(
                                                        MDListItemHeadlineText(
                                                            text= '###'+ str(item['id']),
                                                        ),
                                                        MDListItemSupportingText(
                                                            text= '     Para: '+item['destination_name'],
                                                        ),
                                                        MDListItemTertiaryText(
                                                            text= '         Preparado: '+item['preparation_date'],
                                                        ),
                                                        MDListItemTrailingIcon(
                                                            icon="package-variant-closed-plus",
                                                        ),
                                                    )
                                              )

        
        for item in on_road['results']:
            
            self.branch_details.ids.branch_details_c.add_widget(MDListItem(
                                                        MDListItemHeadlineText(
                                                            text= '###'+ str(item['id']),
                                                            ),
                                                        MDListItemSupportingText(
                                                            text= '     De: '+item['origin_name'],
                                                            ),
                                                        MDListItemTertiaryText(
                                                            text= '         Preparado: '+item['preparation_date'],
                                                            ),
                                                        MDListItemTrailingIcon(
                                                            icon="package-variant-minus",
                                                            ),
                                                        ))
        

        
        self.screen_manager.current= 'branchdetailsscreen'
        
    def order_list(self, branch_details):
        
        self.branch_details= branch_details
        
        self.ids.mdlist.clear_widgets(self.ids.mdlist.children)
        
        if self.parent.user.id_user != {}:
            
            receiver= self.parent.user.view_road('?d=c!'+ str(self.parent.user.perfil))
        
            nodes= self.parent.user.nodes_origin
            
            if receiver['count'] != 0:
                text_headeer= 'Tienes '+ str(receiver['count']) + ' pedidos para recibir'
            else:
                text_headeer= 'No tienes pedidos a recibir'
            
            self.ids.mdlist.add_widget(
                MDListItem(
                    MDListItemHeadlineText(
                        text= text_headeer
                        ), 
                    MDListItemTrailingIcon(
                        MDBadge(
                          text= str(receiver['count'])  
                        ),
                        icon= 'information-variant',
                    )
                )
            )
            
            for order in receiver['results']:
                
                if order['status'] == 'p':
                    status= 'Preprado'
                else:
                    status= 'En camino' 
                
                self.ids.mdlist.add_widget(MDListItem(
                                                MDListItemLeadingIcon(
                                                    icon='package-variant-plus',
                                                        ),
                                                MDListItemSupportingText(
                                                    text= '## '+ str(order['id']),
                                                ),
                                                MDListItemTertiaryText(
                                                    text= 'De '+ order['origin_name'] + '   Estdo: '+ status
                                                ),
                                                MDListItemTrailingIcon(
                                                    icon="view-sequential-outline",
                                                ),
                                                ids= order,
                                               # on_press= self.node_details
                                            ))

                
class BranchDetails(MDScreen):
    
    def back_branchsecreen(self, *args):
        
        
        self.ids.branch_details_p.clear_widgets(self.ids.branch_details_p.children)
        
        self.ids.branch_details_c.clear_widgets(self.ids.branch_details_c.children)
        
        self.parent.current= 'branchscreen'