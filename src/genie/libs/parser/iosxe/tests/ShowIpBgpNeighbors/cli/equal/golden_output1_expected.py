expected_output = {
    "list_of_neighbors": ["192.168.197.254"],
    "vrf": {
        "default": {
            "neighbor": {
                "192.168.197.254": {
                    "address_family": {
                        "ipv4 unicast": {
                            "advertise_bit": 0,
                            "bgp_table_version": 1,
                            "dynamic_slow_peer_recovered": "never",
                            "index": 0,
                            "last_detected_dynamic_slow_peer": "never",
                            "last_received_refresh_end_of_rib": "never",
                            "last_received_refresh_start_of_rib": "never",
                            "last_sent_refresh_end_of_rib": "1w5d",
                            "last_sent_refresh_start_of_rib": "1w5d",
                            "local_policy_denied_prefixes_counters": {
                                "inbound": {"total": 0},
                                "outbound": {"total": 0},
                            },
                            "max_nlri": 0,
                            "min_nlri": 0,
                            "neighbor_version": "1/0",
                            "output_queue_size": 0,
                            "prefix_activity_counters": {
                                "received": {
                                    "explicit_withdraw": 0,
                                    "implicit_withdraw": 0,
                                    "prefixes_current": 0,
                                    "prefixes_total": 0,
                                    "used_as_bestpath": 0,
                                    "used_as_multipath": 0,
                                },
                                "sent": {
                                    "explicit_withdraw": 0,
                                    "implicit_withdraw": 0,
                                    "prefixes_current": 0,
                                    "prefixes_total": 0,
                                    "used_as_bestpath": "n/a",
                                    "used_as_multipath": "n/a",
                                },
                            },
                            "refresh_activity_counters": {
                                "received": {
                                    "refresh_end_of_rib": 0,
                                    "refresh_start_of_rib": 0,
                                },
                                "sent": {
                                    "refresh_end_of_rib": 1,
                                    "refresh_start_of_rib": 1,
                                },
                            },
                            "refresh_epoch": 1,
                            "refresh_out": 0,
                            "slow_peer_detection": False,
                            "slow_peer_split_update_group_dynamic": False,
                        },
                        "l2vpn vpls": {
                            "advertise_bit": 1,
                            "bgp_table_version": 9431,
                            "community_attribute_sent": True,
                            "dynamic_slow_peer_recovered": "never",
                            "extended_community_attribute_sent": True,
                            "index": 38,
                            "last_detected_dynamic_slow_peer": "never",
                            "last_received_refresh_end_of_rib": "02:01:32",
                            "last_received_refresh_start_of_rib": "02:01:36",
                            "last_sent_refresh_end_of_rib": "02:41:38",
                            "last_sent_refresh_start_of_rib": "02:41:38",
                            "local_policy_denied_prefixes_counters": {
                                "inbound": {
                                    "bestpath_from_this_peer": "n/a",
                                    "total": 0,
                                },
                                "outbound": {
                                    "bestpath_from_this_peer": 402,
                                    "total": 402,
                                },
                            },
                            "max_nlri": 199,
                            "min_nlri": 0,
                            "neighbor_version": "9431/0",
                            "output_queue_size": 0,
                            "prefix_activity_counters": {
                                "received": {
                                    "explicit_withdraw": 0,
                                    "implicit_withdraw": 402,
                                    "prefixes_total": 603,
                                    "used_as_bestpath": 201,
                                    "used_as_multipath": 0,
                                },
                                "sent": {
                                    "explicit_withdraw": 307,
                                    "implicit_withdraw": 5646,
                                    "prefixes_total": 6356,
                                    "used_as_bestpath": "n/a",
                                    "used_as_multipath": "n/a",
                                },
                            },
                            "refresh_activity_counters": {
                                "received": {
                                    "refresh_end_of_rib": 2,
                                    "refresh_start_of_rib": 2,
                                },
                                "sent": {
                                    "refresh_end_of_rib": 1,
                                    "refresh_start_of_rib": 1,
                                },
                            },
                            "refresh_epoch": 3,
                            "refresh_in": 4,
                            "refresh_out": 0,
                            "route_reflector_client": True,
                            "slow_peer_detection": False,
                            "slow_peer_split_update_group_dynamic": False,
                            "suppress_ldp_signaling": True,
                            "update_group_member": 38,
                        },
                        "vpnv4 unicast": {
                            "advertise_bit": 2,
                            "bgp_table_version": 29454374,
                            "dynamic_slow_peer_recovered": "never",
                            "extended_community_attribute_sent": True,
                            "index": 44,
                            "last_detected_dynamic_slow_peer": "never",
                            "last_received_refresh_end_of_rib": "02:01:32",
                            "last_received_refresh_start_of_rib": "02:01:36",
                            "last_sent_refresh_end_of_rib": "02:41:11",
                            "last_sent_refresh_start_of_rib": "02:41:38",
                            "local_policy_denied_prefixes_counters": {
                                "inbound": {
                                    "bestpath_from_this_peer": "n/a",
                                    "total": 0,
                                },
                                "outbound": {
                                    "bestpath_from_this_peer": 3100,
                                    "total": 3100,
                                },
                            },
                            "max_nlri": 270,
                            "min_nlri": 0,
                            "neighbor_version": "29454374/0",
                            "output_queue_size": 0,
                            "prefix_activity_counters": {
                                "received": {
                                    "explicit_withdraw": 206,
                                    "implicit_withdraw": 40708,
                                    "prefixes_total": 61115,
                                    "used_as_bestpath": 20201,
                                    "used_as_multipath": 0,
                                },
                                "sent": {
                                    "explicit_withdraw": 1131817,
                                    "implicit_withdraw": 64677991,
                                    "prefixes_total": 68207251,
                                    "used_as_bestpath": "n/a",
                                    "used_as_multipath": "n/a",
                                },
                            },
                            "refresh_activity_counters": {
                                "received": {
                                    "refresh_end_of_rib": 1,
                                    "refresh_start_of_rib": 1,
                                },
                                "sent": {
                                    "refresh_end_of_rib": 1,
                                    "refresh_start_of_rib": 1,
                                },
                            },
                            "refresh_epoch": 2,
                            "refresh_in": 4,
                            "refresh_out": 27,
                            "route_reflector_client": True,
                            "slow_peer_detection": False,
                            "slow_peer_split_update_group_dynamic": False,
                            "update_group_member": 44,
                        },
                    },
                    "bgp_neighbor_session": {"sessions": 1},
                    "bgp_negotiated_capabilities": {
                        "enhanced_refresh": "advertised and received",
                        "four_octets_asn": "advertised and received",
                        "graceful_restart": "advertised and received",
                        "graceful_restart_af_advertised_by_peer": [
                            "vpnv4 unicast",
                            "l2vpn vpls",
                        ],
                        "ipv4_unicast": "advertised",
                        "l2vpn_vpls": "advertised and received",
                        "multisession": "advertised",
                        "remote_restart_timer": 120,
                        "route_refresh": "advertised and received(new)",
                        "stateful_switchover": "NO for session 1",
                        "vpnv4_unicast": "advertised and received",
                    },
                    "bgp_negotiated_keepalive_timers": {
                        "hold_time": 90,
                        "keepalive_interval": 30,
                        "min_holdtime": 0,
                    },
                    "bgp_neighbor_counters": {
                        "messages": {
                            "in_queue_depth": 0,
                            "out_queue_depth": 0,
                            "received": {
                                "keepalives": 346,
                                "notifications": 0,
                                "opens": 1,
                                "route_refresh": 0,
                                "total": 13183,
                                "updates": 12830,
                            },
                            "sent": {
                                "keepalives": 347,
                                "notifications": 0,
                                "opens": 1,
                                "route_refresh": 4,
                                "total": 12180,
                                "updates": 11824,
                            },
                        }
                    },
                    "bgp_session_transport": {
                        "address_tracking_status": "enabled",
                        "connection": {
                            "dropped": 38,
                            "established": 39,
                            "last_reset": "02:42:06",
                            "reset_reason": "Peer closed the session",
                        },
                        "gr_restart_time": 120,
                        "gr_stalepath_time": 360,
                        "graceful_restart": "enabled",
                        "min_time_between_advertisement_runs": 0,
                        "rib_route_ip": "192.168.197.254",
                        "sso": False,
                        "tcp_connection": False,
                        "tcp_path_mtu_discovery": "enabled",
                    },
                    "bgp_version": 4,
                    "link": "internal",
                    "remote_as": 5918,
                    "router_id": "192.168.197.254",
                    "session_state": "Idle",
                    "shutdown": False,
                }
            }
        }
    },
}
