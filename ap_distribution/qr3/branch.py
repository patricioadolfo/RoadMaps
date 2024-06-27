from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText, MDListItemTrailingIcon


class Branch(MDScreen):
    
    def node_details(self, instance, *args):

        prepared= self.user.view_road('?p=p!'+ str(instance.ids['id']))
        
        on_road= self.user.view_road('?c=c!'+ str(instance.ids['id']))
             
        self.box_details.ids.branch_details_lb.text= instance.ids['name']

        for item in prepared['results']:
            
            self.box_details.ids.branch_details_p.add_widget(MDListItem(
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
            
            self.box_details.ids.branch_details_c.add_widget(MDListItem(
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
        
        self.box.parent.current= 'Sucursal-detail'
        
    def branch_nodes(self, box, box_details):
        
        self.box= box
        
        self.box_details= box_details
        
        box.ids.mdlist.clear_widgets(box.ids.mdlist.children)
        
        if self.user.id_user != {}:
        
            nodes= self.user.nodes_origin
            
            for node in nodes:
                box.ids.mdlist.add_widget(MDListItem(
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
    
    def close_card(self, *args):
        
        self.parent.current= 'Sucursales'
        
        self.ids.branch_details_p.clear_widgets(self.ids.branch_details_p.children)
        
        self.ids.branch_details_c.clear_widgets(self.ids.branch_details_p.children)
                        
        