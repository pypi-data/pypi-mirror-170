# openapi_client.RealTimeMonitoringIPsecApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_crypto_ipsec_identity**](RealTimeMonitoringIPsecApi.md#create_crypto_ipsec_identity) | **GET** /device/ipsec/identity | 
[**create_cryptov1_local_sa_list**](RealTimeMonitoringIPsecApi.md#create_cryptov1_local_sa_list) | **GET** /device/ipsec/ikev1 | 
[**create_cryptov2_local_sa_list**](RealTimeMonitoringIPsecApi.md#create_cryptov2_local_sa_list) | **GET** /device/ipsec/ikev2 | 
[**create_i_psec_pwk_inbound_connections**](RealTimeMonitoringIPsecApi.md#create_i_psec_pwk_inbound_connections) | **GET** /device/ipsec/pwk/inbound | 
[**create_i_psec_pwk_local_sa**](RealTimeMonitoringIPsecApi.md#create_i_psec_pwk_local_sa) | **GET** /device/ipsec/pwk/localsa | 
[**create_i_psec_pwk_outbound_connections**](RealTimeMonitoringIPsecApi.md#create_i_psec_pwk_outbound_connections) | **GET** /device/ipsec/pwk/outbound | 
[**create_ike_inbound_list**](RealTimeMonitoringIPsecApi.md#create_ike_inbound_list) | **GET** /device/ipsec/ike/inbound | 
[**create_ike_outbound_list**](RealTimeMonitoringIPsecApi.md#create_ike_outbound_list) | **GET** /device/ipsec/ike/outbound | 
[**create_ike_sessions**](RealTimeMonitoringIPsecApi.md#create_ike_sessions) | **GET** /device/ipsec/ike/sessions | 
[**create_in_bound_list**](RealTimeMonitoringIPsecApi.md#create_in_bound_list) | **GET** /device/ipsec/inbound | 
[**create_local_sa_list**](RealTimeMonitoringIPsecApi.md#create_local_sa_list) | **GET** /device/ipsec/localsa | 
[**create_out_bound_list**](RealTimeMonitoringIPsecApi.md#create_out_bound_list) | **GET** /device/ipsec/outbound | 


# **create_crypto_ipsec_identity**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_crypto_ipsec_identity(device_id)



Get Crypto IPSEC identity entry from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_tloc_address = "remote-tloc-address_example" # str | Remote TLOC address (optional)
    remote_tloc_color = "default" # str | Remote tloc color (optional)
    local_tloc_color = "default" # str | Local tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_crypto_ipsec_identity(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_crypto_ipsec_identity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_crypto_ipsec_identity(device_id, remote_tloc_address=remote_tloc_address, remote_tloc_color=remote_tloc_color, local_tloc_color=local_tloc_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_crypto_ipsec_identity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_tloc_address** | **str**| Remote TLOC address | [optional]
 **remote_tloc_color** | **str**| Remote tloc color | [optional]
 **local_tloc_color** | **str**| Local tloc color | [optional]

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

# **create_cryptov1_local_sa_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cryptov1_local_sa_list(device_id)



Get Crypto IKEv1 SA entry from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_tloc_address = "remote-tloc-address_example" # str | Remote TLOC address (optional)
    remote_tloc_color = "default" # str | Remote tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cryptov1_local_sa_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_cryptov1_local_sa_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cryptov1_local_sa_list(device_id, remote_tloc_address=remote_tloc_address, remote_tloc_color=remote_tloc_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_cryptov1_local_sa_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_tloc_address** | **str**| Remote TLOC address | [optional]
 **remote_tloc_color** | **str**| Remote tloc color | [optional]

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

# **create_cryptov2_local_sa_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cryptov2_local_sa_list(device_id)



Get Crypto IKEv2 SA entry from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cryptov2_local_sa_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_cryptov2_local_sa_list: %s\n" % e)
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

# **create_i_psec_pwk_inbound_connections**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_i_psec_pwk_inbound_connections(device_id)



Get IPSEC pairwise key inbound entry from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_tloc_address = "remote-tloc-address_example" # str | Remote TLOC address (optional)
    remote_tloc_color = "default" # str | Remote tloc color (optional)
    local_tloc_color = "default" # str | Local tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_i_psec_pwk_inbound_connections(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_i_psec_pwk_inbound_connections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_i_psec_pwk_inbound_connections(device_id, remote_tloc_address=remote_tloc_address, remote_tloc_color=remote_tloc_color, local_tloc_color=local_tloc_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_i_psec_pwk_inbound_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_tloc_address** | **str**| Remote TLOC address | [optional]
 **remote_tloc_color** | **str**| Remote tloc color | [optional]
 **local_tloc_color** | **str**| Local tloc color | [optional]

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

# **create_i_psec_pwk_local_sa**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_i_psec_pwk_local_sa(device_id)



Get IPSEC pairwise key local SA  entry from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_tloc_address = "remote-tloc-address_example" # str | Remote TLOC address (optional)
    remote_tloc_color = "default" # str | Remote tloc color (optional)
    local_tloc_color = "default" # str | Local tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_i_psec_pwk_local_sa(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_i_psec_pwk_local_sa: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_i_psec_pwk_local_sa(device_id, remote_tloc_address=remote_tloc_address, remote_tloc_color=remote_tloc_color, local_tloc_color=local_tloc_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_i_psec_pwk_local_sa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_tloc_address** | **str**| Remote TLOC address | [optional]
 **remote_tloc_color** | **str**| Remote tloc color | [optional]
 **local_tloc_color** | **str**| Local tloc color | [optional]

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

# **create_i_psec_pwk_outbound_connections**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_i_psec_pwk_outbound_connections(device_id)



Get IPSEC pairwise key outbound entry from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_tloc_address = "remote-tloc-address_example" # str | Remote TLOC address (optional)
    remote_tloc_color = "default" # str | Remote tloc color (optional)
    local_tloc_color = "default" # str | Local tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_i_psec_pwk_outbound_connections(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_i_psec_pwk_outbound_connections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_i_psec_pwk_outbound_connections(device_id, remote_tloc_address=remote_tloc_address, remote_tloc_color=remote_tloc_color, local_tloc_color=local_tloc_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_i_psec_pwk_outbound_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_tloc_address** | **str**| Remote TLOC address | [optional]
 **remote_tloc_color** | **str**| Remote tloc color | [optional]
 **local_tloc_color** | **str**| Local tloc color | [optional]

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

# **create_ike_inbound_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_ike_inbound_list(device_id)



Get IPsec IKE inbound connection list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ike_inbound_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_ike_inbound_list: %s\n" % e)
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

# **create_ike_outbound_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_ike_outbound_list(device_id)



Get IPsec IKE outbound connection list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ike_outbound_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_ike_outbound_list: %s\n" % e)
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

# **create_ike_sessions**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_ike_sessions(device_id)



Get IPsec IKE sessions from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_tloc_address = "remote-tloc-address_example" # str | Remote TLOC address (optional)
    remote_tloc_color = "default" # str | Remote tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ike_sessions(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_ike_sessions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_ike_sessions(device_id, remote_tloc_address=remote_tloc_address, remote_tloc_color=remote_tloc_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_ike_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_tloc_address** | **str**| Remote TLOC address | [optional]
 **remote_tloc_color** | **str**| Remote tloc color | [optional]

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

# **create_in_bound_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_in_bound_list(device_id)



Get IPsec inbound connection list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_tloc_address = "remote-tloc-address_example" # str | Remote TLOC address (optional)
    remote_tloc_color = "default" # str | Remote tloc color (optional)
    local_tloc_color = "default" # str | Local tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_in_bound_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_in_bound_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_in_bound_list(device_id, remote_tloc_address=remote_tloc_address, remote_tloc_color=remote_tloc_color, local_tloc_color=local_tloc_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_in_bound_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_tloc_address** | **str**| Remote TLOC address | [optional]
 **remote_tloc_color** | **str**| Remote tloc color | [optional]
 **local_tloc_color** | **str**| Local tloc color | [optional]

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

# **create_local_sa_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_local_sa_list(device_id)



Get IPsec local SA list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_local_sa_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_local_sa_list: %s\n" % e)
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

# **create_out_bound_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_out_bound_list(device_id)



Get IPsec outbound connection list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_i_psec_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_i_psec_api.RealTimeMonitoringIPsecApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    remote_tloc_address = "remote-tloc-address_example" # str | Remote TLOC address (optional)
    remote_tloc_color = "default" # str | Remote tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_out_bound_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_out_bound_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_out_bound_list(device_id, remote_tloc_address=remote_tloc_address, remote_tloc_color=remote_tloc_color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPsecApi->create_out_bound_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **remote_tloc_address** | **str**| Remote TLOC address | [optional]
 **remote_tloc_color** | **str**| Remote tloc color | [optional]

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

