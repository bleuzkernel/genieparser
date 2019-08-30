# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_segment_routing import (ShowSegmentRoutingMplsLB,
                                                          ShowSegmentRoutingMplsState,
                                                          ShowSegmentRoutingMplsLbLock,
                                                          ShowSegmentRoutingMplsConnectedPrefixSidMap,
                                                          ShowSegmentRoutingMplsGb,
                                                          ShowSegmentRoutingMplsGbLock,
                                                          ShowSegmentRoutingMplsConnectedPrefixSidMapLocal,
                                                          ShowSegmentRoutingTrafficEngTopology)


# =============================================================
# Unittest for:
#   * 'show segment-routing mpls connected-prefix-sid-map ipv4'
# =============================================================
class test_show_routing_mpls_connected_prefix_sid_map(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'segment_routing': {
            'bindings': {
                'local_prefix_sid': {
                    'ipv4': {
                        'ipv4_prefix_sid_local': {
                            '10.4.1.1/32': {
                                'algorithm': {
                                    'ALGO_0': {
                                        'prefix': '10.4.1.1/32',
                                        'algorithm': 'ALGO_0',
                                        'value_type': 'Indx',
                                        'sid': '1',
                                        'range': '1',
                                        'srgb': 'Y',
                                        },
                                    },
                                },
                            },
                        },
                    },
                'connected_prefix_sid_map': {
                    'ipv4': {
                        'ipv4_prefix_sid': {
                            '10.4.1.1/32': {
                                'algorithm': {
                                    'ALGO_0': {
                                        'prefix': '10.4.1.1/32',
                                        'algorithm': 'ALGO_0',
                                        'value_type': 'Indx',
                                        'sid': '1',
                                        'range': '1',
                                        'srgb': 'Y',
                                        'source': 'OSPF Area 8 10.4.1.1',
                                        },
                                    },
                                },
                            '10.16.2.2/32': {
                                'algorithm': {
                                    'ALGO_0': {
                                        'prefix': '10.16.2.2/32',
                                        'algorithm': 'ALGO_0',
                                        'value_type': 'Indx',
                                        'sid': '2',
                                        'range': '1',
                                        'srgb': 'Y',
                                        'source': 'OSPF Area 8 10.16.2.2',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output1 = {'execute.return_value': '''
        PE1#show segment-routing mpls connected-prefix-sid-map ipv4
 
                       PREFIX_SID_CONN_MAP ALGO_0
         
            Prefix/masklen   SID Type Range Flags SRGB
                10.4.1.1/32     1 Indx     1         Y
         
                       PREFIX_SID_PROTOCOL_ADV_MAP ALGO_0
         
            Prefix/masklen   SID Type Range Flags SRGB Source
                10.4.1.1/32     1 Indx     1         Y  OSPF Area 8 10.4.1.1
                10.16.2.2/32     2 Indx     1         Y  OSPF Area 8 10.16.2.2
         
                       PREFIX_SID_CONN_MAP ALGO_1
         
            Prefix/masklen   SID Type Range Flags SRGB
         
                       PREFIX_SID_PROTOCOL_ADV_MAP ALGO_1
         
            Prefix/masklen   SID Type Range Flags SRGB Source
        PE1#
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsConnectedPrefixSidMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(address_family='ipv4')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowSegmentRoutingMplsConnectedPrefixSidMap(device=self.device)
        parsed_output = obj.parse(address_family='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

# ==================================
# Unittest for:
#   * 'show segment-routing mpls gb'
# ==================================
class test_show_routing_mpls_gb(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'default': 'Yes',
        'label_max': 23999,
        'label_min': 16000,
        'state': 'ENABLED'}

    golden_output1 = {'execute.return_value': '''
        PE1#show segment-routing mpls gb
        LABEL-MIN  LABEL_MAX  STATE           DEFAULT   
        16000      23999      ENABLED         Yes       
        PE1#
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsGb(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowSegmentRoutingMplsGb(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# ==================================
# Unittest for:
#   * 'show segment-routing mpls lb'
# ==================================
class test_show_routing_mpls_lb(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'label_min': 15000,
        'label_max': 15999,
        'state': 'ENABLED',
        'default': 'Yes',
    }

    golden_output = {'execute.return_value': '''
        show segment-routing mpls lb
        LABEL-MIN  LABEL_MAX  STATE           DEFAULT
        15000      15999      ENABLED         Yes
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsLB(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsLB(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =====================================
# Unittest for:
#   * 'show segment-routing mpls state'
# =====================================
class test_show_routing_mpls_state(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'sr_mpls_state': "ENABLED",
    }

    golden_output = {'execute.return_value': '''
        Device#show segment-routing mpls state
        Segment Routing MPLS State : ENABLED
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsState(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsState(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==============================================
# Parser for 'show segment-routing mpls lb lock'
# ==============================================

class test_show_routing_mpls_lb_lock(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'label_min': 15000,
        'label_max': 15999
    }

    golden_output = {'execute.return_value': '''
        show segment-routing mpls lb lock
        SR LB (15000, 15999) Lock Users :
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsLbLock(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsLbLock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==================================================
# Unit tests for 'show segment-routing mpls gb lock'
# ==================================================
class test_show_segment_routing_mpls_gb_lock(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show segment-routing mpls gb lock
        SR GB (9000, 10000) Lock Users :
    '''}

    golden_parsed_output = {
        'label_min': 9000,
        'label_max': 10000
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsGbLock(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsGbLock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# ====================================================================
# Unittest for:
#   * 'show segment-routing mpls connected-prefix-sid-map local ipv4'
#   * 'show segment-routing mpls connected-prefix-sid-map local ipv6'
# ====================================================================
class test_show_routing_mpls_connected_prefix_sid_map_local(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'segment_routing': {
            'bindings': {
                'local_prefix_sid': {
                    'ipv4': {
                        'ipv4_prefix_sid_local': {
                            '10.4.1.1/32': {
                                'algorithm': {
                                    'ALGO_0': {
                                        'prefix': '10.4.1.1/32',
                                        'algorithm': 'ALGO_0',
                                        'value_type': 'Indx',
                                        'sid': '1',
                                        'range': '1',
                                        'srgb': 'Y',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output1 = {'execute.return_value': '''
        show segment-routing mpls connected-prefix-sid-map local ipv4

               PREFIX_SID_CONN_MAP ALGO_0

        Prefix/masklen   SID Type Range Flags SRGB
            10.4.1.1/32     1 Indx     1         Y

                PREFIX_SID_CONN_MAP ALGO_1

        Prefix/masklen   SID Type Range Flags SRGB
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsConnectedPrefixSidMapLocal(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(address_family='ipv4')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowSegmentRoutingMplsConnectedPrefixSidMapLocal(device=self.device)
        parsed_output = obj.parse(address_family='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# =============================================================
# Unittest for:
#   * 'show segment-routing traffic-eng topology ipv4'
# =============================================================
class test_show_segment_routing_traffic_eng_topology(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'nodes': {
            1: {
                'ospf_router_id': '10.19.198.239',
                'area_id': 8,
                'domain_id': 0,
                'asn': 65109,
                'prefix_sid': {
                    'prefix': '10.19.198.239',
                    'label': 16073,
                    'label_type': 'regular',
                    'domain_id': 0,
                    'flags': 'N , E',
                },
                'links': {
                    0: {
                        'local_address': '10.19.198.26',
                        'remote_address': '10.19.198.25',
                        'local_node': {
                            'ospf_router_id': '10.19.198.239',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.189.5.252',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 1000,
                            'te': 1000,
                            'delay': 1000,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 0,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '18': 'unprotected',
                            '36': 'protected',
                        },
                    },
                    1: {
                        'local_address': '10.19.198.30',
                        'remote_address': '10.19.198.29',
                        'local_node': {
                            'ospf_router_id': '10.19.198.239',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.189.5.253',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 1000,
                            'te': 1000,
                            'delay': 1000,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 0,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '37': 'unprotected',
                            '38': 'protected',
                        },
                    },
                },
            },
            2: {
                'ospf_router_id': '10.189.5.252',
                'area_id': 8,
                'domain_id': 0,
                'asn': 65109,
                'prefix_sid': {
                    'prefix': '10.189.5.252',
                    'label': 16071,
                    'label_type': 'regular',
                    'domain_id': 0,
                    'flags': 'N',
                },
                'links': {
                    0: {
                        'local_address': '10.19.198.25',
                        'remote_address': '10.19.198.26',
                        'local_node': {
                            'ospf_router_id': '10.189.5.252',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.19.198.239',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 1000,
                            'te': 1000,
                            'delay': 1000,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 125000000,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '24': 'protected',
                        },
                    },
                    1: {
                        'local_address': '10.169.14.122',
                        'remote_address': '10.169.14.121',
                        'local_node': {
                            'ospf_router_id': '10.189.5.252',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.169.14.240',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 100,
                            'te': 100,
                            'delay': 100,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 125000000,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '16': 'protected',
                        },
                    },
                    2: {
                        'local_address': '10.189.5.93',
                        'remote_address': '10.189.5.94',
                        'local_node': {
                            'ospf_router_id': '10.189.5.252',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.189.5.253',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 5,
                            'te': 5,
                            'delay': 5,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 125000000,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '19': 'protected',
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
        show segment-routing traffic-eng topology ipv4
        Node 1:
            TE router ID: 10.19.198.239
            OSPF router ID: 10.19.198.239 area ID: 8 domain ID: 0 ASN: 65109
            Prefix SID:
                Prefix 10.19.198.239, label 16073 (regular), domain ID 0, flags: N , E
            Link[0]: local address 10.19.198.26, remote address 10.19.198.25
                Local node:
                OSPF router ID: 10.19.198.239 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.189.5.252
                OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 1000, TE 1000, Delay 1000
                Bandwidth: Total 125000000, Reservable 0
                Admin-groups: 0x00000000
                Adj SID: 18 (unprotected)  36 (protected)
            Link[1]: local address 10.19.198.30, remote address 10.19.198.29
                Local node:
                OSPF router ID: 10.19.198.239 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.189.5.253
                OSPF router ID: 10.189.5.253 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 1000, TE 1000, Delay 1000
                Bandwidth: Total 125000000, Reservable 0
                Admin-groups: 0x00000000
                Adj SID: 37 (unprotected)  38 (protected)

        Node 2:
            TE router ID: 10.189.5.252
            OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
            Prefix SID:
                Prefix 10.189.5.252, label 16071 (regular), domain ID 0, flags: N
            Link[0]: local address 10.19.198.25, remote address 10.19.198.26
                Local node:
                OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.19.198.239
                OSPF router ID: 10.19.198.239 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 1000, TE 1000, Delay 1000
                Bandwidth: Total 125000000, Reservable 125000000
                Admin-groups: 0x00000000
                Adj SID: 24 (protected)
            Link[1]: local address 10.169.14.122, remote address 10.169.14.121
                Local node:
                OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.169.14.240
                OSPF router ID: 10.169.14.240 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 100, TE 100, Delay 100
                Bandwidth: Total 125000000, Reservable 125000000
                Admin-groups: 0x00000000
                Adj SID: 16 (protected)
            Link[2]: local address 10.189.5.93, remote address 10.189.5.94
                Local node:
                OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.189.5.253
                OSPF router ID: 10.189.5.253 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 5, TE 5, Delay 5
                Bandwidth: Total 125000000, Reservable 125000000
                Admin-groups: 0x00000000
                Adj SID: 19 (protected)
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSegmentRoutingTrafficEngTopology(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingTrafficEngTopology(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()