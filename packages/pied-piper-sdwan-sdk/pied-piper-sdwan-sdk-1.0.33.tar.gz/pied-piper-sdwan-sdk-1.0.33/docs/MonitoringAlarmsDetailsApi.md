# openapi_client.MonitoringAlarmsDetailsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_stale_alarm**](MonitoringAlarmsDetailsApi.md#clear_stale_alarm) | **POST** /alarms/clear | 
[**correl_anti_entropy**](MonitoringAlarmsDetailsApi.md#correl_anti_entropy) | **GET** /alarms/reset | 
[**create_alarm_query_config**](MonitoringAlarmsDetailsApi.md#create_alarm_query_config) | **GET** /alarms/query/input | 
[**create_notification_rule**](MonitoringAlarmsDetailsApi.md#create_notification_rule) | **POST** /notifications/rule | 
[**delete_notification_rule**](MonitoringAlarmsDetailsApi.md#delete_notification_rule) | **DELETE** /notifications/rules | 
[**disable_enable_alarm**](MonitoringAlarmsDetailsApi.md#disable_enable_alarm) | **POST** /alarms/disabled | 
[**dump_correlation_engine_data**](MonitoringAlarmsDetailsApi.md#dump_correlation_engine_data) | **POST** /alarms/dump | 
[**enable_disable_link_state_alarm**](MonitoringAlarmsDetailsApi.md#enable_disable_link_state_alarm) | **POST** /alarms/link-state-alarm | 
[**get_alarm_aggregation_data**](MonitoringAlarmsDetailsApi.md#get_alarm_aggregation_data) | **GET** /alarms/aggregation | 
[**get_alarm_details**](MonitoringAlarmsDetailsApi.md#get_alarm_details) | **GET** /alarms/uuid/{alarm_uuid} | 
[**get_alarm_severity_custom_histogram**](MonitoringAlarmsDetailsApi.md#get_alarm_severity_custom_histogram) | **GET** /alarms/severity/summary | 
[**get_alarm_severity_mappings**](MonitoringAlarmsDetailsApi.md#get_alarm_severity_mappings) | **GET** /alarms/severitymappings | 
[**get_alarm_types_as_key_value**](MonitoringAlarmsDetailsApi.md#get_alarm_types_as_key_value) | **GET** /alarms/rulenamedisplay/keyvalue | 
[**get_alarms**](MonitoringAlarmsDetailsApi.md#get_alarms) | **GET** /alarms | 
[**get_alarms_by_severity**](MonitoringAlarmsDetailsApi.md#get_alarms_by_severity) | **GET** /alarms/severity | 
[**get_count1**](MonitoringAlarmsDetailsApi.md#get_count1) | **GET** /alarms/doccount | 
[**get_count_post1**](MonitoringAlarmsDetailsApi.md#get_count_post1) | **POST** /alarms/doccount | 
[**get_device_topic**](MonitoringAlarmsDetailsApi.md#get_device_topic) | **GET** /alarms/topic | 
[**get_link_state_alarm_config**](MonitoringAlarmsDetailsApi.md#get_link_state_alarm_config) | **GET** /alarms/link-state-alarm | 
[**get_master_manager_state**](MonitoringAlarmsDetailsApi.md#get_master_manager_state) | **GET** /alarms/master | 
[**get_non_viewed_active_alarms_count**](MonitoringAlarmsDetailsApi.md#get_non_viewed_active_alarms_count) | **GET** /alarms/count | 
[**get_non_viewed_alarms**](MonitoringAlarmsDetailsApi.md#get_non_viewed_alarms) | **GET** /alarms/notviewed | 
[**get_notification_rule**](MonitoringAlarmsDetailsApi.md#get_notification_rule) | **GET** /notifications/rules | 
[**get_post_alarm_aggregation_data**](MonitoringAlarmsDetailsApi.md#get_post_alarm_aggregation_data) | **POST** /alarms/aggregation | 
[**get_post_stat_bulk_alarm_raw_data**](MonitoringAlarmsDetailsApi.md#get_post_stat_bulk_alarm_raw_data) | **POST** /alarms/page | 
[**get_raw_alarm_data**](MonitoringAlarmsDetailsApi.md#get_raw_alarm_data) | **POST** /alarms | 
[**get_stat_bulk_alarm_raw_data**](MonitoringAlarmsDetailsApi.md#get_stat_bulk_alarm_raw_data) | **GET** /alarms/page | 
[**get_stat_data_fields1**](MonitoringAlarmsDetailsApi.md#get_stat_data_fields1) | **GET** /alarms/fields | 
[**get_stat_query_fields1**](MonitoringAlarmsDetailsApi.md#get_stat_query_fields1) | **GET** /alarms/query/fields | 
[**get_stats**](MonitoringAlarmsDetailsApi.md#get_stats) | **GET** /alarms/stats | 
[**list_disabled_alarm**](MonitoringAlarmsDetailsApi.md#list_disabled_alarm) | **GET** /alarms/disabled | 
[**mark_alarms_as_viewed**](MonitoringAlarmsDetailsApi.md#mark_alarms_as_viewed) | **POST** /alarms/markviewed | 
[**mark_all_alarms_as_viewed**](MonitoringAlarmsDetailsApi.md#mark_all_alarms_as_viewed) | **POST** /alarms/markallasviewed | 
[**restart_correlation_engine**](MonitoringAlarmsDetailsApi.md#restart_correlation_engine) | **GET** /alarms/restart | 
[**set_periodic_purge_timer**](MonitoringAlarmsDetailsApi.md#set_periodic_purge_timer) | **GET** /alarms/purgefrequency | 
[**start_tracking**](MonitoringAlarmsDetailsApi.md#start_tracking) | **POST** /alarms/starttracking/{testName} | 
[**stop_tracking**](MonitoringAlarmsDetailsApi.md#stop_tracking) | **POST** /alarms/stoptracking/{testName} | 
[**update_notification_rule**](MonitoringAlarmsDetailsApi.md#update_notification_rule) | **PUT** /notifications/rule | 


# **clear_stale_alarm**
> clear_stale_alarm()



Clears specific stale alarm

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    request_body = {"alarm_uuid":"29f9bf31-0fbe-4114-b8f0-e6234699485c"} # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] | alarm_uuid (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.clear_stale_alarm(request_body=request_body)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->clear_stale_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**| alarm_uuid | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **correl_anti_entropy**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} correl_anti_entropy()



Reset correlation engine data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.correl_anti_entropy()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->correl_anti_entropy: %s\n" % e)
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

# **create_alarm_query_config**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_alarm_query_config()



Get query configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_alarm_query_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->create_alarm_query_config: %s\n" % e)
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

# **create_notification_rule**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_notification_rule()



Add notification rule

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Notification rule (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_notification_rule(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->create_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Notification rule | [optional]

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_rule**
> delete_notification_rule(rule_id)



Delete notification rule

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    rule_id = "ruleId_example" # str | Rule Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_notification_rule(rule_id)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->delete_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule Id |

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

# **disable_enable_alarm**
> disable_enable_alarm(event_name, disable, time)



Enable/Disable a specific alarm

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    event_name = "eventName_example" # str | Event name
    disable = True # bool | Disable
    time = 1 # int | time in hours [1, 72], -1 means infinite
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | alarm config (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.disable_enable_alarm(event_name, disable, time)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->disable_enable_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.disable_enable_alarm(event_name, disable, time, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->disable_enable_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| Event name |
 **disable** | **bool**| Disable |
 **time** | **int**| time in hours [1, 72], -1 means infinite |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| alarm config | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dump_correlation_engine_data**
> dump_correlation_engine_data()



dump correlation engine server data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.dump_correlation_engine_data()
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->dump_correlation_engine_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **enable_disable_link_state_alarm**
> enable_disable_link_state_alarm(link_name, enable)



Enable/Disable a specific link-state alarm

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    link_name = "linkName_example" # str | Link name (bgp, ospf)
    enable = True # bool | Enable
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | alarm config (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.enable_disable_link_state_alarm(link_name, enable)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->enable_disable_link_state_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.enable_disable_link_state_alarm(link_name, enable, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->enable_disable_link_state_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_name** | **str**| Link name (bgp, ospf) |
 **enable** | **bool**| Enable |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| alarm config | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_aggregation_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_alarm_aggregation_data()



Gets aggregated list of alarms along with the raw alarm data of each aggregation

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    query = "{"query":{"field":"active","type":"boolean","value":["true"],"operator":"equal"},"aggregation":{"metrics":[{"property":"severity","type":"count"}]}}" # str | Alarm query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_alarm_aggregation_data(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_alarm_aggregation_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Alarm query string | [optional]

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

# **get_alarm_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_alarm_details(alarm_uuid)



Get alarm detail

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    alarm_uuid = "alarm_uuid_example" # str | Alarm Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_alarm_details(alarm_uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_alarm_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_uuid** | **str**| Alarm Id |

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

# **get_alarm_severity_custom_histogram**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_alarm_severity_custom_histogram(query)



Get alarm severity histogram

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    query = "query_example" # str | Alarm histogram query string

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_alarm_severity_custom_histogram(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_alarm_severity_custom_histogram: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Alarm histogram query string |

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

# **get_alarm_severity_mappings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_alarm_severity_mappings()



Gets alarm severity mappings

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_alarm_severity_mappings()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_alarm_severity_mappings: %s\n" % e)
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

# **get_alarm_types_as_key_value**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_alarm_types_as_key_value()



Gets alarm type as key value pair

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_alarm_types_as_key_value()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_alarm_types_as_key_value: %s\n" % e)
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

# **get_alarms**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_alarms()



Get alarms for last 30min if vManage query is not specified

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    query = "{"query":{"field":"active","type":"boolean","value":["true"],"operator":"equal"}}" # str | Alarm query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_alarms(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_alarms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Alarm query string | [optional]

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

# **get_alarms_by_severity**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_alarms_by_severity(severity_level, device_id, query)



Get alarm by severity

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    severity_level = [
        "major",
    ] # [str] | Alarm severity
    device_id = [
        "deviceId_example",
    ] # [str] | Device Id
    query = "query_example" # str | Query filter

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_alarms_by_severity(severity_level, device_id, query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_alarms_by_severity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **severity_level** | **[str]**| Alarm severity |
 **device_id** | **[str]**| Device Id |
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

# **get_count1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count1(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"]}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count1(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_count1: %s\n" % e)
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

# **get_count_post1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post1()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post1(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_count_post1: %s\n" % e)
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

# **get_device_topic**
> get_device_topic(ip)



Get device topic state

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    ip = "172.16.255.14" # str | Query topic

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_device_topic(ip)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_device_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Query topic |

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

# **get_link_state_alarm_config**
> get_link_state_alarm_config()



Get configuration for link-state alarm

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_link_state_alarm_config()
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_link_state_alarm_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_master_manager_state**
> get_master_manager_state()



Get master manager state

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_master_manager_state()
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_master_manager_state: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_non_viewed_active_alarms_count**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_non_viewed_active_alarms_count()



Get count of the alarms which are active and acknowledged by the user

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_non_viewed_active_alarms_count()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_non_viewed_active_alarms_count: %s\n" % e)
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

# **get_non_viewed_alarms**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_non_viewed_alarms()



Get alarms which are active and acknowledged by the user

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_non_viewed_alarms()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_non_viewed_alarms: %s\n" % e)
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

# **get_notification_rule**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_notification_rule()



Get all rules or specific notification rule by its Id

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    rule_id = "ruleId_example" # str | Rule Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_notification_rule(rule_id=rule_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule Id | [optional]

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

# **get_post_alarm_aggregation_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_alarm_aggregation_data()



Gets aggregated list of alarms along with the raw alarm data of each aggregation

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Input query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_alarm_aggregation_data(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_post_alarm_aggregation_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Input query | [optional]

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

# **get_post_stat_bulk_alarm_raw_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_alarm_raw_data(scroll_id, count)



Get paginated alarm raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | Query offset
    count = 10 # int | Query size
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Alarm query string (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_post_stat_bulk_alarm_raw_data(scroll_id, count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_post_stat_bulk_alarm_raw_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_alarm_raw_data(scroll_id, count, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_post_stat_bulk_alarm_raw_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scroll_id** | **str**| Query offset |
 **count** | **int**| Query size |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Alarm query string | [optional]

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

# **get_raw_alarm_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_raw_alarm_data()



Gets lists of alarms along with the raw alarm data of each.

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Alarm query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_raw_alarm_data(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_raw_alarm_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **sort_order** | **str**| sort order | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Alarm query string | [optional]

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

# **get_stat_bulk_alarm_raw_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_alarm_raw_data(query, scroll_id, count)



Get paginated alarm raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    query = "{"query":{"field":"active","type":"boolean","value":["true"],"operator":"equal"}}" # str | Alarm query string
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | Query offset
    count = 10 # int | Query size

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_stat_bulk_alarm_raw_data(query, scroll_id, count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_stat_bulk_alarm_raw_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Alarm query string |
 **scroll_id** | **str**| Query offset |
 **count** | **int**| Query size |

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

# **get_stat_data_fields1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields1()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields1()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_stat_data_fields1: %s\n" % e)
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

# **get_stat_query_fields1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields1()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields1()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_stat_query_fields1: %s\n" % e)
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

# **get_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats()



Get alarm statistics

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stats()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->get_stats: %s\n" % e)
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

# **list_disabled_alarm**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_disabled_alarm()



List all disabled alarms

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_disabled_alarm()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->list_disabled_alarm: %s\n" % e)
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

# **mark_alarms_as_viewed**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} mark_alarms_as_viewed()



Mark alarms as acknowledged by the user

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    request_body = {"uuid":["29f9bf31-0fbe-4114-b8f0-e6234699485c"]} # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] | List of alarms (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.mark_alarms_as_viewed(request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->mark_alarms_as_viewed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**| List of alarms | [optional]

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

# **mark_all_alarms_as_viewed**
> mark_all_alarms_as_viewed()



Mark all larms as acknowledged by the user

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    type = "type_example" # str | Query filter, possible value are \"active\" \"cleared\" (optional)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.mark_all_alarms_as_viewed(type=type, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->mark_all_alarms_as_viewed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Query filter, possible value are \&quot;active\&quot; \&quot;cleared\&quot; | [optional]
 **body** | **str**|  | [optional]

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

# **restart_correlation_engine**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} restart_correlation_engine()



Restart correlation engine

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.restart_correlation_engine()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->restart_correlation_engine: %s\n" % e)
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

# **set_periodic_purge_timer**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_periodic_purge_timer()



Set alarm purge timer

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    interval = "interval_example" # str | Purge interval (optional)
    active_time = "activeTime_example" # str | Purge activeTime (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_periodic_purge_timer(interval=interval, active_time=active_time)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->set_periodic_purge_timer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | **str**| Purge interval | [optional]
 **active_time** | **str**| Purge activeTime | [optional]

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

# **start_tracking**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} start_tracking(test_name)



Start tracking events

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    test_name = "testName_example" # str | test name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.start_tracking(test_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->start_tracking: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_name** | **str**| test name |

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

# **stop_tracking**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} stop_tracking(test_name)



Stop tracking events

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    test_name = "testName_example" # str | test name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.stop_tracking(test_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->stop_tracking: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_name** | **str**| test name |

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

# **update_notification_rule**
> update_notification_rule(rule_id)



Update notification rule

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_alarms_details_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_alarms_details_api.MonitoringAlarmsDetailsApi(api_client)
    rule_id = "ruleId_example" # str | Rule Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Notification rule (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_notification_rule(rule_id)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->update_notification_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_notification_rule(rule_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringAlarmsDetailsApi->update_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Notification rule | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

