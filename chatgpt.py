import openai  # pip install openai

openai.api_key = {{Llave}}
context = {"role": "system",
               "content": "Eres un asistente muy útil."}
messages = [context]
print("Hola jefe. ¿En qué te puedo ayudar?")

while True:
    pregunta = input("\n＞ ")
    if pregunta == "Chao":
        print("¡Hasta luego, jefe!")
        break
    messages.append({"role": "user", "content": pregunta})
    respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(respuesta.choices[0].message.content)