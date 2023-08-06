# openapi_client.RealTimeMonitoringCloudExpressApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_applications_detail_list**](RealTimeMonitoringCloudExpressApi.md#create_applications_detail_list) | **GET** /device/cloudx/application/detail | 
[**create_applications_list**](RealTimeMonitoringCloudExpressApi.md#create_applications_list) | **GET** /device/cloudx/applications | 
[**create_gateway_exits_list**](RealTimeMonitoringCloudExpressApi.md#create_gateway_exits_list) | **GET** /device/cloudx/gatewayexits | 
[**create_lb_applications_list**](RealTimeMonitoringCloudExpressApi.md#create_lb_applications_list) | **GET** /device/cloudx/loadbalance | 
[**create_local_exits_list**](RealTimeMonitoringCloudExpressApi.md#create_local_exits_list) | **GET** /device/cloudx/localexits | 


# **create_applications_detail_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_applications_detail_list()



Get list of cloudexpress applications from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cloud_express_api.RealTimeMonitoringCloudExpressApi(api_client)
    vpn_id = "0" # str | VPN Id (optional)
    application = "application_example" # str | Application (optional)
    query = "query_example" # str | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_applications_detail_list(vpn_id=vpn_id, application=application, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCloudExpressApi->create_applications_detail_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_id** | **str**| VPN Id | [optional]
 **application** | **str**| Application | [optional]
 **query** | **str**| Query | [optional]

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

# **create_applications_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_applications_list()



Get list of cloudexpress applications from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cloud_express_api.RealTimeMonitoringCloudExpressApi(api_client)
    vpn_id = "0" # str | VPN Id (optional)
    application = "application_example" # str | Application (optional)
    query = "query_example" # str | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_applications_list(vpn_id=vpn_id, application=application, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCloudExpressApi->create_applications_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_id** | **str**| VPN Id | [optional]
 **application** | **str**| Application | [optional]
 **query** | **str**| Query | [optional]

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

# **create_gateway_exits_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_gateway_exits_list(device_id)



Get list of cloudexpress gateway exits from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cloud_express_api.RealTimeMonitoringCloudExpressApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    vpn_id = "0" # str | VPN Id (optional)
    application = "application_example" # str | Application (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_gateway_exits_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCloudExpressApi->create_gateway_exits_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_gateway_exits_list(device_id, vpn_id=vpn_id, application=application)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCloudExpressApi->create_gateway_exits_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **vpn_id** | **str**| VPN Id | [optional]
 **application** | **str**| Application | [optional]

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

# **create_lb_applications_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_lb_applications_list()



Get list of cloudexpress load balance applications from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cloud_express_api.RealTimeMonitoringCloudExpressApi(api_client)
    vpn_id = "0" # str | VPN Id (optional)
    application = "application_example" # str | Application (optional)
    query = "query_example" # str | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_lb_applications_list(vpn_id=vpn_id, application=application, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCloudExpressApi->create_lb_applications_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_id** | **str**| VPN Id | [optional]
 **application** | **str**| Application | [optional]
 **query** | **str**| Query | [optional]

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

# **create_local_exits_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_local_exits_list(device_id)



Get list of cloudexpress local exits from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cloud_express_api.RealTimeMonitoringCloudExpressApi(api_client)
    device_id = "00r252U250?250" # str | Device IP
    vpn_id = "0" # str | VPN Id (optional)
    application = "application_example" # str | Application (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_local_exits_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCloudExpressApi->create_local_exits_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_local_exits_list(device_id, vpn_id=vpn_id, application=application)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCloudExpressApi->create_local_exits_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **vpn_id** | **str**| VPN Id | [optional]
 **application** | **str**| Application | [optional]

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

