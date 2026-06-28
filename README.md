# 🌾 Analista de Safra - IA Agrícola

Um protótipo inteligente de gestão agrícola que utiliza Machine Learning para prever o volume de colheita e emitir diagnósticos dinâmicos com base nas condições do solo e do clima. 

Este sistema processa dados históricos de safras e, através de regressão linear, auxilia agricultores na tomada de decisão sobre adubação e irrigação.

## 🚀 Funcionalidades

* **Previsão de Colheita (Toneladas):** Estima a produção com base no índice de nitrogênio do solo e na previsão de chuva em milímetros.
* **Diagnóstico Inteligente:** Analisa o resultado previsto em relação a uma média de referência (150 toneladas) e emite alertas automáticos recomendando ajustes caso a produtividade esperada seja baixa.
* **API RESTful:** Rota dedicada no back-end para integração de dados, retornando pacotes JSON padronizados.
* **Interface Web (Front-end):** Um painel limpo e intuitivo para consulta rápida das previsões diretamente pelo navegador.

## 🛠️ Tecnologias Utilizadas

**Back-end & Inteligência Artificial:**
* **Python:** Linguagem principal do motor lógico.
* **Flask:** Micro-framework para criação do servidor web e da API REST.
* **Pandas:** Biblioteca para Engenharia de Dados (ETL) e manipulação do CSV.
* **Scikit-Learn:** Treinamento do modelo de Inteligência Artificial usando `LinearRegression`.

**Front-end:**
* **HTML5, CSS3 & JavaScript (Vanilla):** Estrutura do painel do usuário e consumo da API de forma assíncrona usando a API `fetch`.

## 📁 Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

* `main.py`: O "coração" do sistema. Roda o servidor Flask, hospeda a API de previsão, processa a regra de negócio dinâmica e serve a interface web.
* `treinamento_ia.py`: Script isolado que demonstra a lógica pura de separação de dados e treinamento do modelo de IA (excelente para fins de estudo e testes rápidos).
* `dados_safra.csv`: Banco de dados histórico contendo registros de anos anteriores (Cultura, Nitrogênio, Chuva, Produção).
* `templates/index.html`: Arquivo da interface gráfica do usuário (deve ser alocado dentro de uma pasta chamada `templates` para que o Flask o reconheça automaticamente).

## ⚙️ Como Executar o Projeto

**1. Clone o repositório e acesse a pasta:**
```bash
git clone [https://github.com/seu-usuario/analista-de-safra.git](https://github.com/seu-usuario/analista-de-safra.git)
cd analista-de-safra
