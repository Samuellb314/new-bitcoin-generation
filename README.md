# 🪙 New Bitcoin Generation (NBG)

## 📌 Visão Geral
O **New Bitcoin Generation (NBG)** é um projeto experimental inspirado no Bitcoin, iniciado em **2025**, com o objetivo de estudo, prática e pesquisa em blockchain.  
Não é uma cópia do Bitcoin, mas sim uma nova implementação com os mesmos princípios de **escassez, halving e supply máximo de 21 milhões de moedas**, oferecendo a esta geração a oportunidade de aprender e experimentar.

---

## ⚙️ Especificações Técnicas

- **Genesis Block:** 15/09/2025  
- **Tempo médio de bloco:** 10 minutos  
- **Recompensa inicial por bloco:** 50 NBG  
- **Halving:** a cada 210.000 blocos (~4 anos)  
- **Supply máximo:** 21.000.000 NBG  

---

## 📂 Estrutura do Projeto

new-bitcoin-generation/
├── blockchain.py # Protótipo da blockchain (Genesis + mineração simples)
├── emission_simulation.py # Simulação da emissão até 2140 (gera CSV e gráficos)
├── README.md # Este guia
└── data/ # Saídas (tabelas e gráficos)


---

## 🚀 Instalação

No **Termux/Debian**:

```bash
pkg update && pkg upgrade -y
pkg install git python3 python-pip -y
pip install matplotlib pandas reportlab

git clone https://github.com/Samuellb314/new-bitcoin-generation.git
cd new-bitcoin-generation

▶️ Como Usar
1. Rodar o protótipo da blockchain

Cria o Genesis Block e minera blocos simulados:

python3 blockchain.py

📜 Saída esperada (exemplo):

Genesis Block criado: {...}
Bloco 1 minerado: {...}
Bloco 2 minerado: {...}
...

Rodar a simulação de emissão

Gera a tabela de emissão anual até 2140:

python3 emission_simulation.py

📊 Saídas geradas em data/:

nbg_emission_full_2025_2140.csv — tabela completa

nbg_emission_full_bar.png — gráfico de emissão anual

nbg_emission_full_cumulative.png — gráfico de supply acumulado

📄 Whitepaper

O whitepaper inicial descrevendo a visão e política monetária do NBG será mantido neste repositório.
Ele inclui a tabela de emissão e gráficos de supply até 2140.

🔮 Próximos Passos

Implementar rede P2P simulada (vários nós minerando e validando).

Adicionar validação de transações e sistema de UTXO.

Criar uma wallet básica para envio e recebimento de NBG.

Integrar mineração real via Proof-of-Work simplificada.

⚠️ Aviso

Este projeto é educacional.
O NBG não é uma moeda oficial, não tem valor financeiro real e não substitui o Bitcoin.
