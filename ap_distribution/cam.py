
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from pyzbar import pyzbar
import cv2
import models
from kivy.uix.button import Button


found = set()   


class  CamBox(BoxLayout):

    def __init__(self, user, **kwargs):
        super().__init__(**kwargs)
        
        self.user = user
        
        self.qr_code= ''
      
        self.on= True
      
        self.orientation='vertical'  
        
        self.cam=cv2.VideoCapture(0)   

        self.img=Image()      

        self.add_widget(self.img)
    
    def change_state(self,*args):
      
        if self.on == True:
           
            self.on = False
        else:
            self.on = True
        
    def callback(self, event):
        
        self.user.on_road(self.qr_code)   
        
        self.pop.dismiss(force=True) 
       
    def pop_cam(self, qr_text):
        
        self.on= False
        
        route= self.user.view_road(qr_text) 
        
        self.pop = Popup(size_hint=(None, None), size=(300, 200),)
        
        self.pop.title= route
        
        btn= Button(text= 'Recibir')
        
        btn.bind(on_press = self.callback)
        

        
        if route == 'Error!':
            
            self.pop.on_dismiss= self.change_state
            
            self.pop.open()
        
        else:
            self.pop.content= btn

            self.pop.on_dismiss= self.change_state
            
            self.pop.open()   

    def update(self,dt):
        
        if self.on:
            ret, frame = self.cam.read()    # retrieve frames from OpenCV camera
            
            if ret:
                buf1=cv2.flip(frame,0)      # convert it into texture 
                buf=buf1.tostring()
                image_texture=Texture.create(size=(frame.shape[1],frame.shape[0]),colorfmt='bgr')
                image_texture.blit_buffer(buf,colorfmt='bgr',bufferfmt='ubyte')
                self.img.texture=image_texture  # display image from the texture
                
                barcodes = pyzbar.decode(frame)     # detect barcode from image
                for barcode in barcodes:
                    (x, y, w, h) = barcode.rect
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                    if barcode.type == 'QRCODE':
                        
                        self.qr_code= barcode.data.decode("utf-8")
                        
                        self.pop_cam(self.qr_code)
        
    def stop_stream(self,*args):
        
        self.cam.release() 
        

    

    