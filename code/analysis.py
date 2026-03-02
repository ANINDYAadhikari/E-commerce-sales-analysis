# =========================
# E-COMMERCE SALES ANALYSIS
# -------------------------
# Author-- Anindya Adhikari
# =========================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')

# Load Dataset
df = pd.read_csv("data/superstore.csv", encoding='latin-1')
print("Dataset Loaded Successfully!\n")


# Preview Data
print("FIRST 5 ROWS")
print(df.head(50))
print("\nDATA SHAPE:", df.shape)
print("\nCOLUMNS:")
print(df.columns)
print("\nDATA INFO:")
print(df.info())
print("\nSTATISTICAL SUMMARY:")
print(df.describe())


# SECTION 1 -- Basic EDA (Understanding the Business)
# Q1
print("How many Unique customers(Segemnt) ? ")
print(df['Segment'].nunique())
print("How many Unique cities ? ")
print(df['City'].nunique())
print("How many Unique states ? ")
print(df['State'].nunique())
print("How many Unique categories ? ")
print(df['Category'].nunique())
print("Missing values per column:\n", df.isnull().sum())
print("\nTotal duplicate rows:", df.duplicated().sum())


# Q2
# Calculate percentage of total orders by segment
segment_percentage = df['Segment'].value_counts(normalize=True) * 100
# Round the percentages to 2 decimal places
segment_percentage = segment_percentage.round(2)
# Print the results
print("Percentage of Total Orders by Segment:", segment_percentage)


# Q3 
# Average Sales, Quantity and Profit per order
# Select the 3 columns and calculate their average (mean)
sales = df[["Sales", "Quantity", "Profit"]].mean()  #[[]] -- used here because pandas only read one column in one [] & [[]] -- here it reads as many as we want
print("Average values per order:", sales)


# SECTION 2 -- Sales Analysis (Pandas + Matplotlib)
# Q1 
# Which category generates: Highest total sales ? Highest average sales per order ?
# Group data by Category and add (sum) all sales
total_sales = df.groupby('Category')['Sales'].sum()
print("Total Sales by Category:", total_sales.idxmax())
# Group data by Category and calculate average sales
avg_sales = df.groupby('Category')['Sales'].mean()
print("\nAverage Sales per Order by Category:", avg_sales.idxmax())
# -------- Bar Chart: Total Sales --------
plt.figure() # this used for commands to open a new graph 
total_sales.plot(kind='barh')
plt.title("Total Sales by Category")
plt.ylabel("Category")
plt.xlabel("Total Sales")
plt.show()
# -------- Bar Chart: Average Sales --------
plt.figure()  
avg_sales.plot(kind='barh')
plt.title("Average Sales per Order by Category")
plt.xlabel("Category")
plt.ylabel("Average Sales")
plt.grid()
plt.show()


# Q2 
# Group the data by 'Sub-Category'
# Then calculate the total quantity sold for each sub-category
# Finally, sort the values in ascending order
most_quantity = df.groupby('Sub-Category')['Quantity'].sum().sort_values()
print(most_quantity)
plt.figure()
most_quantity.plot(kind = 'barh', color = 'teal')
plt.title('Total Quantity Sold by Sub-Category')
plt.xlabel('Total Quantity')
plt.ylabel('Sub-Category')
plt.tight_layout() # Adjust layout to prevent label cutoff
plt.show()


# Q3 
# Top 5 states by sales
# Group the dataset by 'State'
# Then calculate total sales for each state
state_sales = df.groupby('State')['Sales'].sum()
# Get the top 5 states with highest sales
top_state = state_sales.nlargest(5)
print(top_state)
top_state.plot(kind = 'bar', color = 'green')
plt.title('Top 5 States by Sales')
plt.xlabel('Total Quantity')
plt.ylabel('Sub-Category')
plt.tight_layout() # Adjust layout to prevent label cutoff
plt.show()


# Q4
# Monthly Sales Trend: Are sales increasing over years?  Which year had highest revenue?
trend = df.groupby(['Order_Year'])['Sales'].sum()
print(trend)
plt.figure()
trend.plot(kind = 'line', marker = 'o')
plt.title('Yearly Sales Trend')
plt.xlabel('Order Year')
plt.ylabel('Total Sales')
plt.grid(True) # Add grid lines for better readability
plt.tight_layout() # Adjust layout to avoid overlapping labels
plt.show()
print("Year with Highest Sales:", trend.idxmax()) # Identify the year with the highest sales revenue
print("Highest Revenue:", trend.max())



