# openapi_client.RealTimeMonitoringDREApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dre_auto_bypass_stats**](RealTimeMonitoringDREApi.md#get_dre_auto_bypass_stats) | **GET** /device/dre/auto-bypass-stats | 
[**get_dre_peer_stats**](RealTimeMonitoringDREApi.md#get_dre_peer_stats) | **GET** /device/dre/peer-stats | 
[**get_dre_stats**](RealTimeMonitoringDREApi.md#get_dre_stats) | **GET** /device/dre/dre-stats | 
[**get_dre_status**](RealTimeMonitoringDREApi.md#get_dre_status) | **GET** /device/dre/dre-status | 


# **get_dre_auto_bypass_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dre_auto_bypass_stats(device_id)



Get DRE auto-bypass statistics

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dre_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dre_api.RealTimeMonitoringDREApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    appqoe_dre_auto_bypass_server_ip = "00r252U250?250" # str | Server IP (optional)
    appqoe_dre_auto_bypass_port = 3.14 # float | Port (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dre_auto_bypass_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDREApi->get_dre_auto_bypass_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_dre_auto_bypass_stats(device_id, appqoe_dre_auto_bypass_server_ip=appqoe_dre_auto_bypass_server_ip, appqoe_dre_auto_bypass_port=appqoe_dre_auto_bypass_port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDREApi->get_dre_auto_bypass_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **appqoe_dre_auto_bypass_server_ip** | **str**| Server IP | [optional]
 **appqoe_dre_auto_bypass_port** | **float**| Port | [optional]

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

# **get_dre_peer_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dre_peer_stats(device_id)



Get DRE peer statistics

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dre_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dre_api.RealTimeMonitoringDREApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    appqoe_dre_stats_peer_system_ip = "00r252U250?250" # str | System IP (optional)
    appqoe_dre_stats_peer_peer_no = 3.14 # float | Peer Number (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dre_peer_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDREApi->get_dre_peer_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_dre_peer_stats(device_id, appqoe_dre_stats_peer_system_ip=appqoe_dre_stats_peer_system_ip, appqoe_dre_stats_peer_peer_no=appqoe_dre_stats_peer_peer_no)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDREApi->get_dre_peer_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **appqoe_dre_stats_peer_system_ip** | **str**| System IP | [optional]
 **appqoe_dre_stats_peer_peer_no** | **float**| Peer Number | [optional]

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

# **get_dre_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dre_stats(device_id)



Get DRE statistics

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dre_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dre_api.RealTimeMonitoringDREApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dre_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDREApi->get_dre_stats: %s\n" % e)
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

# **get_dre_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dre_status(device_id)



Get DRE status

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dre_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dre_api.RealTimeMonitoringDREApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_dre_status(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDREApi->get_dre_status: %s\n" % e)
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

