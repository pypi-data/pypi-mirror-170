import json
import jsons
import operator
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import random
import logging
import requests
import pandas as pd
import os
import yaml
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

ops = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt
}

root_dir = os.path.abspath(os.path.dirname(__file__))
# retrieving base url
yaml_path = os.path.join(root_dir, '../askdata/askdata_config/base_url.yaml')
with open(yaml_path, 'r') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    url_list = yaml.load(file, Loader=yaml.FullLoader)


def ask_dataframe(dataframe: pd.DataFrame, query: str):
    human2sql_request = {
        "dataframe": dataframe.to_dict(),
        "query": query
    }

    human2sql_url = url_list['BASE_URL_HUMAN2SQL_DEV']

    human2sql_response = requests.post(human2sql_url, json=human2sql_request)
    response_df = []
    if human2sql_response.ok:
        res = human2sql_response.json()
        if 'result' in res:
            all_dfs = res['result']
            for df in all_dfs:
                response_df.append(pd.DataFrame(df))
        if 'messages' in res and res['messages']:
            for mex in res['messages']:
                print(mex)
    else:
        print("Error: " + str(human2sql_response))

    return response_df


def get_conditional_phrases(conditions, phrase1, phrase2):
    bool_array = []
    for condition in conditions:
        for op in ops:
            if op in condition:
                splitted = condition.split(' ' + op + ' ')
                operator = ops[op]
                bool_array.append(operator(splitted[0], splitted[1]))
        # bool_array.append(eval(condition))
    if False in bool_array:
        return phrase2
    else:
        return phrase1


def get_random_synonymous(synonyms):
    random.seed()
    nKeys = len(synonyms.keys())
    pickedItem = random.randint(0, nKeys - 1)
    synPicked = synonyms[pickedItem]
    return synPicked


def words_to_digits(phrase):
    words = phrase.split(" ")
    num = []
    for word in words:
        if "." in word:
            word = word.replace(".", "")
        if "," in word:
            word = word.replace(",", "")
        if word.isdigit():
            num.append(int(word))
    return num


def add_random_synonymous_to_sentence(phrase, placeholder, synonyms):
    random.seed()
    nKeys = len(synonyms.keys())
    pickedItem = random.randint(0, nKeys - 1)
    synPicked = synonyms[pickedItem]
    phrase = phrase.replace(placeholder, synPicked)
    return phrase


def data2nl(df, base_sentence=None, request=None, table_description=False):
    # The parameter "df" is a dataframe, but it will be converted into a dict, and called df in each case

    if request is not None:
        table_description = True
    if base_sentence is not None:
        table_description = False

    if not df.empty:
        headers = {
            "Content-Type": "application/json"
        }
        s = requests.Session()
        s.keep_alive = False
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        s.mount('https://', HTTPAdapter(max_retries=retries))

        url = url_list['BASE_URL_DATA2NL_DEV'] + "/data2nl"

        dict_df = df.to_dict(orient='records')

        if table_description is False:
            response_df = pd.DataFrame()

            for el in dict_df:

                row = "Data: " + str(el)

                if base_sentence is not None:
                    row = "BaseString: " + base_sentence + "\n" + row

                data = {"data": row}

                r = s.post(url=url, headers=headers, json=data)
                r.raise_for_status()

                try:
                    nl = r.json()['nl']
                    el['nl'] = nl
                except Exception as e:
                    logging.error(str(e))
                    el['generated_nl'] = ""
                tmp_df = pd.DataFrame()
                tmp_df = tmp_df.append(el, ignore_index=True)
                response_df = pd.concat([response_df, tmp_df], ignore_index=True, axis=0)
            return response_df
        else:
            row = "Table: " + str(dict_df)

            if request is not None:
                row = row + "\n" + "Request:\'" + request + "\'"
            data = {"data": row}

            r = s.post(url=url, headers=headers, json=data)
            r.raise_for_status()

            try:
                nl = r.json()['nl']
            except Exception as e:
                logging.error(str(e))
                nl = ""
            return nl

    else:
        print("Input DataFrame is empty!")
        df_response = pd.DataFrame()
        return df_response


def query2sql(smartquery, driver, model_version=None):
    # Google Pod
    headers = {
        "Content-Type": "application/json"
    }

    s = requests.Session()
    s.keep_alive = False
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries))

    url = url_list['BASE_URL_QUERY2SQL_DEV'] + "/query_to_sql"

    stringed_smartquery = jsons.dumps(smartquery, strip_nulls=True)
    smartquery = json.loads(stringed_smartquery)

    json_data = {
        "smartquery": smartquery,
        "driver": driver
    }

    # Params check
    params = {}

    if model_version is not None:
        params["model_version"] = model_version

    r = s.post(url=url, headers=headers, json=json_data, params=params)
    r.raise_for_status()

    try:
        response = r.json()
        return response["sql"]
    except Exception as e:
        logging.error(str(e))
        return []


