from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText, MDListItemTrailingIcon


class BranchScreen(MDScreen):
    
    def node_details(self, instance, *args):
        
        try:

            prepared= self.parent.user.view_road('?q='+ str({"status":"p", "origin": instance.ids['id']}).replace("'",'"').replace(' ',''))
                                                        
            
            on_road= self.parent.user.view_road('?q='+ str({"status":"c", "destination": instance.ids['id']}).replace("'",'"').replace(' ',''))
                
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
        

        
            self.parent.current= 'branchdetailsscreen'
            
        except:
            
            self.parent.go_snack('Error de conexión')
        
    def branch_nodes(self, branch_details):
           
        self.branch_details= branch_details

        self.ids.mdlist.clear_widgets(self.ids.mdlist.children)
        
        if self.parent.user.id_user != {}:
        
            nodes= self.parent.user.nodes_origin
            
            for node in nodes:
                self.ids.mdlist.add_widget(MDListItem(
                    MDListItemLeadingIcon(
                        icon='map-marker-radius-outline',
                            ),
                            MDListItemHeadlineText(
                                text= node['name'],
                            ),
                            MDListItemSupportingText(
                                text= node['address'],
                            ),
                            MDListItemTertiaryText(
                                text= node['phoneNumber'],
                            ),
                            MDListItemTrailingIcon(
                                icon="view-sequential-outline",
                            ),
                            ids= node,
                            on_press= self.node_details
                        ))

                
class BranchDetails(MDScreen):
    
    def back_branchsecreen(self, *args):
            
        self.ids.branch_details_p.clear_widgets(self.ids.branch_details_p.children)
        
        self.ids.branch_details_c.clear_widgets(self.ids.branch_details_c.children)
        
        self.parent.current= 'branchscreen'