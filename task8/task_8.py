mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}

not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}
result_catalog = {}
supported_devices = set()

def get_supported_catalog(dict_devices, device):
    if device in dict_devices and device not in not_supported_devices:
        return {device: dict_devices[device]}
    return {}

all_devices = set(mobile_devices.keys()).union(home_devices.keys())

for device in all_devices:
    supported_mob_dev = get_supported_catalog(mobile_devices, device)
    if supported_mob_dev:
        supported_devices.update(supported_mob_dev.keys())
    supported_home_dev = get_supported_catalog(home_devices, device)
    if supported_home_dev:
        supported_devices.update(supported_home_dev.keys())

for device in supported_devices:
    if device in mobile_devices:
        result_catalog[device] = mobile_devices[device]
    elif device in home_devices:
        result_catalog[device] = home_devices[device]

print('Каталог поддерживаемых девайсов:')
print(result_catalog)
