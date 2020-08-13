// ==============================================================================================
/// @file vrmusbcam2l.h                                           VRmUsbCam C API Legacy v3.5.0.0
//  Copyright VRmagic 2004-2014
// ==============================================================================================

#ifndef VRMUSBCAM2L_H
#define VRMUSBCAM2L_H

// all functions in this header are for legacy purpose only and further usage is deprecated!

#if defined(__cplusplus) && !defined(VRM_NO_EXTERN_C)
extern "C" {
#endif

/// VRmUsbCam is C calling convention (cdecl). define this appropriate if your compiler
/// has a different default
#ifndef VRM_API
#define VRM_API
#endif 

// don't define this. for internal use only
#ifndef VRM_EXTERN
#define VRM_EXTERN extern
#endif

// don't define this. for internal use only
#ifndef VRM_STRUCT
#define VRM_STRUCT struct
#endif

// don't define this. for internal use only
#ifndef VRM_ENUM
#define VRM_ENUM enum
#endif


// ------------------------------------------------------------------------
// Error Handling / General Management
// ------------------------------------------------------------------------

/// if an API function fails (return value VRM_FAILED) use this function
/// check if error was a transfer timeout
VRM_EXTERN VRmBOOL VRM_API VRmUsbCamLastErrorWasTransferTimeout(void);

// ------------------------------------------------------------------------
// Image Handling
// ------------------------------------------------------------------------

/// deprecated function to change source format using VRmImageFormat instead of index
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSourceFormat(VRmUsbCamDevice f_device,VRmImageFormat f_source_format);

/// Enable/Disable High-Quality Bayer Filter

/// use this function before calling VRmUsbCamGetTargetFormatListSize/Entry to
/// enable High-Quality Bayer Filter, producing a clearer image but taking
/// more processing time in VRmUsbCamConvertImage. Default is disabled.
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetBayerHQ(VRmBOOL f_enable);

/// Check if High-Quality Bayer Filter is enabled
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetBayerHQ(VRmBOOL* fp_enable);

// ------------------------------------------------------------------------
// Frame Grabber
// ------------------------------------------------------------------------

/// update source format list.
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamUpdateSourceFormatList(VRmUsbCamDevice f_device);

/// get number of available source format list entries
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSourceFormatListSize(VRmUsbCamDevice f_device,VRmDWORD* fp_size);

/// query source format list entry with index = [0...size-1]
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSourceFormatListEntry(VRmUsbCamDevice f_device,VRmDWORD f_index,VRmImageFormat* fp_image_format);

/// get string description of source format with index = [0...size-1]
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSourceFormatListEntryDescription(VRmUsbCamDevice f_device,VRmDWORD f_index,const char** fpp_string);

/// select source format.
/// selects one of the format list entries as source image format.
/// NOTE: don't change while grabber is running. changing source formats also updates the target format list!
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSourceFormatIndex(VRmUsbCamDevice f_device,VRmDWORD f_source_format_index);

/// get current source format index
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSourceFormatIndex(VRmUsbCamDevice f_device,VRmDWORD* fp_source_format_index);

/// get current source format
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSourceFormat(VRmUsbCamDevice f_device,VRmImageFormat* fp_source_format);

/// check if source format is a user roi format
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamIsUserROIFormat(VRmUsbCamDevice f_device,VRmDWORD f_source_format_index,VRmBOOL* fp_is_user_roi);

/// set queue size for usb buffer queue, Valid range: [1;1000], default: 3
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetQueueSize(VRmUsbCamDevice f_device,VRmDWORD f_queue_size);
/// get current queue size
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetQueueSize(VRmUsbCamDevice f_device,VRmDWORD* fp_queue_size);

/// get estimated frame rate for current settings
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetEstimatedFps(VRmUsbCamDevice f_device, double* fp_fps);

/// get number of available target format list entries for current source format.
/// obsolete, use VRmUsbCamGetTargetFormatListSizeEx2() for port #1 instead
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetTargetFormatListSizeEx(VRmUsbCamDevice f_device,VRmDWORD* fp_size);

/// query target format list entry with index = [0...size-1].
/// obsolete, use VRmUsbCamGetTargetFormatListEntryEx2() for port #1 instead
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetTargetFormatListEntryEx(VRmUsbCamDevice f_device,VRmDWORD f_index,VRmImageFormat* fp_target_format);

/// is next image ready.
/// check if the next image can be immediately accessed via VRmUsbCamLockNextImage()
/// if not, you can do something else and check again
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamIsNextImageReady(VRmUsbCamDevice f_device,VRmBOOL* fp_ready);

/// lock source image.
/// use fp_frames_dropped to see if frames have been dropped (optional, pass NULL otherwise),
/// use VRmUsbCamConvertImage() to convert locked image to one of the formats in target format list
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamLockNextImage(VRmUsbCamDevice f_device,VRmImage** fpp_image,VRmBOOL* fp_frames_dropped);

// ------------------------------------------------------------------------
// Configuration Settings
// ------------------------------------------------------------------------

/// there are two possible camera settings stored in hardware:
/// factory default settings and user settings

/// Reload the factory default settings
/// NOTES: this may change the selected source format, as well as trigger mode
/// and all other settings in the Settings structs.
/// the grabber must be stopped when you call this function.
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamReloadFactorySettings(VRmUsbCamDevice f_device);

/// Reload the on-board stored user settings
/// NOTES: this may change the selected source format, as well as trigger mode
/// and all other settings in the Settings structs and is done automatically at 
/// VRmUsbCamOpenDevice.
/// the grabber must be stopped when you call this function.
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamReloadUserSettings(VRmUsbCamDevice f_device);

/// Saves the current settings as user settings (in hardware)
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSaveUserSettings(VRmUsbCamDevice f_device);

/// check if next VRmUsbCamSaveUserSettings requires a firmware compression which takes some seconds (blocking)
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamIsFirmwareCompressionRequired(VRmUsbCamDevice f_device,VRmBOOL* fp_required);

// ------------------------------------------------------------------------
// Trigger Mode Control and Statistics
// ------------------------------------------------------------------------

/// parameter for VRmUsbCamSet/GetTriggerMode()
typedef VRM_ENUM _VRmTriggerMode
{
	/// free-running / untriggered
	VRM_TRIGGERMODE_NONE=0,
	/// snapshot triggered (external)
	VRM_TRIGGERMODE_SNAPSHOT_EXT=1,
	/// snapshot triggered (by VRmUsbCamSoftTrigger())
	VRM_TRIGGERMODE_SNAPSHOT_SOFT=2,
	/// snapshot triggered (by VRmUsbCamSoftTrigger() or external)
	VRM_TRIGGERMODE_SNAPSHOT_EXT_SOFT=3
} VRmTriggerMode;
/// for backwards compatibility:
#define VRM_TRIGGERMODE_REPEATED_SNAPSHOT (VRM_TRIGGERMODE_SNAPSHOT_EXT)

/// set the trigger mode of the camera. By default, VRM_TRIGGERMODE_NONE (free-running)
/// is activated.
/// setting values other than VRM_TRIGGERMODE_NONE is only allowed for devices that support
/// an external trigger. Find out by checking VRmUsbCamGetFeatures() whether the device 
/// supports triggers (VRM_EXT_TRIGGER_SUPPORTED/VRM_SOFT_TRIGGER_SUPPORTED).
/// NOTE: the grabber must be stopped when this function is called
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetTriggerMode(VRmUsbCamDevice f_device, VRmTriggerMode f_mode);

/// get the current trigger mode of the camera
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetTriggerMode(VRmUsbCamDevice f_device, VRmTriggerMode* fp_mode);

/// set trigger timeout.
/// current implementation has a very low precision (+/- 1000ms)
/// and has a minimum of 5000ms (which is default)
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetTriggerTimeout(VRmUsbCamDevice f_device, float f_trigger_timeout_ms);

/// get the current trigger timeout
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetTriggerTimeout(VRmUsbCamDevice f_device, float* fp_trigger_timeout_ms);

/// deprecated
typedef VRM_STRUCT _VRmTriggerStats {
	/// number of trigger edges caught (ie. caused an exposure) since last
	/// call to VRmusbCamReadTriggerStats()
	VRmWORD	m_caught_count;
	/// number of trigger edges dropped (ie. NOT caused an exposure) since 
	/// last call to VRmusbCamReadTriggerStats()
	VRmWORD	m_dropped_count;
	/// timestamp of statistics in ms since last VRmUsbCamRestartTimer()
	double	m_time_stamp;
} VRmTriggerStats;

/// deprecated 
/// just use the frame counter of locked images, which is used as trigger counter in triggered modes
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamReadTriggerStats(VRmUsbCamDevice f_device,VRmTriggerStats* fp_trigger_stats);

// ------------------------------------------------------------------------
// Configuration Settings
// ------------------------------------------------------------------------

typedef VRM_ENUM _VRmFeatures
{
	VRM_SETTINGS1_SUPPORTED=1<<0,
	VRM_SETTINGS2_SUPPORTED=1<<1,
	VRM_SETTINGS3_SUPPORTED=1<<2,
	VRM_SETTINGS4_SUPPORTED=1<<3,
	VRM_SETTINGS5_SUPPORTED=1<<4,
	VRM_SETTINGS6_SUPPORTED=1<<5,
	VRM_SETTINGS7_SUPPORTED=1<<6,
	VRM_SETTINGS8_SUPPORTED=1<<7,
	VRM_SETTINGS9_SUPPORTED=1<<8,
	VRM_EXT_TRIGGER_SUPPORTED=1<<16,
	VRM_SOFT_TRIGGER_SUPPORTED=1<<17,
}VRmFeatures;

/// Check which features are supported,
/// fp_supported is a bitmask of VRmFeatures enums
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetFeatures(VRmUsbCamDevice f_device,int* fp_features);

/// Sensor Settings for VRmC-3, VRmC-4pro
typedef VRM_STRUCT _VRmSettings1
{
	/// [0,m_sensor_width-m_roi_width]
	VRmWORD m_roi_left;
	/// [0,m_sensor_height-m_roi_height]
	VRmWORD m_roi_top;
	/// [2,m_sensor_width], don't change while grabber is running
	VRmWORD m_roi_width;
	/// [2,m_sensor_height], don't change while grabber is running
	VRmWORD m_roi_height;
	/// READ-ONLY
	VRmWORD m_sensor_width;
	/// READ-ONLY
	VRmWORD m_sensor_height;
	/// [0.0;2000.0], exposure time of the camera in milliseconds.
	double m_exposure_time_ms;
	/// [5.0;15.0], set the pixel clock in MHz
	double m_pixel_clock_mhz;
	/// [0;63], red gain, 0=highest possible gain
	VRmBYTE m_red_gain;
	/// [0;63], green gain, 0=highest possible gain, also used as gray gain on /BW cameras
	VRmBYTE m_green_gain;
	/// [0;63], blue gain, 0=highest possible gain
	VRmBYTE m_blue_gain;
	/// [0;63] reset Level Voltage of the Camera
	VRmBYTE m_reset_level;
	/// [0;7] Pixel Bias Voltage Control of the Camera
	VRmBYTE m_pixel_bias_voltage;
	// NOTE: vBlank may be changed using VRmSettings7. For backwards compatibility, it is not 
	// included here.
}VRmSettings1;

VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSettings1(VRmUsbCamDevice f_device,const VRmSettings1* fcp_settings);
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSettings1(VRmUsbCamDevice f_device,VRmSettings1* fp_settings);

/// Illumination Settings for VRmC-3i
typedef VRM_STRUCT _VRmSettings2
{
	/// [0.0;1.0], Illumination 
	double m_illumination_intensity;
}VRmSettings2;

VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSettings2(VRmUsbCamDevice f_device,const VRmSettings2* fcp_settings);
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSettings2(VRmUsbCamDevice f_device,VRmSettings2* fp_settings);

/// Filter Settings for VRmC-3, VRmC-4pro, VRmC-6pro and VRmC-8pro

/// These Filter Settings get applied during VRmUsbCamConvertImage,
/// if you only use VRmUsbCamLockNextImage these settings are IGNORED
typedef VRM_STRUCT _VRmSettings3
{
	/// [0.0;10.0], neutral: 1.0
	float m_gamma;
	/// [-255,255], neutral: 0
	short m_luminance;
	/// [0.0;10.0], neutral: 1.0
	float m_contrast;
}VRmSettings3;

VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSettings3(VRmUsbCamDevice f_device,const VRmSettings3* fcp_settings);
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSettings3(VRmUsbCamDevice f_device,VRmSettings3* fp_settings);

typedef VRM_ENUM _VRmAVCInput
{ 
	VRM_SVIDEO,
	VRM_COMPOSITE,
	VRM_YC
}VRmAVCInput;

/// Signal Settings for VRmAVC-1
typedef VRM_STRUCT _VRmSettings4
{
	/// [0,255], luminance brightness, default: 128
	VRmBYTE m_luminance_brightness;
	/// [0,127], luminance contrast, default: 64
	VRmBYTE m_luminance_contrast;
	/// [0,127], chrominance saturation, default: 64
	VRmBYTE m_chrominance_saturation;
	/// [-128,127], chrominance hue, default: 0
	char m_chrominance_hue;
	/// [VRM_SVIDEO,VRM_COMPOSITE,VRM_YC], input format, default: SVIDEO
	VRmAVCInput m_format;
}VRmSettings4;

VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSettings4(VRmUsbCamDevice f_device,const VRmSettings4* fcp_settings);
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSettings4(VRmUsbCamDevice f_device,VRmSettings4* fp_settings);

/// Sensor Settings for VRmC-6pro
typedef VRM_STRUCT _VRmSettings5
{
	/// [0,m_sensor_width-m_roi_width]
	VRmWORD m_roi_left;
	/// [0,m_sensor_height-m_roi_height]
	VRmWORD m_roi_top;
	/// [2,m_sensor_width], don't change while grabber is running
	VRmWORD m_roi_width;
	/// [2,m_sensor_height], don't change while grabber is running
	VRmWORD m_roi_height;
	/// [1,255], vertical blanking (unit: lines). ATTENTION: low values will not 
	/// work with "single internal" or "multiple internal" driver queuing mode.
	/// see VRmagic USB Driver tool.
	VRmBYTE m_vblank_lines;
	/// READ-ONLY
	VRmWORD m_sensor_width;
	/// READ-ONLY
	VRmWORD m_sensor_height;
	/// [0.0;2000.0], exposure time of the camera in milliseconds.
	double m_exposure_time_ms;
	/// [5.0;43.0], set the pixel clock in MHz
	double m_pixel_clock_mhz;
	/// adapt readout time to exposure time. if enabled, m_pixel_clock_mhz 
	/// is ignored and the pixel clock is set to an optimal value, depending
	/// on the exposure time.
	VRmBOOL m_adapt_readout_to_exposure;
	/// [1;18], red gain, 18=highest possible gain
	VRmBYTE m_red_gain;
	/// [1;18], green gain, 18=highest possible gain
	VRmBYTE m_green_gain;
	/// [1;18], blue gain, 18=highest possible gain
	VRmBYTE m_blue_gain;
	/// [0.0;2.0], VrstLow voltage, adjusts blooming artefacts
	double m_vrst_low_voltage;
} VRmSettings5;

VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSettings5(VRmUsbCamDevice f_device,const VRmSettings5* fcp_settings);
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSettings5(VRmUsbCamDevice f_device,VRmSettings5* fp_settings);

typedef VRM_ENUM _VRmTriggerPolarity
{
	VRM_TRIGGERPOLARITY_POS_EDGE=0,
	VRM_TRIGGERPOLARITY_NEG_EDGE=1,
	VRM_TRIGGERPOLARITY_POS_LEVEL=2,
	VRM_TRIGGERPOLARITY_NEG_LEVEL=3
} VRmTriggerPolarity;

/// External Trigger Settings for VRmC-4pro v2, VRmC-6pro and VRmC-8pro

/// Use VRmUsbCamSetTriggerMode() to enable external trigger,
/// and VRmUsbCamReadTriggerStats to analyse trigger statistics.
typedef VRM_STRUCT _VRmSettings6
{
	/// polarity of external trigger input
	VRmTriggerPolarity m_polarity;
	/// trigger delay (in ms), range [0;1000.0] (edge modes)
	double m_delay_ms;
} VRmSettings6;

VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSettings6(VRmUsbCamDevice f_device,const VRmSettings6* fcp_settings);
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSettings6(VRmUsbCamDevice f_device,VRmSettings6* fp_settings);

/// Additional Sensor Settings for VRmC-3(i) and VRmC-4pro

/// For backwards-compatibility, these settings are not included
/// in VRmSettings1.
typedef VRM_STRUCT _VRmSettings7
{
	/// vertical blanking (unit: lines). ATTENTION: low values may not 
	/// work with "single internal" or "multiple internal" driver queuing mode.
	/// see VRmagic USB Driver tool. range [1;80]
	VRmBYTE	m_vblank_lines;
} VRmSettings7;

VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSettings7(VRmUsbCamDevice f_device,const VRmSettings7* fcp_settings);
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSettings7(VRmUsbCamDevice f_device,VRmSettings7* fp_settings);

/// Sensor Settings for VRmC-8pro
typedef VRM_STRUCT _VRmSettings8
{
	/// [0,m_sensor_width-m_roi_width]
	VRmWORD m_roi_left;
	/// [0,m_sensor_height-m_roi_height]
	VRmWORD m_roi_top;
	/// [2,m_sensor_width], don't change while grabber is running, only EVEN values are valid
	VRmWORD m_roi_width;
	/// [2,m_sensor_height], don't change while grabber is running, only EVEN values are valid
	VRmWORD m_roi_height;
	/// [3,1023], vertical blanking (unit: lines). ATTENTION: low values will not 
	/// work with "single internal" or "multiple internal" driver queuing mode.
	/// see VRmagic USB Driver tool.
	VRmWORD m_vblank_lines;
	/// READ-ONLY
	VRmWORD m_sensor_width;
	/// READ-ONLY
	VRmWORD m_sensor_height;
	/// [0.0;7500.0], exposure time of the camera in milliseconds.
	double m_exposure_time_ms;
	/// [5.0;48.0], set the pixel clock in MHz
	double m_pixel_clock_mhz;
	/// [0.0;128.0], red gain
	float m_red_gain;
	/// [0.0;128.0], green gain
	float m_green_gain;
	/// [0.0;128.0], blue gain
	float m_blue_gain;
} VRmSettings8;

VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSettings8(VRmUsbCamDevice f_device,const VRmSettings8* fcp_settings);
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSettings8(VRmUsbCamDevice f_device,VRmSettings8* fp_settings);

typedef VRM_ENUM _VRmShutterPolarity
{
	VRM_SHUTTERPOLARITY_DISABLED=0,
	VRM_SHUTTERPOLARITY_POS=1,
	VRM_SHUTTERPOLARITY_NEG=2
} VRmShutterPolarity;

/// Shutter Settings for VRmC-4pro v2, VRmC-6pro and VRmC-8pro.
/// This feature is only available with firmware version 11.43 or later.
typedef VRM_STRUCT _VRmSettings9
{
	/// polarity of shutter output
	VRmShutterPolarity m_polarity;
	/// shutter delay (in ms), range [0;1000.0]
	float m_delay_ms;
	/// shutter pulse width (in ms), range [0;1000.0]
	float m_pulse_width_ms;
} VRmSettings9;

VRM_EXTERN VRmRetVal VRM_API VRmUsbCamSetSettings9(VRmUsbCamDevice f_device,const VRmSettings9* fcp_settings);
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamGetSettings9(VRmUsbCamDevice f_device,VRmSettings9* fp_settings);

// ------------------------------------------------------------------------
// Miscellaneous Functions
// ------------------------------------------------------------------------

/// get free space in eeprom, length in bytes

/// can be used to distinguish old devices (8KB eeprom, ~0.5 to ~3kb free space)
/// and new devices (32KB eeprom and >24kb free space)
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamUserDataBytesFree(VRmUsbCamDevice f_device,VRmDWORD* fp_length);

/// register a callback function for the given device.
/// NOTE: a specific callback function pointer can only be registered once per device. 
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamRegisterDeviceCallback(VRmUsbCamDevice f_device, VRmDeviceCallback fp_callback, void* fp_user_data);

/// unregister a callback function for the given device
VRM_EXTERN VRmRetVal VRM_API VRmUsbCamUnregisterDeviceCallback(VRmUsbCamDevice f_device, VRmDeviceCallback fp_callback);

#if defined(__cplusplus) && !defined(VRM_NO_EXTERN_C)
};//extern "C"
#endif

#endif // VRMUSBCAM2L_H
