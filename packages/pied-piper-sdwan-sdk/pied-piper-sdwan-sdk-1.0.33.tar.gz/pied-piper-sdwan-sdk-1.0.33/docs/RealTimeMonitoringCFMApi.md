# openapi_client.RealTimeMonitoringCFMApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mp_database**](RealTimeMonitoringCFMApi.md#get_mp_database) | **GET** /device/cfm/mp/database | 
[**get_mp_local_mep**](RealTimeMonitoringCFMApi.md#get_mp_local_mep) | **GET** /device/cfm/mp/local/mep | 
[**get_mp_local_mip**](RealTimeMonitoringCFMApi.md#get_mp_local_mip) | **GET** /device/cfm/mp/local/mip | 
[**get_mp_remote_mep**](RealTimeMonitoringCFMApi.md#get_mp_remote_mep) | **GET** /device/cfm/mp/remotemep | 


# **get_mp_database**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mp_database(device_id)



Get mp database from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cfm_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cfm_api.RealTimeMonitoringCFMApi(api_client)
    device_id = "00r252U250?250" # str | Device IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_mp_database(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCFMApi->get_mp_database: %s\n" % e)
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

# **get_mp_local_mep**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mp_local_mep(device_id)



Get mp local mep from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cfm_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cfm_api.RealTimeMonitoringCFMApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    domain = "domain_example" # str | Domain Name (optional)
    service = "service_example" # str | Service Name (optional)
    mep_id = 3.14 # float | MEP ID (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_mp_local_mep(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCFMApi->get_mp_local_mep: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_mp_local_mep(device_id, domain=domain, service=service, mep_id=mep_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCFMApi->get_mp_local_mep: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **domain** | **str**| Domain Name | [optional]
 **service** | **str**| Service Name | [optional]
 **mep_id** | **float**| MEP ID | [optional]

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

# **get_mp_local_mip**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mp_local_mip(device_id)



Get mp local mip from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cfm_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cfm_api.RealTimeMonitoringCFMApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    level = 3.14 # float | Level (optional)
    port = "port_example" # str | Port (optional)
    svc_inst = 3.14 # float | Service Instance (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_mp_local_mip(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCFMApi->get_mp_local_mip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_mp_local_mip(device_id, level=level, port=port, svc_inst=svc_inst)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCFMApi->get_mp_local_mip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **level** | **float**| Level | [optional]
 **port** | **str**| Port | [optional]
 **svc_inst** | **float**| Service Instance | [optional]

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

# **get_mp_remote_mep**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mp_remote_mep(device_id)



Get mp remote mep from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cfm_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cfm_api.RealTimeMonitoringCFMApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    domain = "domain_example" # str | Domain Name (optional)
    service = "service_example" # str | Service Name (optional)
    local_mep_id = 3.14 # float | Local MEP ID (optional)
    remote_mep_id = 3.14 # float | Remote MEP ID (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_mp_remote_mep(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCFMApi->get_mp_remote_mep: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_mp_remote_mep(device_id, domain=domain, service=service, local_mep_id=local_mep_id, remote_mep_id=remote_mep_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCFMApi->get_mp_remote_mep: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **domain** | **str**| Domain Name | [optional]
 **service** | **str**| Service Name | [optional]
 **local_mep_id** | **float**| Local MEP ID | [optional]
 **remote_mep_id** | **float**| Remote MEP ID | [optional]

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

