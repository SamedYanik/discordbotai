import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Görselin kaydedileceği klasör
UPLOAD_FOLDER = "D:\KODLAND\Dersler_Kodlar\M7L1\uploads"

# Klasör yoksa oluştur
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bot.command(name="yükle")
async def yükle(ctx):
    attachments = ctx.message.attachments

    if not attachments:
        await ctx.send("❌ Görsel bulunamadı. Lütfen bir görsel yükleyin.")
        return

    for attachment in attachments:
        file_path = os.path.join(UPLOAD_FOLDER, attachment.filename)
        await attachment.save(file_path)
        await ctx.send(f"✅ {attachment.filename} başarıyla kaydedildi!")

# Botu çalıştır
bot.run("token gir")
