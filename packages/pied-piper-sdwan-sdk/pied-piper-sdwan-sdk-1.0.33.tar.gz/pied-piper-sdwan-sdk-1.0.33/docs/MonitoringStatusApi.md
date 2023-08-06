# openapi_client.MonitoringStatusApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_disabled_device_list**](MonitoringStatusApi.md#get_disabled_device_list) | **GET** /statistics/settings/disable/devicelist/{indexName} | 
[**get_enabled_index_for_device**](MonitoringStatusApi.md#get_enabled_index_for_device) | **GET** /statistics/settings/status/device | 
[**get_statistics_settings**](MonitoringStatusApi.md#get_statistics_settings) | **GET** /statistics/settings/status | 
[**update_statistics_device_list**](MonitoringStatusApi.md#update_statistics_device_list) | **PUT** /statistics/settings/disable/devicelist/{indexName} | 
[**update_statistics_settings**](MonitoringStatusApi.md#update_statistics_settings) | **PUT** /statistics/settings/status | 


# **get_disabled_device_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_disabled_device_list(index_name)



Get list of disabled devices for a statistics index

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_status_api.MonitoringStatusApi(api_client)
    index_name = "indexName_example" # str | Index name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_disabled_device_list(index_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatusApi->get_disabled_device_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Index name |

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

# **get_enabled_index_for_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_enabled_index_for_device(device_id)



Get list of enabled device for statistics index

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_status_api.MonitoringStatusApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_enabled_index_for_device(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatusApi->get_enabled_index_for_device: %s\n" % e)
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

# **get_statistics_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_statistics_settings()



Get statistics settings

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_status_api.MonitoringStatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_statistics_settings()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatusApi->get_statistics_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **update_statistics_device_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_statistics_device_list(index_name)



Update list of disabled devices for a statistics index

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_status_api.MonitoringStatusApi(api_client)
    index_name = "indexName_example" # str | Index name
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Disabled device (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_statistics_device_list(index_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatusApi->update_statistics_device_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_statistics_device_list(index_name, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatusApi->update_statistics_device_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| Index name |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Disabled device | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_statistics_settings**
> update_statistics_settings()



Update statistics settings

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_status_api.MonitoringStatusApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats setting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_statistics_settings(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatusApi->update_statistics_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats setting | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

