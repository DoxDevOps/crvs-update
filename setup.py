import requests
import json
import platform
import subprocess
import os
from fabric import Connection
from dotenv import load_dotenv
load_dotenv()
#API_KEY = os.getenv('PROJECT_API_KEY')

""" 
* get data from Xi
* @params url
* return dict
"""
def get_xi_data(url):
    response = requests.get(url)
    data = json.loads(response.text)
    data = data[0]['fields']
    return data

cluster = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_cluster/1')

for site_id in cluster['site']:
    site = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_site/' + str(site_id))

    # functionality for ping re-tries
    count = 0

    while (count < 3):

        # lets check if the site is available
        param = '-n' if platform.system().lower()=='windows' else '-c'

        if subprocess.call(['ping', param, '1', site['ip_address']]) == 0:
            
            # run setup script
            run_api_script = "ssh " + site['username'] + "@" + site['ip_address'] + " 'cd /var/www/crvs && git pull'"
            os.system(run_api_script)
            
            result = Connection("" + site['username'] + "@" + site['ip_address'] + "").run('cd /var/www/BHT-EMR-API && git log', hide=True)
            
            msg = "{0.stdout}"
            
            version = msg.format(result).strip()
