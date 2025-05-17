# Alcohol Market Analysis – Retail & Wholesale Trends

### Table of Contents

  - [Project Overview](#project-overview)
  - [Data Sources](#Data-Sources)
  - [Tools](#Tools)
  - [Data Cleaning and Processing](#Data-Cleaning-and-Processing)
  - [Exploratory Data Analysis](#Exploratory-Data-Analysis)
  - [Dashboards and Visualizations](#Dashboards-and-Visualizations)

    - [Executive Summary](#Executive-Summary)

    - [Time Trends](#Time-Trends)

    - [Supplier Analysis](#Supplier-Analysis)

    - [Product Insights](#Product-Insights)
    
  - [Results](#Results)
  - [Future Work](#Future-Work)
  - [Limitations](#Limitations)

### Project Overview

This project analyzes public alcohol distribution and sales data from Montgomery County, using Python for data cleaning and Power BI for dashboard development. The dataset includes retail, warehouse, and transfer sales of alcoholic and some non-alcoholic beverages, broken down by supplier, product type, and time period.

The goal of this project is to uncover trends in sales volume, supplier performance, and product category demand across different distribution channels.

### Project Questions

1. Which types of alcoholic beverages generate the highest retail sales in Montgomery County, and how have these trends changed over time?

2. Who are the top-performing suppliers by sales volume, and how does their contribution vary by product category?

3. What are the total retail and warehouse sales quantities from 2017-2020? How many products were sold? How do these numbers vary by year?

### Data Sources

The data in this project is sourced from a data.gov publicly available .csv file which contains the alcocol sales and transfers (retail and warehouse) within Montgomery county.

Data.gov Montgomery County website link:
https://catalog.data.gov/dataset/warehouse-and-retail-sales 

### Tools

![Excel](https://img.shields.io/badge/Tool-Excel-green?logo=microsoft-excel&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Data%20Visualization-yellow)
  
### Data Cleaning and Processing

The data in this project was cleaned and standardized using a python script which handled these steps:

- Date formatting and consistency

- Missing value handling, filtering out incomplete entries

- Column renaming

- Duplicate row removal

After these steps were completed, processed data was then loaded into Microsoft PowerBI

### Dashboards and Visualizations

This project features a series of interactive Power BI dashboards that provide actionable insights across multiple aspects of retail and warehouse sales. The dashboards are designed for clarity, interactivity, and overall sales analysis, with an executive summary page that summarizes the key charts and findings.

Below are screenshots and explanations of each dashboard designed in Power BI to explore different facets of alcohol sales trends and supplier performance.

### Executive Summary


![Executive Summary](https://github.com/user-attachments/assets/9fc043d9-6fee-493a-95f9-499bf008e420)


### Time Trends


![Time Trends](https://github.com/user-attachments/assets/c6221d6e-6748-465d-b6b4-2395cc9b112f)


### Supplier Analysis


![Supplier Analysis](https://github.com/user-attachments/assets/bd545aa1-4524-448e-92e7-9a76bb17ba8c)


### Product Insights


![Product Insights](https://github.com/user-attachments/assets/7b69b189-e69c-45c9-92d5-23ad90f4338d)


### Results

From 2017 to 2020, the leading contributors to retail alcohol sales in Montgomery County were Liquor (37%), Wine (35%), and Beer (27%), as shown in the donut chart. All three categories experienced seasonal fluctuations, with a noticeable spike in late 2017d. Aside from this spike and minor peaks in late 2019 and early 2020, retail sales remained relatively stable throughout the period. By July 2020, each of the top product categories ended with sales volumes comparable to their starting levels in July 2017.

The top three suppliers by retail sales were:

  - E & J Gallo Winery – $166K in sales, predominantly from wine

  - Diageo North America Inc – $145K, primarily from liquor

  - Constellation Brands – $137K, mainly wine

As shown in the “Retail Sales from Top Suppliers Over Time” chart, all three suppliers saw a major sales spike in late 2017, followed by a period of relative stability and increased fluctuations beginning in 2019. These suppliers were also among the top performers in the warehouse channel, reflecting a consistent and broad distribution presence across retail and wholesale operations.

Across the full dataset, 34,030 unique products were sold, generating $2.15 million in retail sales, $7.80 million in warehouse sales, and $2.13 million in retail transfers. Year-over-year analysis reveals a dip in both retail and warehouse sales in 2018, followed by a significant peak in 2019, particularly in warehouse sales which approached $4 million. The “Time Trends” visuals confirm 2019 as the most active year, with the highest average sales in both distribution channels. A dual-axis chart comparing averages shows warehouse sales continuing to rise after 2018, while retail sales growth tapered off slightly by 2020.


### Future Work

To further enhance the depth and utility of this analysis, several avenues of future work could be pursued:

Customer Demographics: Incorporating demographic data such as age, gender, and location could help uncover consumption trends and preferences across different population segments.

Pricing and Profitability Analysis: Adding unit pricing and profit margin data would enable analysis of not only sales volume but also overall profitability by product type and supplier.

Forecasting Models: Applying time series forecasting could help predict future demand trends for retail and warehouse sales.

### Limitations

While the dashboard offers valuable insights, there are several limitations to be aware of:

Missing Contextual Data: The dataset lacks external variables such as pricing, marketing campaigns, or economic indicators that might explain fluctuations in sales.

Data Collected Monthly: Data is aggregated at a monthly level, which limits the ability to perform more granular, day-to-day trend analysis.

No Consumer Behavior Data: The analysis is limited to supply-side metrics and does not include end-consumer behaviors, purchase motivations, or satisfaction metrics.

Static Time Range: The dataset only covers the years 2017–2020, meaning any conclusions may not reflect post-2020 market dynamics or pandemic recovery patterns.

Assumption of Data Accuracy: The analysis assumes the underlying dataset is complete and accurate; any gaps or inconsistencies in reporting could influence the reliability of findings.
