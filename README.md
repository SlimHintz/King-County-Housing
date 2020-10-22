# Kings County Housing Price Preditions

**Authors**: [Tim Hintz](mailto:tjhintz@gmail.com)

![img](./images/seattle)

## Overview


The present research utilized the King County data set to build a predictive linear model of housing prices in that region. The present model generated 420 features via interactions and polynomial columns as well as some non-linear transformations of the square footage columns. 

I made a focus on geospatial analysis. Due to time constraints, I was unable to scrape location data for key features like good schools, water fronts and public transport. Instead I used Geohash2 to fit a z-space curve filling line to my region. I then dummied all of the columns and included them in my dataset. 

RFE and K best did not improve my models RMSE through feature selection. However Lasso regression brought my RMSE down by almost $10,000. My final model is therefore a sklearn lasso regressor object that has been pickled and stored as `model.pickle`


Due to this being a predictive problem, my results are not interpretable.

### Business Problem

We need to be able to accurately predict the price of a house based on it's features in order to compete in the market. If you undervalue the property you lose money on the investment and if you over price your house you run the risk of not selling the property at an opportune time. 

This model allows you to predict housing prices. with `still don't know the official RMSE`


### The Data

In the folder `raw` are movie datasets from:

* https://www.kingcounty.gov/services/gis/GISData.aspx
* Flatiron School
* Kaggle


In the folder `cleanedData` are the data frames that I use in my model construction.

### Methods

No data cleaning was used apart from the imputation of 12 observations that had been determined to have false records when I cross referenced them with Zillow listings and infered from google maps. 

The data was standardized using sklearn's standard scalar. The same scalar is pickled as scalar.pickle in the repo and was used to transform my test set.

I used independent T tests to decide which features were key in determining price. Then I created interaction columns and polynomial columns for all of my features. In handling geospatial data, I geohashed the houses based on their coordinates and createde dummy columns for the geohashes. The zipcodes were also dummied and added to the data set. Before lasso regression I had 420 features. 

When developing my model, after adding or modifying any feature I conducted a train test split on the data followed by an analysis of RMSE. If it went down, I continued, otherwise I would backtrack and try something else. Before I used Lasso my train test split gave me 129K with a 10 fold cross validation score of 0.84 with a std of 0.01.

For Lasso regression I used an alpha of 0.01, 0.02 and 0.03 but visually I did not see a change in the distribution. When I ran a Levene's test for difference in variation between them was not significant. 


### Results

#### The location of the house is important in determining it's price 
![img](./images/predictionDistributions.png )

Houses located near water or clustered together with outher houses have a much higher price than those inland and in isolation. 

When I ran a RFE to determine the most important features, I found that all of the top 10 were either geohashes or zipcodes. However, as they were dummy columns 

#### There was a signeficant effect of interactions between variables
![img](./images/bath_bed.png)

During our research we found that some genres are particulalry risky investments in the current market. Westerns and News based movies seem to do badly especially when the budget for them is low. 

On the other hand low budget fantasy, mystery and horror do relatively well. 

Interpreting the first sections findings we think the soundest strategy is an investment in high budget musicals and sports movies with a modertate investment in low budget horror, thriller and crimes movies.


#### Month of Release Had Little Bearing on ROI
![img](./images/predictionDistributions.png)

Finally, we examined the effect of month/seasonality on the ROI of movies released. From this chart, there is little evidence of an effect of month on ROI.


#### Conclusions

It is our opinion that if Microsoft wishes to get into the movie industry, the safest way to do so would be to invest heavily into large, blockbuster type films particularly Musicals and Sports based movies to do well. So long as they invest a over 100 million in their movies, they should be fine.

However, smaller budget films have almost a 15% chance of returning over 1000%. This is something that should be investigated further. In particular, Horror, Crime and Mystery films can yeild an enormous ROI under some currently undiscovered conditions. It is our opinion that any studio should be investing in lower budget indie films in order to maximise their chances of returning on their investment.

#### Further Research

- Our data is only a small subset of the available information. Supplementary data should be used in further analysis in order to: 
    - Try to replicate our findings
    - Perform more powerful statistical analysis


- We in each category there was a signeficant amount of outliers

- We did not look into the effect of celebrity on the success of a movie. A paper published in 2017 (François A. Carrillat et al. Debates and assumptions about motion picture performance: a meta-analysis, Journal of the Academy of Marketing Science (2017). DOI: 10.1007/s11747-017-0561-6) gave strong evidence that most important factors involved in a movies success are
    - Fame of the Actors
    - Marketing Budget
    - Number of screens released on


#### Navigation
- `microsoft-studios-eda.ipynb`: The final notebook containing our collected work and discussions
- `datacleaning`: Notebooks containing the authors preliminary EDA and data cleaning
- `rawdata`: File containing our wrangled and cleaned data sets
- `zippedData`: Original data obtained through the Flatiron School
- `README.md`: Display document containing our key findings and this sentence.
- `src.py`: Collected functions utilized for both data cleaning and EDA

