# openapi_client.RealTimeMonitoringInterfaceApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_device_interface_vpn**](RealTimeMonitoringInterfaceApi.md#generate_device_interface_vpn) | **GET** /device/interface/vpn | 
[**get_device_interface**](RealTimeMonitoringInterfaceApi.md#get_device_interface) | **GET** /device/interface | 
[**get_device_interface_arp_stats**](RealTimeMonitoringInterfaceApi.md#get_device_interface_arp_stats) | **GET** /device/interface/arp_stats | 
[**get_device_interface_error_stats**](RealTimeMonitoringInterfaceApi.md#get_device_interface_error_stats) | **GET** /device/interface/error_stats | 
[**get_device_interface_ipv6_stats**](RealTimeMonitoringInterfaceApi.md#get_device_interface_ipv6_stats) | **GET** /device/interface/ipv6Stats | 
[**get_device_interface_pkt_sizes**](RealTimeMonitoringInterfaceApi.md#get_device_interface_pkt_sizes) | **GET** /device/interface/pkt_size | 
[**get_device_interface_port_stats**](RealTimeMonitoringInterfaceApi.md#get_device_interface_port_stats) | **GET** /device/interface/port_stats | 
[**get_device_interface_qos_stats**](RealTimeMonitoringInterfaceApi.md#get_device_interface_qos_stats) | **GET** /device/interface/qosStats | 
[**get_device_interface_queue_stats**](RealTimeMonitoringInterfaceApi.md#get_device_interface_queue_stats) | **GET** /device/interface/queue_stats | 
[**get_device_interface_stats**](RealTimeMonitoringInterfaceApi.md#get_device_interface_stats) | **GET** /device/interface/stats | 
[**get_device_serial_interface**](RealTimeMonitoringInterfaceApi.md#get_device_serial_interface) | **GET** /device/interface/serial | 
[**get_synced_device_interface**](RealTimeMonitoringInterfaceApi.md#get_synced_device_interface) | **GET** /device/interface/synced | 
[**trustsec**](RealTimeMonitoringInterfaceApi.md#trustsec) | **GET** /device/interface/trustsec | 


# **generate_device_interface_vpn**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_device_interface_vpn(device_id)



Get device interfaces per VPN

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_device_interface_vpn(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->generate_device_interface_vpn: %s\n" % e)
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

# **get_device_interface**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_interface(af_type, device_id)



Get device interfaces

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_interface(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_interface(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_device_interface_arp_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_interface_arp_stats(af_type, device_id)



Get interface ARP statistics

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_interface_arp_stats(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_arp_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_interface_arp_stats(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_arp_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_device_interface_error_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_interface_error_stats(af_type, device_id)



Get interface error stats

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_interface_error_stats(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_error_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_interface_error_stats(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_error_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_device_interface_ipv6_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_interface_ipv6_stats(af_type, device_id)



Get interface IPv6 stats

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_interface_ipv6_stats(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_ipv6_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_interface_ipv6_stats(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_ipv6_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_device_interface_pkt_sizes**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_interface_pkt_sizes(af_type, device_id)



Get interface packet size

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_interface_pkt_sizes(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_pkt_sizes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_interface_pkt_sizes(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_pkt_sizes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_device_interface_port_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_interface_port_stats(af_type, device_id)



Get interface port stats

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_interface_port_stats(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_port_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_interface_port_stats(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_port_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_device_interface_qos_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_interface_qos_stats(af_type, device_id)



Get interface QOS stats

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_interface_qos_stats(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_qos_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_interface_qos_stats(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_qos_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_device_interface_queue_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_interface_queue_stats(af_type, device_id)



Get interface queue stats

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_interface_queue_stats(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_queue_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_interface_queue_stats(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_queue_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_device_interface_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_interface_stats(af_type, device_id)



Get interface stats

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_interface_stats(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_interface_stats(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_interface_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_device_serial_interface**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_serial_interface(af_type, device_id)



Get serial interface

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_serial_interface(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_serial_interface: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_serial_interface(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_device_serial_interface: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **get_synced_device_interface**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_synced_device_interface(af_type, device_id)



Get device interfaces synchronously

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    af_type = "ipv4" # str | AF Type
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "vpn-id_example" # str | VPN Id (optional)
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_synced_device_interface(af_type, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_synced_device_interface: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_synced_device_interface(af_type, device_id, vpn_id=vpn_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->get_synced_device_interface: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **af_type** | **str**| AF Type |
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **ifname** | **str**| IF Name | [optional]

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

# **trustsec**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} trustsec(device_id)



Get policy filter memory usage from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_interface_api.RealTimeMonitoringInterfaceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.trustsec(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringInterfaceApi->trustsec: %s\n" % e)
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

