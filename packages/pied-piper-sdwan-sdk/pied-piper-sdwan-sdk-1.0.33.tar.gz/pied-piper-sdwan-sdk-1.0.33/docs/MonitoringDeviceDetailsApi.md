# openapi_client.MonitoringDeviceDetailsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_sdavcon_device**](MonitoringDeviceDetailsApi.md#enable_sdavcon_device) | **POST** /device/enableSDAVC/{deviceIP}/{enable} | 
[**generate_device_state_data**](MonitoringDeviceDetailsApi.md#generate_device_state_data) | **GET** /data/device/state/{state_data_type} | 
[**generate_device_state_data_fields**](MonitoringDeviceDetailsApi.md#generate_device_state_data_fields) | **GET** /data/device/state/{state_data_type}/fields | 
[**generate_device_state_data_with_query_string**](MonitoringDeviceDetailsApi.md#generate_device_state_data_with_query_string) | **GET** /data/device/state/{state_data_type}/query | 
[**get_all_device_status**](MonitoringDeviceDetailsApi.md#get_all_device_status) | **GET** /device/status | 
[**get_device_counters**](MonitoringDeviceDetailsApi.md#get_device_counters) | **GET** /device/counters | 
[**get_device_list_as_key_value**](MonitoringDeviceDetailsApi.md#get_device_list_as_key_value) | **GET** /device/keyvalue | 
[**get_device_models**](MonitoringDeviceDetailsApi.md#get_device_models) | **GET** /device/models/{uuid} | 
[**get_device_only_status**](MonitoringDeviceDetailsApi.md#get_device_only_status) | **GET** /device/devicestatus | 
[**get_device_running_config**](MonitoringDeviceDetailsApi.md#get_device_running_config) | **GET** /device/config | 
[**get_device_running_config_html**](MonitoringDeviceDetailsApi.md#get_device_running_config_html) | **GET** /device/config/html | 
[**get_device_tloc_status**](MonitoringDeviceDetailsApi.md#get_device_tloc_status) | **GET** /device/tloc | 
[**get_device_tloc_util**](MonitoringDeviceDetailsApi.md#get_device_tloc_util) | **GET** /device/tlocutil | 
[**get_device_tloc_util_details**](MonitoringDeviceDetailsApi.md#get_device_tloc_util_details) | **GET** /device/tlocutil/detail | 
[**get_hardware_health_details**](MonitoringDeviceDetailsApi.md#get_hardware_health_details) | **GET** /device/hardwarehealth/detail | 
[**get_hardware_health_summary**](MonitoringDeviceDetailsApi.md#get_hardware_health_summary) | **GET** /device/hardwarehealth/summary | 
[**get_stats_queues**](MonitoringDeviceDetailsApi.md#get_stats_queues) | **GET** /device/stats | 
[**get_sync_queues**](MonitoringDeviceDetailsApi.md#get_sync_queues) | **GET** /device/queues | 
[**get_unconfigured**](MonitoringDeviceDetailsApi.md#get_unconfigured) | **GET** /device/unconfigured | 
[**get_v_manage_system_ip**](MonitoringDeviceDetailsApi.md#get_v_manage_system_ip) | **GET** /device/vmanage | 
[**get_vedge_inventory**](MonitoringDeviceDetailsApi.md#get_vedge_inventory) | **GET** /device/vedgeinventory/detail | 
[**get_vedge_inventory_summary**](MonitoringDeviceDetailsApi.md#get_vedge_inventory_summary) | **GET** /device/vedgeinventory/summary | 
[**list_all_device_models**](MonitoringDeviceDetailsApi.md#list_all_device_models) | **GET** /device/models | 
[**list_all_devices**](MonitoringDeviceDetailsApi.md#list_all_devices) | **GET** /device | 
[**list_all_monitor_details_devices**](MonitoringDeviceDetailsApi.md#list_all_monitor_details_devices) | **GET** /device/monitor | 
[**list_currently_syncing_devices**](MonitoringDeviceDetailsApi.md#list_currently_syncing_devices) | **GET** /device/sync_status | 
[**list_reachable_devices**](MonitoringDeviceDetailsApi.md#list_reachable_devices) | **GET** /device/reachable | 
[**list_unreachable_devices**](MonitoringDeviceDetailsApi.md#list_unreachable_devices) | **GET** /device/unreachable | 
[**remove_unreachable_device**](MonitoringDeviceDetailsApi.md#remove_unreachable_device) | **DELETE** /device/unreachable/{deviceIP} | 
[**set_block_sync**](MonitoringDeviceDetailsApi.md#set_block_sync) | **POST** /device/blockSync | 
[**sync_all_devices_mem_db**](MonitoringDeviceDetailsApi.md#sync_all_devices_mem_db) | **POST** /device/syncall/memorydb | 


# **enable_sdavcon_device**
> enable_sdavcon_device(device_ip, enable)



Enable/Disable SDAVC on device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP
    enable = True # bool | Enable/Disable flag

    # example passing only required values which don't have defaults set
    try:
        api_instance.enable_sdavcon_device(device_ip, enable)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->enable_sdavcon_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |
 **enable** | **bool**| Enable/Disable flag |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_device_state_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_device_state_data(state_data_type, start_id)



Get device state data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    state_data_type = "state_data_type_example" # str | State data type
    start_id = "startId_example" # str | Start Id
    count = "1000" # str | Count (optional) if omitted the server will use the default value of "1000"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_device_state_data(state_data_type, start_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->generate_device_state_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_device_state_data(state_data_type, start_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->generate_device_state_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_data_type** | **str**| State data type |
 **start_id** | **str**| Start Id |
 **count** | **str**| Count | [optional] if omitted the server will use the default value of "1000"

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

# **generate_device_state_data_fields**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_device_state_data_fields(state_data_type)



Get device state data fileds

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    state_data_type = "state_data_type_example" # str | State data type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_device_state_data_fields(state_data_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->generate_device_state_data_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_data_type** | **str**| State data type |

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

# **generate_device_state_data_with_query_string**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_device_state_data_with_query_string(state_data_type)



Get device state data fileds

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    state_data_type = "state_data_type_example" # str | State data type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_device_state_data_with_query_string(state_data_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->generate_device_state_data_with_query_string: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_data_type** | **str**| State data type |

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

# **get_all_device_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_all_device_status()



Get devices status for vSmart,vBond,vEdge, and cEdge

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_all_device_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_all_device_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_device_counters**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_counters()



Get device counters

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_counters()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_device_counters: %s\n" % e)
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

# **get_device_list_as_key_value**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_list_as_key_value()



Get vEdge inventory as key value (key as systemIp value as hostName)

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_list_as_key_value()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_device_list_as_key_value: %s\n" % e)
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

# **get_device_models**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_models(uuid)



Get device model for the device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_models(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_device_models: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **get_device_only_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_device_only_status()



Get devices status per type

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_only_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_device_only_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_device_running_config**
> str get_device_running_config(device_id)



Get device running configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    device_id = [
        "deviceId_example",
    ] # [str] | Device Id list

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_running_config(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_device_running_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **[str]**| Device Id list |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_running_config_html**
> str get_device_running_config_html(device_id)



Get device running configuration in HTML format

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    device_id = [
        "deviceId_example",
    ] # [str] | Device Id list

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_running_config_html(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_device_running_config_html: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **[str]**| Device Id list |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_tloc_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_tloc_status()



Get TLOC status list

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    device_id = "deviceId_example" # str | Device Id (optional)
    color = "color_example" # str | Status color (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_tloc_status(device_id=device_id, color=color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_device_tloc_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | [optional]
 **color** | **str**| Status color | [optional]

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

# **get_device_tloc_util**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_tloc_util()



Get TLOC list

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_tloc_util()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_device_tloc_util: %s\n" % e)
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

# **get_device_tloc_util_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_tloc_util_details()



Get detailed TLOC list

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    util = "util_example" # str | Tloc util (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_tloc_util_details(util=util)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_device_tloc_util_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **util** | **str**| Tloc util | [optional]

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

# **get_hardware_health_details**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_hardware_health_details()



Get hardware health details for device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    device_id = "deviceId_example" # str | Device Id (optional)
    state = "state_example" # str | Device state (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_hardware_health_details(device_id=device_id, state=state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_hardware_health_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | [optional]
 **state** | **str**| Device state | [optional]

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

# **get_hardware_health_summary**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_hardware_health_summary(vpn_id)



Get hardware health summary for device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    vpn_id = [
        "vpnId_example",
    ] # [str] | VPN Id
    is_cached = False # bool | Status cached (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_hardware_health_summary(vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_hardware_health_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_hardware_health_summary(vpn_id, is_cached=is_cached)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_hardware_health_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_id** | **[str]**| VPN Id |
 **is_cached** | **bool**| Status cached | [optional] if omitted the server will use the default value of False

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

# **get_stats_queues**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_queues()



Get stats queue information

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stats_queues()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_stats_queues: %s\n" % e)
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

# **get_sync_queues**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sync_queues()



Get synchronized queue information, returns information about syncing, queued and stuck devices

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_sync_queues()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_sync_queues: %s\n" % e)
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

# **get_unconfigured**
> [Device] get_unconfigured()



Get wan edge devices not configured by vManage (that is, those in CLI mode)

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from openapi_client.model.device import Device
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_unconfigured()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_unconfigured: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Device]**](Device.md)

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

# **get_v_manage_system_ip**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_v_manage_system_ip()



Get vManage system IP

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_v_manage_system_ip()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_v_manage_system_ip: %s\n" % e)
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

# **get_vedge_inventory**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_vedge_inventory()



Get detailed vEdge inventory

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    status = "status_example" # str | Device status (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vedge_inventory(status=status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_vedge_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Device status | [optional]

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

# **get_vedge_inventory_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_vedge_inventory_summary()



Get vEdge inventory

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_vedge_inventory_summary()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->get_vedge_inventory_summary: %s\n" % e)
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

# **list_all_device_models**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_all_device_models(list)



Get all device models supported by the vManage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    list = "list_example" # str | List type of device

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_all_device_models(list)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->list_all_device_models: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| List type of device |

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

# **list_all_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_all_devices()



List all devices

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_all_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->list_all_devices: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **list_all_monitor_details_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_all_monitor_details_devices()



Get all monitoring details of the devices

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_all_monitor_details_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->list_all_monitor_details_devices: %s\n" % e)
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

# **list_currently_syncing_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_currently_syncing_devices(group_id)



Get list of currently syncing devices

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    group_id = "groupId_example" # str | Group Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_currently_syncing_devices(group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->list_currently_syncing_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group Id |

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

# **list_reachable_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_reachable_devices()



Get list of reachable devices

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_reachable_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->list_reachable_devices: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **list_unreachable_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_unreachable_devices(personality)



Get list of unreachable devices

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    personality = "personality_example" # str | Device personality

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_unreachable_devices(personality)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->list_unreachable_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personality** | **str**| Device personality |

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

# **remove_unreachable_device**
> remove_unreachable_device(device_ip)



Delete unreachable device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_unreachable_device(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->remove_unreachable_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_block_sync**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_block_sync(block_sync)



Set collection manager block set flag

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)
    block_sync = "blockSync_example" # str | Block sync flag

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_block_sync(block_sync)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->set_block_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_sync** | **str**| Block sync flag |

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

# **sync_all_devices_mem_db**
> sync_all_devices_mem_db()



Synchronize memory database for all devices

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_device_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_device_details_api.MonitoringDeviceDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.sync_all_devices_mem_db()
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDeviceDetailsApi->sync_all_devices_mem_db: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

