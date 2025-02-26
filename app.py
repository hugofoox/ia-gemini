import google.generativeai as genai

# Configurar a chave de API
genai.configure(api_key='Chave')

# Selecionar o modelo Gemini
model = genai.GenerativeModel('gemini-2.0-flash')

# Gerar uma resposta
response = model.generate_content("Quem é você?")
print(response.text)