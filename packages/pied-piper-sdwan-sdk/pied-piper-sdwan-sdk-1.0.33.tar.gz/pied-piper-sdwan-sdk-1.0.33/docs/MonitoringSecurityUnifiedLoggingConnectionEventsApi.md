# openapi_client.MonitoringSecurityUnifiedLoggingConnectionEventsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregation_data_by_query14**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_aggregation_data_by_query14) | **GET** /statistics/sul/connections/aggregation | 
[**get_count16**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_count16) | **GET** /statistics/sul/connections/doccount | 
[**get_count_post16**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_count_post16) | **POST** /statistics/sul/connections/doccount | 
[**get_filter_policy_name_list**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_filter_policy_name_list) | **GET** /statistics/sul/connections/filter/policy_name/{policyType} | 
[**get_post_aggregation_app_data_by_query13**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_post_aggregation_app_data_by_query13) | **POST** /statistics/sul/connections/app-agg/aggregation | 
[**get_post_aggregation_data_by_query13**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_post_aggregation_data_by_query13) | **POST** /statistics/sul/connections/aggregation | 
[**get_post_stat_bulk_raw_data14**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_post_stat_bulk_raw_data14) | **POST** /statistics/sul/connections/page | 
[**get_stat_bulk_raw_data14**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_stat_bulk_raw_data14) | **GET** /statistics/sul/connections/page | 
[**get_stat_data_fields16**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_stat_data_fields16) | **GET** /statistics/sul/connections/fields | 
[**get_stat_data_raw_data_as_csv14**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_stat_data_raw_data_as_csv14) | **GET** /statistics/sul/connections/csv | 
[**get_stat_query_fields16**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_stat_query_fields16) | **GET** /statistics/sul/connections/query/fields | 
[**get_stats_raw_data14**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_stats_raw_data14) | **POST** /statistics/sul/connections | 
[**get_sul_stat_data_raw_data**](MonitoringSecurityUnifiedLoggingConnectionEventsApi.md#get_sul_stat_data_raw_data) | **GET** /statistics/sul/connections | 


# **get_aggregation_data_by_query14**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_by_query14()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["24"],"field":"entry_time","type":"date","operator":"last_n_hours"},{"value":["172.16.255.15"],"field":"vdevice_name","type":"string","operator":"in"}]}}" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_by_query14(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_aggregation_data_by_query14: %s\n" % e)
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

# **get_count16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count16(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["24"],"field":"entry_time","type":"date","operator":"last_n_hours"},{"value":["172.16.255.15"],"field":"vdevice_name","type":"string","operator":"in"}]}}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count16(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_count16: %s\n" % e)
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

# **get_count_post16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post16()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post16(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_count_post16: %s\n" % e)
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

# **get_filter_policy_name_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_filter_policy_name_list(policy_type, query)



Get filter Policy Name list

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    policy_type = "zoneBasedFW" # str | Policy type
    query = "{"query":{"condition":"AND","rules":[{"field":"vdevice_name","type":"string","operator":"in","value":["172.16.255.15"]}]}}" # str | query string

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_filter_policy_name_list(policy_type, query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_filter_policy_name_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_type** | **str**| Policy type |
 **query** | **str**| query string |

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

# **get_post_aggregation_app_data_by_query13**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_app_data_by_query13()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_app_data_by_query13(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_post_aggregation_app_data_by_query13: %s\n" % e)
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

# **get_post_aggregation_data_by_query13**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_data_by_query13()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_data_by_query13(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_post_aggregation_data_by_query13: %s\n" % e)
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

# **get_post_stat_bulk_raw_data14**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_raw_data14()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_raw_data14(scroll_id=scroll_id, count=count, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_post_stat_bulk_raw_data14: %s\n" % e)
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

# **get_stat_bulk_raw_data14**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_raw_data14()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["168"],"field":"entry_time","type":"date","operator":"last_n_hours"},{"value":["1"],"field":"vpn_id","type":"int","operator":"in"},{"value":["p1"],"field":"fw_policy","type":"string","operator":"in"},{"value":["172.16.255.15"],"field":"vdevice_name","type":"string","operator":"in"}]}}" # str | Query string (optional)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_bulk_raw_data14(query=query, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_stat_bulk_raw_data14: %s\n" % e)
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

# **get_stat_data_fields16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields16()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields16()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_stat_data_fields16: %s\n" % e)
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

# **get_stat_data_raw_data_as_csv14**
> str get_stat_data_raw_data_as_csv14()



Get raw data with optional query as CSV

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["168"],"field":"entry_time","type":"date","operator":"last_n_hours"},{"value":["1"],"field":"vpn_id","type":"int","operator":"in"},{"value":["p1"],"field":"fw_policy","type":"string","operator":"in"},{"value":["172.16.255.15"],"field":"vdevice_name","type":"string","operator":"in"}]}}" # str | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data_as_csv14(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_stat_data_raw_data_as_csv14: %s\n" % e)
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

# **get_stat_query_fields16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields16()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields16()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_stat_query_fields16: %s\n" % e)
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

# **get_stats_raw_data14**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_raw_data14()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats_raw_data14(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_stats_raw_data14: %s\n" % e)
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

# **get_sul_stat_data_raw_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_sul_stat_data_raw_data()



Get security connection events stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_security_unified_logging_connection_events_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_security_unified_logging_connection_events_api.MonitoringSecurityUnifiedLoggingConnectionEventsApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["24"],"field":"entry_time","type":"date","operator":"last_n_hours"},{"value":["172.16.255.15"],"field":"vdevice_name","type":"string","operator":"in"}]}}" # str | Query string (optional)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sul_stat_data_raw_data(query=query, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringSecurityUnifiedLoggingConnectionEventsApi->get_sul_stat_data_raw_data: %s\n" % e)
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

