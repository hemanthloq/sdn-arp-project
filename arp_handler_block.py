from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet, ipv4
from ryu.lib.packet import ether_types

class ARPBlockHandler(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(ARPBlockHandler, self).__init__(*args, **kwargs)
        self.mac_to_port = {}

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        parser = datapath.ofproto_parser
        ofproto = datapath.ofproto

        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionActions(
            datapath.ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = parser.OFPFlowMod(datapath=datapath,
                               priority=priority,
                               match=match,
                               instructions=inst)
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        parser = datapath.ofproto_parser
        ofproto = datapath.ofproto

        pkt = packet.Packet(msg.data)
        ip_pkt = pkt.get_protocol(ipv4.ipv4)

        if ip_pkt and ip_pkt.src == "10.0.0.1" and ip_pkt.dst == "10.0.0.2":
            match = parser.OFPMatch(eth_type=0x0800,
                                    ipv4_src="10.0.0.1",
                                    ipv4_dst="10.0.0.2")
            self.add_flow(datapath, 100, match, [])
            return

        actions = [parser.OFPActionOutput(ofproto.OFPP_FLOOD)]

        out = parser.OFPPacketOut(datapath=datapath,
                                 buffer_id=msg.buffer_id,
                                 in_port=msg.match['in_port'],
                                 actions=actions,
                                 data=msg.data)
        datapath.send_msg(out)
