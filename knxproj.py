#!/usr/bin/env python3
#
# Copyright (C) 2021 Christian Poessinger <christian@poessinger.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import zipfile
import argparse
import json
import lxml.etree as ET
import pprint

# Copied from https://stackoverflow.com/a/40694411
def find_rec(node, element):
    def _find_rec(node, element, result):
        for el in node.getchildren():
            _find_rec(el, element, result)
        if node.tag == element:
            result.append(node)
    res = list()
    _find_rec(node, element, res)
    return res

def num_to_ga(num):
    """ Convert the KNX group address string to a "well known" representation """
    num = int(num)
    return f"{(num & 0x7800) >> 11}/{(num & 0x700) >> 8}/{num & 0xff}"

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--knxproj", action="store", help="Exported KNX project file", required=True)
parser.add_argument("-d", "--debug", action="store_true", help="Enable development debug output")

args = parser.parse_args()

# Basic configuration dictionary used for the homebridge KNX plugin
#homebridge_config = {
#    "knxd_ip": f"{args.knxd_ip}",
#    "knxd_port": args.knxd_port,
#    "AllowKillHomebridge": True,
#    "Devices": []
#}

# The KNXPROJ file is a ZIP file with a different file extension
try:
    z = zipfile.ZipFile(args.knxproj)
except FileNotFoundError:
    exit('Specified KNXPROJ file does not exist!')
except zipfile.BadZipFile:
    exit('Specified KNXPROJ file is invalid!')

xml = next(n for n in z.namelist() if "0.xml" in n)
data = z.read(xml).decode("utf-8")

root = ET.fromstring(data)
namespace = re.match(r'{.*}', root.tag).group(0)
if namespace != '{http://knx.org/xml/project/20}':
    exit('Only ETS XML schema 20 is supported, e.g. ETS 5.7.x')

for area in find_rec(root, f'{namespace}Area'):
    if args.debug:
        print('== Area ==')
        pprint.pprint(dict(area.attrib))
    for line in find_rec(area, f'{namespace}Line'):
        if args.debug:
            print('  == Line ==')
            pprint.pprint(dict(line.attrib), indent=2)
        for device in find_rec(line, f'{namespace}DeviceInstance'):
            if args.debug:
                print('    == Device ==')
                pprint.pprint(dict(device.attrib), indent=4)

