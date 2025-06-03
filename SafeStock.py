import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


def calcular_recursos(pessoas, vulnerabilidade):

    agua_litros = pessoas * 1,5
    
    refeicoes = pessoas * 2
    
    kits_medicos = max(1, int(pessoas / 5) + round(vulnerabilidade / 5))
    
    return agua_litros, refeicoes, kits_medicos


@st.cache_data
def carregar_dados():
    df = pd.read_csv('dados_abrigo.csv')
    return df


@st.cache_resource
def treinar_modelo(df):
    X = df[['chuva_mm', 'temperatura', 'vulnerabilidade_local', 'eventos_passados', 'distancia_cidade_km', 'capacidade_abrigo']]
    y = df['pessoas_previstas']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(random_state=42, n_estimators=200)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    st.write('### Avaliação do modelo no conjunto de teste:')
    st.write(f'R²: {r2_score(y_test, y_pred):.3f}')
    st.write(f'MAE: {mean_absolute_error(y_test, y_pred):.3f}')
    st.write(f'MSE: {mean_squared_error(y_test, y_pred):.3f}')

    return model


def main():
    st.title("Previsão de Ocupação e Recursos para Abrigos em Eventos Extremos")

    df = carregar_dados()
    model = treinar_modelo(df)

    st.markdown("## Insira os parâmetros do cenário atual:")

    chuva_mm = st.number_input("Quantidade de chuva prevista (mm)", min_value=0.0, max_value=500.0, value=50.0, step=1.0)
    temperatura = st.number_input("Temperatura média (°C)", min_value=-50.0, max_value=60.0, value=25.0, step=0.1)
    vulnerabilidade_local = st.slider("Índice de vulnerabilidade (0 a 10)", 0, 10, 5)
    eventos_passados = st.number_input("Número de eventos extremos anteriores", min_value=0, max_value=20, value=2, step=1)
    distancia_cidade_km = st.number_input("Distância até cidade mais próxima (km)", min_value=0.0, max_value=500.0, value=50.0, step=1.0)
    capacidade_abrigo = st.number_input("Capacidade máxima do abrigo (pessoas)", min_value=1, max_value=1000, value=200, step=1)

    if st.button("Prever Ocupação e Recursos"):
        input_df = pd.DataFrame({
            'chuva_mm': [chuva_mm],
            'temperatura': [temperatura],
            'vulnerabilidade_local': [vulnerabilidade_local],
            'eventos_passados': [eventos_passados],
            'distancia_cidade_km': [distancia_cidade_km],
            'capacidade_abrigo': [capacidade_abrigo]
        })

        pessoas_previstas = model.predict(input_df)[0]
        pessoas_previstas = max(0, round(pessoas_previstas))

        if pessoas_previstas > capacidade_abrigo:
            st.warning(f"A previsão de ocupação ({pessoas_previstas} pessoas) excede a capacidade máxima do abrigo ({capacidade_abrigo} pessoas). Considere aumentar a capacidade ou abrir abrigos adicionais.")
        else:
            st.success(f"A previsão de ocupação está dentro da capacidade do abrigo.")

        agua_litros, refeicoes, kits_medicos = calcular_recursos(pessoas_previstas, vulnerabilidade_local)

        st.write(f"### Resultados da Previsão")
        st.write(f"**Pessoas previstas:** {pessoas_previstas}")
        st.write(f"**Água necessária (litros/dia):** {agua_litros}")
        st.write(f"**Refeições necessárias (por dia):** {refeicoes}")
        st.write(f"**Kits médicos necessários:** {kits_medicos}")


        fig, ax = plt.subplots()
        categorias = ['Ocupação Estimada', 'Capacidade Abrigo']
        valores = [pessoas_previstas, capacidade_abrigo]

        barlist = ax.bar(categorias, valores, color=['orange', 'green'])
        if pessoas_previstas > capacidade_abrigo:
            barlist[0].set_color('red')

        ax.set_ylim(0, max(valores) * 1.2)
        ax.set_ylabel('Número de Pessoas')
        ax.set_title('Ocupação Estimada vs Capacidade do Abrigo')

        st.pyplot(fig)


if __name__ == '__main__':
    main()
