# openapi_client.RealTimeMonitoringIPv6NeighboursApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ipv6_interface**](RealTimeMonitoringIPv6NeighboursApi.md#get_ipv6_interface) | **GET** /device/ndv6 | 


# **get_ipv6_interface**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ipv6_interface(device_id)



Get IPv6 Neighbors from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ipv6_neighbours_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ipv6_neighbours_api.RealTimeMonitoringIPv6NeighboursApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    vpn_id = "0" # str | VPN Id (optional)
    if_name = "ge0/0" # str | Interface name (optional)
    mac = "mac_example" # str | Mac address (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ipv6_interface(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPv6NeighboursApi->get_ipv6_interface: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ipv6_interface(device_id, vpn_id=vpn_id, if_name=if_name, mac=mac)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPv6NeighboursApi->get_ipv6_interface: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **vpn_id** | **str**| VPN Id | [optional]
 **if_name** | **str**| Interface name | [optional]
 **mac** | **str**| Mac address | [optional]

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

