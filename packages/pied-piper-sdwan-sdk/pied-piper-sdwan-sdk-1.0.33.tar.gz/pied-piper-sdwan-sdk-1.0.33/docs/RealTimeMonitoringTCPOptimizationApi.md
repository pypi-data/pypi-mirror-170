# openapi_client.RealTimeMonitoringTCPOptimizationApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_tcp_flows**](RealTimeMonitoringTCPOptimizationApi.md#get_active_tcp_flows) | **GET** /device/tcpopt/activeflows | 
[**get_expired_tcp_flows**](RealTimeMonitoringTCPOptimizationApi.md#get_expired_tcp_flows) | **GET** /device/tcpopt/expiredflows | 
[**get_tcp_summary**](RealTimeMonitoringTCPOptimizationApi.md#get_tcp_summary) | **GET** /device/tcpopt/summary | 


# **get_active_tcp_flows**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_active_tcp_flows(device_id)



Get TCP optimized active flows from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_tcp_optimization_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_tcp_optimization_api.RealTimeMonitoringTCPOptimizationApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_active_tcp_flows(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringTCPOptimizationApi->get_active_tcp_flows: %s\n" % e)
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

# **get_expired_tcp_flows**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_expired_tcp_flows(device_id)



Get TCP optimized expired flows from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_tcp_optimization_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_tcp_optimization_api.RealTimeMonitoringTCPOptimizationApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_expired_tcp_flows(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringTCPOptimizationApi->get_expired_tcp_flows: %s\n" % e)
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

# **get_tcp_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_tcp_summary(device_id)



Get TCP optimization summary from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_tcp_optimization_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_tcp_optimization_api.RealTimeMonitoringTCPOptimizationApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tcp_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringTCPOptimizationApi->get_tcp_summary: %s\n" % e)
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

