import bluetooth
nearby_devices = bluetooth.discover_devices(duration=8, flush_cache=True,lookup_names = True)
target_address = "98:D3:31:FB:00:94"
found_device = False
for addr, name in nearby_devices:
 if target_address == addr:
  target_name = name
  found_device = True
  break
if found_device is True:
  print("found target bluetooth device with address %s and name %s"%(target_address, target_name))
  BT_name = bluetooth.lookup_name(target_address, timeout=10)
  print "Name = ", BT_name

  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((target_address, port))

  print 'Connected'
  sock.settimeout(2.0)
  sock.send("Hello")
  sock.close()
else:
  print "could not find target bluetooth device nearby"
