class Fonte:
    def __init__(self, tensao):
        self.tensao = tensao

class Interruptor:
    def __init__(self):
        self.ligado = False

    def alternar(self):
        self.ligado = not self.ligado

class Resistor:
    def __init__(self, resistencia):
        self.resistencia = resistencia  # em Ohms

class Lampada:
    def __init__(self, tensao_nominal):
        self.tensao_nominal = tensao_nominal
        self.acesa = False
        self.queimada = False

    def verificar_circuito(self, fonte, interruptor, resistor):
        if not interruptor.ligado:
            print("A lâmpada está apagada (circuito aberto).")
            return

        # Calculando a corrente (I = V / R) segundo a Lei de Ohm
        if resistor.resistencia == 0:
            print("PERIGO: Curtociruito! Sem resistor no circuito.")
            self.queimada = True
            return

        corrente = fonte.tensao / resistor.resistencia
        tensao_na_lampada = corrente * 10  # Considerando resistência interna da lâmpada

        if tensao_na_lampada > self.tensao_nominal * 1.2:
            self.queimada = True
            print(f" A lâmpada queimou! Tensão muito alta: {tensao_na_lampada:.1f}V.")
        elif tensao_na_lampada < self.tensao_nominal * 0.8:
            print(f"A lâmpada está fraca. Tensão insuficiente: {tensao_na_lampada:.1f}V.")
        else:
            self.acesa = True
            print(f" A lâmpada acendeu com brilho perfeito! Tensão: {tensao_na_lampada:.1f}V.")

# --- Execução do Jogo ---
print("=== FASE 1: Circuito Simples ===")
bateria = Fonte(12)
chave = Interruptor()
resistor_fase1 = Resistor(10)
lampada1 = Lampada(tensao_nominal=12)

chave.alternar()
lampada1.verificar_circuito(bateria, chave, resistor_fase1)

print("\n=== FASE 2: Dimensionamento de Resistor ===")
# O jogador precisa escolher o resistor correto para uma bateria de 24V
bateria_24v = Fonte(24)
chave_fase2 = Interruptor()
lampada2 = Lampada(tensao_nominal=12)

# Teste com resistor incorreto (muito baixo)
print("\n[Tentativa 1] Usando resistor de 5 Ohms:")
resistor_errado = Resistor(5)
chave_fase2.alternar()
lampada2.verificar_circuito(bateria_24v, chave_fase2, resistor_errado)

# Teste com resistor correto (20 Ohms)
print("\n[Tentativa 2] Ajustando para resistor de 20 Ohms:")
resistor_correto = Resistor(20)
lampada2.verificar_circuito(bateria_24v, chave_fase2, resistor_correto)
