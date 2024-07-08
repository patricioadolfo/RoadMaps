from kivymd.uix.screen import MDScreen
import asynckivy
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.list import MDListItemTrailingIcon
from kivy.uix.behaviors import ButtonBehavior


class TrailingPressedIconButton(
    ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
):
    ...


class ExpansionPanelItem(MDExpansionPanel):
    
    def tap_expansion_chevron(
            self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
        ):
            Animation(
                padding=[0, dp(12), 0, dp(12)]
                if not panel.is_open
                else [0, 0, 0, 0],
                d=0.2,
            ).start(panel)
            panel.open() if not panel.is_open else panel.close()
            panel.set_chevron_down(
                chevron
            ) if not panel.is_open else panel.set_chevron_up(chevron)




class HomeScreen(MDScreen):
    
    def count_routes(self,):
        
        self.ids.text_home.text= 'Hola '+ self.parent.user.id_user['username'] 
        
        prepared= self.parent.user.view_road('?p=p!all')
        
        self.ids.prepared.text='Tienes '+ str(prepared['count']) + ' pedidos para retirar'
     
        on_road= self.parent.user.view_road('?c=c!all')
        
        self.ids.on_road.text='Tienes '+ str(on_road['count']) + ' pedidos entrgar'
    
    def on_start(self):
        async def set_panel_list():
            for i in range(6):
                await asynckivy.sleep(0)
                self.ids.container.add_widget(ExpansionPanelItem())

        asynckivy.start(set_panel_list())   
        

