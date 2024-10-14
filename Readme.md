Car Price Prediction Using Simple Regression Method 
This project aims to predict the prices of cars based on factors such as fuel type, kilometers driven, and the year of the car. The dataset used for this analysis is from Quikr Car Sales, and the model primarily uses simple linear regression.

Table of Contents
1: Objective
2: Dataset
3: Methodology
4: Results

Objective
The objective of this project is to create a predictive model that can estimate the price of a car based on three key factors:
1: The type of fuel
2: The number of kilometers driven
3: The year of the model

Dataset
The dataset used is from Quikr Car Sales. You can download the dataset from this GitHub link.

Dataset Columns:
1: Name: The name of the car
2: Company: The company or manufacturer
3: Year: The year the car was purchased
4: Price: The selling price of the car
5: Kms_Driven: The total kilometers driven by the car
6: Fuel_Type: The type of fuel used by the car

Methodology 
1: Data Preprocessing
    Year: Converted the Year column to integer type.
    Price: Removed entries with 'Ask for Price' and non-numeric characters, converted the column to integer type.
    Kms_Driven: Removed non-numeric characters and converted it to integer type.
    Fuel_Type: Filled missing values with 'Petrol'.

2: Visualization
Several plots are generated to understand the relationships between car prices and factors like the manufacturer, year of manufacture, kilometers driven, and fuel type.

3: Model Building
A linear regression model was used for the price prediction. The model was trained using the features such as the year, kilometers driven, and fuel type.
The model's accuracy was measured using the R-squared value.

4: Example Prediction
A prediction was made for a 2006 Toyota Corolla, which had been driven for about 5100 kilometers and runs on petrol.

5: Results
The predicted price for the 2006 Toyota Corolla was approximately 428,873.63.