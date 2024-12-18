# ESP32 Tabanlı Toprak Nem Ölçer ve Telegram Botu Projesi

## Proje Açıklaması
Bu proje, ESP32 mikrodenetleyicisi kullanarak bir toprak nem ölçüm sistemi ve Telegram botu uygulamasını kapsamaktadır. ESP32, toprak nem sensöründen veri alır ve bir web sunucusu aracılığıyla değerleri paylaşır. Ayrıca, Telegram botu ile nem seviyesi sorgulanabilir ve fan ile su pompası uzaktan kontrol edilebilir.

## Proje Dosyaları
- **esp32.py:** ESP32'nin sensör verilerini okuyup bir web sunucusu üzerinden paylaşmasını sağlar.
- **telegramBot.py:** ESP32 ile iletişim kurarak Telegram botu komutlarını işleyen bot yazılımı.

## Donanım Gereksinimleri
- ESP32 Geliştirme Kartı
- Toprak Nem Sensörü
- Fan ve Su Pompası

## ESP32 Pin Bağlantıları
- **Toprak Nem Sensörü:** Kullanıcı tanımlı GPIO pini
- **Fan:** Kullanıcı tanımlı GPIO pini
- **Su Pompası:** Kullanıcı tanımlı GPIO pini

## Kurulum ve Çalıştırma

### ESP32 Tarafı
1. ESP32'nin `esp32.py` dosyasını yükleyin.
2. Wi-Fi bilgilerini `SSID` ve `PASSWORD` alanlarına girin.
3. ESP32'yi başlatın ve yerel IP adresini not alın.

### Telegram Botu Tarafı
1. `telegramBot.py` dosyasını açın.
2. `ESP32_IP` alanına ESP32'nin yerel IP adresini girin.
3. Bot Token'ını `TOKEN` değişkenine ekleyin.
4. Telegram botunu çalıştırın.

## Kullanım
- **/start:** Bot hakkında bilgi verir.
- **/nem:** Toprak nem seviyesini sorgular.
- **/fan:** Fanı açar.
- **/pompa:** Su pompasını çalıştırır.

---

# ESP32-Based Soil Moisture Sensor and Telegram Bot Project

## Project Description
This project involves an ESP32-based soil moisture monitoring system integrated with a Telegram bot. The ESP32 reads data from a soil moisture sensor and shares values through a web server. The Telegram bot can query the moisture level and remotely control the fan and water pump.

## Project Files
- **esp32.py:** Manages sensor data reading and sharing through a web server.
- **telegramBot.py:** Handles bot commands and communicates with the ESP32.

## Hardware Requirements
- ESP32 Development Board
- Soil Moisture Sensor
- Fan and Water Pump

## ESP32 Pin Connections
- **Soil Moisture Sensor:** Custom-defined GPIO pin
- **Fan:** Custom-defined GPIO pin
- **Water Pump:** Custom-defined GPIO pin

## Setup and Running

### ESP32 Side
1. Upload the `esp32.py` file to the ESP32.
2. Enter your Wi-Fi credentials in the `SSID` and `PASSWORD` fields.
3. Start the ESP32 and note its local IP address.

### Telegram Bot Side
1. Open the `telegramBot.py` file.
2. Enter the ESP32's local IP address in the `ESP32_IP` field.
3. Add the Bot Token in the `TOKEN` variable.
4. Run the Telegram bot.

## Usage
- **/start:** Provides information about the bot.
- **/nem:** Queries the soil moisture level.
- **/fan:** Turns on the fan.
- **/pompa:** Activates the water pump.
