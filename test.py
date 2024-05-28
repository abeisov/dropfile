import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

def analyzes_data(df):
    df['Дата'] = pd.to_datetime(df['Дата'])
    daily_data = df.groupby('Дата').sum()
    monthly_data = df.resample('M', on='Дата').sum()
    # Построение графиков ежедневных сумм
    st.subheader('Графики ежедневных сумм')
    fig, ax = plt.subplots(figsize=(14, 7))
    daily_data[['Итого | Сумма', 'Общие выплаты | Сумма', 'Ущерб имуществу | Сумма']].plot(
        marker='o', ax=ax)
    ax.set_title('Ежедневные суммы')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Суммы')
    ax.legend(['Итого | Сумма', 'Общие выплаты | Сумма', 'Ущерб имуществу | Сумма'])
    ax.grid(True)
    st.pyplot(fig)

    # Построение графиков месячных сумм
    st.subheader('Графики месячных сумм')
    fig, ax = plt.subplots(figsize=(14, 7))
    monthly_data[['Итого | Сумма', 'Общие выплаты | Сумма', 'Ущерб имуществу | Сумма']].plot(
        marker='o', ax=ax)
    ax.set_title('Месячные суммы')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Суммы')
    ax.legend(['Итого | Сумма', 'Общие выплаты | Сумма', 'Ущерб имуществу | Сумма'])
    ax.grid(True)
    st.pyplot(fig)

st.title("Анализ данных")
uploaded_file = st.file_uploader("Загрузите Excel файл", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        st.write("Названия столбцов:")
        st.write(df.columns)

        st.write("Содержимое Excel файла:")
        st.dataframe(df)

        analyzes_data(df)


        
        towrite = io.BytesIO()
        df.to_excel(towrite, index=False, engine="openpyxl")
        towrite.seek(0)

        st.download_button(
            label = "Скачать файл",
            data=towrite,
            file_name="data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        )


    except Exception as e:
        st.error(f"Ошибка при чтении файла: {e}")
else:
    st.info("Пожалуйста загрузите файл")
