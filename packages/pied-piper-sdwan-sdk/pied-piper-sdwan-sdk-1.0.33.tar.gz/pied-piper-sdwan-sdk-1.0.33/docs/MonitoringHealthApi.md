# openapi_client.MonitoringHealthApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_devices_health**](MonitoringHealthApi.md#get_devices_health) | **GET** /health/devices | 
[**get_devices_health_overview**](MonitoringHealthApi.md#get_devices_health_overview) | **GET** /health/devices/overview | 


# **get_devices_health**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_devices_health()



gets page fo devices with health properties

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_health_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_health_api.MonitoringHealthApi(api_client)
    page = 1 # int | Page Number (optional)
    page_size = 1 # int | Page Size (optional)
    sort_by = "sortBy_example" # str | Sort By Property (optional)
    sort_order = "sortOrder_example" # str | Sort Order (optional)
    starting_device_id = "startingDeviceId_example" # str | Optional device ID to start first page (optional)
    site_id = "siteId_example" # str | Optional site ID to filter devices (optional)
    group_id = "group_id_example" # str | Optional group ID to filter devices (optional)
    group_id2 = "groupId_example" # str | Optional group ID to filter devices (optional)
    vpn_id = "vpnId_example" # str | Optional vpn ID to filter devices (optional)
    reachable = True # bool |  (optional)
    control_status = "controlStatus_example" # str |  (optional)
    personality = "personality_example" # str |  (optional)
    health = "health_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_devices_health(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, starting_device_id=starting_device_id, site_id=site_id, group_id=group_id, group_id2=group_id2, vpn_id=vpn_id, reachable=reachable, control_status=control_status, personality=personality, health=health)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringHealthApi->get_devices_health: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional]
 **page_size** | **int**| Page Size | [optional]
 **sort_by** | **str**| Sort By Property | [optional]
 **sort_order** | **str**| Sort Order | [optional]
 **starting_device_id** | **str**| Optional device ID to start first page | [optional]
 **site_id** | **str**| Optional site ID to filter devices | [optional]
 **group_id** | **str**| Optional group ID to filter devices | [optional]
 **group_id2** | **str**| Optional group ID to filter devices | [optional]
 **vpn_id** | **str**| Optional vpn ID to filter devices | [optional]
 **reachable** | **bool**|  | [optional]
 **control_status** | **str**|  | [optional]
 **personality** | **str**|  | [optional]
 **health** | **str**|  | [optional]

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

# **get_devices_health_overview**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_devices_health_overview()



gets devices health overview

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_health_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_health_api.MonitoringHealthApi(api_client)
    vpn_id = "vpn_id_example" # str | Optional vpn ID to filter devices (optional)
    vpn_id2 = "vpnId_example" # str | Optional vpn ID to filter devices (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_devices_health_overview(vpn_id=vpn_id, vpn_id2=vpn_id2)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringHealthApi->get_devices_health_overview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_id** | **str**| Optional vpn ID to filter devices | [optional]
 **vpn_id2** | **str**| Optional vpn ID to filter devices | [optional]

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

