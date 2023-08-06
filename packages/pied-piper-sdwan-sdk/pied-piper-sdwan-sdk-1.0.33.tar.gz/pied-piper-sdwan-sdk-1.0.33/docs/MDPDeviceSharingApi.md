# openapi_client.MDPDeviceSharingApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_devices**](MDPDeviceSharingApi.md#attach_devices) | **POST** /mdp/attachDevices/{nmsId} | 
[**detach_devices**](MDPDeviceSharingApi.md#detach_devices) | **POST** /mdp/detachDevices/{nmsId} | 
[**edit_attached_devices**](MDPDeviceSharingApi.md#edit_attached_devices) | **PUT** /mdp/attachDevices/{nmsId} | 
[**retrieve_mdp_attached_devices**](MDPDeviceSharingApi.md#retrieve_mdp_attached_devices) | **GET** /mdp/attachDevices/{nmsId} | 
[**retrieve_mdp_supported_devices_**](MDPDeviceSharingApi.md#retrieve_mdp_supported_devices_) | **GET** /mdp/devices/{nmsId} | 


# **attach_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} attach_devices(nms_id)



Share devices with MDP

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_device_sharing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_device_sharing_api.MDPDeviceSharingApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | deviceList (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.attach_devices(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPDeviceSharingApi->attach_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attach_devices(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPDeviceSharingApi->attach_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| deviceList | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} detach_devices(nms_id)



Disconnect devices from mpd controller

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_device_sharing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_device_sharing_api.MDPDeviceSharingApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | deviceList (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.detach_devices(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPDeviceSharingApi->detach_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.detach_devices(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPDeviceSharingApi->detach_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| deviceList | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_attached_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_attached_devices(nms_id)



Edit attached devices

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_device_sharing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_device_sharing_api.MDPDeviceSharingApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | deviceList (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_attached_devices(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPDeviceSharingApi->edit_attached_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_attached_devices(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPDeviceSharingApi->edit_attached_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| deviceList | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_mdp_attached_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] retrieve_mdp_attached_devices(nms_id)



Retrieve MDP attached devices

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_device_sharing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_device_sharing_api.MDPDeviceSharingApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_mdp_attached_devices(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPDeviceSharingApi->retrieve_mdp_attached_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |

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

# **retrieve_mdp_supported_devices_**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] retrieve_mdp_supported_devices_(nms_id)



Retrieve MDP supported devices

### Example


```python
import time
import openapi_client
from openapi_client.api import mdp_device_sharing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mdp_device_sharing_api.MDPDeviceSharingApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_mdp_supported_devices_(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MDPDeviceSharingApi->retrieve_mdp_supported_devices_: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |

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

