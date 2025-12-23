import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp
from flask import Flask, request, jsonify
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
from cfonts import render, say


#EMOTES BY YASH X CODEX



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# VariabLes dyli 
#------------------------------------------#
online_writers = {}  # Dictionary to store online writers for multiple accounts
whisper_writers = {}  # Dictionary to store whisper writers for multiple accounts
account_configs = {}  # Dictionary to store account-specific configurations
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
#------------------------------------------#

app = Flask(__name__)

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB51"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.118.1"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
     
async def cHTypE(H):
    if not H: return 'Squid'
    elif H == 1: return 'CLan'
    elif H == 2: return 'PrivaTe'
    
async def SEndMsG(H , message , Uid , chat_id , key , iv):
    TypE = await cHTypE(H)
    if TypE == 'Squid': msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
    elif TypE == 'CLan': msg_packet = await xSEndMsg(message , 1 , chat_id , chat_id , key , iv)
    elif TypE == 'PrivaTe': msg_packet = await xSEndMsg(message , 2 , Uid , Uid , key , iv)
    return msg_packet

async def SEndPacKeT(OnLinE_writer, ChaT_writer, TypE, PacKeT):
    if TypE == 'ChaT' and ChaT_writer and PacKeT: 
        ChaT_writer.write(PacKeT) 
        await ChaT_writer.drain()
    elif TypE == 'OnLine' and OnLinE_writer and PacKeT: 
        OnLinE_writer.write(PacKeT) 
        await OnLinE_writer.drain()
    else: return 'UnsoPorTed TypE ! >> ErrrroR (:():)' 
           
