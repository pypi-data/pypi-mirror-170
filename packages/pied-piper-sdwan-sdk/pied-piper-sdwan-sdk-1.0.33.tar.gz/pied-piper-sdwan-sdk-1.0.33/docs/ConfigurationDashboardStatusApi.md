# openapi_client.ConfigurationDashboardStatusApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_pending_tasks**](ConfigurationDashboardStatusApi.md#cancel_pending_tasks) | **POST** /device/action/status/cancel/{processId} | 
[**clean_status**](ConfigurationDashboardStatusApi.md#clean_status) | **GET** /device/action/status/clean | 
[**delete_status**](ConfigurationDashboardStatusApi.md#delete_status) | **DELETE** /device/action/status/clear | 
[**find_running_tasks**](ConfigurationDashboardStatusApi.md#find_running_tasks) | **GET** /device/action/status/tasks | 
[**find_status**](ConfigurationDashboardStatusApi.md#find_status) | **GET** /device/action/status/{actionName} | 
[**get_active_task_count**](ConfigurationDashboardStatusApi.md#get_active_task_count) | **GET** /device/action/status/tasks/activeCount | 
[**get_clean_status**](ConfigurationDashboardStatusApi.md#get_clean_status) | **GET** /device/action/status/tasks/clean | 


# **cancel_pending_tasks**
> cancel_pending_tasks(process_id)



Bulk cancel task status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_dashboard_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_dashboard_status_api.ConfigurationDashboardStatusApi(api_client)
    process_id = "processId_example" # str | Process Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.cancel_pending_tasks(process_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDashboardStatusApi->cancel_pending_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| Process Id |

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

# **clean_status**
> clean_status(clean_status)



Delete task and status vertex

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_dashboard_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_dashboard_status_api.ConfigurationDashboardStatusApi(api_client)
    clean_status = True # bool | Clear status flag

    # example passing only required values which don't have defaults set
    try:
        api_instance.clean_status(clean_status)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDashboardStatusApi->clean_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clean_status** | **bool**| Clear status flag |

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

# **delete_status**
> delete_status(process_id)



Delete status of action

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_dashboard_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_dashboard_status_api.ConfigurationDashboardStatusApi(api_client)
    process_id = "processId_example" # str | Process Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_status(process_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDashboardStatusApi->delete_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| Process Id |

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

# **find_running_tasks**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_running_tasks()



Find running tasks

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_dashboard_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_dashboard_status_api.ConfigurationDashboardStatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_running_tasks()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDashboardStatusApi->find_running_tasks: %s\n" % e)
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

# **find_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_status(action_name)



Find status of action

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_dashboard_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_dashboard_status_api.ConfigurationDashboardStatusApi(api_client)
    action_name = "push_feature_template_configuration-01232017T154359940" # str | Action name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.find_status(action_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDashboardStatusApi->find_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_name** | **str**| Action name |

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

# **get_active_task_count**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_active_task_count()



Get active task count

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_dashboard_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_dashboard_status_api.ConfigurationDashboardStatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_active_task_count()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDashboardStatusApi->get_active_task_count: %s\n" % e)
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

# **get_clean_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_clean_status(process_id)



Delete task and status vertex

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_dashboard_status_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_dashboard_status_api.ConfigurationDashboardStatusApi(api_client)
    process_id = "processId_example" # str | Process Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_clean_status(process_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDashboardStatusApi->get_clean_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| Process Id |

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

