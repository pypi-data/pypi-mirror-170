# openapi_client.RealTimeMonitoringVMApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cloud_dock_vm_lifecycle_nics**](RealTimeMonitoringVMApi.md#get_cloud_dock_vm_lifecycle_nics) | **GET** /device/vm/notifications | 
[**get_vbranch_vm_lifecycle**](RealTimeMonitoringVMApi.md#get_vbranch_vm_lifecycle) | **GET** /device/vm/oper/state | 
[**get_vbranch_vm_lifecycle_nics**](RealTimeMonitoringVMApi.md#get_vbranch_vm_lifecycle_nics) | **GET** /device/vm/nics | 
[**get_vm_life_cycle_state**](RealTimeMonitoringVMApi.md#get_vm_life_cycle_state) | **GET** /device/vm/state | 


# **get_cloud_dock_vm_lifecycle_nics**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_dock_vm_lifecycle_nics(user_group)



Get CloudDock vm lifecycle state

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vm_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vm_api.RealTimeMonitoringVMApi(api_client)
    user_group = "00r252U250?250" # str | userGroup Name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_dock_vm_lifecycle_nics(user_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVMApi->get_cloud_dock_vm_lifecycle_nics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group** | **str**| userGroup Name |

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

# **get_vbranch_vm_lifecycle**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_vbranch_vm_lifecycle(device_id)



Get vbranch vm lifecycle state

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vm_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vm_api.RealTimeMonitoringVMApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vbranch_vm_lifecycle(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVMApi->get_vbranch_vm_lifecycle: %s\n" % e)
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

# **get_vbranch_vm_lifecycle_nics**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_vbranch_vm_lifecycle_nics(device_id)



Get vbranch vm lifecycle state (NIC)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vm_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vm_api.RealTimeMonitoringVMApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vbranch_vm_lifecycle_nics(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVMApi->get_vbranch_vm_lifecycle_nics: %s\n" % e)
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

# **get_vm_life_cycle_state**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_vm_life_cycle_state(device_id)



Get vm lifecycle state

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vm_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vm_api.RealTimeMonitoringVMApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vm_life_cycle_state(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVMApi->get_vm_life_cycle_state: %s\n" % e)
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

