# Wine Quality Prediction


## Overview

This project is a machine learning model designed to predict the quality of wines based on various chemical attributes. The dataset contains information about fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol content.

## Input Features

Fixed Acidity: The non-volatile acids in the wine.
Volatile Acidity: The amount of acetic acid in the wine, which can lead to an unpleasant, vinegar taste.
Citric Acid: Found in small quantities, citric acid can add a refreshing taste to wines.
Residual Sugar: The amount of sugar remaining after fermentation stops, influencing the sweetness of the wine.
Chlorides: The amount of salt in the wine.
Free Sulfur Dioxide: A form of sulfur dioxide that exists as a dissolved gas in the wine.
Total Sulfur Dioxide: The total amount of sulfur dioxide in the wine, including both free and bound forms.
Density: The density of the wine, which is close to that of water depending on the alcohol content.
pH: Describes how acidic or basic the wine is on a scale from 0 to 14.
Sulphates: Additives that contribute to sulfur dioxide gas (SO2) levels.
Alcohol: The alcohol content of the wine.

## Model Prediction

The machine learning model uses these input features to predict the quality of the wine on a scale. The model has been trained on a dataset, and its performance metrics, such as Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared (R2), can be found in the associated documentation.


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/SumeetChougule/winequality.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n envWQ python=3.11 -y
```

```bash
conda activate envWQ
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/SumeetChougule/winequality.mlflow \
MLFLOW_TRACKING_USERNAME=SumeetChougule \
MLFLOW_TRACKING_PASSWORD=90cd3850e33bbd72900418c750f9caa930f0deda \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/SumeetChougule/winequality.mlflow

export MLFLOW_TRACKING_USERNAME=SumeetChougule

export MLFLOW_TRACKING_PASSWORD=90cd3850e33bbd72900418c750f9caa930f0deda

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

