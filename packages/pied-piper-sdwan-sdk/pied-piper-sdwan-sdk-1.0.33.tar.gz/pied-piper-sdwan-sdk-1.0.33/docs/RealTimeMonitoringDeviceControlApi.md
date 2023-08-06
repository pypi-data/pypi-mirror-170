# openapi_client.RealTimeMonitoringDeviceControlApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection_history_list_real_time**](RealTimeMonitoringDeviceControlApi.md#create_connection_history_list_real_time) | **GET** /device/control/connectionshistory | 
[**create_connections_summary**](RealTimeMonitoringDeviceControlApi.md#create_connections_summary) | **GET** /device/control/summary | 
[**create_link_list**](RealTimeMonitoringDeviceControlApi.md#create_link_list) | **GET** /device/control/links | 
[**create_local_properties_list_list_real_t_ime**](RealTimeMonitoringDeviceControlApi.md#create_local_properties_list_list_real_t_ime) | **GET** /device/control/localproperties | 
[**create_local_properties_synced_list**](RealTimeMonitoringDeviceControlApi.md#create_local_properties_synced_list) | **GET** /device/control/synced/localproperties | 
[**create_real_time_connection_list**](RealTimeMonitoringDeviceControlApi.md#create_real_time_connection_list) | **GET** /device/control/connections | 
[**create_synced_connection_list**](RealTimeMonitoringDeviceControlApi.md#create_synced_connection_list) | **GET** /device/control/synced/connections | 
[**create_valid_devices_list_real_time**](RealTimeMonitoringDeviceControlApi.md#create_valid_devices_list_real_time) | **GET** /device/control/validdevices | 
[**create_valid_v_smarts_list_real_time**](RealTimeMonitoringDeviceControlApi.md#create_valid_v_smarts_list_real_time) | **GET** /device/control/validvsmarts | 
[**create_wan_interface_list_list**](RealTimeMonitoringDeviceControlApi.md#create_wan_interface_list_list) | **GET** /device/control/waninterface | 
[**create_wan_interface_synced_list**](RealTimeMonitoringDeviceControlApi.md#create_wan_interface_synced_list) | **GET** /device/control/synced/waninterface | 
[**get_affinity_config**](RealTimeMonitoringDeviceControlApi.md#get_affinity_config) | **GET** /device/control/affinity/config | 
[**get_affinity_status**](RealTimeMonitoringDeviceControlApi.md#get_affinity_status) | **GET** /device/control/affinity/status | 
[**get_connection_statistics**](RealTimeMonitoringDeviceControlApi.md#get_connection_statistics) | **GET** /device/control/statistics | 
[**get_device_control_status_summary**](RealTimeMonitoringDeviceControlApi.md#get_device_control_status_summary) | **GET** /device/control/summary/device | 
[**get_local_device_status**](RealTimeMonitoringDeviceControlApi.md#get_local_device_status) | **GET** /device/control/status | 
[**get_port_hop_color**](RealTimeMonitoringDeviceControlApi.md#get_port_hop_color) | **GET** /device/control/waninterface/color | 
[**get_total_count_for_device_states**](RealTimeMonitoringDeviceControlApi.md#get_total_count_for_device_states) | **GET** /device/control/count | 
[**get_valid_v_manage_id_real_time**](RealTimeMonitoringDeviceControlApi.md#get_valid_v_manage_id_real_time) | **GET** /device/control/validvmanageid | 
[**network_summary**](RealTimeMonitoringDeviceControlApi.md#network_summary) | **GET** /device/control/networksummary | 


# **create_connection_history_list_real_time**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_connection_history_list_real_time(device_id)



Get connections history list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    peer_type = "vedge" # str | Peer type (optional)
    system_ip = "system-ip_example" # str | Peer system IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_connection_history_list_real_time(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_connection_history_list_real_time: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_connection_history_list_real_time(device_id, peer_type=peer_type, system_ip=system_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_connection_history_list_real_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **peer_type** | **str**| Peer type | [optional]
 **system_ip** | **str**| Peer system IP | [optional]

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

# **create_connections_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_connections_summary(device_id)



Get connections summary from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_connections_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_connections_summary: %s\n" % e)
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

# **create_link_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_link_list(state)



Get connections list

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    state = "state_example" # str | Device State

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_link_list(state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_link_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Device State |

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

# **create_local_properties_list_list_real_t_ime**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_local_properties_list_list_real_t_ime(device_id)



Get local properties list (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_local_properties_list_list_real_t_ime(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_local_properties_list_list_real_t_ime: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |

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

# **create_local_properties_synced_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_local_properties_synced_list(device_id)



Get local properties list

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_local_properties_synced_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_local_properties_synced_list: %s\n" % e)
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

# **create_real_time_connection_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_real_time_connection_list(device_id)



Get connections list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    peer_type = "vedge" # str | Peer type (optional)
    system_ip = "system-ip_example" # str | Peer system IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_real_time_connection_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_real_time_connection_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_real_time_connection_list(device_id, peer_type=peer_type, system_ip=system_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_real_time_connection_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **peer_type** | **str**| Peer type | [optional]
 **system_ip** | **str**| Peer system IP | [optional]

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

# **create_synced_connection_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_synced_connection_list(device_id)



Get connections list from vManage

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    peer_type = "vedge" # str | Peer type (optional)
    system_ip = "system-ip_example" # str | Peer system IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_synced_connection_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_synced_connection_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_synced_connection_list(device_id, peer_type=peer_type, system_ip=system_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_synced_connection_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **peer_type** | **str**| Peer type | [optional]
 **system_ip** | **str**| Peer system IP | [optional]

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

# **create_valid_devices_list_real_time**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_valid_devices_list_real_time(device_id)



Get valid device list (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_valid_devices_list_real_time(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_valid_devices_list_real_time: %s\n" % e)
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

# **create_valid_v_smarts_list_real_time**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_valid_v_smarts_list_real_time(device_id)



Get valid vSmart list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_valid_v_smarts_list_real_time(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_valid_v_smarts_list_real_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |

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

# **create_wan_interface_list_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_wan_interface_list_list(device_id)



Get WAN interface list (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_wan_interface_list_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_wan_interface_list_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |

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

# **create_wan_interface_synced_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_wan_interface_synced_list(device_id)



Get WAN interface list

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_wan_interface_synced_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->create_wan_interface_synced_list: %s\n" % e)
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

# **get_affinity_config**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_affinity_config(device_id)



Get affinity config from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_affinity_config(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->get_affinity_config: %s\n" % e)
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

# **get_affinity_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_affinity_status(device_id)



Get affinity status from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_affinity_status(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->get_affinity_status: %s\n" % e)
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

# **get_connection_statistics**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_connection_statistics(device_id)



Get connection statistics from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_connection_statistics(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->get_connection_statistics: %s\n" % e)
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

# **get_device_control_status_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_control_status_summary(device_id)



Get device control status summary

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_control_status_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->get_device_control_status_summary: %s\n" % e)
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

# **get_local_device_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_local_device_status()



Get local device status

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_local_device_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->get_local_device_status: %s\n" % e)
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

# **get_port_hop_color**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_port_hop_color(device_id)



Get port hop colors

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_port_hop_color(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->get_port_hop_color: %s\n" % e)
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

# **get_total_count_for_device_states**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_total_count_for_device_states()



Get number of vedges and vsmart device in different control states

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    is_cached = False # bool | Device State cached (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_total_count_for_device_states(is_cached=is_cached)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->get_total_count_for_device_states: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_cached** | **bool**| Device State cached | [optional] if omitted the server will use the default value of False

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

# **get_valid_v_manage_id_real_time**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_valid_v_manage_id_real_time(device_id)



Get valid vManage from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_valid_v_manage_id_real_time(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->get_valid_v_manage_id_real_time: %s\n" % e)
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

# **network_summary**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] network_summary()



Get list of unreachable devices

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_device_control_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_device_control_api.RealTimeMonitoringDeviceControlApi(api_client)
    state = "state_example" # str | Device State (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.network_summary(state=state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDeviceControlApi->network_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Device State | [optional]

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