async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5, account_uid=None):
    global spam_room , spammer_uid , spam_chat_id , spam_uid , XX , uid , Spy,data2, Chat_Leave
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            # Store writer in the dictionary with account_uid as key
            online_writers[account_uid] = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            writer.write(bytes_payload)
            await writer.drain()
            while True:
                data2 = await reader.read(9999)
                if not data2: break
                
                if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                    try:
                        print(data2.hex()[10:])
                        packet = await DeCode_PackEt(data2.hex()[10:])
                        print(packet)
                        packet = json.loads(packet)
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT' , JoinCHaT)

                        message = f'[B][C]{get_random_color()}\n- WeLComE To Emote Bot ! '
                        P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                        await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT' , P)

                    except:
                        if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                            try:
                                print(data2.hex()[10:])
                                packet = await DeCode_PackEt(data2.hex()[10:])
                                print(packet)
                                packet = json.loads(packet)
                                OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                                JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT' , JoinCHaT)


                                message = f'[B][C]{get_random_color()}\n- WeLComE To Emote Bot ! \n\n{get_random_color()}- Commands : @a {xMsGFixinG("123456789")} {xMsGFixinG("909000001")}\n\n[00FF00]Dev : @{xMsGFixinG("linux")}'
                                P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT' , P)
                            except:
                                pass

            # Remove writer from dictionary when connection closes
            if account_uid in online_writers:
                online_writers[account_uid].close()
                await online_writers[account_uid].wait_closed()
                del online_writers[account_uid]

        except Exception as e: print(f"- ErroR With {ip}:{port} - {e}")
        await asyncio.sleep(reconnect_delay)
                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5, account_uid=None):
    print(region, 'TCP CHAT')

    global spam_room , spammer_uid , spam_chat_id , spam_uid , chat_id , XX , uid , Spy,data2, Chat_Leave
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writers[account_uid] = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writers[account_uid].write(bytes_payload)
            await whisper_writers[account_uid].drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writers[account_uid]: whisper_writers[account_uid].write(pK) ; await whisper_writers[account_uid].drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                    except:
                        response = None


                    if response:
                        if inPuTMsG.startswith(("/5")):
                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                message = f"[B][C]{get_random_color()}\n\nAccepT My InV FasT\n\n"
                                P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT' , P)
                                PAc = await OpEnSq(key , iv,region)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine' , PAc)
                                C = await cHSq(5, uid ,key, iv,region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine' , C)
                                V = await SEnd_InV(5 , uid , key , iv,region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine' , V)
                                E = await ExiT(None , key , iv)
                                await asyncio.sleep(3)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine' , E)
                            except:
                                print('msg in squad')


                        if inPuTMsG.startswith('/x/'):
                            CodE = inPuTMsG.split('/x/')[1]
                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                EM = await GenJoinSquadsPacket(CodE , key , iv)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine' , EM)


                            except:
                                print('msg in squad')

                        if inPuTMsG.startswith('leave'):
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine' , leave)

                        if inPuTMsG.strip().startswith('/s'):
                            EM = await FS(key , iv)
                            await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine' , EM)


                        if inPuTMsG.strip().startswith('/f'):

                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                message = f"[B][C]{get_random_color()}\n\nOnLy In SQuaD ! \n\n"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT', P)

                            except:
                                print('msg in squad')

                                parts = inPuTMsG.strip().split()
                                print(response.Data.chat_type, uid, chat_id)
                                message = f'[B][C]{get_random_color()}\nACITVE TarGeT -> {xMsGFixinG(uid)}\n'

                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)

                                uid2 = uid3 = uid4 = uid5 = uid6 = None
                                s = False

                                try:
                                    uid = int(parts[1])
                                    uid2 = int(parts[2])
                                    uid3 = int(parts[3])
                                    uid4 = int(parts[4])
                                    uid5 = int(parts[5])
                                    uid6 = int(parts[6])
                                    idT = int(parts[6])

                                except ValueError as ve:
                                    print("ValueError:", ve)
                                    s = True

                                except Exception:
                                    idT = len(parts) - 1
                                    idT = int(parts[idT])
                                    print(idT)
                                    print(uid)

                                if not s:
                                    try:
                                        await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT', P)

                                        # 🚀 Super Fast Emote Loop
                                        for i in range(200):  # repeat count
                                            print(f"Fast Emote {i+1}")
                                            H = await Emote_k(uid, idT, key, iv, region)
                                            await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)

                                            if uid2:
                                                H = await Emote_k(uid2, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)
                                            if uid3:
                                                H = await Emote_k(uid3, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)
                                            if uid4:
                                                H = await Emote_k(uid4, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)
                                            if uid5:
                                                H = await Emote_k(uid5, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)
                                            if uid6:
                                                H = await Emote_k(uid6, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)

                                            await asyncio.sleep(0.08)  # ⚡ super-fast delay

                                    except Exception as e:
                                        print("Fast emote error:", e)

                        if inPuTMsG.strip().startswith('/d'):

                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                message = f"[B][C]{get_random_color()}\n\nOnLy In SQuaD ! \n\n"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT', P)

                            except:
                                print('msg in squad')

                                parts = inPuTMsG.strip().split()
                                print(response.Data.chat_type, uid, chat_id)
                                message = f'[B][C]{get_random_color()}\nACITVE TarGeT -> {xMsGFixinG(uid)}\n'

                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)

                                uid2 = uid3 = uid4 = uid5 = uid6 = None
                                s = False

                                try:
                                    uid = int(parts[1])
                                    uid2 = int(parts[2])
                                    uid3 = int(parts[3])
                                    uid4 = int(parts[4])
                                    uid5 = int(parts[5])
                                    uid6 = int(parts[6])
                                    idT = int(parts[6])

                                except ValueError as ve:
                                    print("ValueError:", ve)
                                    s = True

                                except Exception:
                                    idT = len(parts) - 1
                                    idT = int(parts[idT])
                                    print(idT)
                                    print(uid)

                                if not s:
                                    try:
                                        await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT', P)

                                        H = await Emote_k(uid, idT, key, iv,region)
                                        await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)

                                        if uid2:
                                            H = await Emote_k(uid2, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)
                                        if uid3:
                                            H = await Emote_k(uid3, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)
                                        if uid4:
                                            H = await Emote_k(uid4, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)
                                        if uid5:
                                            H = await Emote_k(uid5, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)
                                            if uid6:
                                                H = await Emote_k(uid6, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', H)
                                        
                                        # Exit after emote execution
                                        LV = await ExiT(account_configs.get(account_uid, {}).get('bot_uid'), key, iv)
                                        await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'OnLine', LV)
                                        await asyncio.sleep(0.03)

                                    except Exception as e:
                                        pass


                        if inPuTMsG in ("linux"):
                            uid = response.Data.uid
                            chat_id = response.Data.Chat_ID
                            message = '/d <uid1> <uid2>... <emoteid> /f <uid1> <uid2>... <emoteid> for fast emote'
                            P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writers.get(account_uid), online_writers.get(account_uid), 'ChaT' , P)
                        response = None
                            
            if account_uid in whisper_writers:
                whisper_writers[account_uid].close() ; await whisper_writers[account_uid].wait_closed() ; del whisper_writers[account_uid]
                    
                    	
                    	
        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writers[account_uid] = None
        await asyncio.sleep(reconnect_delay)
