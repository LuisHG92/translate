import requests

# Texto a traducir
TEXT_TO_TRANSLATE = "Hola, ¿cómo estás?"

# Función para traducir usando la API pública de LibreTranslate
def translate(text):
    url = "https://libretranslate.de/translate"
    payload = {
        "q": text,
        "source": "es",
        "target": "en",
        "format": "text"
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        result = response.json()

        if 'translatedText' in result:
            return result['translatedText']
        else:
            print("❌ Error: 'translatedText' no está en la respuesta.")
            print("Respuesta completa:", result)
            return None
    except Exception as e:
        print("❌ Error al traducir:", e)
        return None

# Ejecutar al iniciar
if __name__ == "__main__":
    print("🚀 Worker de prueba iniciado...")
    translated = translate(TEXT_TO_TRANSLATE)
    if translated:
        print(f"✅ Traducción: {TEXT_TO_TRANSLATE} → {translated}")
    else:
        print("⚠️ No se pudo traducir.")
