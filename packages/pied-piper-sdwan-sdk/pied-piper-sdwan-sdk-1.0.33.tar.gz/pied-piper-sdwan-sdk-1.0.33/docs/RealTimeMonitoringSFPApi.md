# openapi_client.RealTimeMonitoringSFPApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_detail**](RealTimeMonitoringSFPApi.md#get_detail) | **GET** /device/sfp/detail | 
[**get_diagnostic**](RealTimeMonitoringSFPApi.md#get_diagnostic) | **GET** /device/sfp/diagnostic | 
[**get_diagnostic_measurement_alarm**](RealTimeMonitoringSFPApi.md#get_diagnostic_measurement_alarm) | **GET** /device/sfp/diagnosticMeasurementAlarm | 
[**get_diagnostic_measurement_value**](RealTimeMonitoringSFPApi.md#get_diagnostic_measurement_value) | **GET** /device/sfp/diagnosticMeasurementValue | 


# **get_detail**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_detail(device_id)



Get SFP detail

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_sfp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_sfp_api.RealTimeMonitoringSFPApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_detail(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSFPApi->get_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_detail(device_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSFPApi->get_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
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

# **get_diagnostic**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_diagnostic(device_id)



Get SFP diagnostic

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_sfp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_sfp_api.RealTimeMonitoringSFPApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_diagnostic(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSFPApi->get_diagnostic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_diagnostic(device_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSFPApi->get_diagnostic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
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

# **get_diagnostic_measurement_alarm**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_diagnostic_measurement_alarm(device_id)



Get SFP diagnostic measurement alarm

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_sfp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_sfp_api.RealTimeMonitoringSFPApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_diagnostic_measurement_alarm(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSFPApi->get_diagnostic_measurement_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_diagnostic_measurement_alarm(device_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSFPApi->get_diagnostic_measurement_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
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

# **get_diagnostic_measurement_value**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_diagnostic_measurement_value(device_id)



Get SFP diagnostic measurement value

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_sfp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_sfp_api.RealTimeMonitoringSFPApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    ifname = "ge0/0" # str | IF Name (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_diagnostic_measurement_value(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSFPApi->get_diagnostic_measurement_value: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_diagnostic_measurement_value(device_id, ifname=ifname)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringSFPApi->get_diagnostic_measurement_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
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

