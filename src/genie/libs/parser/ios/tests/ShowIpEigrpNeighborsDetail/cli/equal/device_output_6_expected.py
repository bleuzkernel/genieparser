expected_output = {
    "eigrp_instance": {
        "100": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "name": "test",
                            "named_mode": True,
                            "eigrp_interface": {
                                "GigabitEthernet2.90": {
                                    "eigrp_nbr": {
                                        "10.12.90.2": {
                                            "peer_handle": 1,
                                            "hold": 12,
                                            "uptime": "2d10h",
                                            "srtt": 1283.0,
                                            "rto": 5000,
                                            "q_cnt": 0,
                                            "last_seq_number": 5,
                                            "topology_advert_to_peer": "base",
                                            "nbr_sw_ver": {
                                                "os_majorver": 3,
                                                "os_minorver": 3,
                                                "tlv_majorrev": 2,
                                                "tlv_minorrev": 0,
                                            },
                                            "retransmit_count": 0,
                                            "retry_count": 0,
                                            "prefixes": 3,
                                            "topology_ids_from_peer": 0,
                                        }
                                    }
                                },
                                "GigabitEthernet3.90": {
                                    "eigrp_nbr": {
                                        "10.13.90.3": {
                                            "peer_handle": 0,
                                            "hold": 10,
                                            "uptime": "2d10h",
                                            "srtt": 6.0,
                                            "rto": 100,
                                            "q_cnt": 0,
                                            "last_seq_number": 9,
                                            "topology_advert_to_peer": "base",
                                            "nbr_sw_ver": {
                                                "os_majorver": 8,
                                                "os_minorver": 0,
                                                "tlv_majorrev": 1,
                                                "tlv_minorrev": 2,
                                            },
                                            "retransmit_count": 1,
                                            "retry_count": 0,
                                            "prefixes": 3,
                                            "topology_ids_from_peer": 0,
                                        }
                                    }
                                },
                            },
                        }
                    }
                }
            }
        }
    }
}
