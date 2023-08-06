# openapi_client.AdministrationAuditLogApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_audit_log**](AdministrationAuditLogApi.md#generate_audit_log) | **GET** /auditlog/severity | 
[**get_audit_severity_custom_histogram**](AdministrationAuditLogApi.md#get_audit_severity_custom_histogram) | **GET** /auditlog/severity/summary | 
[**get_count**](AdministrationAuditLogApi.md#get_count) | **GET** /auditlog/doccount | 
[**get_count_post**](AdministrationAuditLogApi.md#get_count_post) | **POST** /auditlog/doccount | 
[**get_post_property_aggregation_data**](AdministrationAuditLogApi.md#get_post_property_aggregation_data) | **POST** /auditlog/aggregation | 
[**get_post_stat_bulk_raw_property_data**](AdministrationAuditLogApi.md#get_post_stat_bulk_raw_property_data) | **POST** /auditlog/page | 
[**get_property_aggregation_data**](AdministrationAuditLogApi.md#get_property_aggregation_data) | **GET** /auditlog/aggregation | 
[**get_raw_property_data**](AdministrationAuditLogApi.md#get_raw_property_data) | **POST** /auditlog | 
[**get_stat_bulk_raw_property_data**](AdministrationAuditLogApi.md#get_stat_bulk_raw_property_data) | **GET** /auditlog/page | 
[**get_stat_data_fields**](AdministrationAuditLogApi.md#get_stat_data_fields) | **GET** /auditlog/fields | 
[**get_stat_data_raw_audit_log_data**](AdministrationAuditLogApi.md#get_stat_data_raw_audit_log_data) | **GET** /auditlog | 
[**get_stat_query_fields**](AdministrationAuditLogApi.md#get_stat_query_fields) | **GET** /auditlog/query/fields | 


# **generate_audit_log**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_audit_log()



Get audit logs for last 3 hours

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    query = "query_example" # str | Query filter (optional)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_audit_log(query=query, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->generate_audit_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter | [optional]
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

# **get_audit_severity_custom_histogram**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_audit_severity_custom_histogram()



Get audit log severity histogram

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    query = "query_example" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_audit_severity_custom_histogram(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_audit_severity_custom_histogram: %s\n" % e)
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

# **get_count**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"]}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_count: %s\n" % e)
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

# **get_count_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_count_post: %s\n" % e)
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

# **get_post_property_aggregation_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_property_aggregation_data(body)



Get raw property data aggregated with post action

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    body = "body_example" # str | Query filter for getting stat raw data

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_post_property_aggregation_data(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_post_property_aggregation_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Query filter for getting stat raw data |

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

# **get_post_stat_bulk_raw_property_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_raw_property_data(body)



Get raw property data in bulk with post action

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    body = "body_example" # str | Query filter for getting stat raw data
    scroll_id = "scrollId_example" # str | Offset of the query result (optional)
    count = "count_example" # str | Size of the query result (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_post_stat_bulk_raw_property_data(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_post_stat_bulk_raw_property_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_raw_property_data(body, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_post_stat_bulk_raw_property_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Query filter for getting stat raw data |
 **scroll_id** | **str**| Offset of the query result | [optional]
 **count** | **str**| Size of the query result | [optional]

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

# **get_property_aggregation_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_property_aggregation_data()



Get raw property data aggregated

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    input_query = "inputQuery_example" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_property_aggregation_data(input_query=input_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_property_aggregation_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_query** | **str**| Query filter | [optional]

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

# **get_raw_property_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_raw_property_data(body)



Get raw property data with post action

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    body = "body_example" # str | Query filter for getting stat raw data

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_raw_property_data(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_raw_property_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Query filter for getting stat raw data |

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

# **get_stat_bulk_raw_property_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_raw_property_data()



Get raw property data in bulk

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    input_query = "inputQuery_example" # str | Query filter (optional)
    scroll_id = "scrollId_example" # str | Offset of the query result (optional)
    count = "count_example" # str | size of the query result (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_bulk_raw_property_data(input_query=input_query, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_stat_bulk_raw_property_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_query** | **str**| Query filter | [optional]
 **scroll_id** | **str**| Offset of the query result | [optional]
 **count** | **str**| size of the query result | [optional]

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

# **get_stat_data_fields**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_stat_data_fields: %s\n" % e)
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

# **get_stat_data_raw_audit_log_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_raw_audit_log_data()



Get stat raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)
    input_query = "inputQuery_example" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_audit_log_data(input_query=input_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_stat_data_raw_audit_log_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_query** | **str**| Query filter | [optional]

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

# **get_stat_query_fields**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_audit_log_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_audit_log_api.AdministrationAuditLogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationAuditLogApi->get_stat_query_fields: %s\n" % e)
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

