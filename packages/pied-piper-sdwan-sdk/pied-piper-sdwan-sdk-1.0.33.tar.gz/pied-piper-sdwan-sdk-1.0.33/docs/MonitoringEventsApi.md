# openapi_client.MonitoringEventsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_events_query_config**](MonitoringEventsApi.md#create_events_query_config) | **GET** /event/query/input | 
[**enable_events_from_file**](MonitoringEventsApi.md#enable_events_from_file) | **GET** /event/enable/fileprocess | 
[**find_events**](MonitoringEventsApi.md#find_events) | **GET** /event/severity | 
[**get_aggregation_data_by_query25**](MonitoringEventsApi.md#get_aggregation_data_by_query25) | **GET** /event/aggregation | 
[**get_components_as_key_value**](MonitoringEventsApi.md#get_components_as_key_value) | **GET** /event/component/keyvalue | 
[**get_count27**](MonitoringEventsApi.md#get_count27) | **GET** /event/doccount | 
[**get_count_post27**](MonitoringEventsApi.md#get_count_post27) | **POST** /event/doccount | 
[**get_event_types_as_key_value**](MonitoringEventsApi.md#get_event_types_as_key_value) | **GET** /event/types/keyvalue | 
[**get_listeners_info**](MonitoringEventsApi.md#get_listeners_info) | **GET** /event/listeners | 
[**get_post_aggregation_app_data_by_query24**](MonitoringEventsApi.md#get_post_aggregation_app_data_by_query24) | **POST** /event/app-agg/aggregation | 
[**get_post_aggregation_data_by_query24**](MonitoringEventsApi.md#get_post_aggregation_data_by_query24) | **POST** /event/aggregation | 
[**get_post_stat_bulk_raw_data25**](MonitoringEventsApi.md#get_post_stat_bulk_raw_data25) | **POST** /event/page | 
[**get_severity_histogram**](MonitoringEventsApi.md#get_severity_histogram) | **GET** /event/severity/summary | 
[**get_stat_bulk_raw_data25**](MonitoringEventsApi.md#get_stat_bulk_raw_data25) | **GET** /event/page | 
[**get_stat_data_fields27**](MonitoringEventsApi.md#get_stat_data_fields27) | **GET** /event/fields | 
[**get_stat_data_raw_data24**](MonitoringEventsApi.md#get_stat_data_raw_data24) | **GET** /event | 
[**get_stat_data_raw_data_as_csv25**](MonitoringEventsApi.md#get_stat_data_raw_data_as_csv25) | **GET** /event/csv | 
[**get_stat_query_fields27**](MonitoringEventsApi.md#get_stat_query_fields27) | **GET** /event/query/fields | 
[**get_stats_raw_data25**](MonitoringEventsApi.md#get_stats_raw_data25) | **POST** /event | 


# **create_events_query_config**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_events_query_config()



Create query configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_events_query_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->create_events_query_config: %s\n" % e)
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

# **enable_events_from_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} enable_events_from_file()



Set enable events from file flag

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.enable_events_from_file()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->enable_events_from_file: %s\n" % e)
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

# **find_events**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_events(severity_level)



Retrieve events

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    severity_level = [
        "critical",
    ] # [str] | Severity level
    device_id = "00r252U250?250" # str | Device IP (optional)
    query = "query_example" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.find_events(severity_level)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->find_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.find_events(severity_level, device_id=device_id, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->find_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity_level** | **[str]**| Severity level |
 **device_id** | **str**| Device IP | [optional]
 **query** | **str**| Query filter | [optional]

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

# **get_aggregation_data_by_query25**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_by_query25()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_by_query25(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_aggregation_data_by_query25: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter | [optional]

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

# **get_components_as_key_value**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_components_as_key_value()



Retrieve components as key/value pairs

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_components_as_key_value()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_components_as_key_value: %s\n" % e)
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

# **get_count27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count27(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"]}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count27(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_count27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query |

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

# **get_count_post27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post27()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post27(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_count_post27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_types_as_key_value**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_event_types_as_key_value()



Retrieve event types as key/value pairs

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_event_types_as_key_value()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_event_types_as_key_value: %s\n" % e)
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

# **get_listeners_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_listeners_info()



Retrieve listener information

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_listeners_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_listeners_info: %s\n" % e)
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

# **get_post_aggregation_app_data_by_query24**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_app_data_by_query24()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_app_data_by_query24(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_post_aggregation_app_data_by_query24: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_aggregation_data_by_query24**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_data_by_query24()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_data_by_query24(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_post_aggregation_data_by_query24: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_stat_bulk_raw_data25**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_raw_data25()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_raw_data25(scroll_id=scroll_id, count=count, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_post_stat_bulk_raw_data25: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_severity_histogram**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_severity_histogram(device_id)



Retrieve severity histogram

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    device_id = "deviceId_example" # str | Device IP
    query = "00r252U250?250" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_severity_histogram(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_severity_histogram: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_severity_histogram(device_id, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_severity_histogram: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device IP |
 **query** | **str**| Query filter | [optional]

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

# **get_stat_bulk_raw_data25**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_raw_data25()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"]}" # str | Query string (optional)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_bulk_raw_data25(query=query, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_stat_bulk_raw_data25: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]

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

# **get_stat_data_fields27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields27()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields27()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_stat_data_fields27: %s\n" % e)
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

# **get_stat_data_raw_data24**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_raw_data24()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["2020-05-10T01:00:00 UTC","2020-05-10T01:30:00 UTC"],"field":"entry_time","type":"date","operator":"between"}]},"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data24(query=query, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_stat_data_raw_data24: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **sort_order** | **str**| sort order | [optional]

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

# **get_stat_data_raw_data_as_csv25**
> str get_stat_data_raw_data_as_csv25()



Get raw data with optional query as CSV

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1000,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data_as_csv25(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_stat_data_raw_data_as_csv25: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stat_query_fields27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields27()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields27()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_stat_query_fields27: %s\n" % e)
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

# **get_stats_raw_data25**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_raw_data25()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_events_api.MonitoringEventsApi(api_client)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats_raw_data25(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringEventsApi->get_stats_raw_data25: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **sort_order** | **str**| sort order | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

