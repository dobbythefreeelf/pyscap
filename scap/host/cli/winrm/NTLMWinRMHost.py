# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

from scap.host.cli.WinRMHost import WinRMHost
from scap.Inventory import Inventory
from winrm.protocol import Protocol
import logging

logger = logging.getLogger(__name__)
class NTLMWinRMHost(WinRMHost):
    def connect(self):
        inventory = Inventory()

        if inventory.has_option(self.hostname, 'address'):
            address = inventory.get(self.hostname, 'address')
        else:
            address = self.hostname
        logger.debug('Using address ' + address)

        if inventory.has_option(self.hostname, 'scheme'):
            scheme = inventory.get(self.hostname, 'scheme')
        else:
            scheme = 'http'
        logger.debug('Using url scheme ' + scheme)

        if inventory.has_option(self.hostname, 'port'):
            port = inventory.get(self.hostname, 'port')
        else:
            if scheme == 'http':
                port = '5985'
            elif scheme == 'https':
                port = '5986'
            else:
                raise('Invalid WinRM scheme: ' + scheme)
        logger.debug('Using port ' + port)

        if not inventory.has_option(self.hostname, 'username'):
            raise RuntimeError('Host ' + self.hostname + ' has not specified option: username')
        username = inventory.get(self.hostname, 'username')
        if inventory.has_option(self.hostname, 'domain'):
            username = inventory.get(self.hostname, 'domain') + '\\' + username
        logger.debug('Using username ' + username)

        if not inventory.has_option(self.hostname, 'password'):
            raise RuntimeError('Host ' + self.hostname + ' has not specified option: password')
        password = inventory.get(self.hostname, 'password')

        self.protocol = Protocol(
            endpoint=scheme + '://' + address + ':' + port + '/wsman',
            transport='ntlm',
            username=username,
            password=password)

        try:
            self.shell_id = self.protocol.open_shell()
        except Exception as e:
            logger.warning(str(e))