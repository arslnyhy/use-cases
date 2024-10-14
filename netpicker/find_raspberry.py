from comfy import high
import slurpit


@high(
    name='rule_find_raspberry'
)
def rule_find_raspberry(device):
    host = 'https://sandbox.slurpit.io'
    api_key = '4DTIz5axkWqOuxUGm6gobN4JAaB4l5Cg16589a08019c20'
    api = slurpit.api(host, api_key)
    snapshots = api.device.get_snapshots(hostname=device.ipaddress)
    arp_results = snapshots['ARP']['planning_results']
    vendors = {arp['Mac_vendor'] for arp in arp_results}
    assert 'Raspberry Pi Foundation' not in vendors, "ALERT: SUSPICIOUS DEVICE DETECTED IN THE NETWORK!"LS
