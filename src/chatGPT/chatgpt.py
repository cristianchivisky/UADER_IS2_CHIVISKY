import sys
sys.path.append(r'c:\users\crist\appdata\local\programs\python\python37\lib\site-packages')
import openai
from mi_apy_key import clave

openai.api_key = clave
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"

try:
    userText=input('Introduce una pregunta ')
    if userText != '':
        raise ValueError('Debe ingresar una consulta')
except ValueError as e:
    print(e)
else:
    try:
        userText='You: '+ userText
        print(f'{userText} \n')
    except:
        print('Ha habido un error')
    try:
        completion=openai.Completion.create(engine=MODEL_ENGINE,
                                            prompt=userText,
                                            max_tokens=MAX_TOKENS,
                                            n=NMAX,
                                            top_p=TOP_P,
                                            frequency_penalty=FREQ_PENALTY,
                                            presence_penalty=PRES_PENALTY,
                                            temperature=TEMPERATURE,
                                            stop=STOP)
    except:
        print('Error al llamar a la API')
    else:
        print(f'chatGPT: {completion.choices[0].text}')