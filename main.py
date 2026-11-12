```python
class Fonte:
    def __init__(self, tensao):
        self.tensao = tensao

class Interruptor:
    def __init__(self):
        self.ligado = False

    def alternar(self):
        self.ligado = not self.ligado

class Lampada:
    def __init__(self):
        self.acesa = False

    def verificar_circuito(self, interruptor):
        self.acesa = interruptor.ligado
        if self.acesa:
            print("A lâmpada está acesa! Circuito correto.")
        else:
            print("A lâmpada está apagada. Verifique o interruptor.")

# Início da simulação da Fase 1
bateria = Fonte(12)
interruptor = Interruptor()
lampada = Lampada()

print("--- Fase 1: Iluminação Básica ---")
print("O interruptor está desligado.")
lampada.verificar_circuito(interruptor)

print("\nJogador, alterne o interruptor para ligar a luz:")
interruptor.alternar()
lampada.verificar_circuito(interruptor)
```
