import math


class Constants:
	HEADERS = {
		'AUTH_TYPE': 'authType',
		'SDK_ID': 'sdkId',
		'SDK_SECRET': 'sdkSecret'
	}
	BASE_URL = 'https://app-apis.flagsense.com/v1/sdk-service/'
	EVENTS_BASE_URL = 'https://app-events.flagsense.com/v1/events-service/'
	
	ENVIRONMENTS = ['DEV', 'STAGE', 'PROD']
	MAX_HASH_VALUE = math.pow(2, 32)
	TOTAL_THREE_DECIMAL_TRAFFIC = 100000
	DATA_REFRESH_INTERVAL = 60
	CAPTURE_EVENTS_FLAG = True
	EVENT_FLUSH_INITIAL_DELAY = 2 * 60
	EVENT_FLUSH_INTERVAL = 5 * 60
	MAX_INITIALIZATION_WAIT_TIME = 60