# ---------------------- FLASK ROUTES ----------------------

loop = None

async def perform_emote(team_code: str, uids: list, emote_id: int, account_uid: int = None):
    # If no specific account is provided, use the first available account
    if account_uid is None:
        if online_writers:
            account_uid = next(iter(online_writers))
        else:
            raise Exception("No bot accounts connected")
    
    # Get the specific account's writer
    online_writer = online_writers.get(account_uid)
    if online_writer is None:
        raise Exception(f"Bot account {account_uid} not connected")
    
    # Get account-specific variables
    account_data = account_configs.get(account_uid, {})
    key = account_data.get('key')
    iv = account_data.get('iv')
    region = account_data.get('region')
    bot_uid = account_data.get('bot_uid')

    if online_writer is None:
        raise Exception("Bot not connected")

    try:
        # 1. JOIN SQUAD (super fast)
        EM = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(online_writer, whisper_writers.get(account_uid), 'OnLine', EM)
        await asyncio.sleep(0.12)  # minimal sync delay

        # 2. PERFORM EMOTE instantly
        for uid_str in uids:
            uid = int(uid_str)
            H = await Emote_k(uid, emote_id, key, iv, region)
            await SEndPacKeT(online_writer, whisper_writers.get(account_uid), 'OnLine', H)

        # 3. LEAVE SQUAD instantly (correct bot UID)
        LV = await ExiT(bot_uid, key, iv)
        await SEndPacKeT(online_writer, whisper_writers.get(account_uid), 'OnLine', LV)
        await asyncio.sleep(0.03)

        return {"status": "success", "message": "Emote done & bot left instantly"}

    except Exception as e:
        raise Exception(f"Failed to perform emote: {str(e)}")


