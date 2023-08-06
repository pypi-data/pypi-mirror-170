# openapi_client.RealTimeMonitoringDeviceApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ipv6_data**](RealTimeMonitoringDeviceApi.md#get_ipv6_data) | **GET** /device/ipv6/nd6 | 


# **get_ipv6_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ipv6_data(device_id)



Get ipv6 data from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_api
from openapi_client.model.device_ip import DeviceIP
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_api.RealTimeMonitoringDeviceApi(api_client)
    device_id = DeviceIP(
        device_ip="device_ip_example",
    ) # DeviceIP | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ipv6_data(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceApi->get_ipv6_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **DeviceIP**| Device Id |

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

