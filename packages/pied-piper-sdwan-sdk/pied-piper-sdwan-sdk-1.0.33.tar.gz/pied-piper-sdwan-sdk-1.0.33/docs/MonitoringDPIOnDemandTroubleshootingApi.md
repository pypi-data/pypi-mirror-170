# openapi_client.MonitoringDPIOnDemandTroubleshootingApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_queue_entry**](MonitoringDPIOnDemandTroubleshootingApi.md#create_queue_entry) | **POST** /statistics/on-demand/queue | 
[**delete_queue_entry**](MonitoringDPIOnDemandTroubleshootingApi.md#delete_queue_entry) | **DELETE** /statistics/on-demand/queue/{entryId} | 
[**get_queue_entries**](MonitoringDPIOnDemandTroubleshootingApi.md#get_queue_entries) | **GET** /statistics/on-demand/queue | 
[**get_queue_properties**](MonitoringDPIOnDemandTroubleshootingApi.md#get_queue_properties) | **GET** /statistics/on-demand/queue/properties | 
[**update_queue_entry**](MonitoringDPIOnDemandTroubleshootingApi.md#update_queue_entry) | **PUT** /statistics/on-demand/queue/{entryId} | 


# **create_queue_entry**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_queue_entry()



Create on-demand troubleshooting queue entry

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpion_demand_troubleshooting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpion_demand_troubleshooting_api.MonitoringDPIOnDemandTroubleshootingApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | On-demand queue entry (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_queue_entry(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIOnDemandTroubleshootingApi->create_queue_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| On-demand queue entry | [optional]

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

# **delete_queue_entry**
> delete_queue_entry(entry_id)



removes on-demand queue entry

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpion_demand_troubleshooting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpion_demand_troubleshooting_api.MonitoringDPIOnDemandTroubleshootingApi(api_client)
    entry_id = "entryId_example" # str | Entry Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_queue_entry(entry_id)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIOnDemandTroubleshootingApi->delete_queue_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| Entry Id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue_entries**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_queue_entries()



gets current on-demand queue entries

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpion_demand_troubleshooting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpion_demand_troubleshooting_api.MonitoringDPIOnDemandTroubleshootingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_queue_entries()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIOnDemandTroubleshootingApi->get_queue_entries: %s\n" % e)
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

# **get_queue_properties**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_queue_properties()



gets current size of on-demand queue

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpion_demand_troubleshooting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpion_demand_troubleshooting_api.MonitoringDPIOnDemandTroubleshootingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_queue_properties()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIOnDemandTroubleshootingApi->get_queue_properties: %s\n" % e)
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

# **update_queue_entry**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_queue_entry(entry_id)



Updates on-demand troubleshooting queue entry

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_dpion_demand_troubleshooting_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_dpion_demand_troubleshooting_api.MonitoringDPIOnDemandTroubleshootingApi(api_client)
    entry_id = "entryId_example" # str | Entry Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | On-demand queue entry (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_queue_entry(entry_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIOnDemandTroubleshootingApi->update_queue_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_queue_entry(entry_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringDPIOnDemandTroubleshootingApi->update_queue_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| Entry Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| On-demand queue entry | [optional]

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

