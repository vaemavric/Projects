import usb.core

dev = usb.core.find(idVendor=0x04d8, idProduct=0x005b)

if dev is None:
    raise ValueError('Device not found')
else:
    try: 
        dev.detach_kernel_driver(0)
    except:
        pass
    dev.set_configuration()

    speed1 = 128
    speed2 = 0
    speed3 = 0
    speed4 = 0
    motoronoff = 0b11110001
    enable = 0x30
    servo = 128

    data=[4, speed1, speed2, speed3, speed4, motoronoff, enable, servo]
    dev.write(2,data)

    outputs = 0b11000011
    data=[8, outputs]
    dev.write(2,data)

    inputs = dev.read(0x81,1)
    print "Inputs = {}".format(inputs[0])
