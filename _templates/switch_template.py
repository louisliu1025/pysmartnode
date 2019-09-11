'''
Created on 31.10.2017

@author: Kevin Köck
'''

"""
example config:
{
    package: <package_path>
    component: Switch
    constructor_args: {
        # mqtt_topic: null     #optional, defaults to <mqtt_home>/<device_id>/Buzzer/set
        # friendly_name: null # optional, friendly name shown in homeassistant gui with mqtt discovery
    }
}
"""

__updated__ = "2019-09-08"
__version__ = "1.2"

from pysmartnode import config
from pysmartnode.utils.component.switch import ComponentSwitch

####################
# choose a component name that will be used for logging (not in leightweight_log),
# the default mqtt topic that can be changed by received or local component configuration
# as well as for the component name in homeassistant.
_component_name = "Switch"
####################

_mqtt = config.getMQTT()
_count = 0


class Switch(ComponentSwitch):
    def __init__(self, mqtt_topic=None, friendly_name=None):
        # This makes it possible to use multiple instances of Button. It is needed for every default value.
        global _count
        self._count = _count
        _count += 1
        # mqtt_topic can be adapted otherwise a default mqtt_topic will be generated if None is passed
        super().__init__(_component_name, mqtt_topic, instance_name=None, wait_for_lock=True)
        self._frn = friendly_name

    async def _init(self):
        # in this case not even needed as no additional init is being done.
        # self._off will be called automatically.
        # You can remove this if you don't add additional code
        await super()._init()

    #####################
    # Change these methods according to your device.
    #####################
    async def _on(self):
        """Turn device on."""
        return True  # return True when turning device on was successful.

    async def _off(self):
        """Turn device off. """
        return True  # return True when turning device off was successful.
    #####################
