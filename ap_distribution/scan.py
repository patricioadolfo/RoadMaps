from kivy.properties import ObjectProperty
from camera4kivy import Preview
from PIL import Image
from pyzbar.pyzbar import decode
from kivy.clock import mainthread
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
import threading
from time import sleep


class QrDialog(MDDialog):
                
    def text_card(self, dict, user):
        
        self.dict= dict
        
        self.user= user 
                
        detail_text= self.status(dict)
        
        self.ids.lb_box_card.text= detail_text
        
        if 'origin_name' in dict:
            
            self.ids.origin_dialog.text= 'De '+ dict['origin_name']
            
            self.ids.destin_dialog.text=  'Para '+ dict['destination_name']
                                 
    def close_card(self,):
        
        self.dismiss()      
                
    def status(self, dict):
        
        if 'status' in dict:
        
            if dict['status'] == 'p':
                
                self.ids.btn_rec.disabled= False
                
                detail_text= 'Envio n° {id}, preparado el dia {date} a las {time}'.format(
                    id= str(dict['id']),
                    date= dict['preparation_date'],
                    time= dict['preparation_time'],
                ) 
            
            elif dict['status'] == 'c':
                detail_text= 'Envio n° {id} en camino'.format(id= str(dict['id']))
            
            else:
                detail_text= 'Envio n° {id} recibido'.format(id= str(dict['id']))
            
            return detail_text
        
        if 'qr' in dict:
            
            detail_text= dict['qr'] + '\n' + dict['msj']
            
            return detail_text
            
    def receive_route(self):
    
        self.user.on_road(str(self.dict['id']))
        
        self.close_card()
             
class ScanAnalyze(Preview):
    
    extracted_data=ObjectProperty(None)
    
    def analyze_pixels_callback(self, pixels, image_size, image_pos, scale, mirror):
        
        pimage=Image.frombytes(mode='RGBA', size=image_size, data=pixels)
        
        list_of_all_barcodes=decode(pimage)
        
        if list_of_all_barcodes:
           
            if self.extracted_data:
     
                self.extracted_data(list_of_all_barcodes[0])
        
class QrScreen(MDScreen):
    
    text_qr=''
    
    def clear_qr_text(self,):
        
        sleep(5)
        
        self.text_qr= ''

    def on_focus(self,):
        
        self.ids.scan.connect_camera(enable_analyze_pixels = True ,default_zoom=0.0)
        
    def qr_result(self,):
        
        if self.parent.user.id_user != {}:
            
            self.qr_card= QrDialog()
     
            if self.text_qr != '':
            
                route= self.parent.user.view_road(self.text_qr)
                
                if route != 'Error!':
                
                    self.qr_card.text_card(route, self.parent.user)
                
                else:
                    self.qr_card.text_card(dict(qr= self.text_qr, msj= 'Qr Invalido'), self.parent.user)
  
            else:
                self.qr_card.text_card(dict(qr= self.text_qr, msj= 'Qr Invalido'), self.parent.user)
            
            self.qr_card.open()
            
            threading.Thread(target= self.clear_qr_text).start()
       
    def close_cam(self,):
        
        try:
            self.enable_analyze_pixels = False 
            
            self.ids.scan.disconnect_camera()
            
        except:
            print("fsdf")
            
    @mainthread
    def got_result(self, result):
        
        if self.text_qr != result.data.decode('utf-8'):
            
            self.text_qr = result.data.decode('utf-8')

            self.qr_result()


        
