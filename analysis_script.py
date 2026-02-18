import pandas as pd

# 1. Loading the dataset
# This is the first step where I bring the CSV file into Python
df = pd.read_csv('customer_shopping_behavior.csv')

# 2. Understanding the data
# I use .info() to check for missing values and data types
print(df.info())

# 3. Data Cleaning
# Filling 37 missing ratings using the median of each category
df['review_rating'] = df.groupby('category')['review_rating'].transform(lambda x: x.fillna(x.median()))

# 4. Standardizing column names
# Converting everything to lowercase with underscores (Snake Case)
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# 5. Feature Engineering: Age Groups
# I created these segments to help with demographic analysis
labels = ['Young Adult', 'Adult', 'Middle-Aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

# 6. Feature Engineering: Frequency
# Mapping textual frequency to numeric days for math calculations
freq_map = {'Fortnightly': 14, 'Weekly': 7, 'Monthly': 30, 'Quarterly': 90, 'Annually': 365}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(freq_map)

# 7. Redundancy Check
# Dropping the extra promo code column since it is identical to discount_applied
df.drop(columns=['promo_code_used'], inplace=True)

# 8. Final Preview
# Viewing the first 5 rows to confirm all changes are correct
print(df.head())
