from pathlib import Path
from typing import Optional
import jwt
import requests
import typer
from rich import print
from rich.syntax import Syntax

import os 
import json
import typing
from urllib.parse import urljoin

from . import get_token, get_project_id, get_org_id, BASE_URL, PATH_PURE_DIR


app = typer.Typer()


@app.command()
def add(params, model_name: str, model_version:str) -> str:
    '''`add()` takes a dictionary of parameters and a model name as input and returns a string
    
    Parameters
    ----------
    params : dict
        a dictionary of parameters
    model_name : str
        The name of the model you want to add parameters to.
    model_version: str
        The version of the model
    
    Returns
    -------
        The response.text is being returned.
    
    '''

    user_token = get_token()
    org_id = get_org_id()
    project_id = get_project_id()
    
    url_path_1 = '{}/project/{}/model/{}/params/add'.format(org_id, project_id, model_name)
    url = urljoin(BASE_URL, url_path_1)


    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer {}'.format(user_token)
    }

    params = json.dumps(params)
    data = {'model_name': model_name, 'params': params}

    response = requests.post(url, data=data, headers=headers)


    if response.status_code == 200:
        print(f"[bold green]Params have been registered!")

    else:
        print(f"[bold red]Params have not been registered!")

    
    return response.text
        


@app.command()
def fetch(model_name: str, model_version:str, param:str='') -> str:
    '''
    
    This function fetches the parameters of a model
    
    Parameters
    ----------
    model_name : str
        The name of the model you want to fetch the parameters for.
    model_version: str
        The version of the model
    param : str
        The name of the parameter to fetch. If not specified, all parameters are returned.
    
    Returns
    -------
        The params that are fetched
    
    '''
    user_token = get_token()
    org_id = get_org_id()
    project_id = get_project_id()
    

    url_path_1 = '{}/project/{}/model/{}/params/{}'.format(org_id, project_id, model_name, param)
    url = urljoin(BASE_URL, url_path_1)


    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer {}'.format(user_token)
    }


    response = requests.get(url, headers=headers)

#     params = None
    if response.status_code == 200:
        res_text = json.loads(response.text)

        if param == '':

            params = res_text

            print(f"[bold green]Params have been fetched")
            print(params)

            return params


        else:
            if 'param' in res_text.keys() and 'value' in res_text.keys():
                params = res_text['value']
                # params = json.loads(params)

                print(f"[bold green]Params have been fetched")
                print(res_text['param'], ':', res_text['value'])

                return params

            else:
                print('[bold red]Param {} are not available for the model!'.format(param))
                print(response.text)
                return
        
            

    else:
        print(f"[bold red]Unable to fetch Params!")
        print(response.text)
        return


@app.command()
def delete(param:str, model_name:str, model_version:str) -> str:
    '''This function deletes a parameter from a model
    
    Parameters
    ----------
    model_name : str
        The name of the model you want to delete the parameter from.
    param : str
        The name of the parameter to delete.
    model_version: str
        The version of the model
    
    '''
    user_token = get_token()
    org_id = get_org_id()
    project_id = get_project_id()
    

    url_path_1 = '{}/project/{}/model/{}/params/{}/delete'.format(org_id,project_id, model_name, param)
    url = urljoin(BASE_URL, url_path_1)


    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer {}'.format(user_token)
    }


    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print(f"[bold green]Param has been deleted")
        
    else:
        print(f"[bold red]Unable to delete Param")

    return response.text




if __name__ == "__main__":
    app()