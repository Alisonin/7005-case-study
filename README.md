# 7005 Case Study: E-Commerce Customer Behaviour Analysis

## Objective
to demonstrate understanding of E-commerce Customer Behavior and ability to derive meaningful business insights from data analysis by applying decision tree and ensemble methods in a practical context.

## Dataset
Based on an existing dataset, python is utilized to generate a dataset with features that match the requirements of the topic.

Based dataset：This dataset provides a comprehensive view of customer behavior within an e-commerce platform. Each entry in the dataset corresponds to a unique customer, offering a detailed breakdown of their interactions and transactions. The information is crafted to facilitate a nuanced analysis of customer preferences, engagement patterns, and satisfaction levels, aiding businesses in making data-driven decisions to enhance the customer experience.

> link of based dataset：https://www.kaggle.com/datasets/uom190346a/e-commerce-customer-behavior-dataset

### generated dataset overview
In the backdrop of this dynamic e-commerce landscape, the dataset of customer transactions from an e-commerce website emerges as a valuable asset. This dataset containing 20,000 records, encompasses a wide range of customer attributes and purchase history over the last year, providing a comprehensive view of customer behavior and interactions.

# Roles of three tools
## 1. Talend Data Prep
Data quality is paramount in any analytical process, and Talend Data Preparation addresses this with a suite of features designed to improve the accuracy and consistency of data.  De-duplicates records, standardizes styles, and checks data against predefined patterns or business rules.  The platform's ability to automatically detect and correct errors helps maintain high standards of data quality, which is critical for reliable analytics.  By ensuring that data is clean and well-structured, Talend reduces the risk of inaccurate conclusions.  It also provides a solid foundation for further data exploration and reporting.

### Detail steps
* **Feature creation:** **extract date parts on column LastPurchase Date in Talend.**

*In specific, month of year, day of month, day of the week, week of the year in the time series are extracted in order to mine the cyclical patterns of month, week, and cross terms.*

* **Feature modification:** round value using the ceil mode on the TotalSpent column


* **Data cleaning:** Each of TotalPurchases, TotalSpent, and Occupation has 200 missing values, which is 1% of the total.

    * delete the rows with empty cell on column Occupation.

    * median value is used to estimate the missing values in both TotalPurchases and TotalSpent
      
## 2. KNIME: Data visualization
###  statistical view 
* present a nuanced view of customer behavior, with outliers in terms of spending, buying patterns, and engagement with the site. The high spending outliers and churn rates are particularly significant and suggest areas for deeper analysis to inform business strategies aimed at retaining and maximizing value.
  
###  Univariate analysis
* Categorical Variables Pie Chart:
  * an almost equal distribution of the categories by gender.
  * The occupations, which include artist, manager, teacher, doctor, engineer, and salesperson, appear to be relatively evenly distributed.
  * The product category preference chart shows three segments: Electronics, Clothing, and Housewares, each of which occupies a significant portion of the graph.
  * A larger segment for "Bronze" level members indicates that the majority of members fall into this category, with "Silver" and "Gold" memberships making up smaller proportions, and "Platinum" being the least common.
  * the distribution across cities such as Miami, New York, Los Angeles, Chicago and San Francisco appear fairly balanced.
    
* Histograms of continuous variables
  * 'Age' histogram displays a broad and fairly uniform age range.
  * 'TotalPurchases' is right-skewed, showing most individuals make a few purchases, while a few make many, suggesting a potential focus group for marketing.
  * 'TotalSpent' also exhibits a right skew, with many small transactions and a few large ones, hinting at high spenders as outliers.
  * The 'LastPurchaseDate_DAY_OF_MONTH' histogram suggests more purchases occur at the beginning of the month, possibly reflecting payday impacts or early month promotions.
  * The 'LastPurchaseDate_DAY_OF_MONTH' histogram suggests more purchases occur at the beginning of the month.
  * The 'Frequency of Website Visits' histogram is positively skewed, with most visitors coming to the website infrequently.

## 3. SAS: Modeling
  * specify variable roles(here are three changes needed to be mentioned.)
    * Churn: This could be the target variable , as the aim of this case study is to predict customer churn.
    * LastPurchaseDate: Combing the analysis in Feature creation, It could be rejected, since there are many related variables (like DAY_OF_WEEK, DAY, MONTH, WEEK_OF_YEAR) that interpret the same information.
    * CustomerID: It should be an ID role.
  * **Data partition:** ataset will be split with 80:20 ratio.
  * **Decision Tree**: with 2 branches maximum and a maximum depth of 10 so we can avoid over fitting.
    * the 0.3 misclassification rate may need improvement depending on the business context.
    * Age shows a ratio of 2.1641, indicating a higher relative importance in validation compared to training.
  * **Decision Tree(entropy)-purning**

### **Breakdown rules of the nodes**:
  * Considering customers from Los Angeles or Miami, if the last purchase was made before Friday (Day of Week < 5.5), and the total amount spent is equal to or more than 18.745, then the likelihood of churn is 30%.
  * For the same locations, if the last purchase was made before Friday and the total spent is less than 18.745, and the customer's age is under 28.5 years, the likelihood of churn increases slightly to 35%.
  * Still focusing on Los Angeles and Miami, if the last purchase was made before Friday, the total spent is less than 18.745, but the customer's age is 28.5 years or more, the likelihood of churn drops significantly to 13%.
  * For customers from the same locations who made their last purchase on a Friday or Saturday (Day of Week between 5.5 and 6.5), the likelihood of churn is 24%.
  * Lastly, for customers from Los Angeles or Miami who made their last purchase on a Sunday, the predicted likelihood of churn is 28%.

### Ensemble Methods - Random forest
> an average squared error (ASE) of 0.210, a misclassification rate of 0.301, and a Log Loss of 0.611.

### Ensemble Methods - Gradient boosting
> The misclassification rate is close to 0.30068 on both the training and validation data.

## Outcome
As for comparison, three machine learning models—Random Forest, Bagging, and Boosting—achieve an accuracy of 69.935%. Despite the same accuracy, they employ distinct methods. Random Forest uses an ensemble of decision trees, Bagging trains models on different dataset subsets, and Boosting iteratively improves a weak learner. The choice between them may depend on factors like interpretability and computational efficiency. Additional metrics can provide a more comprehensive evaluation.



# Reflections or Learning Outcomes
* This case study strongly illustrates the importance of thorough model evaluation and selection in sas.

* During data generation, it is a challenge to make the data close to reality.

* In order to overcome challenges such as data imbalance and overfitting, creative solutions such as resampling and oversampling are required.

* To maintain model effectiveness over time, the iterative nature of model deployment and monitoring is critical.

