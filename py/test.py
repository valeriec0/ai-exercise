# this is the script to test the web server
import requests
import json

url = 'http://127.0.0.1:5000/'
problem = """
Jul  1 09:00:55 calvisitor-10-105-160-95 kernel[0]: IOThunderboltSwitch<0>(0x0)::listenerCallback - Thunderbolt HPD packet for route = 0x0 port = 11 unplug = 0
Jul  1 09:01:05 calvisitor-10-105-160-95 com.apple.CDScheduler[43]: Thermal pressure state: 1 Memory pressure state: 0
Jul  1 09:01:06 calvisitor-10-105-160-95 QQ[10018]: FA||Url||taskID[2019352994] dealloc
Jul  1 09:02:26 calvisitor-10-105-160-95 kernel[0]: ARPT: 620701.011328: AirPort_Brcm43xx::syncPowerState: WWEN[enabled]
Jul  1 09:02:26 authorMacBook-Pro kernel[0]: ARPT: 620702.879952: AirPort_Brcm43xx::platformWoWEnable: WWEN[disable]
Jul  1 09:03:11 calvisitor-10-105-160-95 mDNSResponder[91]: mDNS_DeregisterInterface: Frequent transitions for interface awdl0 (FE80:0000:0000:0000:D8A5:90FF:FEF5:7FFF)
Jul  1 09:03:13 calvisitor-10-105-160-95 kernel[0]: ARPT: 620749.901374: IOPMPowerSource Information: onSleep,  SleepType: Normal Sleep,  'ExternalConnected': Yes, 'TimeRemaining': 0,
Jul  1 09:04:33 calvisitor-10-105-160-95 kernel[0]: ARPT: 620750.434035: wl0: wl_update_tcpkeep_seq: Original Seq: 3226706533, Ack: 3871687177, Win size: 4096
Jul  1 09:04:33 authorMacBook-Pro kernel[0]: ARPT: 620752.337198: ARPT: Wake Reason: Wake on Scan offload
Jul  1 09:04:37 authorMacBook-Pro symptomsd[215]: __73-[NetworkAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke unexpected switch value 2
Jul  1 09:12:20 authorMacBook-Pro kernel[0]: IO80211AWDLPeerManager::setAwdlAutoMode Resuming AWDL
Jul  1 09:12:21 calvisitor-10-105-160-95 symptomsd[215]: __73-[NetworkAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke unexpected switch value 2
Jul  1 09:18:16 calvisitor-10-105-160-95 kernel[0]: ARPT: 620896.311264: wl0: MDNS: 0 SRV Recs, 0 TXT Recs
Jul  1 09:19:03 calvisitor-10-105-160-95 kernel[0]: AppleCamIn::systemWakeCall - messageType = 0xE0000340
Jul  1 09:19:03 authorMacBook-Pro configd[53]: setting hostname to "authorMacBook-Pro.local"
Jul  1 09:19:13 calvisitor-10-105-160-95 com.apple.cts[258]: com.apple.icloud.fmfd.heartbeat: scheduler_evaluate_activity told me to run this job; however, but the start time isn't for 439034 seconds.  Ignoring.
Jul  1 09:21:57 authorMacBook-Pro corecaptured[31174]: CCIOReporterFormatter::addRegistryChildToChannelDictionary streams 7
Jul  1 09:21:58 calvisitor-10-105-160-95 com.apple.WebKit.WebContent[25654]: [09:21:58.929] <<<< CRABS >>>> crabsFlumeHostAvailable: [0x7f961cf08cf0] Byte flume reports host available again.
Jul  1 09:22:02 calvisitor-10-105-160-95 com.apple.cts[258]: com.apple.Safari.SafeBrowsing.Update: scheduler_evaluate_activity told me to run this job; however, but the start time isn't for 2450 seconds.  Ignoring.
Jul  1 09:22:25 calvisitor-10-105-160-95 kernel[0]: IO80211AWDLPeerManager::setAwdlAutoMode Resuming AWDL
Jul  1 09:23:26 calvisitor-10-105-160-95 kernel[0]: AirPort: Link Down on awdl0. Reason 1 (Unspecified).
Jul  1 09:23:26 calvisitor-10-105-160-95 kernel[0]: IOThunderboltSwitch<0>(0x0)::listenerCallback - Thunderbolt HPD packet for route = 0x0 port = 11 unplug = 0
Jul  1 09:24:13 calvisitor-10-105-160-95 kernel[0]: PM response took 2010 ms (54, powerd)
"""
data = {'problem': problem}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.text)
else:
    print('Error:', response.status_code, response.text)
