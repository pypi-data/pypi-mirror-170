# openapi_client.RealTimeMonitoringRebootHistoryApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reboot_history_list**](RealTimeMonitoringRebootHistoryApi.md#create_reboot_history_list) | **GET** /device/reboothistory | 
[**create_synced_reboot_history_list**](RealTimeMonitoringRebootHistoryApi.md#create_synced_reboot_history_list) | **GET** /device/reboothistory/synced | 
[**get_reboot_history_details**](RealTimeMonitoringRebootHistoryApi.md#get_reboot_history_details) | **GET** /device/reboothistory/details | 


# **create_reboot_history_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_reboot_history_list(device_id)



Get device reboot history

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_reboot_history_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_reboot_history_api.RealTimeMonitoringRebootHistoryApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_reboot_history_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringRebootHistoryApi->create_reboot_history_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_synced_reboot_history_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_synced_reboot_history_list(device_id)



Get device reboot history synchronously

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_reboot_history_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_reboot_history_api.RealTimeMonitoringRebootHistoryApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_synced_reboot_history_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringRebootHistoryApi->create_synced_reboot_history_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reboot_history_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_reboot_history_details()



Get detailed reboot history list

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_reboot_history_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_reboot_history_api.RealTimeMonitoringRebootHistoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_reboot_history_details()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringRebootHistoryApi->get_reboot_history_details: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

