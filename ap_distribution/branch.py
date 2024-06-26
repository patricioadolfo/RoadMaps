from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText, MDListItemTrailingIcon


class BranchScreen(MDScreen):
    
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
        
    def branch_nodes(self, screen_manager, branch_details):
        
        self.branch_details= branch_details
        
        self.screen_manager= screen_manager

        self.ids.mdlist.clear_widgets(self.ids.mdlist.children)
        
        if screen_manager.user.id_user != {}:
        
            nodes= screen_manager.user.nodes_origin
            
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
        
        self.parent.current= 'branchscreen'
        
        self.ids.branch_details_p.clear_widgets(self.ids.branch_details_p.children)
        
        self.ids.branch_details_c.clear_widgets(self.ids.branch_details_p.children)
                        
        