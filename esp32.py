from machine import ADC, Pin, PWM
from time import sleep
import network
import socket

# ---- Wi-Fi Bilgileri ----
SSID = "BSSID"
PASSWORD = "Password"

# ---- Sensör ve Buzzer Tanımları ----
# Toprak nem sensörü pini (GPIO32)
soil_moisture_pin = ADC(Pin(32))
soil_moisture_pin.atten(ADC.ATTN_11DB)

# Buzzer pini (GPIO4)
buzzer = PWM(Pin(4))

# Buzzer frekans ve görev döngüsü
def buzzer_alert(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(32768)  # Orta seviyede ses çıkışı
    sleep(duration)
    buzzer.duty_u16(0)  # Sesi kapat

# ---- Wi-Fi Bağlantısı ----
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Wi-Fi bağlanıyor...")
        sleep(1)
    print("Wi-Fi bağlantısı kuruldu:", wlan.ifconfig())

# ---- Nem Sensörü ve Buzzer Kontrolü ----
def read_soil_moisture():
    try:
        value = soil_moisture_pin.read()
        print(f"Toprak Nem Değeri: {value}")
        
        # Buzzer uyarısı
        if value > 3000:  # Nem seviyesi yüksekse (kalın ton)
            print("Nem seviyesi yüksek! Kalın tonda uyarı.")
            buzzer_alert(200, 1)  # 200 Hz, 1 saniye
        elif value < 2500:  # Nem seviyesi düşükse (ince ton)
            print("Nem seviyesi düşük! İnce tonda uyarı.")
            buzzer_alert(1000, 1)  # 1000 Hz, 1 saniye

        return value
    except OSError as e:
        print("Sensör okuma hatası:", e)
        return -1  # Hata durumunda bir varsayılan değer döndürülüyor

# ---- HTTP Sunucusu ----
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    server = socket.socket()
    server.bind(addr)
    server.listen(1)
    print("Sunucu çalışıyor, bağlantı bekleniyor...")
    
    while True:
        conn, addr = server.accept()
        print("Bağlantı:", addr)
        request = conn.recv(1024).decode()
        print("İstek:", request)
        
        if "GET /soil-moisture" in request:
            value = read_soil_moisture()
            if value == -1:
                response = "{\"error\": \"Sensör okuma hatası\"}"
            else:
                response = f"{{\"moisture_value\": {value}}}"
                
            # Doğru başlık formatı kullan
            headers = headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nConnection: close\r\n\r\n"
            conn.send(headers)
            conn.send(response)
        else:
            conn.send("HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n")
        
        conn.close()
    
# ---- Wi-Fi ve Sunucu Başlatma ----
try:
    connect_to_wifi()
    start_server()
finally:
    buzzer.deinit()  # Program sonlandığında buzzer'ı devre dışı bırak
