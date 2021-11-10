#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from scipy.stats import skew

import constants


# impute missing values
def missing_val_imputer(df):

    df['SUBSECTOR'] = df['SUBSECTOR'].fillna('UNSPECIFIED')
    df['BI_PERIOD'] = df['BI_PERIOD'].fillna(0) #BI Not insured -> 0, but there are 5 with COVERAGE = PD,BI but this column is nan
    df["TOP_FMLS"] = df["TOP_FMLS"].fillna(0) #there are only 5 exmaples where TOP_FMLS and TOP_MPL are both nan
    df["TOP_MPL"] = df["TOP_MPL"].fillna(0)
    df["OIL"] = df["OIL"].fillna(0)
    df["WORDING"] = df["WORDING"].astype(str) # nan as a new type
    df["QUALITY_RISK_MGT"] = df["QUALITY_RISK_MGT"].fillna('Average') 
    df["ASSET_QUALITY"] = df["ASSET_QUALITY"].fillna('Average')
    df["BI_MITIGATION"] = df["BI_MITIGATION"].fillna('Non applicable')
    df["MB_QUALITY"] = df["MB_QUALITY"].fillna('Average')
    df["INSUREDVALUEBI"] = df["INSUREDVALUEBI"].fillna(0.) # nan -> Coverage == "BI"
    df = df.fillna(0.) #for all the PD BI percent variables
    return df


# convert COVER_BI to a boolean

def convert_coverage(df):

    df['COVER_BI'] = [(True if x.find('BI') != -1 else False) for x in
                      df['COVERAGE']]
    return df


# combine labels in SECTOR, GUARANTEE, BUSINESSUNIT, UWCENTER, SUBSETCOR

def label_combiner(df):

    df.SECTOR.replace(constants.SECTOR_PAIR, inplace=True)
    df.GUARANTEE.replace(constants.GUARANTEE_PAIR, inplace=True)
    df.BUSINESSUNIT.replace(constants.BUSINESSUNIT_PAIR, inplace=True)
    df.UWCENTER.replace(constants.UWCENTER_PAIR, inplace=True)
    df.SUBSECTOR.replace(constants.SUBSECTOR_PAIR, inplace=True)
    return df


# convert 'MAIN_COUNTRY' to 'GEO_MARKET_SEGMENT'

def convert_geo_market_segment(df):

    df['GEO_MARKET_SEGMENT'] = 'Others'

    mask1 = df['MAIN_COUNTRY'].isin(constants.NORTH_AMERICA)
    mask2 = df['MAIN_COUNTRY'].isin(constants.LATIN_AMERICA)
    mask3 = df['MAIN_COUNTRY'].isin(constants.WESTERN_EUROPE)
    mask4 = df['MAIN_COUNTRY'].isin(constants.CENTRAL_AND_EASTERN_EUROPE)
    mask5 = df['MAIN_COUNTRY'].isin(constants.AFRICA)
    mask6 = df['MAIN_COUNTRY'].isin(constants.MIDDLE_EAST)
    mask7 = df['MAIN_COUNTRY'].isin(constants.MATURE_ASIA)
    mask8 = df['MAIN_COUNTRY'].isin(constants.EMERGING_ASIA)

    df.loc[mask1, 'GEO_MARKET_SEGMENT'] = 'North America'
    df.loc[mask2, 'GEO_MARKET_SEGMENT'] = 'Latin America'
    df.loc[mask3, 'GEO_MARKET_SEGMENT'] = 'Western Europe'
    df.loc[mask4, 'GEO_MARKET_SEGMENT'] = 'Central and Eastern Europe'
    df.loc[mask5, 'GEO_MARKET_SEGMENT'] = 'Africa'
    df.loc[mask6, 'GEO_MARKET_SEGMENT'] = 'Middle East'
    df.loc[mask7, 'GEO_MARKET_SEGMENT'] = 'Mature Asia'
    df.loc[mask8, 'GEO_MARKET_SEGMENT'] = 'Emerging Asia'

    return df


# log transform skewed features

# def transform_skew(df):

#     numerical_features = \
#         list(df.select_dtypes(include=[np.number]).columns.values)
#     skewed_features = df[numerical_features].apply(lambda x: \
#             skew(x)).sort_values(ascending=False)
#     high_skewness = skewed_features[abs(skewed_features) > 0.9]
#     skewed_features = high_skewness.index

#     for feature in skewed_features:
#         if feature != 'PREMIUM':
#             df[feature] = np.log1p(df[feature])

#     return df


# remove overfit features

def remove_useless_features(df):

    overfit = []
    for i in df.columns:      
        if df[i].value_counts().iloc[0] / len(df) * 100 > 99:
            overfit.append(i)
    overfit = list(overfit)

    df.drop(columns=overfit, inplace=True)

    print('## Dropped useless features: ', overfit)

    return df


# remove unused columns

def drop_unused(df):

    df.drop(columns=constants.TO_DROP, inplace=True, errors='ignore')
    return df


def UWYEAR_tranform(df): 
    df['UWYEAR_label']=df['UWYEAR'].apply(lambda x: x.split('-')[1]).astype('str')
    df['UWYEAR']=df['UWYEAR'].apply(lambda x: x.split('-')[0]).astype('int64')

    return df

def INCEPTION_month(df):
    df.loc[:, 'INCEPTION_month'] = df['INCEPTION'].dt.month
    return df


def transform_data(df):

    df = missing_val_imputer(df) #Deal with missing values
    print(df.shape)
    df = convert_coverage(df) #COVER_BI to a boolean
    print(df.shape)
    df = label_combiner(df) #Regroup several labels together
    print(df.shape)
    df = convert_geo_market_segment(df) #Regroup several market labels together
    print(df.shape)
    df = remove_useless_features(df) # Remove the columns with 99.9% the same value 
    print(df.shape)
    df = UWYEAR_tranform(df)
    print(df.shape)
    df = INCEPTION_month(df)
    print(df.shape)
    df = drop_unused(df)
    print(df.shape)
 


    return df

