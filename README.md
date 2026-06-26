# 🔐 Cofre com Senha — ESP32 + MicroPython

Cofre eletrônico com senha desenvolvido no simulador [Wokwi](https://wokwi.com), utilizando MicroPython no ESP32. Projeto de estudo focado nos fundamentos de hardware embarcado e MicroPython.

🔗 **Simulação:** [abrir no Wokwi](https://wokwi.com/projects/467832570584526849)

## ⚙️ Funcionalidades

- Entrada de senha via teclado matricial 4x4
- LED verde ao acertar a senha e LED vermelho ao errar
- Buzzer com tons diferentes para acerto (agudo) e erro (grave)
- Contador de tentativas com bloqueio após 3 erros
- Feedback de tentativas restantes no console

## 🧰 Componentes

| Componente | Quantidade |
|---|---|
| ESP32 DevKit | 1 |
| Teclado matricial 4x4 | 1 |
| Display LCD 16x2 (I2C) | 1 |
| LED verde | 1 |
| LED vermelho | 1 |
| Resistor 220Ω | 2 |
| Buzzer | 1 |

## 🔌 Pinagem

| Componente | Pino | GPIO |
|---|---|---|
| Keypad R1 | Linha 1 | 13 |
| Keypad R2 | Linha 2 | 18 |
| Keypad R3 | Linha 3 | 19 |
| Keypad R4 | Linha 4 | 33 |
| Keypad C1 | Coluna 1 | 25 |
| Keypad C2 | Coluna 2 | 26 |
| Keypad C3 | Coluna 3 | 27 |
| Keypad C4 | Coluna 4 | 32 |
| LCD SDA | I2C dados | 21 |
| LCD SCL | I2C clock | 22 |
| LED verde | Saída | 5 |
| LED vermelho | Saída | 4 |
| Buzzer | Saída PWM | 14 |

## 📁 Estrutura do Projeto

```
cofre-4x4/
├── main.py         # código principal
├── diagram.json    # circuito do Wokwi
└── README.md
```

## 🚀 Como rodar

1. Acesse o [projeto no Wokwi](https://wokwi.com/projects/467832570584526849)
2. Clique em Play
3. Digite a senha no teclado (senha padrão: `1234`)

## ⌨️ Como usar

- Digite 4 dígitos no teclado
- Senha correta → LED verde acende + bip agudo
- Senha incorreta → LED vermelho acende + bip grave
- Após 3 tentativas erradas → cofre bloqueia

## 🧠 Como funciona

**Varredura do teclado:** o ESP32 ativa cada linha em nível baixo, uma de cada vez, e lê as colunas. Quando uma coluna lê 0, significa que o botão naquela interseção foi pressionado. A tecla é identificada pelo cruzamento linha × coluna.

**Lógica de senha:** cada tecla pressionada é acumulada em uma string. Ao atingir 4 caracteres, a entrada é comparada com a senha correta.

**Buzzer via PWM:** a frequência do PWM define o tom do som — frequências altas geram sons agudos, baixas geram graves.

## 🗺️ Roadmap

- [x] Leitura do teclado matricial
- [x] Lógica de senha (verificar, abrir, negar)
- [x] LEDs de feedback (verde/vermelho)
- [x] Buzzer com tons diferentes
- [x] Contador de tentativas com bloqueio
- [ ] Exibição no display LCD
- [ ] Troca de senha pelo teclado

## 📚 Conceitos praticados

- GPIO como entrada e saída
- Varredura de matriz (teclado 4x4)
- Pull-up em entradas digitais
- PWM (controle de tom do buzzer)
- Debounce de botões
- Comunicação I2C (display LCD)

## 🛠️ Tecnologias

- [MicroPython](https://micropython.org)
- [ESP32](https://www.espressif.com/en/products/socs/esp32)
- [Wokwi Simulator](https://wokwi.com)
