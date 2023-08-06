# openapi_client.RealTimeMonitoringVDSLServiceApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_co_line_specific_stats**](RealTimeMonitoringVDSLServiceApi.md#get_co_line_specific_stats) | **GET** /device/vdslService/coLineSpecificStats | 
[**get_co_stats**](RealTimeMonitoringVDSLServiceApi.md#get_co_stats) | **GET** /device/vdslService/coStats | 
[**get_cpe_line_specific_stats**](RealTimeMonitoringVDSLServiceApi.md#get_cpe_line_specific_stats) | **GET** /device/vdslService/cpeLineSpecificStats | 
[**get_cpe_stats**](RealTimeMonitoringVDSLServiceApi.md#get_cpe_stats) | **GET** /device/vdslService/cpeStats | 
[**get_line_bonding_stats**](RealTimeMonitoringVDSLServiceApi.md#get_line_bonding_stats) | **GET** /device/vdslService/lineBondingStats | 
[**get_line_specific_stats**](RealTimeMonitoringVDSLServiceApi.md#get_line_specific_stats) | **GET** /device/vdslService/lineSpecificStats | 
[**get_vdsl_info**](RealTimeMonitoringVDSLServiceApi.md#get_vdsl_info) | **GET** /device/vdslService/vdslInfo | 


# **get_co_line_specific_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_co_line_specific_stats(device_id)



Get VDSL service line bonding stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vdsl_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vdsl_service_api.RealTimeMonitoringVDSLServiceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_co_line_specific_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVDSLServiceApi->get_co_line_specific_stats: %s\n" % e)
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

# **get_co_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_co_stats(device_id)



Get CO stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vdsl_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vdsl_service_api.RealTimeMonitoringVDSLServiceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_co_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVDSLServiceApi->get_co_stats: %s\n" % e)
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

# **get_cpe_line_specific_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cpe_line_specific_stats(device_id)



Get VDSL service CPE line specific stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vdsl_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vdsl_service_api.RealTimeMonitoringVDSLServiceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cpe_line_specific_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVDSLServiceApi->get_cpe_line_specific_stats: %s\n" % e)
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

# **get_cpe_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cpe_stats(device_id)



Get CPE stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vdsl_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vdsl_service_api.RealTimeMonitoringVDSLServiceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cpe_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVDSLServiceApi->get_cpe_stats: %s\n" % e)
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

# **get_line_bonding_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_line_bonding_stats(device_id)



Get VDSL service line bonding stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vdsl_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vdsl_service_api.RealTimeMonitoringVDSLServiceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_line_bonding_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVDSLServiceApi->get_line_bonding_stats: %s\n" % e)
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

# **get_line_specific_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_line_specific_stats(device_id)



Get VDSL service line specific stats from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vdsl_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vdsl_service_api.RealTimeMonitoringVDSLServiceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_line_specific_stats(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVDSLServiceApi->get_line_specific_stats: %s\n" % e)
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

# **get_vdsl_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_vdsl_info(device_id)



Get VDSL info from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_vdsl_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_vdsl_service_api.RealTimeMonitoringVDSLServiceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vdsl_info(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringVDSLServiceApi->get_vdsl_info: %s\n" % e)
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

