# openapi_client.RealTimeMonitoringDPIApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dpi_collector_list**](RealTimeMonitoringDPIApi.md#create_dpi_collector_list) | **GET** /device/dpi/applications | 
[**create_dpi_flows_list**](RealTimeMonitoringDPIApi.md#create_dpi_flows_list) | **GET** /device/dpi/flows | 
[**create_dpi_statistics**](RealTimeMonitoringDPIApi.md#create_dpi_statistics) | **GET** /device/dpi/supported-applications | 
[**create_dpi_summary_real_time**](RealTimeMonitoringDPIApi.md#create_dpi_summary_real_time) | **GET** /device/dpi/summary | 
[**get_common_application_list**](RealTimeMonitoringDPIApi.md#get_common_application_list) | **GET** /device/dpi/common/applications | 
[**get_dpi_device_details_field_json**](RealTimeMonitoringDPIApi.md#get_dpi_device_details_field_json) | **GET** /device/dpi/devicedetails/fields | 
[**get_dpi_device_field_json**](RealTimeMonitoringDPIApi.md#get_dpi_device_field_json) | **GET** /device/dpi/application/fields | 
[**get_dpi_field_json**](RealTimeMonitoringDPIApi.md#get_dpi_field_json) | **GET** /device/dpi/device/fields | 
[**get_qosmos_application_list**](RealTimeMonitoringDPIApi.md#get_qosmos_application_list) | **GET** /device/dpi/qosmos/applications | 


# **create_dpi_collector_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_dpi_collector_list(device_id)



Get DPI applications from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dpi_api.RealTimeMonitoringDPIApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "0" # str | VPN Id (optional)
    application = "application_example" # str | Application (optional)
    family = "family_example" # str | Family (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dpi_collector_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->create_dpi_collector_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_dpi_collector_list(device_id, vpn_id=vpn_id, application=application, family=family)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->create_dpi_collector_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **application** | **str**| Application | [optional]
 **family** | **str**| Family | [optional]

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

# **create_dpi_flows_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_dpi_flows_list(device_id)



Get DPI flow list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dpi_api.RealTimeMonitoringDPIApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    vpn_id = "0" # str | VPN Id (optional)
    src_ip = "src-ip_example" # str | Source IP (optional)
    application = "application_example" # str | Application (optional)
    family = "family_example" # str | Family (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dpi_flows_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->create_dpi_flows_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_dpi_flows_list(device_id, vpn_id=vpn_id, src_ip=src_ip, application=application, family=family)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->create_dpi_flows_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **src_ip** | **str**| Source IP | [optional]
 **application** | **str**| Application | [optional]
 **family** | **str**| Family | [optional]

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

# **create_dpi_statistics**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] create_dpi_statistics(device_id)



Get supported applications from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dpi_api.RealTimeMonitoringDPIApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    application = "application_example" # str | Application (optional)
    family = "family_example" # str | Family (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dpi_statistics(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->create_dpi_statistics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_dpi_statistics(device_id, application=application, family=family)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->create_dpi_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **application** | **str**| Application | [optional]
 **family** | **str**| Family | [optional]

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

# **create_dpi_summary_real_time**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_dpi_summary_real_time(device_id)



Get DPI summary from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dpi_api.RealTimeMonitoringDPIApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dpi_summary_real_time(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->create_dpi_summary_real_time: %s\n" % e)
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

# **get_common_application_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_common_application_list()



Get DPI common application list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dpi_api.RealTimeMonitoringDPIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_common_application_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->get_common_application_list: %s\n" % e)
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

# **get_dpi_device_details_field_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dpi_device_details_field_json()



Get DPI detailed field from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dpi_api.RealTimeMonitoringDPIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_dpi_device_details_field_json()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->get_dpi_device_details_field_json: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_dpi_device_field_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dpi_device_field_json()



Get DPI query field from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dpi_api.RealTimeMonitoringDPIApi(api_client)
    is_device_dash_board = False # bool | Flag whether is device dashboard request (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_dpi_device_field_json(is_device_dash_board=is_device_dash_board)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->get_dpi_device_field_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_device_dash_board** | **bool**| Flag whether is device dashboard request | [optional] if omitted the server will use the default value of False

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

# **get_dpi_field_json**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dpi_field_json()



Get DPI field from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dpi_api.RealTimeMonitoringDPIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_dpi_field_json()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->get_dpi_field_json: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_qosmos_application_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_qosmos_application_list()



Get DPI QoSMos application list from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_dpi_api.RealTimeMonitoringDPIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_qosmos_application_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringDPIApi->get_qosmos_application_list: %s\n" % e)
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

