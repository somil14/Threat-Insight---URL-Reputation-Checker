import logging
import logging.config
import click
import json 
import os

from ti.config import Settings
from ti.providers.vt import VirusTotal

logging.config.fileConfig(Settings().logging_conf, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--url', '-u', "url_", help="URL for reputation")
@click.option('--file', '-f', "file_", help="File Hash for reputation")
@click.option('--domain', '-d', "domain_", help="Domain for reputation")
@click.option('--ip', '-i', "ip_", help="IP address for reputation")

def rep(url_, file_, domain_, ip_):
    """Provides reputation about a URL, file, domain or ipaddres"""
    if url_ is None and file_ is None and domain_ is None and ip_ is None:
        logger.error('Either URL,FILE, DOMAIN or IP should be present')
        os._exit(1)
        
    vt = VirusTotal()

    if url_ is not None:
        logger.info("Getting reputation for URL %s", url_)
        result = vt.get_url_reputation(url_)
    elif file_ is not None:
        logger.info("Getting reputation for file %s", file_)
        result = vt.get_file_reputation(file_)
    elif domain_ is not None:
        logger.info("Getting reputation for domain %s", domain_)
        result = vt.get_domain_reputation(domain_)
    elif ip_ is not None:
        logger.info("Getting reputation for IP addres %s", ip_)
        result = vt.get_ip_reputation(ip_)
    else:
        logger.info("Invalid input for reputation")

    logger.info("Reputation %s is as below \n")
    logger.info(json.dumps(result, indent=2))
 