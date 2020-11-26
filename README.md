# Recommend Song Base on Clustering :Project Overview
* Created a tool that recommends the songs by using audio features to help the people to find the thai song base on their preference.
* Optimized the Kmean using the Elbowmethod , Silhouette Score to compare between the original data and the data that have been transform form the PCA method.
* Built a simple website using Flask

## Code and Resources
**Python Version**: 3.8

**Packages**: pandas, numpy, sklearn, matplotlib, seaborn, altair, flask, pickle 

**Data Source** : http://organizeyourmusic.playlistmachinery.com/#

## Data Cleaning
* Removed the unwanted column.
* Droped the duplicates songs
* Removed non thai song
* Extracted the added year and month of the song


## EDA


## Model Building
First, I standardize the data because the data have different magnitude then I created the new data that come from the PCA method of 2 components.

I tried two different methods in evaluating the clustering that is elbow method and silhouette score. I choose the data from the PCA method because it has fewer distortion scores and more silhouette scores.

two different model:
* **Kmeans from the original data**:
* **Kmeans from the PCA data**:


## Productionization
https://chinsongrecommend.herokuapp.com/
