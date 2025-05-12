import requests

def translate(text, source_lang="es", target_lang="en"):
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text"
    }
    try:
        response = requests.post("https://libretranslate.de/translate", json=payload, timeout=10)
        response.raise_for_status()  # Lanza una excepción si hay errores en la respuesta
        data = response.json()
        if "translatedText" in data:
            return data["translatedText"]
        else:
            print("❌ 'translatedText' no está en la respuesta:", data)
            return "[Error en la traducción]"
    except Exception as e:
        print("❌ Error en la petición:", e)
        return "[Error de conexión]"

# Ejemplo de uso
TEXT_TO_TRANSLATE = "Hola, ¿cómo estás?"

translated = translate(TEXT_TO_TRANSLATE)
print(f"✅ Traducción: {TEXT_TO_TRANSLATE} → {translated}")
