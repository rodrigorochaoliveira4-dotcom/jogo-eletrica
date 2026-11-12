class Fonte {
    constructor(tensao) {
        this.tensao = tensao;
    }
}

class Interruptor {
    constructor() {
        this.ligado = false;
    }

    alternar() {
        this.ligado = !this.ligado;
    }
}

class Resistor {
    constructor(resistencia) {
        this.resistencia = resistencia; // em Ohms
    }
}

class Lampada {
    constructor(tensaoNominal) {
        this.tensaoNominal = tensaoNominal;
        this.acesa = false;
        this.queimada = false;
    }

    verificarCircuito(fonte, interruptor, resistor) {
        if (!interruptor.ligado) {
            console.log("A lâmpada está apagada (circuito aberto).");
            return;
        }

        // Calculando a corrente (I = V / R) segundo a Lei de Ohm
        if (resistor.resistencia === 0) {
            console.log("PERIGO: Curtociruito! Sem resistor no circuito.");
            this.queimada = true;
            return;
        }

        let corrente = fonte.tensao / resistor.resistencia;
        let tensaoNaLampada = corrente * 10; // Considerando resistência interna da lâmpada

        if (tensaoNaLampada > this.tensaoNominal * 1.2) {
            this.queimada = true;
            console.log(`❌ A lâmpada queimou! Tensão muito alta: ${tensaoNaLampada.toFixed(1)}V.`);
        } else if (tensaoNaLampada < this.tensaoNominal * 0.8) {
            console.log(`⚠️ A lâmpada está fraca. Tensão insuficiente: ${tensaoNaLampada.toFixed(1)}V.`);
        } else {
            this.acesa = true;
            console.log(`✨ A lâmpada acendeu com brilho perfeito! Tensão: ${tensaoNaLampada.toFixed(1)}V.`);
        }
    }
}

// --- Execução do Jogo ---
console.log("=== FASE 1: Circuito Simples ===");
let bateria = new Fonte(12);
let chave = new Interruptor();
let resistorFase1 = new Resistor(10);
let lampada1 = new Lampada(12);

chave.alternar();
lampada1.verificarCircuito(bateria, chave, resistorFase1);

console.log("\n=== FASE 2: Dimensionamento de Resistor ===");
// O jogador precisa escolher o resistor correto para uma bateria de 24V
let bateria24v = new Fonte(24);
let chaveFase2 = new Interruptor();
let lampada2 = new Lampada(12);

// Teste com resistor incorreto (muito baixo)
console.log("\n[Tentativa 1] Usando resistor de 5 Ohms:");
let resistorErrado = new Resistor(5);
chaveFase2.alternar();
lampada2.verificarCircuito(bateria24v, chaveFase2, resistorErrado);

// Teste com resistor correto (20 Ohms)
console.log("\n[Tentativa 2] Ajustando para resistor de 20 Ohms:");
let resistorCorreto = new Resistor(20);
lampada2.verificarCircuito(bateria24v, chaveFase2, resistorCorreto);
