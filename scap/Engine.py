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

import logging, inspect, uuid
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class Engine(object):
    def __init__(self, content, hosts):
        self.hosts = hosts
        from scap.Model import Model
        self.content = Model.load_child(None, content.getroot())

    def collect(self, args):
        for host in self.hosts:
            host.connect()

            host.collect_facts()
            #TODO cache facts

            from scap.collector.ResultCollector import ResultCollector
            host.add_result_collector(ResultCollector.load_collector(host, self.content, args))
            host.collect_results()

            host.disconnect()

    def report(self):
        from scap.model.arf_1_1.AssetReportCollection import AssetReportCollection
        arc = AssetReportCollection()

        #TODO commented to reduce amoutn of output
        # from scap.model.arf_1_1.ReportRequest import ReportRequest
        # rr = ReportRequest()
        # rr.id = 'report-request_' + uuid.uuid4().hex
        # rr.content = self.content.to_xml()
        # arc.report_requests.append(rr)

        for host in self.hosts:
            from scap.model.arf_1_1.Asset import Asset
            asset = Asset()
            asset.id = 'asset_' + host.facts['root_uuid']
            # TODO: fallback to mobo guid, eth0 mac address, eth0 ip address, hostname
            arc.assets.append(asset)

            from scap.model.ai_1_1.ComputingDevice import ComputingDevice
            comp = ComputingDevice()
            for cpe in host.facts['hw_cpe']:
                comp.cpes.append(cpe)
            comp.fqdn = host.facts['fqdn']
            comp.hostname = host.facts['hostname']
            try:
                comp.motherboard_guid = host.facts['hardware']['configuration']['uuid']
            except KeyError:
                logger.debug("Couldn't parse motherboard-guid")
            asset.asset = comp

            from scap.model.ai_1_1.Connection import Connection
            for dev, net_con in host.facts['network_connections'].items():
                logger.debug('Producing Connection for device ' + dev)
                for address in net_con['network_addresses']:
                    conn = Connection()
                    conn.mac_address = host.facts['network_connections'][dev]['mac_address']
                    conn.ip_address = address['address']
                    conn.subnet_mask = address['subnet_mask']
                    if 'default_route' in host.facts['network_connections'][dev]:
                        conn.default_route = host.facts['network_connections'][dev]['default_route']
                    comp.connections.append(conn)

            # network services
            from scap.model.ai_1_1.Service import Service
            for svc in host.facts['network_services']:
                s = Service()
                s.host = svc['ip_address']
                s.port = svc['port']
                s.protocol = svc['protocol']

            from scap.model.arf_1_1.Report import Report
            report = Report()
            report.id = 'report_' + uuid.uuid4().hex
            arc.reports.append(report)

            from scap.model.rep_core_1_1.relationship import relationship
            rel = relationship()
            rel.subject = report.id
            rel.type = 'isAbout'
            rel.refs.append(asset.id)
            arc.relationships.append(rel)

            # TODO createdFor relationship

        arc_et = ET.ElementTree(element=arc.to_xml())
        from StringIO import StringIO
        sio = StringIO()
        arc_et.write(sio, encoding='UTF-8', xml_declaration=True)
        sio.write("\n")
        return sio.getvalue()
