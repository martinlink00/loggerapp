// ==============================================================================================
/// @file vrmusbcam2props.h                         VRmUsbCam C API Property Identifiers v3.5.0.0
//  Copyright VRmagic 2004-2014
// ==============================================================================================

#ifndef VRMUSBCAM2PROPS_H
#define VRMUSBCAM2PROPS_H

#ifndef VRM_PROPID
#define VRM_PROPID(name) VRM_PROPID_##name
#endif

#ifndef VRM_DEFINE_PROPID_ENUM
#define VRM_DEFINE_PROPID_ENUM typedef enum _VRmPropId
#endif

VRM_DEFINE_PROPID_ENUM {

	VRM_PROPID(CAM_EXPOSURE_TIME_F) = 0x1001,
	VRM_PROPID(CAM_AUTO_EXPOSURE_B) = 0x1003,
	VRM_PROPID(CAM_AUTO_EXPOSURE_MAX_F),

	VRM_PROPID(CAM_SIGNAL_SOURCE_E) = 0x1009,
	VRM_PROPID(CAM_SIGNAL_SOURCE_UNKNOWN) = 0x10090000,
	VRM_PROPID(CAM_SIGNAL_SOURCE_SVIDEO),
	VRM_PROPID(CAM_SIGNAL_SOURCE_COMPOSITE),
	VRM_PROPID(CAM_SIGNAL_SOURCE_YC),

	VRM_PROPID(CAM_FRAMERATE_MAX_F) = 0x100A,
	VRM_PROPID(CAM_EXPOSURE_TIME1_F),

	VRM_PROPID(CAM_EXPOSURE_OFFSET0_ODD_LINE_F) = 0x100C,
	VRM_PROPID(CAM_EXPOSURE_OFFSET1_ODD_LINE_F),

	VRM_PROPID(CAM_ACQUISITION_RATE_MAX_F) = 0x100E,
	VRM_PROPID(CAM_AUTO_EXPOSURE_TARGET_LUMA_I) = 0x100F,

	VRM_PROPID(CAM_HBLANK_DURATION_I) = 0x1010,
	VRM_PROPID(CAM_VBLANK_DURATION_I),
	VRM_PROPID(CAM_TRG2EXP_TIME_F),

	VRM_PROPID(CAM_EXP2VS_TIME_F) = 0x1014,
	VRM_PROPID(CAM_ROW_TIME_F),

	VRM_PROPID(CAM_GAIN_RED_I) = 0x1020,
	VRM_PROPID(CAM_GAIN_GREEN_I),
	VRM_PROPID(CAM_GAIN_BLUE_I),
	VRM_PROPID(CAM_GAIN_MONOCHROME_I),
	VRM_PROPID(CAM_AUTO_GAIN_B),
	VRM_PROPID(CAM_AUTO_GAIN_MAX_I),
	VRM_PROPID(CAM_OFFSET_RED_I),
	VRM_PROPID(CAM_OFFSET_GREEN_I),
	VRM_PROPID(CAM_OFFSET_BLUE_I),
	VRM_PROPID(CAM_BRIGHTNESS_I),
	VRM_PROPID(CAM_CONTRAST_I),
	VRM_PROPID(CAM_SATURATION_I),
	VRM_PROPID(CAM_HUE_I),

	VRM_PROPID(CAM_ANTI_BLOOMING_B) = 0x1030,
	VRM_PROPID(CAM_ANTI_BLOOMING_VOLTAGE_F),
	VRM_PROPID(CAM_DARK_OFFSET_B),
	VRM_PROPID(CAM_DARK_OFFSET_VOLTAGE_F),

	VRM_PROPID(CAM_SENSOR_SIZE_I) = 0x1040,

	VRM_PROPID(CAM_MONOCHROME_MODE_B) = 0x1042,
	VRM_PROPID(CAM_GLOBAL_SHUTTER_B),
	VRM_PROPID(CAM_VIDEO_STANDARD_E) = 0x1044,
	VRM_PROPID(CAM_VIDEO_STANDARD_UNKNOWN) = 0x10440000,
	VRM_PROPID(CAM_VIDEO_STANDARD_PAL),
	VRM_PROPID(CAM_VIDEO_STANDARD_NTSC),
	VRM_PROPID(CAM_DEVICE_TYPE_E) = 0x1045,
	VRM_PROPID(CAM_DEVICE_TYPE_CMOS) = 0x10450000,
	VRM_PROPID(CAM_DEVICE_TYPE_CCD),
	VRM_PROPID(CAM_DEVICE_TYPE_AVC),
	VRM_PROPID(CAM_READOUT_FLIP_H_B) = 0x1046,
	VRM_PROPID(CAM_READOUT_FLIP_V_B),

	VRM_PROPID(CAM_HIGH_DYNAMIC_MODE_B) = 0x1050,
	VRM_PROPID(CAM_HIDYN_KNEE_COUNT_I),
	VRM_PROPID(CAM_HIDYN_AUTO_RATIO_B),
	VRM_PROPID(CAM_HIDYN_AUTO_RATIO1_I),
	VRM_PROPID(CAM_HIDYN_AUTO_RATIO2_I),
	VRM_PROPID(CAM_HIDYN_AUTO_RATIO3_I),
	VRM_PROPID(CAM_HIDYN_AUTO_RATIO4_I),
	VRM_PROPID(CAM_HIDYN_EXPOSURE_KNEE1_F),
	VRM_PROPID(CAM_HIDYN_EXPOSURE_KNEE2_F),
	VRM_PROPID(CAM_HIDYN_EXPOSURE_KNEE3_F),
	VRM_PROPID(CAM_HIDYN_EXPOSURE_KNEE4_F),
	VRM_PROPID(CAM_HIDYN_STEP_VOLTAGE1_F),
	VRM_PROPID(CAM_HIDYN_STEP_VOLTAGE2_F),
	VRM_PROPID(CAM_HIDYN_STEP_VOLTAGE3_F),
	VRM_PROPID(CAM_HIDYN_STEP_VOLTAGE4_F),

	VRM_PROPID(CAM_TEMPERATURE_F) = 0x1060,
	VRM_PROPID(CAM_HIDYN_STEP_VOLTAGE1_RAW_I),
	VRM_PROPID(CAM_HIDYN_STEP_VOLTAGE2_RAW_I),
	VRM_PROPID(CAM_HIDYN_STEP_VOLTAGE3_RAW_I),
	VRM_PROPID(CAM_HIDYN_STEP_VOLTAGE4_RAW_I),

	VRM_PROPID(CAM_VREF1_ADJUST_I) = 0x1070,
	VRM_PROPID(CAM_AUTO_BLACKLEVEL_B),
	VRM_PROPID(CAM_BLACKLEVEL_ADJUST_I),

	VRM_PROPID(CAM_VREF1_VOLTAGE_F) = 0x1080,
	VRM_PROPID(CAM_VREF2_VOLTAGE_F),
	VRM_PROPID(CAM_VREF3_VOLTAGE_F),
	VRM_PROPID(CAM_VREF4_VOLTAGE_F),

	VRM_PROPID(CAM_VLN1_VOLTAGE_F) = 0x1090,
	VRM_PROPID(CAM_VLN2_VOLTAGE_F),

	VRM_PROPID(CAM_VLP_VOLTAGE_F) = 0x10A0,

	VRM_PROPID(CAM_VRST_PIX_VOLTAGE_F) = 0x10B0,

	VRM_PROPID(CAM_RESET_LEVEL_ADJ_I) = 0x1500,
	VRM_PROPID(CAM_PIXEL_BIAS_ADJ_I),
	VRM_PROPID(CAM_VBLANK_DURATION_PIXELS_I),

	VRM_PROPID(CAM_GAIN_DOUBLING_B) = 0x1600,

	VRM_PROPID(CAM_AUTO_EXPOSURE_BRIGHT_THRESHOLD_I) = 0x1701,
	VRM_PROPID(CAM_AUTO_EXPOSURE_BRIGHT_PERCENTAGE_F),

	VRM_PROPID(CAM_CMOSIS_EXPOSURE_TIME_ALTERNATING_B) = 0x1A00,
	VRM_PROPID(CAM_CMOSIS_ADC_GAIN_I),
	VRM_PROPID(CAM_CMOSIS_VRAMP1_I),
	VRM_PROPID(CAM_CMOSIS_VRAMP2_I),
	VRM_PROPID(CAM_CMOSIS_TEMP_RAW_I),

	VRM_PROPID(CAM_MSARE1_GAIN_F) = 0x1B00,
	VRM_PROPID(CAM_MSARE1_REFERENCE_VOLTAGE_F),

	// MT9M021/AR0134-specific
	VRM_PROPID(CAM_EMBEDDED_SENSOR_REGISTER_LINES_ENABLE_B) = 0x1c00,
	VRM_PROPID(CAM_EMBEDDED_AE_STATISTICS_LINES_ENABLE_B) = 0x1c01,

	VRM_PROPID(DEVICE_HARDWARE_REVISION_I) = 0x2000,
	VRM_PROPID(DEVICE_FIRMWARE_REVISION_I),
	VRM_PROPID(DEVICE_NV_MEM_TOTAL_I),
	VRM_PROPID(DEVICE_NV_MEM_FREE_I),
	VRM_PROPID(DEVICE_NV_MEM_FILESYS_FORMAT_B),
	VRM_PROPID(DEVICE_FIRMWARE_COMPRESSED_B),
	VRM_PROPID(DEVICE_USB_HIGH_SPEED_B),
	VRM_PROPID(DEVICE_USB_STARTUP_HIGH_SPEED_B),
	VRM_PROPID(DEVICE_STATUS_LED_B),

	VRM_PROPID(CAM_PIXEL_CLOCK_F) = 0x2100,
	VRM_PROPID(CAM_REFERENCE_FREQ_ADJ_I),
	VRM_PROPID(CAM_AUTO_PIXEL_CLOCK_B),
	VRM_PROPID(CAM_ALLOW_OVERCLOCKING_B),

	VRM_PROPID(CAM_ILLUMINATION_INTENSITY_F) = 0x2110,

	VRM_PROPID(CAM_TRIGGER_POLARITY_E) = 0x2120,
	VRM_PROPID(CAM_TRIGGER_POLARITY_POS_EDGE) = 0x21200000,
	VRM_PROPID(CAM_TRIGGER_POLARITY_NEG_EDGE),
	VRM_PROPID(CAM_TRIGGER_POLARITY_POS_LEVEL),
	VRM_PROPID(CAM_TRIGGER_POLARITY_NEG_LEVEL),

	VRM_PROPID(CAM_TRIGGER_DELAY_F) = 0x2121,
	VRM_PROPID(CAM_INTERNAL_TRIGGER_RATE_F) = 0x2123,
	VRM_PROPID(CAM_TRIGGER_BURST_COUNT_I),

	VRM_PROPID(CAM_TRIGGER_EXPOSURE_REDUCTION_I) = 0x2127,

	VRM_PROPID(CAM_LAST_EXTERNAL_TRIGGER_TIMESTAMP_D) = 0x212A,
	VRM_PROPID(CAM_TRIGGER_MSARE1_RRO_BURST_COUNT_I) = 0x212C,
	VRM_PROPID(CAM_TRIGGER_MSARE1_RRO_DELAY_F),

	VRM_PROPID(CAM_STROBE_POLARITY_E) = 0x2130,
	VRM_PROPID(CAM_STROBE_POLARITY_DISABLED) = 0x21300000,
	VRM_PROPID(CAM_STROBE_POLARITY_POS),
	VRM_PROPID(CAM_STROBE_POLARITY_NEG),

	VRM_PROPID(CAM_STROBE_DELAY_F) = 0x2131,
	VRM_PROPID(CAM_STROBE_WIDTH_F),
	VRM_PROPID(CAM_STROBE_ILLUMINATION_B),
	VRM_PROPID(CAM_STROBE_BURST_COUNT_I),
	VRM_PROPID(CAM_STROBE_OUT_REDUCTION_I) = 0x2139,

	VRM_PROPID(GRAB_SOURCE_FORMAT_E) = 0x3000,
	VRM_PROPID(GRAB_SOURCE_FORMAT_8BIT_RAW) = 0x30000000,
	VRM_PROPID(GRAB_SOURCE_FORMAT_16BIT_RAW),
	VRM_PROPID(GRAB_SOURCE_FORMAT_8BIT_RLE),

	VRM_PROPID(GRAB_READOUT_ORIGIN_POINT_I) = 0x3001,
	VRM_PROPID(GRAB_HOST_RINGBUFFER_SIZE_I),
	VRM_PROPID(GRAB_FRAMERATE_AVERAGE_F),
	VRM_PROPID(GRAB_FRAMERATE_ESTIMATED_F),
	VRM_PROPID(GRAB_HOST_RINGBUFFER_IMAGES_READY_I),
	VRM_PROPID(GRAB_CONFIG_E) = 0x3006,
	VRM_PROPID(GRAB_CONFIG_FACTORY_DEFAULTS) = 0x30060000,
	VRM_PROPID(GRAB_CONFIG_USER_DEFAULTS),
	VRM_PROPID(GRAB_CONFIG_2),
	VRM_PROPID(GRAB_CONFIG_3),
	VRM_PROPID(GRAB_CONFIG_4),
	VRM_PROPID(GRAB_CONFIG_5),
	VRM_PROPID(GRAB_CONFIG_6),
	VRM_PROPID(GRAB_CONFIG_7),
	VRM_PROPID(GRAB_CONFIG_8),
	VRM_PROPID(GRAB_CONFIG_9),

	VRM_PROPID(GRAB_CONFIG_DESCRIPTION_S) = 0x3007,
	VRM_PROPID(GRAB_DATARATE_AVERAGE_I),
	VRM_PROPID(GRAB_SYNC_FREERUN_JITTER_F),

	VRM_PROPID(GRAB_USER_ROI_RECT_I) = 0x3010,
	VRM_PROPID(GRAB_DEVICE_RINGBUFFER_IMAGES_READY_I),
	VRM_PROPID(GRAB_DEVICE_RINGBUFFER_SIZE_I),

	VRM_PROPID(GRAB_DEVICE_RAMGRAB_MODE_E) = 0x3014,
	VRM_PROPID(GRAB_DEVICE_RAMGRAB_MODE_BUFFERING) = 0x30140000,
	VRM_PROPID(GRAB_DEVICE_RAMGRAB_MODE_BUFFERING_DT),
	VRM_PROPID(GRAB_DEVICE_RAMGRAB_MODE_LOW_LATENCY),
	VRM_PROPID(GRAB_DEVICE_RAMGRAB_MODE_LOW_LATENCY_DT),

	VRM_PROPID(GRAB_DEVICE_MULTIFRAME_COUNT_I) = 0x3039,
	VRM_PROPID(GRAB_FPGA_GLOBAL_LUT_DISABLE_B),

	VRM_PROPID(GRAB_MODE_E) = 0x3080,
	VRM_PROPID(GRAB_MODE_FREERUNNING) = 0x30800000,
	VRM_PROPID(GRAB_MODE_TRIGGERED_EXT),
	VRM_PROPID(GRAB_MODE_TRIGGERED_SOFT),
	VRM_PROPID(GRAB_MODE_TRIGGERED_SOFT_EXT),
	VRM_PROPID(GRAB_MODE_FREERUNNING_SEQUENTIAL),
	VRM_PROPID(GRAB_MODE_SYNCHRONIZED_FREERUNNING),
	VRM_PROPID(GRAB_MODE_TRIGGERED_INTERNAL),

	VRM_PROPID(GRAB_TRIGGER_TIMEOUT_F) = 0x3081,

	VRM_PROPID(GRAB_SENSOR_PROPS_SELECT_E) = 0x3090,
	VRM_PROPID(GRAB_SENSOR_PROPS_SELECT_1) = 0x30900001,
	VRM_PROPID(GRAB_SENSOR_PROPS_SELECT_2),
	VRM_PROPID(GRAB_SENSOR_PROPS_SELECT_3),
	VRM_PROPID(GRAB_SENSOR_PROPS_SELECT_4),
	VRM_PROPID(GRAB_SENSOR_PROPS_SELECT_5),
	VRM_PROPID(GRAB_SENSOR_PROPS_SELECT_6),

	VRM_PROPID(GRAB_SENSOR_ENABLE_1_B) = 0x3091,
	VRM_PROPID(GRAB_SENSOR_ENABLE_2_B),
	VRM_PROPID(GRAB_SENSOR_ENABLE_3_B),
	VRM_PROPID(GRAB_SENSOR_ENABLE_4_B),
	VRM_PROPID(GRAB_SENSOR_ENABLE_5_B),
	VRM_PROPID(GRAB_SENSOR_ENABLE_6_B),

	VRM_PROPID(GRAB_AVC_FIELD_SELECT_E) = 0x30A0,
	VRM_PROPID(GRAB_AVC_FIELD_SELECT_TOP) = 0x30A00000,
	VRM_PROPID(GRAB_AVC_FIELD_SELECT_BOTTOM),
	VRM_PROPID(GRAB_AVC_FIELD_REDUCTION_E) = 0x30A1,
	VRM_PROPID(GRAB_AVC_FIELD_REDUCTION_OFF) = 0x30A10000,
	VRM_PROPID(GRAB_AVC_FIELD_REDUCTION_ON),
	VRM_PROPID(GRAB_AVC_READOUT_E) = 0x30A2,
	VRM_PROPID(GRAB_AVC_READOUT_FIELD) = 0x30A20000,
	VRM_PROPID(GRAB_AVC_READOUT_FRAME),
	VRM_PROPID(GRAB_AVC_READOUT_PROGRESSIVE_FRAME),

	VRM_PROPID(GRAB_YUV_BYTE_ORDER_E) = 0x30A5,
	VRM_PROPID(GRAB_YUV_BYTE_ORDER_YUYV) = 0x30A50000,
	VRM_PROPID(GRAB_YUV_BYTE_ORDER_UYVY),

	VRM_PROPID(FILTER_MASTER_GAMMA_F) = 0x3100,
	VRM_PROPID(FILTER_MASTER_LUMINANCE_I),
	VRM_PROPID(FILTER_MASTER_CONTRAST_F),
	VRM_PROPID(FILTER_MASTER_BLACKLEVEL_I),

	VRM_PROPID(FILTER_ALAW_COMPENSATION_B) = 0x3108,

	VRM_PROPID(FILTER_RED_GAMMA_F) = 0x3110,
	VRM_PROPID(FILTER_RED_LUMINANCE_I),
	VRM_PROPID(FILTER_RED_CONTRAST_F),

	VRM_PROPID(FILTER_GREEN_GAMMA_F) = 0x3120,
	VRM_PROPID(FILTER_GREEN_LUMINANCE_I),
	VRM_PROPID(FILTER_GREEN_CONTRAST_F),

	VRM_PROPID(FILTER_BLUE_GAMMA_F) = 0x3130,
	VRM_PROPID(FILTER_BLUE_LUMINANCE_I),
	VRM_PROPID(FILTER_BLUE_CONTRAST_F),

	VRM_PROPID(PLUGIN_AUTO_EXPOSURE_B) = 0x3200,
	VRM_PROPID(PLUGIN_AUTO_EXPOSURE_MAX_F),
	VRM_PROPID(PLUGIN_AUTO_EXPOSURE_TARGET_MEAN_VALUE_I),
	VRM_PROPID(PLUGIN_AUTO_EXPOSURE_TARGET_MEAN_VALUE_TOLERANCE_I),
	VRM_PROPID(PLUGIN_AUTO_EXPOSURE_ROI_RECT_I),

	VRM_PROPID(PLUGIN_AUTO_RESET_LEVEL_B) = 0x3210,

	VRM_PROPID(PLUGIN_AUTO_WHITE_BALANCE_FILTER_B) = 0x3220,
	VRM_PROPID(PLUGIN_AUTO_WHITE_BALANCE_GAINS_B),
	VRM_PROPID(PLUGIN_AUTO_WHITE_BALANCE_ROI_RECT_I),

	VRM_PROPID(PLUGIN_AUTO_CHANNEL_BALANCE_FILTER_B) = 0x3228,

	VRM_PROPID(PLUGIN_IMAGE_PROCESSING_B) = 0x3500,

	VRM_PROPID(CONVERTER_BAYER_HQ_B) = 0x4000,
	VRM_PROPID(CONVERTER_FLIP_H_B),
	VRM_PROPID(CONVERTER_FLIP_V_B),
	VRM_PROPID(CONVERTER_PREFER_GRAY_OUTPUT_B),

	VRM_PROPID(IMAGEPROC_DPM_B) = 0x4100,

	VRM_PROPID(ETHCAM_SERVER_RINGBUFFER_SIZE_I) = 0x5100,
	VRM_PROPID(ETHCAM_SERVER_MTU_I),

	VRM_PROPID(DAV_WAIT_FOR_STROBE_E) = 0x5900,

	VRM_PROPID(DAV_WAIT_FOR_STROBE_DISABLE)= 0x59000001,
	VRM_PROPID(DAV_WAIT_FOR_STROBE_EDGE_RISING),
	VRM_PROPID(DAV_WAIT_FOR_STROBE_EDGE_FALLING)

} VRmPropId;

#endif//VRMUSBCAM2PROPS_H
