# openapi_client.RealTimeMonitoringIGMPApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_igmp_groups_list**](RealTimeMonitoringIGMPApi.md#create_igmp_groups_list) | **GET** /device/igmp/groups | 
[**create_igmp_interface_list**](RealTimeMonitoringIGMPApi.md#create_igmp_interface_list) | **GET** /device/igmp/interface | 
[**create_igmp_statistics_list**](RealTimeMonitoringIGMPApi.md#create_igmp_statistics_list) | **GET** /device/igmp/statistics | 
[**create_igmp_summary**](RealTimeMonitoringIGMPApi.md#create_igmp_summary) | **GET** /device/igmp/summary | 


# **create_igmp_groups_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_igmp_groups_list(device_id)



Get IGMP neighbor list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_igmp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_igmp_api.RealTimeMonitoringIGMPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_igmp_groups_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIGMPApi->create_igmp_groups_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **create_igmp_interface_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_igmp_interface_list(device_id)



Get IGMP interface list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_igmp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_igmp_api.RealTimeMonitoringIGMPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_igmp_interface_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIGMPApi->create_igmp_interface_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **create_igmp_statistics_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_igmp_statistics_list(device_id)



Get IGMP statistics list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_igmp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_igmp_api.RealTimeMonitoringIGMPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_igmp_statistics_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIGMPApi->create_igmp_statistics_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **create_igmp_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_igmp_summary(device_id)



Get IGMP summary from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_igmp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_igmp_api.RealTimeMonitoringIGMPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_igmp_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIGMPApi->create_igmp_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

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

