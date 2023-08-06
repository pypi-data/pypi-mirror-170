# openapi_client.TroubleshootingToolsDeviceGroupApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_device_group_list**](TroubleshootingToolsDeviceGroupApi.md#list_device_group_list) | **GET** /group | 
[**list_device_groups**](TroubleshootingToolsDeviceGroupApi.md#list_device_groups) | **GET** /group/device | 
[**list_group_devices**](TroubleshootingToolsDeviceGroupApi.md#list_group_devices) | **GET** /group/devices | 
[**list_group_devices_for_map**](TroubleshootingToolsDeviceGroupApi.md#list_group_devices_for_map) | **GET** /group/map/devices | 
[**list_group_links_for_map**](TroubleshootingToolsDeviceGroupApi.md#list_group_links_for_map) | **GET** /group/map/devices/links | 


# **list_device_group_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_device_group_list()



Retrieve device group list

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_group_api.TroubleshootingToolsDeviceGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_device_group_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceGroupApi->list_device_group_list: %s\n" % e)
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

# **list_device_groups**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_device_groups()



Retrieve device groups

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_group_api.TroubleshootingToolsDeviceGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_device_groups()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceGroupApi->list_device_groups: %s\n" % e)
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

# **list_group_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_group_devices(group_id)



Retrieve devices in group

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_group_api
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
    api_instance = troubleshooting_tools_device_group_api.TroubleshootingToolsDeviceGroupApi(api_client)
    group_id = "groupId_example" # str | Group Id
    ssh = False # bool | SSH (optional) if omitted the server will use the default value of False
    vpn_id = [
        VPNID(
            vpn="vpn_example",
        ),
    ] # [VPNID] | VPN Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_group_devices(group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceGroupApi->list_group_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_group_devices(group_id, ssh=ssh, vpn_id=vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceGroupApi->list_group_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group Id |
 **ssh** | **bool**| SSH | [optional] if omitted the server will use the default value of False
 **vpn_id** | [**[VPNID]**](VPNID.md)| VPN Id | [optional]

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

# **list_group_devices_for_map**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_group_devices_for_map(group_id)



Retrieve group devices for map

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_group_api
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
    api_instance = troubleshooting_tools_device_group_api.TroubleshootingToolsDeviceGroupApi(api_client)
    group_id = "groupId_example" # str | Group Id
    vpn_id = [
        VPNID(
            vpn="vpn_example",
        ),
    ] # [VPNID] | VPN Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_group_devices_for_map(group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceGroupApi->list_group_devices_for_map: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_group_devices_for_map(group_id, vpn_id=vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceGroupApi->list_group_devices_for_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group Id |
 **vpn_id** | [**[VPNID]**](VPNID.md)| VPN Id | [optional]

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

# **list_group_links_for_map**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_group_links_for_map(group_id)



Retrieve devices in group for map

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_group_api.TroubleshootingToolsDeviceGroupApi(api_client)
    group_id = "groupId_example" # str | Group Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_group_links_for_map(group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceGroupApi->list_group_links_for_map: %s\n" % e)
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

