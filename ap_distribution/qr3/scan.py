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
               
    def close_card(self, *args):
        
        self.parent.remove_widget(self)
        
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
    
        self.parent.user.on_road(str(self.dict['id']))
        
        self.parent.remove_widget(self)
        
class ScanAnalyze(Preview):
    
    extracted_data=ObjectProperty(None)
    
    def analyze_pixels_callback(self, pixels, image_size, image_pos, scale, mirror):
        
        pimage=Image.frombytes(mode='RGBA',size=image_size,data=pixels)
        
        list_of_all_barcodes=decode(pimage)
        
        if list_of_all_barcodes:
           
            if self.extracted_data:
     
                self.extracted_data(list_of_all_barcodes[0])
    
    @mainthread
    def got_result(self,result):

        self.lb_cam.text=result.data.decode('utf-8')

        self.lb_cam.color= 'white'
    
    def run(self, box):
        
        box.clear_widgets(box.children)
        
        self.connect_camera(enable_analyze_pixels = True ,default_zoom=0.0)

        self.aspect_ratio='16:9'
        
        self.extracted_data=self.got_result
        
        box_label=BoxLayout(
                            orientation= 'horizontal',
                            size_hint= (.7, .2),
                            pos_hint= {'center_x': .5,'center_y': .2},
                            spacing= '15dp'
                            ) 
      
        self.lb_cam= MDLabel(
                             text= '',
                             bold= True,
                             font_style= "Headline",
                             role= "small",
                             size_hint_x= .7,
                             pos_hint= {'center_x': .5,'center_y': .5}
                             )
        
        btn_cam= MDIconButton(
                              icon= "arrow-right-bold-circle",
                              style= "filled",
                              size= ("90dp", "90dp"),
                              size_hint_x= .3,
                              halign= "center",
                              pos_hint= {'center_x': .5,'center_y': .5},
                              on_press= self.qr_result
                              )
        
        
        box_label.add_widget(self.lb_cam)
        
        box_label.add_widget(btn_cam)
        
        box.add_widget(self)
        
        box.add_widget(box_label)
   
    def qr_result(self, *args):
        
        if self.user.id_user != {}:
            
            id= self.lb_cam.text
            
            if id != '':
            
                route= self.user.view_road(id)
                
                if route != 'Error!':
                
                    qr_card= QrCard()
                
                    qr_card.text_card(route)
                
                    self.add_widget(qr_card)
                
                else:
                    self.lb_cam.text= 'Qr Invalido'
  
            else:
                self.lb_cam.text= 'Qr Invalido'
            
        else:
            self.lb_cam.text= 'Inicie Sesion'

    def close_cam(self, box):
        
        try:
            self.enable_analyze_pixels = False 
            
            self.disconnect_camera()
            
            box.clear_widgets(box.children)
        
        except:
            print("fsdf")

        

        
