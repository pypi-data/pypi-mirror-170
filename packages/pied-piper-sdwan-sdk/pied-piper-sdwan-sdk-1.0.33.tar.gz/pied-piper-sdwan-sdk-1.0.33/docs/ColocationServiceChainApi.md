# openapi_client.ColocationServiceChainApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_service_chain**](ColocationServiceChainApi.md#attach_service_chain) | **POST** /colocation/servicechain/attach | 
[**attach_service_chain1**](ColocationServiceChainApi.md#attach_service_chain1) | **POST** /colocation/servicechain/autoattach | 
[**cancel_button**](ColocationServiceChainApi.md#cancel_button) | **POST** /colocation/servicechain/cancel | 
[**detach_service_chain**](ColocationServiceChainApi.md#detach_service_chain) | **PUT** /colocation/servicechain/detach | 
[**get_edge_devices**](ColocationServiceChainApi.md#get_edge_devices) | **GET** /colocation/servicechain/edge/devices | 
[**getpnf_devices**](ColocationServiceChainApi.md#getpnf_devices) | **GET** /colocation/servicechain/edge/pnfdevices | 


# **attach_service_chain**
> attach_service_chain()



Attach service chain to cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_chain_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_chain_api.ColocationServiceChainApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Attach service chain request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.attach_service_chain(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceChainApi->attach_service_chain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Attach service chain request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_service_chain1**
> attach_service_chain1()



Attach service chain to cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_chain_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_chain_api.ColocationServiceChainApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Attach service chain request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.attach_service_chain1(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceChainApi->attach_service_chain1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Attach service chain request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_button**
> cancel_button()



Cancel button to cancel configuring devices

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_chain_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_chain_api.ColocationServiceChainApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cancel configuring devices (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.cancel_button(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceChainApi->cancel_button: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cancel configuring devices | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_service_chain**
> detach_service_chain()



Detach service chain

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_chain_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_chain_api.ColocationServiceChainApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Detach service chain request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.detach_service_chain(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceChainApi->detach_service_chain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Detach service chain request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_edge_devices()



Get edge devices

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_chain_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_chain_api.ColocationServiceChainApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_edge_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceChainApi->get_edge_devices: %s\n" % e)
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

# **getpnf_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] getpnf_devices(pnf_device_type)



Get PNF edge devices

### Example


```python
import time
import openapi_client
from openapi_client.api import colocation_service_chain_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = colocation_service_chain_api.ColocationServiceChainApi(api_client)
    pnf_device_type = "pnfDeviceType_example" # str | PNF device type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.getpnf_devices(pnf_device_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ColocationServiceChainApi->getpnf_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pnf_device_type** | **str**| PNF device type |

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

