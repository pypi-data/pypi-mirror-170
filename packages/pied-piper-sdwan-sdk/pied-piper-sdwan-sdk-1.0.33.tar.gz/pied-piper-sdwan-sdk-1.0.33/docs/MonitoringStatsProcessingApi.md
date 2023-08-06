# openapi_client.MonitoringStatsProcessingApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_statistics_demo_mode**](MonitoringStatsProcessingApi.md#enable_statistics_demo_mode) | **GET** /statistics/demomode | 
[**generate_stats_collect_thread_report**](MonitoringStatsProcessingApi.md#generate_stats_collect_thread_report) | **GET** /statistics/collect/thread/status | 
[**generate_stats_process_report**](MonitoringStatsProcessingApi.md#generate_stats_process_report) | **GET** /statistics/process/status | 
[**generate_stats_process_thread_report**](MonitoringStatsProcessingApi.md#generate_stats_process_thread_report) | **GET** /statistics/process/thread/status | 
[**get_statistic_type**](MonitoringStatsProcessingApi.md#get_statistic_type) | **GET** /statistics | 
[**get_statistics_processing_counters**](MonitoringStatsProcessingApi.md#get_statistics_processing_counters) | **GET** /statistics/process/counters | 
[**process_statistics_data**](MonitoringStatsProcessingApi.md#process_statistics_data) | **GET** /statistics/process | 
[**reset_stats_collection**](MonitoringStatsProcessingApi.md#reset_stats_collection) | **GET** /statistics/collection/reset/{processQueue} | 
[**start_stats_collection**](MonitoringStatsProcessingApi.md#start_stats_collection) | **GET** /statistics/collect | 


# **enable_statistics_demo_mode**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} enable_statistics_demo_mode()



Enable statistic demo mode

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_processing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_processing_api.MonitoringStatsProcessingApi(api_client)
    enable = True # bool | Demo mode flag (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.enable_statistics_demo_mode(enable=enable)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsProcessingApi->enable_statistics_demo_mode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable** | **bool**| Demo mode flag | [optional] if omitted the server will use the default value of True

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

# **generate_stats_collect_thread_report**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_stats_collect_thread_report()



Get stats collect thread report

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_processing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_processing_api.MonitoringStatsProcessingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_stats_collect_thread_report()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsProcessingApi->generate_stats_collect_thread_report: %s\n" % e)
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

# **generate_stats_process_report**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_stats_process_report()



Get stats process report

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_processing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_processing_api.MonitoringStatsProcessingApi(api_client)
    process_queue = 1 # int | Process queue (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_stats_process_report(process_queue=process_queue)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsProcessingApi->generate_stats_process_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_queue** | **int**| Process queue | [optional]

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

# **generate_stats_process_thread_report**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_stats_process_thread_report()



Get stats process thread report

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_processing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_processing_api.MonitoringStatsProcessingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_stats_process_thread_report()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsProcessingApi->generate_stats_process_thread_report: %s\n" % e)
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

# **get_statistic_type**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_statistic_type()



Get statistics types

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_processing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_processing_api.MonitoringStatsProcessingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_statistic_type()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsProcessingApi->get_statistic_type: %s\n" % e)
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

# **get_statistics_processing_counters**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_statistics_processing_counters()



Get statistics processing counters

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_processing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_processing_api.MonitoringStatsProcessingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_statistics_processing_counters()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsProcessingApi->get_statistics_processing_counters: %s\n" % e)
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

# **process_statistics_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} process_statistics_data()



Process stats data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_processing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_processing_api.MonitoringStatsProcessingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.process_statistics_data()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsProcessingApi->process_statistics_data: %s\n" % e)
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

# **reset_stats_collection**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} reset_stats_collection()



Reset stats collect thread report

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_processing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_processing_api.MonitoringStatsProcessingApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.reset_stats_collection()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsProcessingApi->reset_stats_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_queue** | **int**| Process queue | defaults to -1

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

# **start_stats_collection**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} start_stats_collection()



Start stats collect

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_processing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_processing_api.MonitoringStatsProcessingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.start_stats_collection()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsProcessingApi->start_stats_collection: %s\n" % e)
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

