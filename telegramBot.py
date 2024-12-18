import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# ESP32'nin IP adresi (ESP32 çalıştığında konsolda gösterilir)
ESP32_IP = "0.0.0.0"  # ESP32'nin yerel IP adresini buraya girin

# Bot Token
TOKEN = "BOT_TOKEN"

# /start komutu
async def start(update: Update, context):
    await update.message.reply_text("Merhaba! Ben bir Telegram botuyum. Nem seviyesini öğrenmek için /nem yazabilirsiniz ,/pompa ile pompayı çalıştırabilirsiniz , /fan ile fanı çalıştırabilirsiniz.")

# /nem komutu
async def nem(update: Update, context):
    try:
        # ESP32'den nem verisini al
        url = f"http://{ESP32_IP}/soil-moisture"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "moisture_value" in data:
                moisture_value = data["moisture_value"]
                await update.message.reply_text(f"Toprak nem değeri: {moisture_value}")
            else:
                await update.message.reply_text("ESP32'den geçersiz bir yanıt alındı.")
        else:
            await update.message.reply_text("ESP32'ye bağlanılamadı.")
    except Exception as e:
        await update.message.reply_text(f"Bir hata oluştu: {e}")

# /fan komutu
async def fan(update: Update, context):
    try:
        # ESP32'den fan kontrolü
        url = f"http://{ESP32_IP}/fan-on"
        response = requests.get(url)
        if response.status_code == 200:
            await update.message.reply_text("Fan başarıyla açıldı.")
        else:
            await update.message.reply_text("ESP32'ye bağlanılamadı.")
    except Exception as e:
        await update.message.reply_text(f"Bir hata oluştu: {e}")

# /pompa komutu
async def pompa(update: Update, context):
    try:
        # ESP32'den pompa kontrolü
        url = f"http://{ESP32_IP}/su-pompa-on"
        response = requests.get(url)
        if response.status_code == 200:
            await update.message.reply_text("Su pompası başarıyla açıldı.")
        else:
            await update.message.reply_text("ESP32'ye bağlanılamadı.")
    except Exception as e:
        await update.message.reply_text(f"Bir hata oluştu: {e}")

# Botu oluştur ve çalıştır
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("nem", nem))
app.add_handler(CommandHandler("fan", fan))
app.add_handler(CommandHandler("pompa", pompa))

print("Telegram bot çalışıyor...")
app.run_polling()
