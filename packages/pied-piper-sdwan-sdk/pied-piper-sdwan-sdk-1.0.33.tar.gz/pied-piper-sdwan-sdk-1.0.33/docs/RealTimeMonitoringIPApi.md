# openapi_client.RealTimeMonitoringIPApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fib_list**](RealTimeMonitoringIPApi.md#create_fib_list) | **GET** /device/ip/fib | 
[**create_ietf_routing_list**](RealTimeMonitoringIPApi.md#create_ietf_routing_list) | **GET** /device/ip/ipRoutes | 
[**create_ip_mfib_oil_list**](RealTimeMonitoringIPApi.md#create_ip_mfib_oil_list) | **GET** /device/ip/mfiboil | 
[**create_ip_mfib_stats_list**](RealTimeMonitoringIPApi.md#create_ip_mfib_stats_list) | **GET** /device/ip/mfibstats | 
[**create_ip_mfib_summary_list**](RealTimeMonitoringIPApi.md#create_ip_mfib_summary_list) | **GET** /device/ip/mfibsummary | 
[**create_nat64_translation_list**](RealTimeMonitoringIPApi.md#create_nat64_translation_list) | **GET** /device/ip/nat64/translation | 
[**create_nat_filter_list**](RealTimeMonitoringIPApi.md#create_nat_filter_list) | **GET** /device/ip/nat/filter | 
[**create_nat_interface_list**](RealTimeMonitoringIPApi.md#create_nat_interface_list) | **GET** /device/ip/nat/interface | 
[**create_nat_interface_statistics_list**](RealTimeMonitoringIPApi.md#create_nat_interface_statistics_list) | **GET** /device/ip/nat/interfacestatistics | 
[**create_nat_translation_list**](RealTimeMonitoringIPApi.md#create_nat_translation_list) | **GET** /device/ip/nat/translation | 
[**create_route_table_list**](RealTimeMonitoringIPApi.md#create_route_table_list) | **GET** /device/ip/routetable | 


# **create_fib_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_fib_list(device_id)



Get FIB list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id
    vpn_id = "0" # str | VPN Id (optional)
    address_family = "IPv4" # str | Address family (optional)
    prefix = "prefix_example" # str | IP prefix (optional)
    tloc = "tloc_example" # str | tloc IP (optional)
    color = "default" # str | tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_fib_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_fib_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_fib_list(device_id, vpn_id=vpn_id, address_family=address_family, prefix=prefix, tloc=tloc, color=color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_fib_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **address_family** | **str**| Address family | [optional]
 **prefix** | **str**| IP prefix | [optional]
 **tloc** | **str**| tloc IP | [optional]
 **color** | **str**| tloc color | [optional]

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

# **create_ietf_routing_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_ietf_routing_list(device_id)



Get ietf routing list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id
    routing_instance_name = "routing-instance-name_example" # str | VPN Id (optional)
    address_family = "address-family_example" # str | Address family (optional)
    outgoing_interface = "outgoing-interface_example" # str | Outgoing Interface (optional)
    source_protocol = "source-protocol_example" # str | Source Protocol (optional)
    next_hop_address = "next-hop-address_example" # str | Next Hop Address (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ietf_routing_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_ietf_routing_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_ietf_routing_list(device_id, routing_instance_name=routing_instance_name, address_family=address_family, outgoing_interface=outgoing_interface, source_protocol=source_protocol, next_hop_address=next_hop_address)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_ietf_routing_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **routing_instance_name** | **str**| VPN Id | [optional]
 **address_family** | **str**| Address family | [optional]
 **outgoing_interface** | **str**| Outgoing Interface | [optional]
 **source_protocol** | **str**| Source Protocol | [optional]
 **next_hop_address** | **str**| Next Hop Address | [optional]

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

# **create_ip_mfib_oil_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_ip_mfib_oil_list(device_id)



Get IP MFIB OIL list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ip_mfib_oil_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_ip_mfib_oil_list: %s\n" % e)
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

# **create_ip_mfib_stats_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_ip_mfib_stats_list(device_id)



Get IP MFIB statistics list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ip_mfib_stats_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_ip_mfib_stats_list: %s\n" % e)
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

# **create_ip_mfib_summary_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_ip_mfib_summary_list(device_id)



Get IP MFIB summary list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ip_mfib_summary_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_ip_mfib_summary_list: %s\n" % e)
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

# **create_nat64_translation_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_nat64_translation_list(device_id)



Get NAT64 interface list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_nat64_translation_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_nat64_translation_list: %s\n" % e)
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

# **create_nat_filter_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_nat_filter_list(device_id)



Get NAT filter list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id
    nat_vpn_id = "nat-vpn-id_example" # str | NAT VPN Id (optional)
    nat_ifname = "nat-ifname_example" # str | NAT interface name (optional)
    private_source_address = "private-source-address_example" # str | Private source address (optional)
    proto = "icm" # str | Protocol (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_nat_filter_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_nat_filter_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_nat_filter_list(device_id, nat_vpn_id=nat_vpn_id, nat_ifname=nat_ifname, private_source_address=private_source_address, proto=proto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_nat_filter_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **nat_vpn_id** | **str**| NAT VPN Id | [optional]
 **nat_ifname** | **str**| NAT interface name | [optional]
 **private_source_address** | **str**| Private source address | [optional]
 **proto** | **str**| Protocol | [optional]

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

# **create_nat_interface_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_nat_interface_list(device_id)



Get NAT interface list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_nat_interface_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_nat_interface_list: %s\n" % e)
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

# **create_nat_interface_statistics_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_nat_interface_statistics_list(device_id)



Get NAT interface statistics list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_nat_interface_statistics_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_nat_interface_statistics_list: %s\n" % e)
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

# **create_nat_translation_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_nat_translation_list(device_id)



Get NAT translation list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_nat_translation_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_nat_translation_list: %s\n" % e)
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

# **create_route_table_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_route_table_list(device_id)



Get route table list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ip_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ip_api.RealTimeMonitoringIPApi(api_client)
    device_id = "00r252U250?250" # str | Device Id
    vpn_id = "0" # str | VPN Id (optional)
    address_family = "IPv4" # str | Address family (optional)
    prefix = "prefix_example" # str | IP prefix (optional)
    protocol = "protocol_example" # str | IP protocol (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_route_table_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_route_table_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_route_table_list(device_id, vpn_id=vpn_id, address_family=address_family, prefix=prefix, protocol=protocol)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPApi->create_route_table_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **address_family** | **str**| Address family | [optional]
 **prefix** | **str**| IP prefix | [optional]
 **protocol** | **str**| IP protocol | [optional]

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

