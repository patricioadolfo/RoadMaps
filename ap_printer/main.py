from model import SrvPrinter
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText, MDListItemTrailingCheckbox
import threading



class Check(MDListItemTrailingCheckbox):
    pass

class AppPrinter(MDApp):
    
    def on_stop(self):

        self.srv.stop_receive()
    
    def on_checkbox_active(self, checkbox, value):
        
        if value:
            
            self.srv.set_printers(checkbox.parent.parent.children[1].children[0].children[0].text)
           
    def list_printers(self,):
        
        printers= self.srv.get_printers()
    
        for printer in printers:
        
            self.root.ids.mdlist.add_widget(MDListItem(
                                                MDListItemLeadingIcon(  
                                                    icon= 'printer'),
                                                MDListItemHeadlineText(
                                                    text= str(printer[0]),
                                                    ),
                                                MDListItemSupportingText(
                                                    text= printer[1],
                                                    ),
                                                MDListItemTertiaryText(
                                                    text= printer[2],
                                                    ),
                                                Check(
                                                    ),
                                                ))
    
    def build(self,):
        
        self.srv= SrvPrinter()
        
        self.srv.password()
        
        threading.Thread(target= self.srv.receive).start()

        return Builder.load_file('kv.kv')
    
AppPrinter().run()