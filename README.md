# Projet: iRail

## Description

This project aims to develop a small application to retrieve and analyse data from iRail API.

You can find the documentation of the API here: https://docs.irail.be/


## Language

* Python 3

## Requirements

* Create a virtual environnment
* Install the requirements


Use the following command in terminal to install requirements:

```
pip install -r requirements.txt
```

## Features

Give: 

* The percentage of trains running in the next hour (by destination).
* The average delay for trains in the next hour (by destination).
* The number of cancelled trains during the last 2 hours (by destination).

Input:

* iRail API -> Connections endpoint

Output:

* JSON files by destination with the data


## Prerequisite

You can add parameters to configuration file (Configuration directory).

By default, the application gives data about the connection between Nivelles and Charleroi.

For ex:

CONNECTIONS:
  1: ["Nivelles", "Charleroi"]

## Launch the app

* Launch the folling command:
```
python irail
```
