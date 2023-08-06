# openapi_client.RealTimeMonitoringApplicationAwareRouteApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_route_sla_class_list**](RealTimeMonitoringApplicationAwareRouteApi.md#create_app_route_sla_class_list) | **GET** /device/app-route/sla-class | 
[**create_app_route_statistics_list**](RealTimeMonitoringApplicationAwareRouteApi.md#create_app_route_statistics_list) | **GET** /device/app-route/statistics | 


# **create_app_route_sla_class_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_app_route_sla_class_list(device_id)



Get SLA class list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_application_aware_route_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_application_aware_route_api.RealTimeMonitoringApplicationAwareRouteApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_app_route_sla_class_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringApplicationAwareRouteApi->create_app_route_sla_class_list: %s\n" % e)
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

# **create_app_route_statistics_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_app_route_statistics_list(device_id)



Get application-aware routing statistics from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_application_aware_route_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_application_aware_route_api.RealTimeMonitoringApplicationAwareRouteApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_system_ip = "remote-system-ip_example" # str | Remote system IP (optional)
    local_color = "default" # str | Local color (optional)
    remote_color = "default" # str | Remote color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_app_route_statistics_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringApplicationAwareRouteApi->create_app_route_statistics_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_app_route_statistics_list(device_id, remote_system_ip=remote_system_ip, local_color=local_color, remote_color=remote_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringApplicationAwareRouteApi->create_app_route_statistics_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_system_ip** | **str**| Remote system IP | [optional]
 **local_color** | **str**| Local color | [optional]
 **remote_color** | **str**| Remote color | [optional]

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

