import pandas as pd
from flask import Flask, jsonify, render_template
from sklearn.linear_model import LinearRegression 

app = Flask(__name__)

@app.route('/')
def exibir_vitrine():
    return render_template('index.html')

@app.route('/api/previsao/<nome_cultura>/<solo_n>/<chuva_mm>', methods=['GET'])
def prever_safra(nome_cultura, solo_n, chuva_mm):

    solo_n = float(solo_n)
    chuva_mm = float(chuva_mm)

    # PASSO 1: ENGENHARIA DE DADOS (ETL) 
    tabela = pd.read_csv("dados_safra.csv")
    tabela_filtrada = tabela[tabela['cultura'] == nome_cultura]

    # TRAVA DE SEGURANÇA
    if tabela_filtrada.empty:
        return jsonify({"erro": f"Cultura '{nome_cultura}' não encontrada no banco de dados"}), 404
    
    # PASSO 2: TREINAMENTO DA INTELIGÊNCIA ARTIFICIAL
    X = tabela_filtrada[['solo_n', 'chuva_mm']]
    y = tabela_filtrada['producao_ton']

    # Instancia o modelo a partir da classe
    modelo = LinearRegression()
    # O modelo estuda os dados do CSV 
    modelo.fit(X, y)

    # PASSO 3: A PREVISÃO 
    novo_cenario = pd.DataFrame({'solo_n': [solo_n], 'chuva_mm': [chuva_mm]})
    previsao = modelo.predict(novo_cenario)
    toneladas_previstas = previsao[0]

    # PASSO 4: A REGRA DE NEGÓCIO DINÂMICA
    MEDIA_SAFRA_REFERENCIA = 150.00
    if toneladas_previstas >= MEDIA_SAFRA_REFERENCIA:
        diagnostico = "Previsão Otimista: As condições informadas indicam uma colheita rentável."
    else: 
        diagnostico = "Alerta: Previsão de baixa produtividade. Recomenda-se ajsutar adubação (Nitrogênio) ou irrigação (Chuva)."
        
    # PASSO 5: O PACOTE DE RESPOSTA (JSON)
    resposta = {
        "cultura": nome_cultura, 
        "cenario_informado": {
            "nitrogenio_solo": solo_n,
            "previsao_chuva_mm": chuva_mm
        },
        "previsao_toneladas": round(toneladas_previstas, 2),
        "diagnostico": diagnostico
    }

    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
