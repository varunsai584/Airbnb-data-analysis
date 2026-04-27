#  Airbnb Data Analysis

##  Project Overview
Performed exploratory data analysis (EDA) on Airbnb NYC dataset (~48,000 listings) to uncover pricing patterns, location trends, and host behavior.

##  Objectives
- Analyze pricing trends across neighborhoods
- Understand impact of room types on pricing
- Explore relationship between reviews and price
- Identify high-performing hosts and listing patterns

##  Key Insights
- Manhattan has the highest average listing prices among all boroughs  
- Entire homes/apartments are priced significantly higher than private/shared rooms  
- Listings with higher availability tend to have lower prices (supply-demand trend)  
- Review count has weak correlation with price, indicating pricing is location-driven  

##  Tech Stack
- Python (Pandas, NumPy)
- Data Visualization (Matplotlib, Seaborn)
- Jupyter Notebook

##  Visualizations
- Price distribution histogram  
- Average price by neighborhood group  
- Room type vs price comparison  
- Reviews vs price scatter plot  
- Availability analysis  

##  Dataset
- Source: Kaggle (Airbnb NYC 2019 dataset)
- Size: ~48,000 rows

##  How to Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
