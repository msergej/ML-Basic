import numpy as np
import pandas as pd
         # Функция установки уровня z-значения
def level_coder (z_val):
    if z_val < -0.1: return 'low'
    elif z_val > 0.5: return 'high'
    else: return 'mean'
         # Функция формирования массива и расчета z-значений
def calculate_normal_distribution_stats(mean_val, size_val, sigma_val, random_seed_val):
    if random_seed_val is not None: np.random.seed(random_seed_val)

    arr = np.random.normal(mean_val, sigma_val, size_val)
    df = pd.DataFrame({'value': arr})

    df['z_value'] = ((df['value'] - df['value'].mean()) / df['value'].std(ddof=1)).round(2)
    df['category'] = df['z_value'].apply(level_coder)
    category_fractions = df['category'].value_counts(normalize=True).round(2)

    print(arr)
    print(df)

    return category_fractions.to_dict()

print(calculate_normal_distribution_stats(0.1, 15, 0.1, 42))