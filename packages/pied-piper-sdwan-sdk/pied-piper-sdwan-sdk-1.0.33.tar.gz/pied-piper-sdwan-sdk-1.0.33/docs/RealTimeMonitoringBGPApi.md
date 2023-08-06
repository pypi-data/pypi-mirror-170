# openapi_client.RealTimeMonitoringBGPApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bgp_neighbors_list**](RealTimeMonitoringBGPApi.md#create_bgp_neighbors_list) | **GET** /device/bgp/neighbors | 
[**create_bgp_routes_list**](RealTimeMonitoringBGPApi.md#create_bgp_routes_list) | **GET** /device/bgp/routes | 
[**create_bgp_summary**](RealTimeMonitoringBGPApi.md#create_bgp_summary) | **GET** /device/bgp/summary | 


# **create_bgp_neighbors_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_bgp_neighbors_list(device_id)



Get BGP neighbors list (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bgp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bgp_api.RealTimeMonitoringBGPApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "0" # str | VPN Id (optional)
    peer_addr = "peer-addr_example" # str | Peer address (optional)
    _as = "as_example" # str | AS number (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_bgp_neighbors_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBGPApi->create_bgp_neighbors_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_bgp_neighbors_list(device_id, vpn_id=vpn_id, peer_addr=peer_addr, _as=_as)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBGPApi->create_bgp_neighbors_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **peer_addr** | **str**| Peer address | [optional]
 **_as** | **str**| AS number | [optional]

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

# **create_bgp_routes_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_bgp_routes_list(device_id)



Get BGP routes list (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bgp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bgp_api.RealTimeMonitoringBGPApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "0" # str | VPN Id (optional)
    prefix = "prefix_example" # str | IP prefix (optional)
    nexthop = "nexthop_example" # str | Next hop (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_bgp_routes_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBGPApi->create_bgp_routes_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_bgp_routes_list(device_id, vpn_id=vpn_id, prefix=prefix, nexthop=nexthop)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBGPApi->create_bgp_routes_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **prefix** | **str**| IP prefix | [optional]
 **nexthop** | **str**| Next hop | [optional]

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

# **create_bgp_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_bgp_summary(device_id)



Get BGP summary (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_bgp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_bgp_api.RealTimeMonitoringBGPApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_bgp_summary(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringBGPApi->create_bgp_summary: %s\n" % e)
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

