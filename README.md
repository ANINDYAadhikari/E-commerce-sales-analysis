# 🛒 E-Commerce Sales Analysis

**Author:** Anindya Adhikari

---

## 📊 Project Overview

Retail businesses operate in highly competitive markets where understanding sales performance, profitability drivers, customer behavior, and regional differences is critical for strategic decision-making.

This project analyzes a Superstore E-commerce dataset to uncover actionable business insights related to:

* Revenue generation
* Profitability optimization
* Customer value
* Regional performance
* Operational efficiency
* Growth sustainability

The goal is to move beyond descriptive statistics and extract strategic recommendations that can support data-driven business decisions.


## 🛠 Tools & Technologies

* **Python**
* **Pandas** – Data manipulation & aggregation
* **NumPy** – Business logic & metric engineering
* **Matplotlib & Seaborn** – Data visualization


## 📁 Dataset Information

The dataset contains transactional-level order data including:

* Sales
* Profit
* Quantity
* Discount
* Category & Sub-Category
* Customer Name
* Region & State
* Shipping Mode
* Order Year

It represents a retail superstore’s historical sales performance across multiple regions and product categories.


## 🔎 Analysis Performed

### 1️⃣ Exploratory Data Analysis (EDA)

* Checked for missing values and duplicate records
* Analyzed unique customer segments, states, and categories
* Reviewed statistical distribution of key numeric variables


### 2️⃣ Sales Performance Analysis

* Total and average sales by category
* Top 5 states by revenue
* Yearly sales trend analysis
* Identification of highest revenue-generating categories


### 3️⃣ Profitability & Loss Analysis

* Most and least profitable categories
* Identification of loss-making sub-categories
* Correlation analysis between discount and profit
* Profit segmentation using NumPy (Loss / Medium / High Profit)


### 4️⃣ Regional Performance Analysis

* Total sales and profit by region
* Profit margin calculation by region
* Heatmap visualization of Category vs Region profitability
* Identification of high-sales but low-profit states


### 5️⃣ Customer Intelligence

* Top 10 customers by sales and profit
* Identification of revenue concentration among key customers
* Repeat ordering behavior by state


### 6️⃣ Operational Insights

* Profit distribution across shipping modes
* Average profitability comparison between shipping strategies


### 7️⃣ Advanced Business Metrics

* Year-over-Year (YoY) growth rate calculation
* Profit margin engineering using NumPy
* Correlation matrix for Sales, Profit, Quantity, and Discount
* Scatter analysis of Quantity vs Profit


## 💡 Key Insights

* **Technology** generates the highest overall sales revenue.
* Some sub-categories consistently produce losses, primarily associated with high discount levels.
* There is a **negative correlation between Discount and Profit**, indicating aggressive discounting reduces profitability.
* Certain states rank high in revenue but low in profit, suggesting cost inefficiencies or pricing strategy issues.
* Sales show an overall upward trend, but growth is not perfectly consistent year-over-year.
* Revenue contribution is concentrated among a relatively small group of top customers.
* Profit margins vary significantly across regions, highlighting strategic regional differences.


## 🚀 Strategic Business Recommendations

1. **Optimize Discount Strategy**
   Reduce heavy discounting on already low-margin products.

2. **Double Down on High-Performing Categories**
   Invest more in categories that generate both strong revenue and healthy margins.

3. **Investigate High-Sales, Low-Profit States**
   Review logistics costs, operational expenses, and pricing models in these regions.

4. **Strengthen Customer Retention Programs**
   Develop loyalty or targeted marketing campaigns for top customers.

5. **Shipping Mode Optimization**
   Evaluate cost-to-profit relationship across shipping strategies to improve operational margins.

6. **Monitor Growth Volatility**
   Focus on stabilizing year-over-year growth to ensure sustainable expansion.


## 📂 Project Structure

ecommerce-sales-analysis/
│
├── Code/
│   └── analysis.py
│
├── Data/
│   └── superstore.csv
│
├── Images/
│   ├── code/
│   └── plots/
│
└── README.md