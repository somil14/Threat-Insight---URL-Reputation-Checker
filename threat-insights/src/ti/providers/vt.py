from pathlib import Path
import logging
import requests

logger = logging.getLogger(__name__)

from ti.config import Settings

requests.packages.urllib3.disable_warnings() 

class VirusTotal():
    
    def __init__(self):
        self.__api_key = Settings().vt_api_key
        self.__base = 'https://www.virustotal.com/vtapi/v2'
     
    def get_url_reputation(self, url):
        logger.info('Getting url rep for  %s from  virus total', url)
        return self.__report(self.__base + '/url/report', 'resource', url)
      
    def get_file_reputation(self, file_hash):
        logger.info('Getting file rep for  %s from  virus total', file_hash)
        return self.__report(self.__base + '/file/report', 'resource', file_hash)
    
    def get_domain_reputation(self, domain):
        logger.info('Getting domain rep for  %s from  virus total', domain)
        return self.__report(self.__base + '/domain/report', 'domain', domain)
      
    def get_ip_reputation(self, ip):
        logger.info('Getting ip rep for  %s from  virus total', ip)
        return self.__report(self.__base + '/ip-address/report', 'ip', ip)

    def __report(self, url, r_name, r_value):
        params = {
            'apikey': self.__api_key, 
            r_name: r_value
        }
        response = requests.get(url, params=params, verify=False)
        response.raise_for_status()
        return response.json()
