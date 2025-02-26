import google.generativeai as genai

historico = []

genai.configure(api_key='Chave')
model = genai.GenerativeModel('gemini-2.0-flash')

def Pergunta(_pergunta):
    interacaoAnterior = ""
    for info in historico:
        interacaoAnterior += f"{info}"

    response = model.generate_content(f"{interacaoAnterior}\n{_pergunta}")
    historico.append(response.text)
    print(response.text)

while True:
    _pergunta = input("Pergunta: ")
    Pergunta(_pergunta)