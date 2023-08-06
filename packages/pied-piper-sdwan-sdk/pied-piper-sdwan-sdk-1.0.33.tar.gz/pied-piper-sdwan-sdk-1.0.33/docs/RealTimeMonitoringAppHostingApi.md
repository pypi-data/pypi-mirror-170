# openapi_client.RealTimeMonitoringAppHostingApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_hosting_attached_devices**](RealTimeMonitoringAppHostingApi.md#get_app_hosting_attached_devices) | **GET** /device/app-hosting/attached-devices | 
[**get_app_hosting_details**](RealTimeMonitoringAppHostingApi.md#get_app_hosting_details) | **GET** /device/app-hosting/details | 
[**get_app_hosting_guest_routes**](RealTimeMonitoringAppHostingApi.md#get_app_hosting_guest_routes) | **GET** /device/app-hosting/guest-routes | 
[**get_app_hosting_network_devices**](RealTimeMonitoringAppHostingApi.md#get_app_hosting_network_devices) | **GET** /device/app-hosting/network-interfaces | 
[**get_app_hosting_network_utils**](RealTimeMonitoringAppHostingApi.md#get_app_hosting_network_utils) | **GET** /device/app-hosting/network-utilization | 
[**get_app_hosting_processes**](RealTimeMonitoringAppHostingApi.md#get_app_hosting_processes) | **GET** /device/app-hosting/processes | 
[**get_app_hosting_storage_utils**](RealTimeMonitoringAppHostingApi.md#get_app_hosting_storage_utils) | **GET** /device/app-hosting/storage-utilization | 
[**get_app_hosting_utilization**](RealTimeMonitoringAppHostingApi.md#get_app_hosting_utilization) | **GET** /device/app-hosting/utilization | 


# **get_app_hosting_attached_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_hosting_attached_devices(device_id)



Get App hosting attached device from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_app_hosting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_app_hosting_api.RealTimeMonitoringAppHostingApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_hosting_attached_devices(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppHostingApi->get_app_hosting_attached_devices: %s\n" % e)
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

# **get_app_hosting_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_hosting_details(device_id)



Get App hosting details from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_app_hosting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_app_hosting_api.RealTimeMonitoringAppHostingApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_hosting_details(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppHostingApi->get_app_hosting_details: %s\n" % e)
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

# **get_app_hosting_guest_routes**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_hosting_guest_routes(device_id)



Get App hosting guest routes from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_app_hosting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_app_hosting_api.RealTimeMonitoringAppHostingApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_hosting_guest_routes(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppHostingApi->get_app_hosting_guest_routes: %s\n" % e)
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

# **get_app_hosting_network_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_hosting_network_devices(device_id)



Get App hosting network interface from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_app_hosting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_app_hosting_api.RealTimeMonitoringAppHostingApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_hosting_network_devices(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppHostingApi->get_app_hosting_network_devices: %s\n" % e)
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

# **get_app_hosting_network_utils**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_hosting_network_utils(device_id)



Get App hosting network utilization from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_app_hosting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_app_hosting_api.RealTimeMonitoringAppHostingApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_hosting_network_utils(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppHostingApi->get_app_hosting_network_utils: %s\n" % e)
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

# **get_app_hosting_processes**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_hosting_processes(device_id)



Get App hosting processes from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_app_hosting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_app_hosting_api.RealTimeMonitoringAppHostingApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_hosting_processes(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppHostingApi->get_app_hosting_processes: %s\n" % e)
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

# **get_app_hosting_storage_utils**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_hosting_storage_utils(device_id)



Get App hosting storage utilization from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_app_hosting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_app_hosting_api.RealTimeMonitoringAppHostingApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_hosting_storage_utils(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppHostingApi->get_app_hosting_storage_utils: %s\n" % e)
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

# **get_app_hosting_utilization**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_app_hosting_utilization(device_id)



Get App hosting utilization from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_app_hosting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_app_hosting_api.RealTimeMonitoringAppHostingApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app_hosting_utilization(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringAppHostingApi->get_app_hosting_utilization: %s\n" % e)
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

