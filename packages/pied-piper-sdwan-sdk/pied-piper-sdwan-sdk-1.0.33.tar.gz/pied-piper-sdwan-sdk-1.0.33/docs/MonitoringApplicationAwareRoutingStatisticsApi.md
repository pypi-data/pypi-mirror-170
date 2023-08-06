# openapi_client.MonitoringApplicationAwareRoutingStatisticsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transport_health**](MonitoringApplicationAwareRoutingStatisticsApi.md#get_transport_health) | **GET** /statistics/approute/transport/{type} | 
[**get_transport_health_summary**](MonitoringApplicationAwareRoutingStatisticsApi.md#get_transport_health_summary) | **GET** /statistics/approute/transport/summary/{type} | 


# **get_transport_health**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_transport_health(type, limit)



Get application-aware routing statistics from device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_application_aware_routing_statistics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_statistics_api.MonitoringApplicationAwareRoutingStatisticsApi(api_client)
    type = "type_example" # str | Type
    limit = "limit_example" # str | Query filter
    query = "query_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transport_health(type, limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingStatisticsApi->get_transport_health: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transport_health(type, limit, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingStatisticsApi->get_transport_health: %s\n" % e)
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
from openapi_client.api import monitoring_application_aware_routing_statistics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_application_aware_routing_statistics_api.MonitoringApplicationAwareRoutingStatisticsApi(api_client)
    type = "type_example" # str | Type
    limit = 10 # int | Query result size (optional) if omitted the server will use the default value of 10
    query = "{"size":25,"query":{"condition":"AND","rules":[{"field":"summary_name","type":"string","value":["loss_percentage"],"operator":"equal"},{"field":"summary_interval","type":"string","value":["last_24_hours"],"operator":"equal"}]},"plotData":[],"sort":[{"field":"loss_percentage","type":"double","order":"desc"}],"additionalProperties":{},"fields":["name","jitter","rx_octets","loss_percentage","latency","tx_octets","summary_time"]}" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transport_health_summary(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingStatisticsApi->get_transport_health_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transport_health_summary(type, limit=limit, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringApplicationAwareRoutingStatisticsApi->get_transport_health_summary: %s\n" % e)
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

