from machine import Pin, PWM
import time
from machine import Pin, PWM, SoftI2C
from i2c_lcd import I2cLcd

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.putstr("Digite a senha:")

led_verde = Pin(5, Pin.OUT)
led_vermelho = Pin(4, Pin.OUT)

linhas = [

    Pin(13, Pin.OUT),
    Pin(18, Pin.OUT),
    Pin(19, Pin.OUT),
    Pin(33, Pin.OUT)
]

colunas = [

    Pin(25, Pin.IN, Pin.PULL_UP),
    Pin(26, Pin.IN, Pin.PULL_UP),
    Pin(27, Pin.IN, Pin.PULL_UP),
    Pin(32, Pin.IN, Pin.PULL_UP)

]

teclas = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]


def ler_teclas():
    for i, linha in enumerate(linhas):
        linha.value(0)
        for j, coluna in enumerate(colunas):
            if coluna.value() == 0:
                linha.value(1)
                return teclas[i][j]
        linha.value(1)
    return None


senha_correta = '1234'
entrada = ''

tentativas = 0
max_tentativas = 3

buzzer = PWM(Pin(14), freq=1000, duty=0)


def bip(freq=1000, duracao=100):
    buzzer.freq(freq)  # define freq
    buzzer.duty(512)  # liga na metade da potencia
    time.sleep_ms(duracao)
    buzzer.duty(0)  # volta para desligado


while True:
    tecla = ler_teclas()
    if tecla is not None:
        entrada += tecla  # soma os string para verificar a validade da senha
        print('Entrada', entrada)

        if len(entrada) == 4:  # defino o tamanho de cada tentativa
            if entrada == senha_correta:
                print('Aberto')
                bip(freq=2000)  # bipa em freq aguda em caso de acerto
                led_verde.value(1)  # aciona a luz verde se correto
                time.sleep(1)
                led_verde.value(0)
                tentativas = 0
                break
            else:
                tentativas += 1
                print('Senha incorreta')
                bip(freq=100)  # bipa em freq grave em caso de erro
                led_vermelho.value(1)  # aciona a luz vermelha se incorreto
                time.sleep(1)
                led_vermelho.value(0)
                entrada = ''
                print(f'você tem {max_tentativas - tentativas} tentativas restantes')
            if tentativas == max_tentativas:  # se atingir a cota de tentativas é bloqueado
                print('Bloqueado')
                break

    time.sleep_ms(100)

