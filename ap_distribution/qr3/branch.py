from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText, MDListItemTrailingIcon
from kivymd.uix.card import MDCard



class Branch(MDScreen):
    
    def node_details(self, instance, *args):

        prepared= self.user.view_road('?p=p!'+ str(instance.ids['id']))
        
        on_road= self.user.view_road('?c=c!'+ str(instance.ids['id']))
        
        card= BranchCard()
        
        card.open_branch_card(prepared['results'],on_road['results'], instance.ids['name'])
        
        self.box.add_widget(card)
    
    def branch_nodes(self, box):
        
        self.box= box
        
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
                


        else:
            print(box.parent.parent.children)
            print(box.parent.parent.parent.children)

                
class BranchCard(MDCard):
    
    
    def open_branch_card(self, p_items, c_items, name):
        
        self.ids.branch_card_lb.text= name
        
        for item in p_items:
            
            self.ids.card_branch_p.add_widget(MDListItem(
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
                                                    ))
        
        for item in c_items:
            
            self.ids.card_branch_c.add_widget(MDListItem(
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
    
    def close_card(self, *args):
        
        self.parent.remove_widget(self)
                        
        