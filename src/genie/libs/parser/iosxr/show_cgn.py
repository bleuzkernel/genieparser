'''
show_cgn.py

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional


# ====================================================
#  schema for show cgn nat44 statistics
# ====================================================
class ShowCgnNat44StatsSchema(MetaParser):
    """Schema for :
       show cgn nat44 <name> statistics | utility head -n 21"""

    schema = {
        'cgn_instance': {
            'type': str, 
            'instance': str,
            'actv_transl': int,
            'sessions': int,
            'transl_create_rate': int,
            'transl_delete_rate': int,
            'in_out_forward_rate': int,
            'out_in_forward_rate': int,
            'in_out_drops_pt_lim_ex': int,
            'in_out_drops_sys_lim_': int,
            'in_out_drops_rsrc_deplet': int,
            'no_transl_entry_drops': int,
            'pptp_actv_tunl': int,
            'pptp_actv_ch': int,
            'pptp_ctrl_msg_drops': int,
            'subscribers': int,
            'drops_sess_db_lim_ex': int,
            'drops_src_ip_not_config': int,
            'pool_addr_total_free': int,
            'pool_addr_used': int,
        }
    }


# ====================================================
#  parser for show cgn nat44 statistics
# ====================================================
# ====================================================
#  parser for show route summary
# ====================================================
class ShowCgnNat44Stats(ShowCgnNat44StatsSchema):
    """Parser for :
       show cgn nat44 <name> statistics | utility head -n 21"""

    cli_command = ['show cgn nat44 {name} statistics | utility head -n 21']

    '''
    Statistics summary of NAT44 instance: 'nat44-1'
    Number of active translations: 1824731
    Number of sessions: 66952
    Translations create rate: 11041
    Translations delete rate: 12748
    Inside to outside forward rate: 908520
    Outside to inside forward rate: 3461710
    Inside to outside drops port limit exceeded: 6950309293
    Inside to outside drops system limit reached: 0
    Inside to outside drops resource depletion: 0
    No translation entry drops: 39718165879
    PPTP active tunnels: 11
    PPTP active channels: 11
    PPTP ctrl message drops: 41099
    Number of subscribers: 34941
    Drops due to session db limit exceeded: 0
    Drops due to source ip not configured: 0

    Pool address totally free: 1033
    Pool address used: 9207
    '''

    def cli(self, name=None, output=None):
        if output is None:
            cmd = self.cli_command[0].format(name=name)
            out = self.device.execute(cmd)
        else:
            out = output

        # Statistics summary of NAT44 instance: 'nat44-1'
        p1 = re.compile(r"^Statistics summary of (?P<type>\w+) instance: '(?P<instance>.*)'")
        
        p_test = [
            # Number of active translations: 1824731
            '^Number of active translations: (?P<var_name>.*)',
            # Number of sessions: 66952
            '^Number of sessions: (?P<var_name>.*)',
            # Translations create rate: 11041
            '^Translations create rate: (?P<var_name>.*)',
            # Translations delete rate: 12748
            '^Translations delete rate: (?P<var_name>.*)',
            # Inside to outside forward rate: 908520
            '^Inside to outside forward rate: (?P<var_name>.*)',
            # Outside to inside forward rate: 3461710
            '^Outside to inside forward rate: (?P<var_name>.*)',
            # Inside to outside drops port limit exceeded: 6950309293
            '^Inside to outside drops port limit exceeded: (?P<var_name>.*)',
            # Inside to outside drops system limit reached: 0
            '^Inside to outside drops system limit reached: (?P<var_name>.*)',
            # Inside to outside drops resource depletion: 0
            '^Inside to outside drops resource depletion: (?P<var_name>.*)',
            # No translation entry drops: 39718165879
            '^No translation entry drops: (?P<var_name>.*)',
            # PPTP active tunnels: 11
            '^PPTP active tunnels: (?P<var_name>.*)',
            # PPTP active channels: 11
            '^PPTP active channels: (?P<var_name>.*)',
            # PPTP ctrl message drops: 41099
            '^PPTP ctrl message drops: (?P<var_name>.*)',
            # Number of subscribers: 34941
            '^Number of subscribers: (?P<var_name>.*)',
            # Drops due to session db limit exceeded: 0
            '^Drops due to session db limit exceeded: (?P<var_name>.*)',
            # Drops due to source ip not configured: 0
            '^Drops due to source ip not configured: (?P<var_name>.*)',
            # Pool address totally free: 1033
            '^Pool address totally free: (?P<var_name>.*)',
            # Pool address used: 9207
            '^Pool address used: (?P<var_name>.*)'
        ]

        dict_keys = [
            'actv_transl',
            'sessions',
            'transl_create_rate',
            'transl_delete_rate',
            'in_out_forward_rate',
            'out_in_forward_rate',
            'in_out_drops_pt_lim_ex',
            'in_out_drops_sys_lim_',
            'in_out_drops_rsrc_deplet',
            'no_transl_entry_drops',
            'pptp_actv_tunl',
            'pptp_actv_ch',
            'pptp_ctrl_msg_drops',
            'subscribers',
            'drops_sess_db_lim_ex',
            'drops_src_ip_not_config',
            'pool_addr_total_free',
            'pool_addr_used',
        ]

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                cgn_dict = ret_dict.setdefault('cgn_instance',{})
                cgn_dict.update({'type': m.groupdict()['type']})
                cgn_dict.update({'instance': m.groupdict()['instance']})

            for test in p_test:
                p = re.compile(f'{test}')
                m = p.match(line)
                if m:
                    cgn_dict.update({dict_keys[p_test.index(test)]: int(m.groupdict()['var_name'])})

        return ret_dict