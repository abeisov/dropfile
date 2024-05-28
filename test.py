import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Анализ данных из Excel файла')

# Загрузка файла
uploaded_file = st.file_uploader("Загрузите Excel файл", type=["xlsx"])

if uploaded_file:
    data = pd.read_excel(uploaded_file, sheet_name='Лист1')

    # Преобразование столбца с датами в формат datetime
    data['Дата'] = pd.to_datetime(data['Дата'])

    # Группировка данных по датам для получения сумм за день
    daily_data = data.groupby('Дата').sum()

    # Ресэмплинг данных по месяцам для получения сумм за месяц
    monthly_data = data.resample('M', on='Дата').sum()

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

    # Вычисление и отображение корреляционной матрицы
    st.subheader('Корреляционная матрица')
    correlation_matrix = data.corr()
    st.write(correlation_matrix)

    # Построение тепловой карты корреляционной матрицы
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Тепловая карта корреляционной матрицы')
    st.pyplot(fig)
else:
    st.info('Пожалуйста, загрузите Excel файл для анализа.')
