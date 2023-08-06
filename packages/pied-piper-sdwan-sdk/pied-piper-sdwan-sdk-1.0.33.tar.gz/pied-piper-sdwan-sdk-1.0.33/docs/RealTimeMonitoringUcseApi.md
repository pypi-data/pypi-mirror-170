# openapi_client.RealTimeMonitoringUcseApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ucse_stats**](RealTimeMonitoringUcseApi.md#create_ucse_stats) | **GET** /device/ucse/stats | 


# **create_ucse_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_ucse_stats(device_id)



Get  UCSE stats entry from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ucse_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ucse_api.RealTimeMonitoringUcseApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_tloc_address = "remote-tloc-address_example" # str | Remote TLOC address (optional)
    remote_tloc_color = "default" # str | Remote tloc color (optional)
    local_tloc_color = "default" # str | Local tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ucse_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringUcseApi->create_ucse_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_ucse_stats(device_id, remote_tloc_address=remote_tloc_address, remote_tloc_color=remote_tloc_color, local_tloc_color=local_tloc_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringUcseApi->create_ucse_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_tloc_address** | **str**| Remote TLOC address | [optional]
 **remote_tloc_color** | **str**| Remote tloc color | [optional]
 **local_tloc_color** | **str**| Local tloc color | [optional]

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

