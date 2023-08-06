# openapi_client.SystemCloudServiceWebexApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webex_data_centers**](SystemCloudServiceWebexApi.md#delete_webex_data_centers) | **DELETE** /webex/datacenter | 
[**get_webex_data_centers**](SystemCloudServiceWebexApi.md#get_webex_data_centers) | **POST** /webex/datacenter | 
[**get_webex_data_centers_sync_status**](SystemCloudServiceWebexApi.md#get_webex_data_centers_sync_status) | **GET** /webex/datacenter/syncstatus | 
[**set_webex_data_centers_sync_status**](SystemCloudServiceWebexApi.md#set_webex_data_centers_sync_status) | **PUT** /webex/datacenter/syncstatus | 
[**update_webex_data_centers**](SystemCloudServiceWebexApi.md#update_webex_data_centers) | **POST** /webex/datacenter/sync | 


# **delete_webex_data_centers**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_webex_data_centers()



Delete webex data center data in DB

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_webex_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_webex_api.SystemCloudServiceWebexApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_webex_data_centers()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceWebexApi->delete_webex_data_centers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webex_data_centers**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_webex_data_centers()



TEMP-Insert webex data center details manually for test setup

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_webex_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_webex_api.SystemCloudServiceWebexApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_webex_data_centers(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceWebexApi->get_webex_data_centers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webex_data_centers_sync_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_webex_data_centers_sync_status()



Get webex data center sync status from DB

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_webex_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_webex_api.SystemCloudServiceWebexApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_webex_data_centers_sync_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceWebexApi->get_webex_data_centers_sync_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_webex_data_centers_sync_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_webex_data_centers_sync_status()



Set webex data center sync needed to false

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_webex_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_webex_api.SystemCloudServiceWebexApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.set_webex_data_centers_sync_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceWebexApi->set_webex_data_centers_sync_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webex_data_centers**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_webex_data_centers()



TEMP-Update webex data center data in DB with data from Webex API

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_webex_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_webex_api.SystemCloudServiceWebexApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.update_webex_data_centers()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceWebexApi->update_webex_data_centers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

