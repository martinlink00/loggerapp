#!/usr/bin/env python
# -*- mode: Python; coding: utf-8 -*-

# Copyright © 2016 Christian Gross

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import vrmusbcamapi as vrm
import ctypes as ct
import numpy as np

# clean up any left overs
# r = vrm.VRmUsbCamCleanup()
# print(r)

# update key list
r = vrm.VRmUsbCamUpdateDeviceKeyList()

# get number of devices
ndev = vrm.VRmDWORD()
r = vrm.VRmUsbCamGetDeviceKeyListSize(ct.byref(ndev))
print('Found %i cameras' % int(ndev.value))

# get a VRmDeviceKey
nodev = 1
devkey = vrm.POINTER(vrm.VRmDeviceKey)()
r = vrm.VRmUsbCamGetDeviceKeyListEntry(nodev - 1, ct.byref(devkey))
if r == 1:
    print('Busy? %i' % devkey.contents.m_busy)
    print('Serial %i' % devkey.contents.m_serial)
    print('Manufacturer %s' %
          devkey.contents.mp_manufacturer_str.data.decode('utf-8'))
    print('Product %s' % devkey.contents.mp_product_str.data.decode('utf-8'))

    # get a handle by opening a device
    if not devkey.contents.m_busy == 1:
        devhand = vrm.VRmUsbCamDevice()
        r = vrm.VRmUsbCamOpenDevice(devkey, ct.byref(devhand))
        print('Got handle? %i' % r)
    else:
        print('Camera busy!')

    # set format
    nsrcfmt = vrm.VRmDWORD()
    r = vrm.VRmUsbCamGetSourceFormatListSize(devhand, ct.byref(nsrcfmt))
    imagefmt = vrm.VRmImageFormat()  # The image format
    r = vrm.VRmUsbCamGetSourceFormatListEntry(devhand, nsrcfmt.value-1, ct.byref(imagefmt))
    r = vrm.VRmUsbCamSetSourceFormatIndex(devhand, nsrcfmt.value-1)

    # get number of sensor ports
    nports = vrm.VRmDWORD()
    r = vrm.VRmUsbCamGetSensorPortListSize(devhand, ct.byref(nports))
    print('Ports: %i' % nports.value)

    # configure
    # r = vrm.VRmUsbCamLoadConfig(devhand, 1)
    # print('Load config? %i' % r)

    # get all properties
    nprops = vrm.VRmDWORD()
    r = vrm.VRmUsbCamGetPropertyListSize(devhand, ct.byref(nprops))
    print('Number of properities: %i' % nprops.value)
    propid = vrm.VRmPropId()
    propinfo = vrm.VRmPropInfo()
    prop_attr_b = vrm.VRmPropAttribsB()
    prop_b = vrm.VRmBOOL()
    prop_attr_d = vrm.VRmPropAttribsD()
    prop_d = vrm.c_double()
    prop_attr_i = vrm.VRmPropAttribsI()
    prop_i = ct.c_int()
    prop_attr_f = vrm.VRmPropAttribsF()
    prop_f = ct.c_float()
    prop_attr_e = vrm.VRmPropAttribsE()
    prop_e = vrm.VRmPropId()
    prop_attr_s = vrm.VRmPropAttribsS()
    prop_s = ct.c_char_p()
    # set exposure time
    r = vrm.VRmUsbCamSetPropertyValueF(devhand, vrm.VRmPropId(4097), ct.byref(ct.c_float(1.0)))
    for ii in range(nprops.value):
        # for ii in range(1):
        r = vrm.VRmUsbCamGetPropertyListEntry(devhand, ii, ct.byref(propid))
        r = vrm.VRmUsbCamGetPropertyInfo(devhand, propid.value, ct.byref(propinfo))
        if propinfo.m_type == 1:
            r = vrm.VRmUsbCamGetPropertyAttribsB(devhand, propid.value, ct.byref(prop_attr_b))
            r = vrm.VRmUsbCamGetPropertyValueB(devhand, propid.value, ct.byref(prop_b))
            val = prop_b.value
        elif propinfo.m_type == 2:
            r = vrm.VRmUsbCamGetPropertyAttribsI(devhand, propid.value, ct.byref(prop_attr_i))
            r = vrm.VRmUsbCamGetPropertyValueI(devhand, propid.value, ct.byref(prop_i))
            val = prop_i.value
        elif propinfo.m_type == 3:
            r = vrm.VRmUsbCamGetPropertyAttribsF(devhand, propid.value, ct.byref(prop_attr_f))
            r = vrm.VRmUsbCamGetPropertyValueF(devhand, propid.value, ct.byref(prop_f))
            val = prop_f.value
        elif propinfo.m_type == 4:
            r = vrm.VRmUsbCamGetPropertyAttribsS(devhand, propid.value, ct.byref(prop_attr_s))
            r = vrm.VRmUsbCamGetPropertyValueS(devhand, propid.value, ct.byref(prop_s))
            val = prop_s.value
        elif propinfo.m_type == 5:
            r = vrm.VRmUsbCamGetPropertyAttribsE(devhand, propid.value, ct.byref(prop_attr_e))
            r = vrm.VRmUsbCamGetPropertyValueE(devhand, propid.value, ct.byref(prop_e))
            val = prop_e.value
        elif propinfo.m_type == 6:
            pass
        elif propinfo.m_type == 7:
            pass
        elif propinfo.m_type == 8:
            pass
        elif propinfo.m_type == 9:
            r = vrm.VRmUsbCamGetPropertyAttribsD(devhand, propid.value, ct.byref(prop_attr_d))
            r = vrm.VRmUsbCamGetPropertyValueD(devhand, propid.value, ct.byref(prop_d))
            val = prop_d.value
        if propinfo.m_writeable == 1:
            print('(W) Property %s has id %i, type %s and value %s' % (propinfo.m_description.data.decode('utf-8'), propinfo.m_id, propinfo.m_type, val))
        else:
            print('(R) Property %s has id %i, type %s and value %s' % (propinfo.m_description.data.decode('utf-8'), propinfo.m_id, propinfo.m_type, val))

    from time import sleep
    sleep(1)

    # start the camera frame grabber
    r = vrm.VRmUsbCamStart(devhand)
    framesdropped = vrm.VRmBOOL()
    imgready = vrm.VRmBOOL()
    image = vrm.POINTER(vrm.VRmImage)()
    print('Started? %i' % r)
    for ii in range(2):
        r = vrm.VRmUsbCamLockNextImage(devhand, ct.byref(image), ct.byref(framesdropped))
        print('Got image? %i' % r)
        if r == 1:
            height = image.contents.m_image_format.m_height
            width = image.contents.m_image_format.m_width
            pitch = image.contents.m_pitch
            print('pitch-width %s' % (pitch-width))
            im = np.array(image.contents.mp_buffer[0:height * pitch]).reshape(height, pitch)
        else:
            r = vrm.VRmUsbCamGetLastError()
            print(r.data.decode('utf-8'))
        r = vrm.VRmUsbCamUnlockNextImage(devhand, ct.byref(image))
        print('Unlocked image? %i' % r)
    # stop the camera frame grabber
    r = vrm.VRmUsbCamStop(devhand)
    print('Stopped? %i' % r)


    # close the device
    r = vrm.VRmUsbCamCloseDevice(devhand)
    print('Closed? %i' % r)

    # free device key
    r = vrm.VRmUsbCamFreeDeviceKey(ct.byref(devkey))
    print('Key free? %i' % r)

else:
    print('ERROR: Could not get key.')
    # get error
    r = vrm.VRmUsbCamGetLastError()
    print(r.data.decode('utf-8'))

