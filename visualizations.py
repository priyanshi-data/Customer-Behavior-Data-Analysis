import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
df = pd.read_csv(r'C:\Users\dell\Desktop\cleaned_customer_data.csv')

# 2. EMERGENCY RENAME: To ensures 'purchase_amount' exists no matter what
# We search for any column that contains the word 'purchase' and 'amount'
possible_cols = [c for c in df.columns if 'purchase' in c and 'amount' in c]
if possible_cols:
    df.rename(columns={possible_cols[0]: 'purchase_amount'}, inplace=True)

sns.set_theme(style="whitegrid")

# 1. REVENUE BY GENDER
plt.figure(figsize=(8, 5))
sns.barplot(x='gender', y='purchase_amount', data=df, estimator=sum, palette='viridis', errorbar=None)
plt.title('Total Revenue by Gender')
plt.savefig(r'C:\Users\dell\Desktop\1_revenue_gender.png')
plt.close()

# 2. TOP 5 RATED PRODUCTS
plt.figure(figsize=(10, 6))
top_rated = df.groupby('item_purchased')['review_rating'].mean().sort_values(ascending=False).head(5)
top_rated.plot(kind='bar', color='skyblue')
plt.title('Top 5 Rated Products')
plt.savefig(r'C:\Users\dell\Desktop\2_top_rated.png')
plt.close()

# 3. SHIPPING METHOD PERFORMANCE
plt.figure(figsize=(8, 5))
shipping_df = df[df['shipping_type'].isin(['Standard', 'Express'])]
sns.barplot(x='shipping_type', y='purchase_amount', data=shipping_df, palette='magma')
plt.title('Avg Spend: Standard vs Express')
plt.savefig(r'C:\Users\dell\Desktop\3_shipping_analysis.png')
plt.close()

# 4. SUBSCRIPTION REVENUE
plt.figure(figsize=(8, 5))
sns.barplot(x='subscription_status', y='purchase_amount', data=df, estimator=sum, palette='coolwarm', errorbar=None)
plt.title('Revenue: Subscribers vs Non-Subscribers')
plt.savefig(r'C:\Users\dell\Desktop\4_subscription_revenue.png')
plt.close()

# 5. REVENUE BY AGE GROUP
plt.figure(figsize=(10, 6))
sns.barplot(x='age_group', y='purchase_amount', data=df, estimator=sum, palette='rocket', errorbar=None)
plt.title('Total Revenue by Age Group')
plt.savefig(r'C:\Users\dell\Desktop\5_revenue_age.png')
plt.close()

# 6. REVENUE BY CATEGORY
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='purchase_amount', data=df, estimator=sum, palette='plasma', errorbar=None)
plt.title('Total Revenue by Category')
plt.savefig(r'C:\Users\dell\Desktop\6_revenue_category.png')
plt.close()

# 7. SALES VOLUME BY CATEGORY
plt.figure(figsize=(10, 6))
sns.countplot(x='category', data=df, palette='Set2')
plt.title('Items Sold by Category')
plt.savefig(r'C:\Users\dell\Desktop\7_sales_volume_category.png')
plt.close()

# 8. SUBSCRIPTION DONUT
plt.figure(figsize=(8, 8))
sub_counts = df['subscription_status'].value_counts()
plt.pie(sub_counts, labels=sub_counts.index, autopct='%1.1f%%', startangle=140)
plt.gca().add_artist(plt.Circle((0,0),0.70,fc='white'))
plt.title('Subscription Distribution')
plt.savefig(r'C:\Users\dell\Desktop\8_subscription_donut.png')
plt.close()

# 9. CUSTOMER LOYALTY DISTRIBUTION
plt.figure(figsize=(8, 5))
sns.histplot(df['previous_purchases'], bins=10, kde=True, color='orange')
plt.title('Customer Loyalty Distribution')
plt.savefig(r'C:\Users\dell\Desktop\9_customer_loyalty.png')
plt.close()

# 10. SALES VOLUME BY AGE GROUP
plt.figure(figsize=(10, 6))
sns.countplot(x='age_group', data=df, palette='cubehelix')
plt.title('Sales Volume by Age Group')
plt.savefig(r'C:\Users\dell\Desktop\10_sales_age.png')
plt.close()