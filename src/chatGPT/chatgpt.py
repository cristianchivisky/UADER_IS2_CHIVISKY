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

userText=input('Introduce una pregunta ')
if userText != '':
    userText='You: '+ userText
    print(f'{userText} \n')
    completion=openai.Completion.create(engine=MODEL_ENGINE,
                                        prompt=userText,
                                        max_tokens=MAX_TOKENS,
                                        n=NMAX,
                                        top_p=TOP_P,
                                        frequency_penalty=FREQ_PENALTY,
                                        presence_penalty=PRES_PENALTY,
                                        temperature=TEMPERATURE,
                                        stop=STOP)
    print(f'chatGPT: {completion.choices[0].text}')