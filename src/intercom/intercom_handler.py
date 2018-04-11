import socket

import config


class IntercomHandler:
    """Handle intercom door opening"""

    def open():
        """Send any UDP packet to intercom driver to open the door"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b'data-is-irrelevant', (config.INTERCOM_DRIVER_IP, config.INTERCOM_DRIVER_PORT))
