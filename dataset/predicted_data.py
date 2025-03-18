
import pandas as pd  # Для работы с DataFrame
import numpy as np  # Для работы с числовыми данными
from sklearn.preprocessing import StandardScaler, LabelEncoder  # Для масштабирования и кодирования данных
from sklearn.impute import SimpleImputer  # Для обработки пропущенных значений
import joblib  # Для загрузки сохраненных объектов (модели, imputer, scaler и т.д.)

# Загрузка всех объектов
loaded_model = joblib.load("best_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
imputer = joblib.load("imputer.pkl")
scaler = joblib.load("scaler.pkl")
original_columns = joblib.load("original_columns.pkl")

# Функция для предсказания стоимости
def predict_house_price(model, label_encoders, imputer, scaler, new_data, original_columns):
    """
    Функция для предсказания стоимости жилья.
    
    Параметры:
    - model: Обученная модель.
    - label_encoders: Словарь с LabelEncoders для категориальных признаков.
    - imputer: Объект SimpleImputer для обработки пропущенных значений.
    - scaler: Объект StandardScaler для масштабирования данных.
    - new_data: DataFrame или словарь с новыми данными для предсказания.
    - original_columns: Список всех признаков из обучающего набора данных.
    
    Возвращает:
    - predicted_price: Предсказанная стоимость жилья.
    """
    # Преобразуем входные данные в DataFrame, если это словарь
    if isinstance(new_data, dict):
        new_data = pd.DataFrame([new_data])
    
    # Добавляем отсутствующие столбцы и заполняем их нулями
    missing_columns = set(original_columns) - set(new_data.columns)
    for col in missing_columns:
        new_data[col] = 0  # Заполняем отсутствующие столбцы нулями
    
    # Перестраиваем порядок столбцов, чтобы он соответствовал обучающим данным
    new_data = new_data[original_columns]
    
    # Кодируем категориальные переменные
    for col, le in label_encoders.items():
        if col in new_data.columns and new_data[col].dtype == 'object':
            # Если значение отсутствует в обучении, используем "неизвестное" значение
            new_data[col] = new_data[col].apply(lambda x: x if x in le.classes_ else 'Unknown')
            new_data[col] = le.transform(new_data[col].astype(str))
    
    # Обработка пропущенных значений
    new_data_imputed = imputer.transform(new_data)
    
    # Масштабирование данных
    new_data_scaled = scaler.transform(new_data_imputed)
    
    # Предсказываем стоимость
    predicted_price = model.predict(new_data_scaled)
    
    return predicted_price[0]

# Пример использования функции
if __name__ == "__main__":
    # Определяем список всех признаков из обучающего набора данных
    original_columns = list(data.drop(columns=['Price']).columns)
    
    # Пример новых данных (словарь с характеристиками дома)
    new_house = {
        "Size": 1500,              # Размер дома (в квадратных футах)
        "Resale": "0",            # Является ли дом вторичным
        "Gymnasium": "0",         # Наличие тренажерного зала
        "SwimmingPool": "1",      # Наличие бассейна
        "Area": "1000"            # Район
    }
    
    # Вызываем функцию для предсказания
    predicted_price = predict_house_price(loaded_model, label_encoders, imputer, scaler, new_house, original_columns)
    print(f"Predicted Price: {predicted_price:.2f}")