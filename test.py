import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# Заголовок сайта
st.set_page_config(page_title="Анализ данных Excel", page_icon="📊")
st.title("Анализ данных Excel")

# Опция для выбора цвета фона
background_color = st.selectbox(
    "Выберите цвет фона страницы",
    ["Белый", "Светло-голубой", "Голубой", "Темно-синий", "Светло-красный", "Красный", "Темно-красный"]
)

# Словарь для цветов фона
background_colors = {
    "Белый": "#FFFFFF",
    "Светло-голубой": "#E0FFFF",
    "Голубой": "#ADD8E6",
    "Темно-синий": "#00008B",
    "Светло-красный": "#FFA07A",
    "Красный": "#FF0000",
    "Темно-красный": "#8B0000"
}

# Определение цвета текста в зависимости от фона
text_color = "#000000" if background_color == "Белый" else "#FFFFFF"

# Применение выбранного цвета фона и цвета текста
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_colors[background_color]};
        color: {text_color};
    }}
    .stApp h1 {{
        color: {text_color};
    }}
    .stApp .css-1d391kg p {{
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

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

        # Создание файла для скачивания
        towrite = io.BytesIO()
        df.to_excel(towrite, index=False, engine='openpyxl')
        towrite.seek(0)

        # Кнопка для скачивания файла
        st.download_button(
            label="Скачать Excel файл",
            data=towrite,
            file_name='analyzed_data.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

    except Exception as e:
        st.error(f"Ошибка при чтении файла: {e}")
else:
    st.info("Пожалуйста, загрузите файл для отображения его содержимого.")


