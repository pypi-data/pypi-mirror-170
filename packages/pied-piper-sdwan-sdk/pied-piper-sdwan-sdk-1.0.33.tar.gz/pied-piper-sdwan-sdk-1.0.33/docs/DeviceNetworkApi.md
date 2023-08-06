# openapi_client.DeviceNetworkApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network_issues_summary**](DeviceNetworkApi.md#get_network_issues_summary) | **GET** /network/issues/summary | 
[**get_network_status_summary**](DeviceNetworkApi.md#get_network_status_summary) | **GET** /network/status | 
[**get_reboot_count**](DeviceNetworkApi.md#get_reboot_count) | **GET** /network/issues/rebootcount | 
[**get_vmanage_control_status**](DeviceNetworkApi.md#get_vmanage_control_status) | **GET** /network/connectionssummary | 


# **get_network_issues_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_network_issues_summary()



Retrieve network issues summary

### Example


```python
import time
import openapi_client
from openapi_client.api import device_network_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = device_network_api.DeviceNetworkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_network_issues_summary()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeviceNetworkApi->get_network_issues_summary: %s\n" % e)
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

# **get_network_status_summary**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_network_status_summary()



Retrieve network status summary

### Example


```python
import time
import openapi_client
from openapi_client.api import device_network_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = device_network_api.DeviceNetworkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_network_status_summary()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeviceNetworkApi->get_network_status_summary: %s\n" % e)
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

# **get_reboot_count**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_reboot_count()



Retrieve reboot count

### Example


```python
import time
import openapi_client
from openapi_client.api import device_network_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = device_network_api.DeviceNetworkApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_reboot_count()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeviceNetworkApi->get_reboot_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_cached** | **bool**| Is cached flag | defaults to False

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

# **get_vmanage_control_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_vmanage_control_status()



Retrieve vManage control status

### Example


```python
import time
import openapi_client
from openapi_client.api import device_network_api
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
    api_instance = device_network_api.DeviceNetworkApi(api_client)
    is_cached = False # bool | Is cached flag (optional) if omitted the server will use the default value of False
    vpn_id = [
        VPNID(
            vpn="vpn_example",
        ),
    ] # [VPNID] | VPN Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vmanage_control_status(is_cached=is_cached, vpn_id=vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeviceNetworkApi->get_vmanage_control_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_cached** | **bool**| Is cached flag | [optional] if omitted the server will use the default value of False
 **vpn_id** | [**[VPNID]**](VPNID.md)| VPN Id | [optional]

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

