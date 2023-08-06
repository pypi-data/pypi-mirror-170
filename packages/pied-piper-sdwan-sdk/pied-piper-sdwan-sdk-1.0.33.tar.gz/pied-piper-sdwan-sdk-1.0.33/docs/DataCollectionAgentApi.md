# openapi_client.DataCollectionAgentApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dca_analytics_data_file**](DataCollectionAgentApi.md#create_dca_analytics_data_file) | **POST** /dca/settings/configuration/{type}/dca | 
[**create_stats**](DataCollectionAgentApi.md#create_stats) | **PUT** /dca/analytics | 
[**generate_alarm**](DataCollectionAgentApi.md#generate_alarm) | **POST** /dca/cloudservices/alarm | 
[**generate_dca_device_state_data**](DataCollectionAgentApi.md#generate_dca_device_state_data) | **POST** /dca/data/device/state/{state_data_type} | 
[**generate_dca_device_statistics_data**](DataCollectionAgentApi.md#generate_dca_device_statistics_data) | **POST** /dca/data/device/statistics/{stats_data_type} | 
[**get_access_token**](DataCollectionAgentApi.md#get_access_token) | **GET** /dca/cloudservices/accesstoken | 
[**get_all_stats_data_dca**](DataCollectionAgentApi.md#get_all_stats_data_dca) | **POST** /dca/analytics/all | 
[**get_cloud_services_configuration_dca**](DataCollectionAgentApi.md#get_cloud_services_configuration_dca) | **GET** /dca/settings/configuration/cloudservices/dca | 
[**get_crash_logs**](DataCollectionAgentApi.md#get_crash_logs) | **POST** /dca/device/crashlog/details | 
[**get_crash_logs_synced**](DataCollectionAgentApi.md#get_crash_logs_synced) | **GET** /dca/device/crashlog/synced | 
[**get_dca_attached_config_to_device**](DataCollectionAgentApi.md#get_dca_attached_config_to_device) | **POST** /dca/template/device/config/attachedconfig | 
[**get_dca_tenant_owners**](DataCollectionAgentApi.md#get_dca_tenant_owners) | **GET** /dca/dcatenantowners | 
[**get_devices_details_dca**](DataCollectionAgentApi.md#get_devices_details_dca) | **POST** /dca/system/device | 
[**get_id_token**](DataCollectionAgentApi.md#get_id_token) | **GET** /dca/cloudservices/idtoken | 
[**get_stats_db_index_status**](DataCollectionAgentApi.md#get_stats_db_index_status) | **POST** /dca/statistics/settings/status | 
[**get_telemetry_settings**](DataCollectionAgentApi.md#get_telemetry_settings) | **GET** /dca/cloudservices/telemetry | 
[**get_template_policy_definitions_dca**](DataCollectionAgentApi.md#get_template_policy_definitions_dca) | **POST** /dca/template/policy/definition/approute | 
[**get_vedge_template_list_dca**](DataCollectionAgentApi.md#get_vedge_template_list_dca) | **POST** /dca/template/policy/vedge | 
[**get_vpn_lists_dca**](DataCollectionAgentApi.md#get_vpn_lists_dca) | **POST** /dca/template/policy/list/vpn | 
[**get_vsmart_template_list_dca**](DataCollectionAgentApi.md#get_vsmart_template_list_dca) | **POST** /dca/template/policy/vsmart | 
[**list_all_devices_dca**](DataCollectionAgentApi.md#list_all_devices_dca) | **POST** /dca/device | 
[**store_access_token**](DataCollectionAgentApi.md#store_access_token) | **POST** /dca/cloudservices/accesstoken | 
[**store_id_token**](DataCollectionAgentApi.md#store_id_token) | **POST** /dca/cloudservices/idtoken | 


# **create_dca_analytics_data_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_dca_analytics_data_file(type)



Create analytics config data

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    type = "analytics" # str | Data type
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_dca_analytics_data_file(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->create_dca_analytics_data_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_dca_analytics_data_file(type, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->create_dca_analytics_data_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Data type |
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

# **create_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_stats()



Get statistics data

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_stats(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->create_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query | [optional]

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

# **generate_alarm**
> generate_alarm()



Generate DCA alarms

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | DCA alarm message (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.generate_alarm(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->generate_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| DCA alarm message | [optional]

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

# **generate_dca_device_state_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_dca_device_state_data(state_data_type)



Get device state data

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    state_data_type = "state_data_type_example" # str | Device state data
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_dca_device_state_data(state_data_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->generate_dca_device_state_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_dca_device_state_data(state_data_type, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->generate_dca_device_state_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_data_type** | **str**| Device state data |
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

# **generate_dca_device_statistics_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_dca_device_statistics_data(stats_data_type)



Get device statistics data

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    stats_data_type = "stats_data_type_example" # str | Device statistics data
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_dca_device_statistics_data(stats_data_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->generate_dca_device_statistics_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_dca_device_statistics_data(stats_data_type, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->generate_dca_device_statistics_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_data_type** | **str**| Device statistics data |
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

# **get_access_token**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_access_token()



Get DCA access token

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_access_token()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_access_token: %s\n" % e)
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

# **get_all_stats_data_dca**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_stats_data_dca()



Get all statistics setting data

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats setting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_stats_data_dca(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_all_stats_data_dca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats setting | [optional]

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

# **get_cloud_services_configuration_dca**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_services_configuration_dca()



Get DCA cloud service configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_services_configuration_dca()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_cloud_services_configuration_dca: %s\n" % e)
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

# **get_crash_logs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_crash_logs()



Get crash log

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_crash_logs(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_crash_logs: %s\n" % e)
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

# **get_crash_logs_synced**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_crash_logs_synced(device_id)



Get device crash log

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_crash_logs_synced(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_crash_logs_synced: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

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

# **get_dca_attached_config_to_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dca_attached_config_to_device()



Get attached config to device

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_dca_attached_config_to_device(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_dca_attached_config_to_device: %s\n" % e)
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

# **get_dca_tenant_owners**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dca_tenant_owners()



Get DCA tenant owners

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_dca_tenant_owners()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_dca_tenant_owners: %s\n" % e)
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

# **get_devices_details_dca**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_devices_details_dca()



Get device details

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_devices_details_dca(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_devices_details_dca: %s\n" % e)
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

# **get_id_token**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_id_token()



Get DCA Id token

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_id_token()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_id_token: %s\n" % e)
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

# **get_stats_db_index_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_db_index_status()



Get statistics setting status

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats setting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats_db_index_status(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_stats_db_index_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats setting | [optional]

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

# **get_telemetry_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_telemetry_settings()



Get DCA telemetry settings

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_telemetry_settings()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_telemetry_settings: %s\n" % e)
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

# **get_template_policy_definitions_dca**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_template_policy_definitions_dca()



Get template policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_template_policy_definitions_dca(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_template_policy_definitions_dca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query string | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_vedge_template_list_dca**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vedge_template_list_dca()



Get vEdge template list

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vedge_template_list_dca(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_vedge_template_list_dca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query string | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_vpn_lists_dca**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vpn_lists_dca()



Get VPN details

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vpn_lists_dca(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_vpn_lists_dca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query string | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_vsmart_template_list_dca**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vsmart_template_list_dca()



Get vSmart template list

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vsmart_template_list_dca(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->get_vsmart_template_list_dca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query string | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **list_all_devices_dca**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_all_devices_dca()



Get all devices

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_all_devices_dca(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->list_all_devices_dca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query string | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **store_access_token**
> store_access_token()



Set DCA access token

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | DCA access token (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.store_access_token(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->store_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| DCA access token | [optional]

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

# **store_id_token**
> store_id_token()



Set DCA Id token

### Example


```python
import time
import openapi_client
from openapi_client.api import data_collection_agent_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_collection_agent_api.DataCollectionAgentApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | DCA Id token (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.store_id_token(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling DataCollectionAgentApi->store_id_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| DCA Id token | [optional]

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

