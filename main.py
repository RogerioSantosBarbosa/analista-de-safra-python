import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# 1. Rota Dinâmica: O Flask agora captura a palavra que vem depois da barra
@app.route('/api/laudo/<nome_cultura>', methods=['GET'])
def gerar_laudo(nome_cultura):
    tabela = pd.read_csv("dados_safra.csv")
    MEDIA_SAFRA_REFERENCIA = 150.00

    # 2. O filtro agora usa a variável que veio da URL
    tabela_filtrada = tabela[tabela['cultura'] == nome_cultura]

    # TRAVA DE SEGURANÇA: Caso o usuário digitar uma cultura que não existe no CSV
    if tabela_filtrada.empty:
        # Devolvemos um JSON de erro e o código 404 (Não Encontrado)
        return jsonify({"erro": f"Cultura '{nome_cultura}' não encontrada no banco de dados"}), 404
    
    # 3. O cálculo continua igual
    media = tabela_filtrada['producao_ton'].mean()

    if media >= MEDIA_SAFRA_REFERENCIA:
        diagnostico = "Produtividade satisfatória. O solo mantém bons índices de rendimento."
    else:
        diagnostico = "Atenção! Produtividade abaixo do limiar aceitável. Recomenda-se iniciar a análise para rotação de culturas."

    resposta = {
        "cultura": nome_cultura,
        "periodo_analisado_anos": len(tabela_filtrada),
        "media_toneladas": round(media, 2),
        "meta_referencia": MEDIA_SAFRA_REFERENCIA,
        "diagnostico": diagnostico
    }

    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)