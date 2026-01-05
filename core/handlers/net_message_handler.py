import ctypes
from .game_packet_handler import GamePacketHandler
from core.enums import NetMessage
from core.utils import read_u32
from core.ffi import enet_peer_disconnect

class NetMessageHandler:
    @staticmethod
    def handle(client, packet):
        if packet.dataLength < 4:
            print("Received packet is too short to read message type.")
            return

        message_type = NetMessage(read_u32(packet.data))

        data_start = ctypes.addressof(packet.data.contents) + 4
        match message_type:
            case NetMessage.ServerHello:
                onServerHello(client)
            case NetMessage.GameMessage:
                onGameMessage(client, data_start, packet)
            case NetMessage.GamePacket:
                onGamePacket(client, data_start)

def onServerHello(client):
    data = None
    if client.redirected:
        data = (
            "UUIDToken|{}\nprotocol|{}\nfhash|{}\nmac|{}\nrequestedName|{}\n"
            "hash2|{}\nfz|{}\nf|{}\nplayer_age|{}\ngame_version|{}\nlmode|{}\n"
            "cbits|{}\nrid|{}\nGDPR|{}\nhash|{}\ncategory|{}\ntoken|{}\n"
            "total_playtime|{}\ndoor_id|{}\nklv|{}\nmeta|{}\nplatformID|{}\n"
            "deviceVersion|{}\nzf|{}\ncountry|{}\nuser|{}\nwk|{}\naat|{}\n"
        ).format(
            client.login_info.uuid,
            client.login_info.protocol,
            client.login_info.fhash,
            client.login_info.mac,
            client.login_info.requested_name,
            client.login_info.hash2,
            client.login_info.fz,
            client.login_info.f,
            client.login_info.player_age,
            client.login_info.game_version,
            client.login_info.lmode,
            client.login_info.cbits,
            client.login_info.rid,
            client.login_info.gdpr,
            client.login_info.hash,
            client.login_info.category,
            client.login_info.token,
            client.login_info.total_play_time,
            client.login_info.door_id,
            client.login_info.klv,
            client.login_info.meta,
            client.login_info.platform_id,
            client.login_info.device_version,
            client.login_info.zf,
            client.login_info.country,
            client.login_info.user,
            client.login_info.wk,
            client.login_info.aat,
        )
        client.redirected = False
    else:
        data = f"protocol|{client.login_info.protocol}\nltoken|{client.login_info.ltoken}\nplatformID|{client.login_info.platform_id}\n"

    client.send_packet(NetMessage.GenericText, data)

def onGameMessage(client, data, packet):
    try:
        text_data = ctypes.string_at(data, packet.dataLength - 4).decode("utf-8").strip()
        print(f"GameMessage received: {text_data}")

        if "action|logon_fail" in text_data:
            enet_peer_disconnect(client.peer, 0)
    except UnicodeDecodeError:
        print("Failed to decode GameMessage as UTF-8.")

def onGamePacket(client, packet):
    GamePacketHandler.handle(client, packet)