# openapi_client.RealTimeMonitoringOrchestratorApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection_history_list**](RealTimeMonitoringOrchestratorApi.md#create_connection_history_list) | **GET** /device/orchestrator/connectionshistory | 
[**create_connection_list_from_device**](RealTimeMonitoringOrchestratorApi.md#create_connection_list_from_device) | **GET** /device/orchestrator/connections | 
[**create_connection_summary**](RealTimeMonitoringOrchestratorApi.md#create_connection_summary) | **GET** /device/orchestrator/summary | 
[**create_local_properties_list_list**](RealTimeMonitoringOrchestratorApi.md#create_local_properties_list_list) | **GET** /device/orchestrator/localproperties | 
[**create_reverse_proxy_mapping_list**](RealTimeMonitoringOrchestratorApi.md#create_reverse_proxy_mapping_list) | **GET** /device/orchestrator/proxymapping | 
[**create_valid_devices_list**](RealTimeMonitoringOrchestratorApi.md#create_valid_devices_list) | **GET** /device/orchestrator/validvedges | 
[**create_valid_v_smarts_list**](RealTimeMonitoringOrchestratorApi.md#create_valid_v_smarts_list) | **GET** /device/orchestrator/validvsmarts | 
[**get_statistics**](RealTimeMonitoringOrchestratorApi.md#get_statistics) | **GET** /device/orchestrator/statistics | 
[**get_valid_v_manage_id**](RealTimeMonitoringOrchestratorApi.md#get_valid_v_manage_id) | **GET** /device/orchestrator/validvmanageid | 


# **create_connection_history_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_connection_history_list(device_id)



Get connection history list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_orchestrator_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_orchestrator_api.RealTimeMonitoringOrchestratorApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_connection_history_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringOrchestratorApi->create_connection_history_list: %s\n" % e)
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

# **create_connection_list_from_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_connection_list_from_device(device_id)



Get connection list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_orchestrator_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_orchestrator_api.RealTimeMonitoringOrchestratorApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_connection_list_from_device(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringOrchestratorApi->create_connection_list_from_device: %s\n" % e)
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

# **create_connection_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_connection_summary(device_id)



Get connection summary from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_orchestrator_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_orchestrator_api.RealTimeMonitoringOrchestratorApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_connection_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringOrchestratorApi->create_connection_summary: %s\n" % e)
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

# **create_local_properties_list_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_local_properties_list_list(device_id)



Get local properties list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_orchestrator_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_orchestrator_api.RealTimeMonitoringOrchestratorApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_local_properties_list_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringOrchestratorApi->create_local_properties_list_list: %s\n" % e)
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

# **create_reverse_proxy_mapping_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_reverse_proxy_mapping_list(device_id)



Get reverse proxy mapping from vbond

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_orchestrator_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_orchestrator_api.RealTimeMonitoringOrchestratorApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_reverse_proxy_mapping_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringOrchestratorApi->create_reverse_proxy_mapping_list: %s\n" % e)
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

# **create_valid_devices_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_valid_devices_list(device_id)



Get valid device list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_orchestrator_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_orchestrator_api.RealTimeMonitoringOrchestratorApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_valid_devices_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringOrchestratorApi->create_valid_devices_list: %s\n" % e)
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

# **create_valid_v_smarts_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_valid_v_smarts_list(device_id)



Get valid vSmart list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_orchestrator_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_orchestrator_api.RealTimeMonitoringOrchestratorApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_valid_v_smarts_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringOrchestratorApi->create_valid_v_smarts_list: %s\n" % e)
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

# **get_statistics**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_statistics(device_id)



Get statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_orchestrator_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_orchestrator_api.RealTimeMonitoringOrchestratorApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_statistics(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringOrchestratorApi->get_statistics: %s\n" % e)
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

# **get_valid_v_manage_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_valid_v_manage_id(device_id)



Get valid vManage Id from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_orchestrator_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_orchestrator_api.RealTimeMonitoringOrchestratorApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_valid_v_manage_id(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringOrchestratorApi->get_valid_v_manage_id: %s\n" % e)
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

