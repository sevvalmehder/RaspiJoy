# Raspberry'de yapılacaklar

Bu tutorial Raspberry Pi Zero'yu simülatörda kullanılabilir konsol haline getirmek için yapılması gerekenleri anlatır.

### Adım 0

Son Raspian sürümünün indirilip, imaj SD karta yüklenir. Bu konuda Raspberry'nin hazırlamış olduğu [detaylı bir anlatım](https://www.raspberrypi.org/documentation/installation/installing-images/) bulunmaktadır.  

Not: Şubat 2016'da çıkan Kernal 4.4'e ihtiyacımız olduğu için güncel sürüm olması önemlidir. Güncel olmayan Raspian sürümünün güncellenmesi için:
```
$ sudo BRANCH=next rpi-update
```

### Adım 1

[Gbaman tarafından yazılan bir blog yazısında](https://blog.gbaman.info/?p=699) anlatıldığı üzere Linux USB Gadget modülleri kullanılarak, Pi Zero sanal insan arabirim cihazı (Human Interface Device) olarak, örneğin klavye, fare ve oyun konsolu olarak görünebilir. Bunun için config dosyası ve modüllerin düzenlenmesi işlemi şu şekilde yapılır:
```
$ echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
$ echo "dwc2" | sudo tee -a /etc/modules
$ sudo echo "libcomposite" | sudo tee -a /etc/modules
```

### Adım 2

Bir usb aygıt oluşturmak için birçok fonksiyon mevcuttur. Aygıt, hangi konfigürasyonların olacağına ve bunların hangi işlevleri sağlayacağına karar verilerek oluşturulur.  
Bu konfigürasyon işlemi için script oluşturulur ve çalıştırma yetkisi verilir:
```
$ sudo touch /usr/bin/raspijoy_usb
$ sudo chmod +x /usr/bin/raspijoy_usb
```

### Adım 3

Oluşturulan script Raspberry açılır açılmaz çalışmaya başlamalıdır. Bu nedenle /etc klasörü altındaki rc.local dosyası konsolda açılır:
```
$ sudo nano /etc/rc.local
```
Ve en alttaki "exit" satırının üstünde olacak şekilde şu satır eklenir:
```
/usr/bin/raspijoy_usb
```

### Adım 4
Konfigürasyon dosyasının(raspijoy_usb) yazılması işlemi gerçekleşir.

### Adım 5
Analog sinyal üreten analog kumanda kollarından veri okunabilmesi için ADC kullanılmalıdır. Bu projede MCP3008 isimli çip kullanılmıştır. Çip ile ilgili [bağlantı işlemi](https://github.com/sevvalmehder/RaspiJoy/blob/master/Connection%20Design/connection.jpg) gerçekleştikten sonra [Adafruit Tutorial](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008)'ındaki gerekli kurulumlar yapılır. Ardından veri gönderimi için [connect.py](https://github.com/sevvalmehder/RaspiJoy/blob/master/src/RaspberrySide/connect.py) kodu kullanılır.
