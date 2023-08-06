# openapi_client.ConfigurationTopologyApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_topology**](ConfigurationTopologyApi.md#create_device_topology) | **GET** /topology/device | 
[**create_full_topology**](ConfigurationTopologyApi.md#create_full_topology) | **GET** /topology | 
[**create_physical_topology**](ConfigurationTopologyApi.md#create_physical_topology) | **GET** /topology/physical | 
[**get_site_topology**](ConfigurationTopologyApi.md#get_site_topology) | **GET** /topology/device/site/{siteId} | 


# **create_device_topology**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_device_topology(device_id)



Create device topology

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_topology_api
from openapi_client.model.device_ip import DeviceIP
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_topology_api.ConfigurationTopologyApi(api_client)
    device_id = [
        DeviceIP(
            device_ip="device_ip_example",
        ),
    ] # [DeviceIP] | Device Id list

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_device_topology(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTopologyApi->create_device_topology: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**[DeviceIP]**](DeviceIP.md)| Device Id list |

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

# **create_full_topology**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_full_topology()



Create full topology

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_topology_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_topology_api.ConfigurationTopologyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_full_topology()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTopologyApi->create_full_topology: %s\n" % e)
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

# **create_physical_topology**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_physical_topology(device_id)



Create pysical topology

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_topology_api
from openapi_client.model.device_ip import DeviceIP
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_topology_api.ConfigurationTopologyApi(api_client)
    device_id = [
        DeviceIP(
            device_ip="device_ip_example",
        ),
    ] # [DeviceIP] | Device Id list

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_physical_topology(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTopologyApi->create_physical_topology: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**[DeviceIP]**](DeviceIP.md)| Device Id list |

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

# **get_site_topology**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_site_topology(site_id)



Get topology for a given site id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_topology_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_topology_api.ConfigurationTopologyApi(api_client)
    site_id = "siteId_example" # str | Site Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_site_topology(site_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTopologyApi->get_site_topology: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Id |

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

