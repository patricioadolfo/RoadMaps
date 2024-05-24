""">>> import requests
>>> from requests.auth import HTTPBasicAuth
>>> auth = HTTPBasicAuth('Route@dmin', 'rA5390202')
>>> print(requests.get('http://127.0.0.1:8000/api/api-route/27/', auth=auth))
<Response [200]>
>>> r=requests.get('http://127.0.0.1:8000/api/api-route/27/', auth=auth)
>>> print(r.text)
{"id":27,"origin_name":"Central","destination_name":"Jure","description":"Envio 7898646","barcode":456464,"preparation_date":"2024-04-14","preparation_time":"19:51:59","state":"r","origin":1,"destination":2}
>>> print(r.json)
<bound method Response.json of <Response [200]>>
>>> print(r.json())
{'id': 27, 'origin_name': 'Central', 'destination_name': 'Jure', 'description': 'Envio 7898646', 'barcode': 456464, 'preparation_date': '2024-04-14', 'preparation_time': '19:51:59', 'state': 'r', 'origin': 1, 'destination': 2}
>>> payload = {'state': 'p'}
>>> p = requests.post('http://127.0.0.1:8000/api/api-route/27/', json=payload, auth= auth)
>>> print(p.text)
{"detail":"Método \"POST\" no permitido."}
>>> p = requests.put('http://127.0.0.1:8000/api/api-route/27/', json=payload, auth= auth)
>>> print(p.text)
{"description":["Este campo es requerido."],"barcode":["Este campo es requerido."]}
>>> p = requests.patch('http://127.0.0.1:8000/api/api-route/27/', json=payload, auth= auth)
>>> print(p.text)
{"id":27,"origin_name":"Central","destination_name":"Jure","description":"Envio 7898646","barcode":456464,"preparation_date":"2024-04-14","preparation_time":"19:51:59","state":"p","origin":1,"destination":2}
>>> payload = {'state': 'c'}
>>> p = requests.patch('http://127.0.0.1:8000/api/api-route/27/', json=payload, auth= auth)
>>> print(p.json())
{'id': 27, 'origin_name': 'Central', 'destination_name': 'Jure', 'description': 'Envio 7898646', 'barcode': 456464, 'preparation_date': '2024-04-14', 'preparation_time': '19:51:59', 'state': 'c', 'origin': 1, 'destination': 2}"""


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy_garden.zbarcam import ZBarCam

class QrScanner(BoxLayout):
    def __init__(self, **kwargs):
        super(QrScanner, self).__init__(**kwargs)
        btn1 = Button(text='Scan Me',  font_size="50sp")
        btn1.bind(on_press=self.callback)
        self.add_widget(btn1)

    def callback(self, instance):
        """On click button, initiate zbarcam and schedule text reader"""
        self.remove_widget(instance) # remove button
        self.zbarcam = ZBarCam()
        self.add_widget(self.zbarcam)
        Clock.schedule_interval(self.read_qr_text, 1)

    def read_qr_text(self, *args):
        """Check if zbarcam.symbols is filled and stop scanning in such case"""
        if(len(self.zbarcam.symbols) > 0): # when something is detected
            self.qr_text = self.zbarcam.symbols[0].data # text from QR
            print(self.qr_text)
            Clock.unschedule(self.read_qr_text, 1)
            self.zbarcam.stop() # stop zbarcam
            self.zbarcam.ids['xcamera']._camera._device.release() # release camera
            self.callback


#class QrApp(App):
#    def build(self):
#        return QrScanner()

#if __name__ == '__main__':
#    QrApp().run()

