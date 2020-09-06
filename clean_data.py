# setup
import pandas as pd
import numpy as np

def seperate_occupations_2017(data, name):
    # input: data - survey data
    #        name - the name of column which is the occupations
    # output: result - a new data_frame with new column: is_DS, is_ML, is_DA
    result = pd.DataFrame({'is_DS': [False for _ in range(data.shape[0])],
                           'is_ML': [False for _ in range(data.shape[0])],
                           'is_DEV':[False for _ in range(data.shape[0])]})
    for i in range(data.shape[0]):
        if not pd.isna(data[name][i]):
            list_oc = data[name][i].split(';')
            for j in range(len(list_oc)):
                oc = list_oc[j]
                while(oc[0] == ' '):
                    oc = oc[1:]
                if oc == 'Data scientist':
                    result['is_DS'][i] = True
                if oc == 'Machine learning specialist':
                    result['is_ML'][i] = True
                if oc.find('Developer') != -1 or oc.find('developer') != -1:
                    result['is_DEV'][i] = True
    result['is_DS_ML'] = (result['is_ML'] | result['is_DS'])
    return result

def seperate_otherEd_2018_2019(data, name):
    # input: data - survey data
    #        name - the name of column which is the occupations
    # output: result - a new data_frame with new column: is_DS, is_ML, is_DA
    result = pd.DataFrame({'online_course': [False for _ in range(data.shape[0])],
                           'bootcamp': [False for _ in range(data.shape[0])]})
    for i in range(data.shape[0]):
        if not pd.isna(data[name][i]):
            list_oc = data[name][i].split(';')
            for j in range(len(list_oc)):
                oc = list_oc[j]
                while(oc[0] == ' '):
                    oc = oc[1:]
                if oc.find('MOOC') != -1:
                    result['online_course'][i] = True
                if oc.find('bootcamp') != -1:
                    result['bootcamp'][i] = True
    return result

def seperate_occupations_2018_2019(data, name):
    # input: data - survey data
    #        name - the name of column which is the occupations
    # output: result - a new data_frame with new column: is_DS, is_ML, is_DA
    result = pd.DataFrame({'is_DS_ML': [False for _ in range(data.shape[0])],
                           'is_DA': [False for _ in range(data.shape[0])],
                           'is_DEV':[False for _ in range(data.shape[0])]})
    for i in range(data.shape[0]):
        if not pd.isna(data[name][i]):
            list_oc = data[name][i].split(';')
            for j in range(len(list_oc)):
                oc = list_oc[j]
                while(oc[0] == ' '):
                    oc = oc[1:]
                if oc == 'Data scientist or machine learning specialist':
                    result['is_DS_ML'][i] = True
                if oc == 'Data or business analyst':
                    result['is_DA'][i] = True
                if oc.find('Developer') != -1 or oc.find('developer') != -1:
                    result['is_DEV'][i] = True
    return result

def convert_salary(salary, salary_freq):
    # convert salary into annual salary
    salary_annual = salary.copy()
    for i in range(len(salary)):
        if salary_freq[i] == 'Weekly':
            salary_annual[i] = salary[i] * (365/7)
        if salary_freq[i] == 'Monthly':
            salary_annual[i] = salary[i] * 12
    return salary_annual


def converted_company_size_2019(data_2019_q2, data_2019):
    # convert 2019 survey question "company_size" into three category
    # "small", "middle", "big"
    data_2019_q2['company_size'] = 'unknown'
    data_2019_q2['company_size'] = 'unknown'
    for i in range(data_2019.shape[0]):
        x = data_2019['OrgSize'][i]
        if not pd.isna(x):
            if (x.find('freelancer') !=-1 or x.find('99') != -1
                or x.find('19') != -1 or x.find('9') != -1):
                data_2019_q2.loc[i, 'company_size'] = 'small'
            if (x.find('499') != -1 or x.find('999') != -1):
                data_2019_q2.loc[i, 'company_size'] = 'middle'
            if (x.find('4,999') != -1 or x.find('9,999')!= -1 or x.find('10,000') != -1):
                data_2019_q2.loc[i, 'company_size'] = 'big'  
    return

def convert_company_size_2018(data_2018, data_2018_q2):
    # convert 2018 survey question "company_size" into three category
    # "small", "middle", "big"
    data_2018_q2['company_size'] = 'unknown'
    for i in range(data_2018.shape[0]):
        x = data_2018['CompanySize'][i]
        if not pd.isna(x):
            if (x.find('10') !=-1 or x.find('99') != -1
                or x.find('19') != -1):
                data_2018_q2.loc[i, 'company_size'] = 'small'
            if (x.find('499') != -1 or x.find('999') != -1):
                data_2018_q2.loc[i, 'company_size'] = 'middle'
            if (x.find('4,999') != -1 or x.find('9,999')!= -1 or x.find('10,000') != -1):
                data_2018_q2.loc[i, 'company_size'] = 'big'
    return

def add_number(ax, props, order):
    # add number in the bar chart
    for i in range(props.shape[0]):
        i_category= order[i]
        i_p = props[props['category'] == i_category].percent.values[0]
        ax.text(i_p, i, np.round(i_p,2))

def find_DL(data): 
    # determined whether used tensorflow or pytorch
    result = pd.DataFrame({'tensorflow': [False for _ in range(data.shape[0])],
                           'pytorch': [False for _ in range(data.shape[0])]})
    for i in range(data.shape[0]):
        if not pd.isna(data[i]):
            list_oc = data[i].split(';')
            for j in range(len(list_oc)):
                oc = list_oc[j]
                while(oc[0] == ' '):
                    oc = oc[1:]
                if oc.find('TensorFlow') != -1:
                    result['tensorflow'][i] = True
                if oc.find('PyTorch') != -1:
                    result['pytorch'][i] = True
    result['use_DL'] = result['pytorch'] | result['tensorflow']
    return result