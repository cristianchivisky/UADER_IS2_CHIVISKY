#!/usr/bin/python
'''Agregué sys.phat.append porque no me importaba openai'''
import sys
import openai

openai.api_key = '' #Ingrse aquí su API KEY para que  funcione
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
def get_completion(prompt):
    '''En get_completion se llama a la API de chatGPT'''
    return openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=prompt,
        max_tokens=MAX_TOKENS,
        n=NMAX,
        top_p=TOP_P,
        frequency_penalty=FREQ_PENALTY,
        presence_penalty=PRES_PENALTY,
        temperature=TEMPERATURE,
        stop=STOP
    ).choices[0].text
def start_conversation():
    '''En start_conversation se inicia el modo conversación con la API'''
    print('Bienvenido al modo conversación, para salir ingrese "exit"')
    conversation_history = '' #Se inicializa el buffer
    while True:
        try:
            user_text=input('You: ')
            if not user_text: #Se ontrola que no ingrese una cadena vacía con el Try/Except
                raise ValueError('Debe ingresar una consulta!')
            if user_text=='exit':     #Si ingresa "exit" se corta el ciclo while y sale.
                break
        except ValueError as error:
            print(error) #Aquí se imprime el error si ingresa la cadena vacía
        else:  # en la linea sig se agrega la consulta y al buffer con el prefijo "You: "
            conversation_history += f'\n {USERNAME}{user_text}\n {AI_NAME}'
            try: #En este Try/Except se captura cualquier error que pueda haber en la API
                message=get_completion(conversation_history)
            except:
                print('Error en la llamada a la API de chatGPT en start_conversation')
            else:
                conversation_history += message #Se agrega la respuesta de la API al buffer
                print(f'{AI_NAME}{message.strip()}\n') #Se muestra en pantalla la respuesta

if len(sys.argv) > 1 and sys.argv[1] == '--convers':
    try:        #En la linea anterior se controla que exista el argumento y sea el esperado
        start_conversation() #Ingresa en la conversación
    except:
        print('Error en start_conversation')
else:                       #En caso contrario llama a la API una única vez
    print('Ingrese su consulta')
    consultation = input('You: ')
    try:
        print(f'chatGPT: {get_completion(consultation)}') #Llama a la API y muestra la respuesta
    except:
        print('Error en la llamada a la API de chatGPT')
