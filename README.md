# Shroom and Doom

## Project Description
- This project is my first personal project. It will go through the data science pipeline and attempt to discover whether a mushroom is edible. This repo will include working files as well as finals.

## Project Goals
- Find determining factors for mushroom edibility
- Construct a ML classification model that accurately predicts a mushrooms edibility above the baseline
- Deliver a report that a non-data scientist can read through and understand 

## Initial Questions
1. How many mushrooms are edible/inedible?
2. What features are most important in determining a mushroom's edibility?

## Project Plan
- Acquire data from Kaggle
- Prepare data
  - Remove unnecessary features
  - Identify and replace missing values
  - Alter innapropriate data types
- Explore the data to find dactors related to a mushrooms edibility
- Create a model to predict if a mushroom is edible or not
  - Use features identified in explore to build predictive models
  - Evaluate models on train and validate data
  - Select the best model based on highest accuracy, lowest false negative rate, and lowest difference between test and validate scores
  - Evaluate the best model on test data
- Conclude with recommendations and next steps

## Data Dictionary
| Feature | Definition | Data Type |
|:--------|:-----------|:----------|
|  cap-shape | bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s | object |
|  cap-surface | fibrous=f,grooves=g,scaly=y,smooth=s | object |
| cap-color | brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y | object |
| bruises | bruises=t,no=f | object |
| odor | almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s | object |
| gill-attachment | attached=a,descending=d,free=f,notched=n | object |
| gill-spacing | close=c,crowded=w,distant=d | object |
| gill-size | broad=b,narrow=n | object |
| gill-color | black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y | object |
| stalk-shape: | enlarging=e,tapering=t | object |
| stalk-root | bulbous=b,club=c,cup=u,equal=e, rhizomorphs=z,rooted=r,missing=? | object |
| stalk-surface-above-ring | fibrous=f,scaly=y,silky=k,smooth=s | object |
| stalk-surface-below-ring | fibrous=f,scaly=y,silky=k,smooth=s | object |
| stalk-color-above-ring | brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y | object |
| stalk-color-below-ring | brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y | object |
| veil-type | partial=p,universal=u | object |
| veil-color | brown=n,orange=o,white=w,yellow=y | object |
| ring-number | none=n,one=o,two=t | object |
| ring-type | cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z | object |
| spore-print-color | black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y | object |
| population | abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y| object |
| habitat | grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d | object |
|Additional Features|Encoded categorical data| uint8 |

## Steps to Reproduce
1. Clone this repo
2. Run notebook

## Takeaways
- TBD

## Recommendations
- TBD
