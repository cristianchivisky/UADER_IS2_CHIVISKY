#!/usr/bin/python
import sys
sys.path.append(r'c:\users\crist\appdata\local\programs\python\python37\lib\site-packages')
import openai
from mi_apy_key import clave

openai.api_key = clave 
#Los siguientes son parámetros para la API
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=["You: ", "chatGPT: "]
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"
USERNAME='You: '
AI_NAME='chatGPT: '
#En get_completion se llama a la API de chatGPT
def get_completion(userText):
    completion=openai.Completion.create(engine=MODEL_ENGINE,
                                        prompt=userText,
                                        max_tokens=MAX_TOKENS,
                                        n=NMAX,
                                        top_p=TOP_P,
                                        frequency_penalty=FREQ_PENALTY,
                                        presence_penalty=PRES_PENALTY,
                                        temperature=TEMPERATURE,
                                        stop=STOP)
    return completion.choices[0].text
#En start_conversation se inicia el modo conversación con la API
def start_conversation():
    print('Bienvenido al modo conversación, para salir ingrese "exit"')
    conversation_history = ''
    while True:
        try:
            user_text=input('You: ')
            if user_text == '':
                raise ValueError('Debe ingresar una consulta!')
            elif user_text=='exit':     #Si el usuario ingresa "exit" se corta el ciclo while y sale.
                break
        except ValueError as e:
            print(e)
        else:
            conversation_history += f'\n {USERNAME}{user_text}\n {AI_NAME}'
            try:
                message=get_completion(conversation_history)
            except:
                print('Error en la llamada a la API')
            else:
                conversation_history += message
                print(f'{AI_NAME}{message.strip()}\n')

if len(sys.argv) > 1:
   aux=str(sys.argv[1])
   if aux=='--convers':
    try:
        start_conversation()
    except:
        print('Error en start_conversation')
else:
    print('Ingrese su consulta')
    aux=input('You: ')
    try:
        print(f'chatGPT: {get_completion(aux)}')
    except:
        print('Error en la llamada a la API')