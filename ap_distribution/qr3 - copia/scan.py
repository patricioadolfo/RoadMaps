from kivy.properties import ObjectProperty
from camera4kivy import Preview
from PIL import Image
from pyzbar.pyzbar import decode
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.screen import MDScreen


class QrCard(MDCard):
                
    def text_card(self, dict):
        
        self.dict= dict
        
        self.status()
        
        origin= 'De: '+dict['origin_name']
        
        destin= 'Para: '+dict['destination_name']
        
        preparation= 'Preparado: '+ dict['preparation_date']
        
        time= 'A las: ' + dict['preparation_time']
        
        info= origin + '\n' + destin + '\n' + preparation + '\n' + time + '\n'
        
        self.ids.lb_box_card.text= info
               
    def close_card(self,):
  
        self.parent.remove_widget(self)
        print(self.ids)
        
    def status(self,):
        
        btn_rec= MDButton(
                        MDButtonIcon(
                            icon="package-variant-closed-plus",
                        ),
                        MDButtonText(
                            text="Recibir",
                        ),
                        style="elevated",   
                        pos_hint= {'center_x': .5, 'center_y': .9},   
                        on_press= self.receive_route
                        )
        
        if self.dict['status'] == 'p':
            
            self.ids.box_qr_card.add_widget(btn_rec) 
            
            self.ids.lb_box_card.text= 'Recibir'
        
        elif self.dict['status'] == 'c':
            self.ids.lb_box_card.text= 'En camino'
        
        else:
            self.ids.lb_box_card.text= 'Recibido'
            
    def receive_route(self, *args):
    
        self.parent.parent.user.on_road(str(self.dict['id']))
        
        self.parent.remove_widget(self)
        
class ScanAnalyze(Preview):
    
    extracted_data=ObjectProperty(None)
    
    def analyze_pixels_callback(self, pixels, image_size, image_pos, scale, mirror):
        
        pimage=Image.frombytes(mode='RGBA',size=image_size,data=pixels)
        
        list_of_all_barcodes=decode(pimage)
        
        if list_of_all_barcodes:
           
            if self.extracted_data:
     
                self.extracted_data(list_of_all_barcodes[0])


        
class QrScreen(MDScreen):

    def on_focus(self,):
        
        self.ids.scan.connect_camera(enable_analyze_pixels = True ,default_zoom=0.0)
        
    def qr_result(self,):
        
        if self.parent.user.id_user != {}:
            
            id= self.ids.lab_qr.text
            
            if id != '':
            
                route= self.parent.user.view_road(id)
                
                if route != 'Error!':
                
                    qr_card= QrCard()
                
                    qr_card.text_card(route)
                
                    self.add_widget(qr_card)
                
                else:
                    self.ids.lab_qr.text= 'Qr Invalido'
  
            else:
                self.ids.lab_qr.text= 'Qr Invalido'
            
        else:
            self.ids.lab_qr.text= 'Inicie Sesion'
       
    def close_cam(self,):
        
        try:
            self.enable_analyze_pixels = False 
            
            self.ids.scan.disconnect_camera()
            
        except:
            print("fsdf")
            
    @mainthread
    def got_result(self, result):
        
        if self.ids.lab_qr.text != result.data.decode('utf-8'):
            
            self.ids.lab_qr.text=result.data.decode('utf-8')

            self.qr_result()


        