# SECTION 3 -- Profit & Loss Analysis 
# Q1
# Which category has: Highest profit? Lowest profit? Negative profit?
#Use: groupby('Category')['Profit'].sum()
profit_analysis = df.groupby('Category')['Profit'].sum()
print(profit_analysis)
print("Highest Profit Category:", profit_analysis.idxmax())
print("Lowest Profit Category:", profit_analysis.idxmin())
print("Categories with Negative Profit:")
print(profit_analysis[profit_analysis < 0])    # Filter and display categories with negative profit (loss)


# Q2
# Which sub-categories are loss-making? Filter: df[df['Profit'] < 0]
# Then group by sub-category
loss_making = df[df['Profit'] < 0]    # Filter rows where Profit is negative
loss_by_subcategory = loss_making.groupby('Sub-Category')['Profit'].sum()   # Group by Sub-Category and calculate total loss
print(loss_by_subcategory)


# Q3: Is discount affecting profit?
# Business Question: Do higher discounts reduce profit?
# Calculate correlation between Discount and Profit
discount_corr = df[['Discount', 'Profit']].corr()
print("Correlation Matrix:")
print(discount_corr)
plt.figure()
plt.scatter(df['Discount'], df['Profit'], c=df['Profit'], cmap='viridis')
plt.colorbar(label='Profit')  # Shows color scale
# Add labels and title for clarity
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Discount vs Profit")
plt.show()


# SECTION 4 -- Regional Performance
# Q1
# Which region has highest sales? Highest profit margin?
# Step 1: Create Profit Margin column
df['Profit_Margin'] = df['Profit'] / df['Sales']
region_data = df.groupby('Region').agg({    # Step 2: Calculate total Sales and Profit by Region
    'Sales': 'sum',
    'Profit': 'sum'
    })
region_data['Profit_Margin'] = region_data['Profit'] / region_data['Sales'] # Step 3: Calculate Profit Margin using regional totals
print(region_data)
print("Region with Highest Sales:", region_data['Sales'].idxmax())  # Step 4: Find region with highest Sales
print("Region with Highest Profit Margin:", region_data['Profit_Margin'].idxmax())  # Step 5: Find region with highest Profit Margin


# Q2 
# Create a heatmap: Category vs Region (Profit) 
# Use: pivot_table(), sns.heatmap()
# Create pivot table (Category vs Region with total Profit)
profit_pivot = df.pivot_table(
    values='Profit',
    index='Category',
    columns='Region',
    aggfunc='sum'
)
print(profit_pivot)
plt.figure(figsize=(8,5))
sns.heatmap(profit_pivot, annot=True, fmt='.0f', cmap='coolwarm')
plt.title("Profit Heatmap: Category vs Region")
plt.show()



# SECTION 5 — Customer Intelligence
# Q1
# Top 10 customers by: Sales, Profit
customers = df.groupby('Customer Name').sum()  # Group data by Customer Name
customers = customers[['Sales', 'Profit']]  # Select only Sales and Profit columns
customers_sorted_sales = customers.sort_values('Sales', ascending=False)  # Sort customers by Sales (highest first)
top10_sales = customers_sorted_sales.head(10)  # Get top 10 customers by Sales
print("Top 10 Customers by Sales:", top10_sales)
customers_sorted_profit = customers.sort_values('Profit', ascending=False)  # Sort customers by Profit (highest first)
top10_profit = customers_sorted_profit.head(10)  # Get top 10 customers by Profit
print("\nTop 10 Customers by Profit:", top10_profit)


# Q2 
# Repeat customer's state: who ordered more than 5 times
state_orders = df['State'].value_counts()  # Count number of orders per state
repeat_states = state_orders[state_orders > 5]  # Select states with more than 5 orders
print("States with more than 5 orders:", repeat_states)



# SECTION 6 -— Shipping & Operations
# Q1
# Boxplot: Profit distribution by Shipping Mode.
# Calculate average profit per shipping mode
ship_profit = df.groupby('Ship Mode')['Profit'].mean()
print("Average Profit by Shipping Mode:", ship_profit)
print("\nShipping Mode with Highest Average Profit:", ship_profit.idxmax()) # Shipping mode with highest average profit
plt.figure()
sns.boxplot(data=df, x='Ship Mode', y='Profit')
plt.title("Profit Distribution by Shipping Mode")
plt.suptitle("")  # Removes automatic extra title
plt.grid(True)
plt.xlabel("Shipping Mode")
plt.ylabel("Profit")
plt.show()


