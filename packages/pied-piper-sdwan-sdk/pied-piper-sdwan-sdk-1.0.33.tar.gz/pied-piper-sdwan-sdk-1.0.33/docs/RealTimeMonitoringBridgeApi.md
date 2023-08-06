# openapi_client.RealTimeMonitoringBridgeApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bridge_interface_list**](RealTimeMonitoringBridgeApi.md#get_bridge_interface_list) | **GET** /device/bridge/interface | 
[**get_bridge_interface_mac**](RealTimeMonitoringBridgeApi.md#get_bridge_interface_mac) | **GET** /device/bridge/mac | 
[**get_bridge_interface_table**](RealTimeMonitoringBridgeApi.md#get_bridge_interface_table) | **GET** /device/bridge/table | 


# **get_bridge_interface_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bridge_interface_list(device_id)



Get device bridge interface list (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bridge_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bridge_api.RealTimeMonitoringBridgeApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_bridge_interface_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBridgeApi->get_bridge_interface_list: %s\n" % e)
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

# **get_bridge_interface_mac**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bridge_interface_mac(device_id)



Get device bridge interface MAC (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bridge_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bridge_api.RealTimeMonitoringBridgeApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    bridge_id = "bridge-id_example" # str | Bridge ID (optional)
    if_name = "ge0/0" # str | Interface name (optional)
    mac_address = "mac-address_example" # str | MAC address (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_bridge_interface_mac(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBridgeApi->get_bridge_interface_mac: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_bridge_interface_mac(device_id, bridge_id=bridge_id, if_name=if_name, mac_address=mac_address)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBridgeApi->get_bridge_interface_mac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **bridge_id** | **str**| Bridge ID | [optional]
 **if_name** | **str**| Interface name | [optional]
 **mac_address** | **str**| MAC address | [optional]

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

# **get_bridge_interface_table**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bridge_interface_table(device_id)



Get device bridge interface table (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bridge_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bridge_api.RealTimeMonitoringBridgeApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_bridge_interface_table(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBridgeApi->get_bridge_interface_table: %s\n" % e)
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

