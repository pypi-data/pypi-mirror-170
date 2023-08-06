# openapi_client.MonitoringCflowdFlowsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cflow_collector_list**](MonitoringCflowdFlowsApi.md#create_cflow_collector_list) | **GET** /device/cflowd/flows | 
[**create_cflowd_collector_list**](MonitoringCflowdFlowsApi.md#create_cflowd_collector_list) | **GET** /device/cflowd/collector | 
[**create_cflowd_flows_count_list**](MonitoringCflowdFlowsApi.md#create_cflowd_flows_count_list) | **GET** /device/cflowd/flows-count | 
[**create_cflowd_statistics**](MonitoringCflowdFlowsApi.md#create_cflowd_statistics) | **GET** /device/cflowd/statistics | 
[**create_cflowd_template**](MonitoringCflowdFlowsApi.md#create_cflowd_template) | **GET** /device/cflowd/template | 
[**get_cflowd_dpi_device_field_json**](MonitoringCflowdFlowsApi.md#get_cflowd_dpi_device_field_json) | **GET** /device/cflowd/application/fields | 
[**get_cflowd_dpi_field_json**](MonitoringCflowdFlowsApi.md#get_cflowd_dpi_field_json) | **GET** /device/cflowd/device/fields | 
[**get_fn_f_cache_stats**](MonitoringCflowdFlowsApi.md#get_fn_f_cache_stats) | **GET** /device/cflowd/fnf/cache-stats | 
[**get_fn_f_export_client_stats**](MonitoringCflowdFlowsApi.md#get_fn_f_export_client_stats) | **GET** /device/cflowd/fnf/export-client-stats | 
[**get_fn_f_export_stats**](MonitoringCflowdFlowsApi.md#get_fn_f_export_stats) | **GET** /device/cflowd/fnf/export-stats | 
[**get_fn_f_monitor_stats**](MonitoringCflowdFlowsApi.md#get_fn_f_monitor_stats) | **GET** /device/cflowd/fnf/monitor-stats | 
[**get_fnf**](MonitoringCflowdFlowsApi.md#get_fnf) | **GET** /device/cflowd/fnf/flow-monitor | 


# **create_cflow_collector_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_cflow_collector_list(device_id)



Get list of cflowd flows from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    vpn_id = "0" # str | VPN Id (optional)
    src_ip = "src-ip_example" # str | Source IP (optional)
    dest_ip = "dest-ip_example" # str | Destination IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflow_collector_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->create_cflow_collector_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cflow_collector_list(device_id, vpn_id=vpn_id, src_ip=src_ip, dest_ip=dest_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->create_cflow_collector_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **vpn_id** | **str**| VPN Id | [optional]
 **src_ip** | **str**| Source IP | [optional]
 **dest_ip** | **str**| Destination IP | [optional]

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

# **create_cflowd_collector_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_cflowd_collector_list(device_id)



Get cflowd collector list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflowd_collector_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->create_cflowd_collector_list: %s\n" % e)
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

# **create_cflowd_flows_count_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cflowd_flows_count_list(device_id)



Get cflowd flow count from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    vpn_id = "0" # str | VPN Id (optional)
    src_ip = "src-ip_example" # str | Source IP (optional)
    dest_ip = "dest-ip_example" # str | Destination IP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflowd_flows_count_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->create_cflowd_flows_count_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cflowd_flows_count_list(device_id, vpn_id=vpn_id, src_ip=src_ip, dest_ip=dest_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->create_cflowd_flows_count_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **vpn_id** | **str**| VPN Id | [optional]
 **src_ip** | **str**| Source IP | [optional]
 **dest_ip** | **str**| Destination IP | [optional]

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

# **create_cflowd_statistics**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cflowd_statistics(device_id)



Get cflowd statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflowd_statistics(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->create_cflowd_statistics: %s\n" % e)
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

# **create_cflowd_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cflowd_template(device_id)



Get cflowd template from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cflowd_template(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->create_cflowd_template: %s\n" % e)
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

# **get_cflowd_dpi_device_field_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cflowd_dpi_device_field_json()



Get Cflowd DPI query field JSON

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    is_device_dash_board = False # bool | Flag whether it is device dashboard request (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cflowd_dpi_device_field_json(is_device_dash_board=is_device_dash_board)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->get_cflowd_dpi_device_field_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_device_dash_board** | **bool**| Flag whether it is device dashboard request | [optional] if omitted the server will use the default value of False

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

# **get_cflowd_dpi_field_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cflowd_dpi_field_json()



Get CflowdvDPI query field JSON

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    is_device_dash_board = False # bool | Flag whether it is device dashboard request (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cflowd_dpi_field_json(is_device_dash_board=is_device_dash_board)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->get_cflowd_dpi_field_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_device_dash_board** | **bool**| Flag whether it is device dashboard request | [optional] if omitted the server will use the default value of False

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

# **get_fn_f_cache_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fn_f_cache_stats(device_id)



Get FnF cache stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fn_f_cache_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->get_fn_f_cache_stats: %s\n" % e)
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

# **get_fn_f_export_client_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fn_f_export_client_stats(device_id)



Get FnF export client stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fn_f_export_client_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->get_fn_f_export_client_stats: %s\n" % e)
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

# **get_fn_f_export_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fn_f_export_stats(device_id)



Get FnF export stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fn_f_export_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->get_fn_f_export_stats: %s\n" % e)
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

# **get_fn_f_monitor_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fn_f_monitor_stats(device_id)



Get FnF monitor stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fn_f_monitor_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->get_fn_f_monitor_stats: %s\n" % e)
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

# **get_fnf**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_fnf(device_id)



Get FnF from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_cflowd_flows_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_cflowd_flows_api.MonitoringCflowdFlowsApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fnf(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringCflowdFlowsApi->get_fnf: %s\n" % e)
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

