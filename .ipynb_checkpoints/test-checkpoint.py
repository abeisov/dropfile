import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка файла
uploaded_file = st.file_uploader("Загрузите ваш Excel файл", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Чтение файла Excel
        df = pd.read_excel(uploaded_file)

        # Отображение данных
        st.write("Содержимое Excel файла:")
        st.dataframe(df)

        # Преобразование столбца "Дата" в тип datetime
        df['Дата'] = pd.to_datetime(df['Дата'])

        # Построение графиков
        fig, ax = plt.subplots(3, 1, figsize=(10, 15))

        # График 1: Количество выплат
        ax[0].plot(df['Дата'], df['Итого | Кол-во'], marker='o', linestyle='-')
        ax[0].set_title('Количество выплат по датам')
        ax[0].set_xlabel('Дата')
        ax[0].set_ylabel('Количество выплат')

        # График 2: Общая сумма выплат
        ax[1].plot(df['Дата'], df['Итого | Сумма'], marker='o', linestyle='-')
        ax[1].set_title('Общая сумма выплат по датам')
        ax[1].set_xlabel('Дата')
        ax[1].set_ylabel('Общая сумма выплат')

        # График 3: Средняя сумма выплат
        ax[2].plot(df['Дата'], df['Итого | Ср. сумма'], marker='o', linestyle='-')
        ax[2].set_title('Средняя сумма выплат по датам')
        ax[2].set_xlabel('Дата')
        ax[2].set_ylabel('Средняя сумма выплат')

        # Отображение графиков в Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Ошибка при чтении файла: {e}")
else:
    st.info("Пожалуйста, загрузите файл для отображения его содержимого.")
