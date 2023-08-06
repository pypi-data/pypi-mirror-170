# openapi_client.MonitoringApplicationAwareRoutingApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregation_data_app_route**](MonitoringApplicationAwareRoutingApi.md#get_aggregation_data_app_route) | **POST** /statistics/approute/fec/aggregation | 
[**get_aggregation_data_by_query2**](MonitoringApplicationAwareRoutingApi.md#get_aggregation_data_by_query2) | **GET** /statistics/approute/aggregation | 
[**get_approute_grid_stat**](MonitoringApplicationAwareRoutingApi.md#get_approute_grid_stat) | **GET** /statistics/approute/device/tunnel/summary | 
[**get_count4**](MonitoringApplicationAwareRoutingApi.md#get_count4) | **GET** /statistics/approute/doccount | 
[**get_count_post4**](MonitoringApplicationAwareRoutingApi.md#get_count_post4) | **POST** /statistics/approute/doccount | 
[**get_post_aggregation_app_data_by_query2**](MonitoringApplicationAwareRoutingApi.md#get_post_aggregation_app_data_by_query2) | **POST** /statistics/approute/app-agg/aggregation | 
[**get_post_aggregation_data_by_query2**](MonitoringApplicationAwareRoutingApi.md#get_post_aggregation_data_by_query2) | **POST** /statistics/approute/aggregation | 
[**get_post_stat_bulk_raw_data2**](MonitoringApplicationAwareRoutingApi.md#get_post_stat_bulk_raw_data2) | **POST** /statistics/approute/page | 
[**get_stat_bulk_raw_data2**](MonitoringApplicationAwareRoutingApi.md#get_stat_bulk_raw_data2) | **GET** /statistics/approute/page | 
[**get_stat_data_fields4**](MonitoringApplicationAwareRoutingApi.md#get_stat_data_fields4) | **GET** /statistics/approute/fields | 
[**get_stat_data_raw_data2**](MonitoringApplicationAwareRoutingApi.md#get_stat_data_raw_data2) | **GET** /statistics/approute | 
[**get_stat_data_raw_data_as_csv2**](MonitoringApplicationAwareRoutingApi.md#get_stat_data_raw_data_as_csv2) | **GET** /statistics/approute/csv | 
[**get_stat_query_fields4**](MonitoringApplicationAwareRoutingApi.md#get_stat_query_fields4) | **GET** /statistics/approute/query/fields | 
[**get_stats_raw_data2**](MonitoringApplicationAwareRoutingApi.md#get_stats_raw_data2) | **POST** /statistics/approute | 
[**get_transport_health**](MonitoringApplicationAwareRoutingApi.md#get_transport_health) | **GET** /statistics/approute/transport/{type} | 
[**get_transport_health_summary**](MonitoringApplicationAwareRoutingApi.md#get_transport_health_summary) | **GET** /statistics/approute/transport/summary/{type} | 
[**get_tunnel**](MonitoringApplicationAwareRoutingApi.md#get_tunnel) | **GET** /statistics/approute/device/tunnels | 
[**get_tunnel_chart**](MonitoringApplicationAwareRoutingApi.md#get_tunnel_chart) | **GET** /statistics/approute/tunnel/{type}/summary | 
[**get_tunnels**](MonitoringApplicationAwareRoutingApi.md#get_tunnels) | **GET** /statistics/approute/tunnels/{type} | 
[**get_tunnels_health**](MonitoringApplicationAwareRoutingApi.md#get_tunnels_health) | **GET** /statistics/approute/tunnels/health/{type} | 
[**get_tunnels_summary**](MonitoringApplicationAwareRoutingApi.md#get_tunnels_summary) | **GET** /statistics/approute/tunnels/summary/{type} | 


# **get_aggregation_data_app_route**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_app_route()



Get aggregation data and fec recovery rate

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_app_route(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_aggregation_data_app_route: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query filter | [optional]

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

# **get_aggregation_data_by_query2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_by_query2()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_by_query2(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_aggregation_data_by_query2: %s\n" % e)
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

# **get_approute_grid_stat**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_approute_grid_stat()



Get statistics for top applications per tunnel in a grid table

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    query = "query_example" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_approute_grid_stat(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_approute_grid_stat: %s\n" % e)
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

# **get_count4**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count4(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"]}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count4(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_count4: %s\n" % e)
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

# **get_count_post4**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post4()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post4(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_count_post4: %s\n" % e)
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

# **get_post_aggregation_app_data_by_query2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_app_data_by_query2()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_app_data_by_query2(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_post_aggregation_app_data_by_query2: %s\n" % e)
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

# **get_post_aggregation_data_by_query2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_data_by_query2()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_data_by_query2(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_post_aggregation_data_by_query2: %s\n" % e)
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

# **get_post_stat_bulk_raw_data2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_raw_data2()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_raw_data2(scroll_id=scroll_id, count=count, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_post_stat_bulk_raw_data2: %s\n" % e)
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

# **get_stat_bulk_raw_data2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_raw_data2()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"]}" # str | Query string (optional)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_bulk_raw_data2(query=query, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_stat_bulk_raw_data2: %s\n" % e)
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

# **get_stat_data_fields4**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields4()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields4()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_stat_data_fields4: %s\n" % e)
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

# **get_stat_data_raw_data2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_raw_data2()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["2020-05-10T01:00:00 UTC","2020-05-10T01:30:00 UTC"],"field":"entry_time","type":"date","operator":"between"}]},"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data2(query=query, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_stat_data_raw_data2: %s\n" % e)
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

# **get_stat_data_raw_data_as_csv2**
> str get_stat_data_raw_data_as_csv2()



Get raw data with optional query as CSV

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1000,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data_as_csv2(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_stat_data_raw_data_as_csv2: %s\n" % e)
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

# **get_stat_query_fields4**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields4()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields4()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_stat_query_fields4: %s\n" % e)
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

# **get_stats_raw_data2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_raw_data2()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats_raw_data2(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_stats_raw_data2: %s\n" % e)
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

# **get_transport_health**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_transport_health(type, limit)



Get application-aware routing statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    type = "type_example" # str | Type
    limit = "limit_example" # str | Query filter
    query = "query_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transport_health(type, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_transport_health: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transport_health(type, limit, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_transport_health: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type |
 **limit** | **str**| Query filter |
 **query** | **str**|  | [optional]

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

# **get_transport_health_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_transport_health_summary(type)



Get application-aware routing statistics summary from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    type = "type_example" # str | Type
    limit = 10 # int | Query result size (optional) if omitted the server will use the default value of 10
    query = "{"size":25,"query":{"condition":"AND","rules":[{"field":"summary_name","type":"string","value":["loss_percentage"],"operator":"equal"},{"field":"summary_interval","type":"string","value":["last_24_hours"],"operator":"equal"}]},"plotData":[],"sort":[{"field":"loss_percentage","type":"double","order":"desc"}],"additionalProperties":{},"fields":["name","jitter","rx_octets","loss_percentage","latency","tx_octets","summary_time"]}" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transport_health_summary(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_transport_health_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transport_health_summary(type, limit=limit, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_transport_health_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type |
 **limit** | **int**| Query result size | [optional] if omitted the server will use the default value of 10
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

# **get_tunnel**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_tunnel()



Get statistics for top applications per tunnel in a grid table

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    query = "query_example" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_tunnel(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_tunnel: %s\n" % e)
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

# **get_tunnel_chart**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_tunnel_chart(type, query)



Get tunnel top statistics in as chart

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    type = "type_example" # str | Type
    query = "query_example" # str | Query filter

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tunnel_chart(type, query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_tunnel_chart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type |
 **query** | **str**| Query filter |

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

# **get_tunnels**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_tunnels(type)



Get tunnel top statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    type = "type_example" # str | Type
    query = "query_example" # str | Query filter (optional)
    limit = 1 # int | Query result size (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tunnels(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_tunnels: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_tunnels(type, query=query, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_tunnels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type |
 **query** | **str**| Query filter | [optional]
 **limit** | **int**| Query result size | [optional]

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

# **get_tunnels_health**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_tunnels_health(type)



Get tunnel health

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    type = "type_example" # str | Type
    limit = 10 # int | Query result size (optional) if omitted the server will use the default value of 10
    last_n_hours = 3 # int | Time range for health average (optional) if omitted the server will use the default value of 3

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tunnels_health(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_tunnels_health: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_tunnels_health(type, limit=limit, last_n_hours=last_n_hours)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_tunnels_health: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type |
 **limit** | **int**| Query result size | [optional] if omitted the server will use the default value of 10
 **last_n_hours** | **int**| Time range for health average | [optional] if omitted the server will use the default value of 3

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

# **get_tunnels_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_tunnels_summary(type)



Get tunnel top statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_api.MonitoringApplicationAwareRoutingApi(api_client)
    type = "type_example" # str | Type
    query = "query_example" # str | Query filter (optional)
    limit = 10 # int | Query result size (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tunnels_summary(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_tunnels_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_tunnels_summary(type, query=query, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingApi->get_tunnels_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type |
 **query** | **str**| Query filter | [optional]
 **limit** | **int**| Query result size | [optional] if omitted the server will use the default value of 10

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

