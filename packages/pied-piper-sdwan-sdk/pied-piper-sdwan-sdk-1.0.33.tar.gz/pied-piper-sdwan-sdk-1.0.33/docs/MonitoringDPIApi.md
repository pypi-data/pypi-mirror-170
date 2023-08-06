# openapi_client.MonitoringDPIApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dpi_device_and_app_details**](MonitoringDPIApi.md#create_dpi_device_and_app_details) | **GET** /statistics/dpi/device/details/applications | 
[**create_dpi_device_grid_data**](MonitoringDPIApi.md#create_dpi_device_grid_data) | **GET** /statistics/dpi/device/applications | 
[**create_dpi_flows_grid_list_query**](MonitoringDPIApi.md#create_dpi_flows_grid_list_query) | **GET** /statistics/dpi/applications | 
[**create_dpi_summary**](MonitoringDPIApi.md#create_dpi_summary) | **GET** /statistics/dpi/applications/summary | 
[**get_aggregation_data_by_query12**](MonitoringDPIApi.md#get_aggregation_data_by_query12) | **GET** /statistics/dpi/aggregation | 
[**get_aggregation_data_dpi**](MonitoringDPIApi.md#get_aggregation_data_dpi) | **POST** /statistics/dpi/recovery/aggregation | 
[**get_aggregation_data_for_packet_dup**](MonitoringDPIApi.md#get_aggregation_data_for_packet_dup) | **POST** /statistics/dpi/pktdup/aggregation | 
[**get_count14**](MonitoringDPIApi.md#get_count14) | **GET** /statistics/dpi/doccount | 
[**get_count_post14**](MonitoringDPIApi.md#get_count_post14) | **POST** /statistics/dpi/doccount | 
[**get_post_aggregation_app_data**](MonitoringDPIApi.md#get_post_aggregation_app_data) | **POST** /statistics/dpi/agg-app/aggregation | 
[**get_post_aggregation_data**](MonitoringDPIApi.md#get_post_aggregation_data) | **POST** /statistics/dpi/aggregation | 
[**get_post_stat_bulk_raw_data12**](MonitoringDPIApi.md#get_post_stat_bulk_raw_data12) | **POST** /statistics/dpi/page | 
[**get_stat_bulk_raw_data12**](MonitoringDPIApi.md#get_stat_bulk_raw_data12) | **GET** /statistics/dpi/page | 
[**get_stat_data_fields14**](MonitoringDPIApi.md#get_stat_data_fields14) | **GET** /statistics/dpi/fields | 
[**get_stat_data_raw_data12**](MonitoringDPIApi.md#get_stat_data_raw_data12) | **GET** /statistics/dpi | 
[**get_stat_data_raw_data_as_csv12**](MonitoringDPIApi.md#get_stat_data_raw_data_as_csv12) | **GET** /statistics/dpi/csv | 
[**get_stat_query_fields14**](MonitoringDPIApi.md#get_stat_query_fields14) | **GET** /statistics/dpi/query/fields | 
[**get_stats_raw_data12**](MonitoringDPIApi.md#get_stats_raw_data12) | **POST** /statistics/dpi | 
[**get_unique_flow_count**](MonitoringDPIApi.md#get_unique_flow_count) | **GET** /statistics/dpi/device/application/flowcount | 


# **create_dpi_device_and_app_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_dpi_device_and_app_details(query)



Get detailed DPI device and app list

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    query = "query_example" # str | Query string

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dpi_device_and_app_details(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->create_dpi_device_and_app_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string |

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

# **create_dpi_device_grid_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_dpi_device_grid_data(query)



Get detailed DPI flows list

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    query = "query_example" # str | Query string
    limit = "limit_example" # str | Query size (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dpi_device_grid_data(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->create_dpi_device_grid_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_dpi_device_grid_data(query, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->create_dpi_device_grid_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string |
 **limit** | **str**| Query size | [optional]

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

# **create_dpi_flows_grid_list_query**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_dpi_flows_grid_list_query(query)



Get detailed DPI application flows list in a grid table

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    query = "query_example" # str | Query string
    limit = "limit_example" # str | Query size (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dpi_flows_grid_list_query(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->create_dpi_flows_grid_list_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_dpi_flows_grid_list_query(query, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->create_dpi_flows_grid_list_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string |
 **limit** | **str**| Query size | [optional]

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

# **create_dpi_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_dpi_summary(query)



Get detailed DPI application flows summary

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    query = "query_example" # str | Query string
    limit = "limit_example" # str | Query size (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dpi_summary(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->create_dpi_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_dpi_summary(query, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->create_dpi_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string |
 **limit** | **str**| Query size | [optional]

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

# **get_aggregation_data_by_query12**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_by_query12()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_by_query12(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_aggregation_data_by_query12: %s\n" % e)
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

# **get_aggregation_data_dpi**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_dpi()



Get aggregation data and fec recovery rate if available

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_dpi(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_aggregation_data_dpi: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query string | [optional]

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

# **get_aggregation_data_for_packet_dup**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_for_packet_dup()



Get time series aggregation data for packet duplication for an application over TLOCs if available

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_for_packet_dup(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_aggregation_data_for_packet_dup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query string | [optional]

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

# **get_count14**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count14(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"]}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count14(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_count14: %s\n" % e)
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

# **get_count_post14**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post14()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post14(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_count_post14: %s\n" % e)
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

# **get_post_aggregation_app_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_app_data()



Get raw aggregated data and display applications with the highest utilization for a device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_app_data(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_post_aggregation_app_data: %s\n" % e)
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

# **get_post_aggregation_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_data()



Get raw aggregated data and display applications with the highest utilization for a device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_data(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_post_aggregation_data: %s\n" % e)
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

# **get_post_stat_bulk_raw_data12**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_raw_data12()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_raw_data12(scroll_id=scroll_id, count=count, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_post_stat_bulk_raw_data12: %s\n" % e)
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

# **get_stat_bulk_raw_data12**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_raw_data12()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"]}" # str | Query string (optional)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_bulk_raw_data12(query=query, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_stat_bulk_raw_data12: %s\n" % e)
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

# **get_stat_data_fields14**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields14()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields14()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_stat_data_fields14: %s\n" % e)
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

# **get_stat_data_raw_data12**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_raw_data12()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["2020-05-10T01:00:00 UTC","2020-05-10T01:30:00 UTC"],"field":"entry_time","type":"date","operator":"between"}]},"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data12(query=query, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_stat_data_raw_data12: %s\n" % e)
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

# **get_stat_data_raw_data_as_csv12**
> str get_stat_data_raw_data_as_csv12()



Get raw data with optional query as CSV

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1000,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data_as_csv12(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_stat_data_raw_data_as_csv12: %s\n" % e)
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

# **get_stat_query_fields14**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields14()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields14()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_stat_query_fields14: %s\n" % e)
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

# **get_stats_raw_data12**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_raw_data12()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats_raw_data12(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_stats_raw_data12: %s\n" % e)
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

# **get_unique_flow_count**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_unique_flow_count(device_id, interval, application, window, family)



Get application flow count per tunnel

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpi_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpi_api.MonitoringDPIApi(api_client)
    device_id = "deviceId_example" # str | Device Id
    interval = "interval_example" # str | Interval
    application = "application_example" # str | Application
    window = "window_example" # str | Window
    family = "family_example" # str | Family

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_unique_flow_count(device_id, interval, application, window, family)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIApi->get_unique_flow_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **interval** | **str**| Interval |
 **application** | **str**| Application |
 **window** | **str**| Window |
 **family** | **str**| Family |

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

