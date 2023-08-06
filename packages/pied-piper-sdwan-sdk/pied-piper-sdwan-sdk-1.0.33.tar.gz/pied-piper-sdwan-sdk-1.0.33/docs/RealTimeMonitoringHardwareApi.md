# openapi_client.RealTimeMonitoringHardwareApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alarm_list**](RealTimeMonitoringHardwareApi.md#create_alarm_list) | **GET** /device/hardware/alarms | 
[**create_environment_list**](RealTimeMonitoringHardwareApi.md#create_environment_list) | **GET** /device/hardware/environment | 
[**create_error_alarm_list**](RealTimeMonitoringHardwareApi.md#create_error_alarm_list) | **GET** /device/hardware/errors | 
[**create_inventory_list**](RealTimeMonitoringHardwareApi.md#create_inventory_list) | **GET** /device/hardware/inventory | 
[**create_status_summary**](RealTimeMonitoringHardwareApi.md#create_status_summary) | **GET** /device/hardware/status/summary | 
[**create_synced_alarm_list**](RealTimeMonitoringHardwareApi.md#create_synced_alarm_list) | **GET** /device/hardware/synced/alarms | 
[**create_synced_environment_list**](RealTimeMonitoringHardwareApi.md#create_synced_environment_list) | **GET** /device/hardware/synced/environment | 
[**create_synced_inventory_list**](RealTimeMonitoringHardwareApi.md#create_synced_inventory_list) | **GET** /device/hardware/synced/inventory | 
[**create_system_list**](RealTimeMonitoringHardwareApi.md#create_system_list) | **GET** /device/hardware/system | 
[**create_temp_threshold_list**](RealTimeMonitoringHardwareApi.md#create_temp_threshold_list) | **GET** /device/hardware/threshold | 


# **create_alarm_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_alarm_list(device_id)



Get hardware alarm list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_alarm_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_alarm_list: %s\n" % e)
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

# **create_environment_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_environment_list(device_id)



Get hardware environment list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_environment_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_environment_list: %s\n" % e)
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

# **create_error_alarm_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_error_alarm_list()



Get hardware error list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_error_alarm_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_error_alarm_list: %s\n" % e)
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

# **create_inventory_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_inventory_list(device_id)



Get hardware inventory list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_inventory_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_inventory_list: %s\n" % e)
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

# **create_status_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_status_summary(device_id)



Get hardware status summary from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_status_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_status_summary: %s\n" % e)
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

# **create_synced_alarm_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_synced_alarm_list(device_id)



Get hardware alarm list synchronously from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_synced_alarm_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_synced_alarm_list: %s\n" % e)
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

# **create_synced_environment_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_synced_environment_list(device_id)



Get hardware environment list synchronously from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_synced_environment_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_synced_environment_list: %s\n" % e)
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

# **create_synced_inventory_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_synced_inventory_list(device_id)



Get hardware inventory list synchronously from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_synced_inventory_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_synced_inventory_list: %s\n" % e)
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

# **create_system_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_system_list(device_id)



Get hardware system data list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_system_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_system_list: %s\n" % e)
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

# **create_temp_threshold_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_temp_threshold_list(device_id)



Get hardware temperature list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_hardware_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_hardware_api.RealTimeMonitoringHardwareApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_temp_threshold_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringHardwareApi->create_temp_threshold_list: %s\n" % e)
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