@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Emote Executor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #121212;
            color: white;
        }
        .emote-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
            gap: 10px;
            margin-top: 20px;
        }
        .emote-box {
            background-color: #333;
            border: 2px solid #555;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
        }
        .emote-box:hover {
            background-color: #444;
            transform: scale(1.05);
        }
        .emote-box.selected {
            background-color: #007bff;
            border-color: #0056b3;
        }
        .controls {
            margin: 20px 0;
        }
        input, button {
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
            border: 1px solid #555;
            background-color: #333;
            color: white;
        }
        button {
            background-color: #007bff;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Emote Executor</h1>
    <div class="controls">
        <input type="text" id="teamCode" placeholder="Team Code" value="TEST">
        <input type="text" id="uids" placeholder="UIDs (comma separated)" value="123456,789012">
        <button onclick="executeSelectedEmotes()">Execute Selected Emotes</button>
        <button onclick="selectAll()">Select All</button>
        <button onclick="clearSelection()">Clear Selection</button>
    </div>
    <div class="emote-grid" id="emoteGrid">
        <!-- Emotes will be loaded here -->
    </div>

    <script>
        // Fetch emote IDs from the external source
        async function loadEmotes() {
            try {
                // Using a proxy to avoid CORS issues
                const proxy = 'https://api.allorigins.win/raw?url=';
                const url = 'https://0xme.github.io/ItemID2/?mode=2&page=1&q=collectionType%3AEMOTE';
                
                // For now, we'll use a mock list of emotes since direct access might be blocked
                const mockEmotes = [];
                for (let i = 1; i <= 50; i++) {
                    mockEmotes.push({
                        id: i,
                        name: `Emote ${i}`
                    });
                }
                
                displayEmotes(mockEmotes);
            } catch (error) {
                console.error('Error loading emotes:', error);
                
                // Fallback to mock emotes
                const fallbackEmotes = [];
                for (let i = 1; i <= 20; i++) {
                    fallbackEmotes.push({
                        id: i,
                        name: `Emote ${i}`
                    });
                }
                displayEmotes(fallbackEmotes);
            }
        }

        function displayEmotes(emotes) {
            const grid = document.getElementById('emoteGrid');
            grid.innerHTML = '';
            
            emotes.forEach(emote => {
                const emoteBox = document.createElement('div');
                emoteBox.className = 'emote-box';
                emoteBox.innerHTML = `
                    <div>${emote.name}</div>
                    <div style="font-size: 12px; color: #aaa;">ID: ${emote.id}</div>
                `;
                emoteBox.onclick = () => toggleEmoteSelection(emoteBox, emote.id);
                grid.appendChild(emoteBox);
            });
        }

        let selectedEmotes = new Set();

        function toggleEmoteSelection(box, emoteId) {
            box.classList.toggle('selected');
            if (box.classList.contains('selected')) {
                selectedEmotes.add(emoteId);
            } else {
                selectedEmotes.delete(emoteId);
            }
        }

        function selectAll() {
            document.querySelectorAll('.emote-box').forEach(box => {
                if (!box.classList.contains('selected')) {
                    box.classList.add('selected');
                    const emoteId = parseInt(box.querySelector('div:last-child').textContent.split(': ')[1]);
                    selectedEmotes.add(emoteId);
                }
            });
        }

        function clearSelection() {
            document.querySelectorAll('.emote-box').forEach(box => {
                box.classList.remove('selected');
            });
            selectedEmotes.clear();
        }

        async function executeSelectedEmotes() {
            if (selectedEmotes.size === 0) {
                alert('Please select at least one emote');
                return;
            }

            const teamCode = document.getElementById('teamCode').value;
            const uidsInput = document.getElementById('uids').value;
            const uids = uidsInput.split(',').map(uid => uid.trim()).filter(uid => uid);

            if (!teamCode || uids.length === 0) {
                alert('Please enter team code and at least one UID');
                return;
            }

            // Execute each selected emote
            for (const emoteId of selectedEmotes) {
                try {
                    const url = `/join?tc=${teamCode}&emote_id=${emoteId}&${uids.map((uid, i) => `uid${i+1}=${uid}`).join('&')}`;
                    const response = await fetch(url);
                    const data = await response.json();
                    console.log(`Emote ${emoteId} executed:`, data);
                } catch (error) {
                    console.error(`Error executing emote ${emoteId}:`, error);
                }
                
                // Small delay between emotes to avoid overwhelming the server
                await new Promise(resolve => setTimeout(resolve, 500));
            }
            
            alert(`Executed ${selectedEmotes.size} emotes successfully!`);
        }

        // Load emotes when page loads
        window.onload = loadEmotes;
    </script>
</body>
</html>
    '''

@app.route('/join')
def join_team():
    global loop
    team_code = request.args.get('tc')
    uid1 = request.args.get('uid1')
    uid2 = request.args.get('uid2')
    uid3 = request.args.get('uid3')
    uid4 = request.args.get('uid4')
    uid5 = request.args.get('uid5')
    uid6 = request.args.get('uid6')
    emote_id_str = request.args.get('emote_id')
    account_uid = request.args.get('account_uid')  # Optional parameter to specify which account to use

    if not team_code or not emote_id_str:
        return jsonify({"status": "error", "message": "Missing tc or emote_id"})

    try:
        emote_id = int(emote_id_str)
    except:
        return jsonify({"status": "error", "message": "emote_id must be integer"})

    uids = [uid for uid in [uid1, uid2, uid3, uid4, uid5, uid6] if uid]

    if not uids:
        return jsonify({"status": "error", "message": "Provide at least one UID"})

    # Convert account_uid to int if provided
    account_uid_int = int(account_uid) if account_uid else None

    asyncio.run_coroutine_threadsafe(
        perform_emote(team_code, uids, emote_id, account_uid_int), loop
    )

    return jsonify({
        "status": "success",
        "team_code": team_code,
        "uids": uids,
        "emote_id": emote_id_str,
        "account_uid": account_uid,
        "message": "Emote triggered"
    })


def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)


# ---------------------- MAIN BOT SYSTEM ----------------------

async def MaiiiinE(uid=None, password=None):
    global loop
    
    if uid is None or password is None:
        # Default account if none provided
        uid, password = '4313083403', 'LINUX_NI0G0_BY_SPIDEERIO_GAMING_8SKE8'

    open_id, access_token = await GeNeRaTeAccEss(uid, password)
    if not open_id or not access_token:
        print(f"ErroR - InvaLid AccounT {uid}")
        return None

    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE:
        print(f"TarGeT AccounT {uid} => BannEd / NoT ReGisTeReD !")
        return None

    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    print(UrL)
    region = MajoRLoGinauTh.region

    ToKen = MajoRLoGinauTh.token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp

    loop = asyncio.get_running_loop()

    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa:
        print(f"ErroR - GeTinG PorTs From LoGin DaTa for {uid}!")
        return None

    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port

    OnLineiP, OnLineporT = OnLinePorTs.split(":")
    ChaTiP, ChaTporT = ChaTPorTs.split(":")

    acc_name = LoGinDaTaUncRypTinG.AccountName
    print(ToKen)

    equie_emote(ToKen, UrL)

    # Store account configuration
    account_configs[TarGeT] = {
        'key': key,
        'iv': iv,
        'region': region,
        'bot_uid': TarGeT
    }

    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)
    ready_event = asyncio.Event()

    task1 = asyncio.create_task(
        TcPChaT(ChaTiP, ChaTporT, AutHToKen, key, iv,
                LoGinDaTaUncRypTinG, ready_event, region, account_uid=TarGeT)
    )

    await ready_event.wait()
    await asyncio.sleep(1)

    task2 = asyncio.create_task(
        TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen, account_uid=TarGeT)
    )

    os.system('clear')
    print(render('linux', colors=['white', 'green'], align='center'))
    print(f"\n - BoT STarTinG And OnLine on TarGet : {TarGeT} | BOT NAME : {acc_name}")
    print(" - BoT sTaTus > GooD | OnLinE ! (: \n")

    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    await asyncio.gather(task1, task2)


def load_accounts_from_file(file_path):
    """Load accounts from JSON file"""
    try:
        with open(file_path, 'r') as f:
            accounts = json.load(f)
        return accounts
    except Exception as e:
        print(f"Error loading accounts from {file_path}: {e}")
        return []


async def start_multiple_accounts():
    """Start multiple accounts simultaneously to avoid server flooding"""
    global loop
    
    # Load accounts from JSON file
    accounts = load_accounts_from_file('account.json')
    
    if not accounts:
        print("No accounts found in account.json, starting with default account")
        # Start with default account
        await MaiiiinE()
        return
    
    print(f"Starting {len(accounts)} accounts...")
    
    # Create tasks for all accounts
    tasks = []
    for account in accounts:
        uid = account.get('uid')
        password = account.get('password')
        
        if uid and password:
            # Add a small delay between account connections to avoid server flooding
            task = asyncio.create_task(MaiiiinE(uid, password))
            tasks.append(task)
            # Delay between account connections to prevent flooding the server
            await asyncio.sleep(2)  # 2 second delay between connections
        
    # Wait for all accounts to be connected
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)


async def StarTinG():
    while True:
        try:
            await asyncio.wait_for(start_multiple_accounts(), timeout=7 * 60 * 60)
        except asyncio.TimeoutError:
            print("Token ExpiRed ! , ResTartinG")
        except Exception as e:
            print(f"ErroR TcP - {e} => ResTarTinG ...")


if __name__ == '__main__':
    asyncio.run(StarTinG())