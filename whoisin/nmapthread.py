import logging
import time
from threading import Thread

import nmap

import config

logger = logging.getLogger(__name__)


class NmapThread(Thread):

    def __init__(self, container):
        self.container = container
        super().__init__()

    def get_most_complete_nmap_result(self, nm):
        ret_hosts = []
        for i in range(2):
            nm.scan(config.NMAP_NETWORK, arguments=config.NMAP_ARGS)
            hosts = [nm[h] for h in nm.all_hosts()]
            if len(hosts) > len(ret_hosts):
                ret_hosts = hosts
        return ret_hosts

    def run(self):
        from whoisin.models import Host
        nm = nmap.PortScanner()
        logger.info('Scheduling nmap scanning')
        while True:
            logger.info('Running nmap scan...')
            hosts = self.get_most_complete_nmap_result(nm)
            online_hosts = []
            for host in hosts:
                try:
                    ip = host['addresses']['ipv4']
                except KeyError:
                    ip = host['addresses']['ipv6']
                try:
                    mac = host['addresses']['mac'].upper()
                except KeyError:
                    logging.debug(f"Couldn't find mac address for {ip}, skipping it")
                    continue
                hostname = host.hostname()
                host_obj = Host(ip=ip, mac=mac, hostname=hostname)
                try:
                    host_obj = Host.objects.get(mac=mac)
                except Host.DoesNotExist:
                    logging.info(f"host with mac {mac} doesn't exists, so new one will be created")
                logging.info(f'Found {host_obj!r}')

                host_obj.save()
                online_hosts.append(host_obj)
            self.container.value = online_hosts
            logging.debug(f'Setting value to container of id {id(self.container)}')
            logging.info(f'Nmap scan done found {len(hosts)} hosts.')

            time.sleep(config.NMAP_SCAN_INTERVAL)