def nl2query(nl, language="en-US"):
    # Google Pod
    headers = {
        "Content-Type": "application/json"
    }

    s = requests.Session()
    s.keep_alive = False
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries))

    url = url_list['BASE_URL_NL2QUERY_DEV'] + "/query"

    if "it" in language:
        language = "it-IT"
    else:
        language = "en-US"

    data = {
        "nl_ner": nl,
        "lang": language
    }

    r = s.post(url=url, headers=headers, json=data)
    r.raise_for_status()

    try:
        response = r.json()
        smartquery, version = response['smartquery'], response['model_version']
        return smartquery, version
    except Exception as e:
        logging.error(str(e))
        print("!-!-! Failed SmartQuery object creation. !-!-!")
        return None, None


def complex_field_calculator(smartquery, driver):
    # Google Pod
    headers = {
        "Content-Type": "application/json"
    }

    s = requests.Session()
    s.keep_alive = False
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries))

    url = url_list['BASE_URL_QUERY2SQL_DEV'] + "/query_to_sql"

    stringed_smartquery = jsons.dumps(smartquery, strip_nulls=True)
    smartquery = json.loads(stringed_smartquery)

    data = {
        "smartquery": smartquery,
        "driver": driver
    }

    r = s.post(url=url, headers=headers, json=data)
    r.raise_for_status()

    try:
        dict_response = r.json()
        sql = dict_response['sql']
        return sql
    except Exception as e:
        logging.error(str(e))


def complex_filter_calculator(smartquery, driver):
    # Google Pod
    headers = {
        "Content-Type": "application/json"
    }

    s = requests.Session()
    s.keep_alive = False
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries))

    url = url_list['BASE_URL_QUERY2SQL_DEV'] + "/query_to_sql"

    stringed_smartquery = jsons.dumps(smartquery, strip_nulls=True)
    smartquery = json.loads(stringed_smartquery)

    data = {
        "smartquery": smartquery,
        "driver": driver
    }

    r = s.post(url=url, headers=headers, json=data)
    r.raise_for_status()

    try:
        dict_response = r.json()
        sql = dict_response['sql']
        return sql
    except Exception as e:
        logging.error(str(e))


def smartner(nl, datasets, token, use_cache=None, cache_mode=None, similarity_threshold=None, model_version=None,
             env="dev", language="en", response_type="deanonymize"):

    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer " + token
    }

    s = requests.Session()
    s.keep_alive = False
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries))

    if env == "dev":
        url = url_list['BASE_URL_SMARTNER_DEV'] + "/query"
    else:
        url = url_list['BASE_URL_SMARTNER_PROD'] + "/query"

    json_data = {
        "nl": nl,
        "lang": language,
        "datasets": datasets
    }

    # Params check
    params = {}

    if use_cache in [True, False]:
        params["use_cache"] = use_cache
        if cache_mode in ["standard", "similarity", "only_cache"]:
            params["cache_mode"] = cache_mode

    if type(similarity_threshold) == int or type(similarity_threshold) == float:
        params["similarity_threshold"] = similarity_threshold

    if model_version is not None:
        params["model_version"] = model_version

    if response_type in ["anonymize", "nl2query", "deanonymize", "query2sql"]:
        params["response_type"] = response_type

    r = s.post(url=url, headers=headers, json=json_data, params=params)
    r.raise_for_status()

    try:
        response = r.json()
        return response["results"]
    except Exception as e:
        logging.error(str(e))
        return []


def smartner_automated_analysis(suggestions, token, env="dev", response_type="deanonymize"):

    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer " + token
    }

    s = requests.Session()
    s.keep_alive = False
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries))

    if env == "dev":
        url = url_list['BASE_URL_SMARTNER_DEV'] + "/automated_analysis"
    else:
        url = url_list['BASE_URL_SMARTNER_PROD'] + "/automated_analysis"

    json_data = {
        "suggestions": suggestions
    }

    # Params check
    params = {}

    if response_type in ["anonymize", "nl2query", "deanonymize", "query2sql"]:
        params["response_type"] = response_type

    r = s.post(url=url, headers=headers, json=json_data, params=params)
    r.raise_for_status()

    try:
        response = r.json()
        return response["results"]
    except Exception as e:
        logging.error(str(e))
        return []
