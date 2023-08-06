# openapi_client.RealTimeMonitoringIPv6FIBApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ipv6_fib_list**](RealTimeMonitoringIPv6FIBApi.md#create_ipv6_fib_list) | **GET** /device/ip/v6fib | 


# **create_ipv6_fib_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_ipv6_fib_list(device_id)



Get IPv6 FIB list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ipv6_fib_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ipv6_fib_api.RealTimeMonitoringIPv6FIBApi(api_client)
    device_id = "00r252U250?250" # str | Device Id
    vpn_id = "0" # str | VPN Id (optional)
    prefix = "prefix_example" # str | IP prefix (optional)
    tloc = "tloc_example" # str | tloc IP (optional)
    color = "default" # str | tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ipv6_fib_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPv6FIBApi->create_ipv6_fib_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_ipv6_fib_list(device_id, vpn_id=vpn_id, prefix=prefix, tloc=tloc, color=color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPv6FIBApi->create_ipv6_fib_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **prefix** | **str**| IP prefix | [optional]
 **tloc** | **str**| tloc IP | [optional]
 **color** | **str**| tloc color | [optional]

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

