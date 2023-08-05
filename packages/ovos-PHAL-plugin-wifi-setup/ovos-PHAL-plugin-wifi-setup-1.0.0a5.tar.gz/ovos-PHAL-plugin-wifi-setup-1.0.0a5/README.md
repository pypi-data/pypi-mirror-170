# PHAL plugin - Wifi Setup

central wifi setup plugin, client plugins can register with this plugin to provide a wifi setup mechanism

This plugin is part of a larger collection of Wifi setup related plugins

# Install

`pip install ovos-PHAL-plugin-wifi-setup`

# Events

```python

# Event Documentation
# ===================
# Registeration:
# ----------------
# ovos.phal.wifi.plugin.register.client
# type: Request
# description: Register a client to the plugin (requested by the client)
#
# ovos.phal.wifi.plugin.deregister.client
# type: Request
# description: Deregister a client from the plugin (requested by the client)
#
# ovos.phal.wifi.plugin.client.registration.failure
# type: Response
# description: Registration failed
#
# ovos.phal.wifi.plugin.client.registered
# type: Response
# description: Registration successful
# 
# ovos.phal.wifi.plugin.client.deregistered
# type: Response
# description: Deregistration successful
#
# Client Activation / Deactivation
# --------------------------------
# ovos.phal.wifi.plugin.set.active.client
# type: Request
# description: Activate a client (requested by the client) 
#
# ovos.phal.wifi.plugin.remove.active.client
# type: Request
# description: Deactivate a client (requested by the client)
#
# ovos.phal.wifi.plugin.activate.{clientID}
# type: Response
# description: Inform the client that the activation was successful 
#
# ovos.phal.wifi.plugin.deactivate.{clientID}
# type: Response
# description: Inform the client that the deactivation was successful
#
# Client Setup Running / Finished
# --------------------------------
# ovos.phal.wifi.plugin.client.setup.failure
# type: Request
# description: Inform the wifi plugin that the client setup failed
#
# Plugin VUI / GUI Interaction (Client Selection)
# --------------------------------------------
# ovos.phal.wifi.plugin.client.select
# type: Request
# description: Inform the wifi plugin that a client was selected
#
# ovos.phal.wifi.plugin.skip.setup
# type: Request
# description: Inform the wifi plugin that further setup is not needed
#
# ovos.phal.wifi.plugin.user.activated
# type: Request
# description: Inform the wifi plugin that the user has activated the client
# 
# Generic Messages (Plugin Actions)
# ----------------
# mycroft.internet.connected
# type: Request
# description: Inform the wifi plugin that the internet is connected
#
# ovos.phal.wifi.plugin.alive
# type: Response
# description: Inform the wifi clients that the plugin is alive on startup
#
# ovos.phal.wifi.plugin.status
# type: Request
# description: Request the wifi plugin to send the status of the plugin
# 
# ovos.phal.wifi.plugin.stop.setup.event
# type: Response
# description: Inform the wifi clients to stop the setup event completely and clean up
#
# ovos.phal.wifi.plugin.setup.failed
# type: Response
# description: Inform the interested parties that the plugin itself failed


```
