# openapi_client.RealTimeMonitoringBFDApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bfd_history_list**](RealTimeMonitoringBFDApi.md#create_bfd_history_list) | **GET** /device/bfd/history | 
[**create_bfd_link_list**](RealTimeMonitoringBFDApi.md#create_bfd_link_list) | **GET** /device/bfd/links | 
[**create_bfd_sessions**](RealTimeMonitoringBFDApi.md#create_bfd_sessions) | **GET** /device/bfd/sessions | 
[**create_bfd_summary**](RealTimeMonitoringBFDApi.md#create_bfd_summary) | **GET** /device/bfd/summary | 
[**create_synced_bfd_session**](RealTimeMonitoringBFDApi.md#create_synced_bfd_session) | **GET** /device/bfd/synced/sessions | 
[**create_tloc_summary**](RealTimeMonitoringBFDApi.md#create_tloc_summary) | **GET** /device/bfd/tloc | 
[**get_bfd_site_state_detail**](RealTimeMonitoringBFDApi.md#get_bfd_site_state_detail) | **GET** /device/bfd/sites/detail | 
[**get_bfd_sites_summary**](RealTimeMonitoringBFDApi.md#get_bfd_sites_summary) | **GET** /device/bfd/sites/summary | 
[**get_device_bfd_state_summary**](RealTimeMonitoringBFDApi.md#get_device_bfd_state_summary) | **GET** /device/bfd/state/device | 
[**get_device_bfd_state_summary_tloc**](RealTimeMonitoringBFDApi.md#get_device_bfd_state_summary_tloc) | **GET** /device/bfd/state/device/tloc | 
[**get_device_bfd_status**](RealTimeMonitoringBFDApi.md#get_device_bfd_status) | **GET** /device/bfd/status | 
[**get_device_bfd_status_summary**](RealTimeMonitoringBFDApi.md#get_device_bfd_status_summary) | **GET** /device/bfd/summary/device | 


# **create_bfd_history_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_bfd_history_list(device_id)



Get BFD session history from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    device_id = "deviceId_example" # str | Device IP
    system_ip = "system-ip_example" # str | System IP (optional)
    color = "default" # str | Remote color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_bfd_history_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->create_bfd_history_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_bfd_history_list(device_id, system_ip=system_ip, color=color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->create_bfd_history_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **system_ip** | **str**| System IP | [optional]
 **color** | **str**| Remote color | [optional]

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

# **create_bfd_link_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_bfd_link_list(state)



Get list of BFD connections

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    state = "state_example" # str | Device state

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_bfd_link_list(state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->create_bfd_link_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Device state |

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

# **create_bfd_sessions**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_bfd_sessions(device_id)



Get list of BFD sessions from vManage (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    device_id = "deviceId_example" # str | Device IP
    system_ip = "system-ip_example" # str | System IP (optional)
    color = "default" # str | Remote color (optional)
    local_color = "default" # str | Source color (optional)
    region_type = "core" # str | Region type (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_bfd_sessions(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->create_bfd_sessions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_bfd_sessions(device_id, system_ip=system_ip, color=color, local_color=local_color, region_type=region_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->create_bfd_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **system_ip** | **str**| System IP | [optional]
 **color** | **str**| Remote color | [optional]
 **local_color** | **str**| Source color | [optional]
 **region_type** | **str**| Region type | [optional]

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

# **create_bfd_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_bfd_summary(device_id)



Get BFD summary from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_bfd_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->create_bfd_summary: %s\n" % e)
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

# **create_synced_bfd_session**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_synced_bfd_session(device_id)



Get list of BFD sessions from vManage synchronously

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    system_ip = "system-ip_example" # str | System IP (optional)
    color = "default" # str | Remote color (optional)
    local_color = "default" # str | Source color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_synced_bfd_session(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->create_synced_bfd_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_synced_bfd_session(device_id, system_ip=system_ip, color=color, local_color=local_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->create_synced_bfd_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **system_ip** | **str**| System IP | [optional]
 **color** | **str**| Remote color | [optional]
 **local_color** | **str**| Source color | [optional]

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

# **create_tloc_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_tloc_summary(device_id)



Get TLOC summary from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    device_id = "deviceId_example" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_tloc_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->create_tloc_summary: %s\n" % e)
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

# **get_bfd_site_state_detail**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bfd_site_state_detail()



Get detailed BFD site details

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_bfd_site_state_detail()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->get_bfd_site_state_detail: %s\n" % e)
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

# **get_bfd_sites_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_bfd_sites_summary(vpn_id)



Get BFD site summary

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from openapi_client.model.vpnid import VPNID
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    vpn_id = [
        VPNID(
            vpn="vpn_example",
        ),
    ] # [VPNID] | Filter VPN
    is_cached = False # bool | Flag for caching (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_bfd_sites_summary(vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->get_bfd_sites_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_bfd_sites_summary(vpn_id, is_cached=is_cached)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->get_bfd_sites_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_id** | [**[VPNID]**](VPNID.md)| Filter VPN |
 **is_cached** | **bool**| Flag for caching | [optional] if omitted the server will use the default value of False

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

# **get_device_bfd_state_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_bfd_state_summary(device_id)



Get device BFD state summary

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_bfd_state_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->get_device_bfd_state_summary: %s\n" % e)
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

# **get_device_bfd_state_summary_tloc**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_bfd_state_summary_tloc(device_id)



Get device BFD state summary with tloc color

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_bfd_state_summary_tloc(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->get_device_bfd_state_summary_tloc: %s\n" % e)
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

# **get_device_bfd_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_bfd_status()



Get device BFD status

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_bfd_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->get_device_bfd_status: %s\n" % e)
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

# **get_device_bfd_status_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_bfd_status_summary(device_id)



Get device BFD status summary

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bfd_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bfd_api.RealTimeMonitoringBFDApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_bfd_status_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBFDApi->get_device_bfd_status_summary: %s\n" % e)
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