# SECTION 7 -— NumPy-Based Business Metrics
# Q1
# Create Profit Margin column using NumPy: np.where(Sales > 0, Profit/Sales, 0)
#  Which category has best average margin?
# Create Profit Margin column using NumPy
df['Profit_Margin'] = np.where(df['Sales'] > 0, df['Profit'] / df['Sales'],0)
print(df[['Sales', 'Profit', 'Profit_Margin']].head())
# Calculate average profit margin per category
category_margin = df.groupby('Category')['Profit_Margin'].mean()
print("\nAverage Profit Margin by Category:", category_margin)
print("\nCategory with Best Average Margin:", category_margin.idxmax())



# Q2 
# Classify orders into: High Profit, Medium Profit, Loss
# Using NumPy conditions.
# Example: np.select(), Count how many orders fall in each category
# Define conditions
conditions = [df['Profit'] < 0, (df['Profit'] >= 0) & (df['Profit'] <= 200), df['Profit'] > 200]
# Define labels
choices = ['Loss', 'Medium Profit', 'High Profit']
# Add default as string
df['Profit_Category'] = np.select(conditions, choices, default='Unknown')
profit_counts = df['Profit_Category'].value_counts()  # Step 4: Count orders in each category
print("Number of Orders in Each Profit Category:", profit_counts)
plt.figure()
profit_counts.plot(kind='bar')
plt.title("Orders by Profit Category")
plt.xlabel("Profit Category")
plt.ylabel("Number of Orders")
plt.show()



# SECTION 8 — Advanced (Stand-Out Level)
# Q1
# Month-over-Month Growth Rate
# Calculate: pct_change()
# Question: Is the business growing consistently?

# Step 1: Calculate total sales per year
yearly_sales = df.groupby('Order_Year')['Sales'].sum()
print("Yearly Sales:",yearly_sales)
# Step 2: Calculate growth rate using pct_change()
yearly_growth = yearly_sales.pct_change()
# Step 3: Combine into one table
growth_table = pd.DataFrame({'Yearly Sales': yearly_sales, 'Growth Rate': yearly_growth})
print("\nYear-over-Year Growth Table:", growth_table)

# Step 4: Plot Sales Trend
plt.figure()
yearly_sales.plot()
plt.title("Yearly Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.show()

# Step 5: Plot Growth Rate
plt.figure()
yearly_growth.plot()
plt.title("Year-over-Year Growth Rate")
plt.xlabel("Year")
plt.ylabel("Growth Rate")
plt.show()


# Q2
# Find top 5 combinations: Category + Region, With highest profit. 
# Use: groupby(['Category','Region'])
# Step 1: Group by Category and Region
category_region_profit = df.groupby(['Category', 'Region'])['Profit'].sum()
print("Total Profit by Category and Region:", category_region_profit)
# Step 2: Sort by Profit (highest first)
sorted_profit = category_region_profit.sort_values(ascending=False)
# Step 3: Get Top 5 combinations
top5_combinations = sorted_profit.head(5)
print("\nTop 5 Category + Region Combinations by Profit:", top5_combinations)


# Q3
# Which states have high sales but low profit?
# Hint: Compare sales ranking vs profit ranking.
# Group by State and calculate total Sales and Profit
state_data = df.groupby('State')[['Sales', 'Profit']].sum()
print("State-wise Sales and Profit:", state_data)
# Rank states by Sales (highest = rank 1)
state_data['Sales_Rank'] = state_data['Sales'].rank(ascending=False)
# Rank states by Profit (highest = rank 1)
state_data['Profit_Rank'] = state_data['Profit'].rank(ascending=False)
print("\nState Rankings:", state_data)
# Filter states with high sales but low profit
problem_states = state_data[(state_data['Sales_Rank'] <= 10) & (state_data['Profit_Rank'] > 10)]
print("\nStates with High Sales but Low Profit:", problem_states)



# SECTION 9 -— Correlation & Insights
# Q1
# Correlation matrix of: Sales, Profit, Quantity, Discount
# Plot heatmap.
# Step 1: Select required columns
corr_data = df[['Sales', 'Profit', 'Quantity', 'Discount']]
# Step 2: Calculate correlation matrix
corr_matrix = corr_data.corr()
print("Correlation Matrix:", corr_matrix)

# Step 3: Plot heatmap
plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix Heatmap")
plt.show()


# Q2
# Does higher quantity always mean higher profit?
# Plot: Scatter plot (Quantity vs Profit)
# Step 1: Scatter plot
plt.figure()
plt.scatter(df['Quantity'], df['Profit'])
plt.title("Quantity vs Profit")
plt.xlabel("Quantity")
plt.ylabel("Profit")
plt.show()

