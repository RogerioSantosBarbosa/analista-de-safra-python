import pandas as pd
from flask import Flask, jsonify

# Inicializando o servidor
app = Flask(__name__)

# Criando a "porta de atendimento" (Rota da API)
@app.route('/api/laudo', methods=['GET'])
def gerar_laudo():
    tabela = pd.read_csv("dados_safra.csv")
    MEDIA_SAFRA_REFERENCIA = (150.00)

    # 1. FILTRO E CÁLCULO
    tabela_filtrada = tabela[tabela['cultura'] == 'Milho']
    media = tabela_filtrada['producao_ton'].mean()

    # 2. REGRA DE NEGÓCIO
    if media >= MEDIA_SAFRA_REFERENCIA:
        diagnostico = "Produtividade satisfatória. O solo mantém bons índices de rendimento."
    else:
        diagnostico = "Atenção! Produtividade abaixo do limiar aceitável. Recomenda-se iniciar a análise para rotação de culturas."

    # 3. EMPACOTANDO A RESPOSTA NO FORMATO QUE ROBÔS LEEM (JSON/DICIONÁRIO)
    resposta = {
        "cultura": "Milho",
        "periodo_analisado_anos": len(tabela_filtrada),
        "media_toneladas": round(media, 2),
        "meta_referencia": MEDIA_SAFRA_REFERENCIA,
        "diagnostico": diagnostico
    }

    # 4. DEVOLVENDO O PACOTE PARA QUEM PEDIU
    return jsonify(resposta)

# Ligando o motor
if __name__ == '__main__':
    app.run(debug=True)