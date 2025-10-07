from microbit import *

# Bloco vermelho: variável
botao_nao_pressionado = True

while True:
    # Enquanto a variável botao_nao_pressionado for True
    while botao_nao_pressionado:
        if pin1.is_touched():  # Se o pino P1 for pressionado
            display.show("A")
            # Aqui você pode tocar um som usando music.play(music.C4), se desejar
            botao_nao_pressionado = False  # Bloco vermelho: alterando o valor da variável
        sleep(50)

    # Se os botões A+B forem pressionados juntos, restaura a variável
    if button_a.is_pressed() and button_b.is_pressed():
        botao_nao_pressionado = True  # Bloco vermelho: resetando a variável
        display.clear()
    sleep(50)