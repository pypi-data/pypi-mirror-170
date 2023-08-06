# openapi_client.WorkflowManagementApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowManagementApi.md#create_workflow) | **POST** /workflow | 
[**delete_workflow**](WorkflowManagementApi.md#delete_workflow) | **DELETE** /workflow | 
[**get_workflows**](WorkflowManagementApi.md#get_workflows) | **GET** /workflow | 
[**save_workflow**](WorkflowManagementApi.md#save_workflow) | **PUT** /workflow | 


# **create_workflow**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_workflow()



Creates a workflow in the system

### Example


```python
import time
import openapi_client
from openapi_client.api import workflow_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_management_api.WorkflowManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Request to create workflow with given user context (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_workflow(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowManagementApi->create_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Request to create workflow with given user context | [optional]

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

# **delete_workflow**
> delete_workflow()



Deletes the workflow

### Example


```python
import time
import openapi_client
from openapi_client.api import workflow_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_management_api.WorkflowManagementApi(api_client)
    id = "id_example" # str | Workflow id (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Request to delete the workflow (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_workflow(id=id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowManagementApi->delete_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Request to delete the workflow | [optional]

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflows**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_workflows()



List all workflows for the given tenant

### Example


```python
import time
import openapi_client
from openapi_client.api import workflow_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_management_api.WorkflowManagementApi(api_client)
    type = "type_example" # str | Workflow type (optional)
    id = "id_example" # str | Workflow id (optional)
    group_id = "group-id_example" # str | group id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_workflows(type=type, id=id, group_id=group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowManagementApi->get_workflows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Workflow type | [optional]
 **id** | **str**| Workflow id | [optional]
 **group_id** | **str**| group id | [optional]

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

# **save_workflow**
> save_workflow()



Saves the workflow

### Example


```python
import time
import openapi_client
from openapi_client.api import workflow_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_management_api.WorkflowManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Request to save already created workflow with given user context (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.save_workflow(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowManagementApi->save_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Request to save already created workflow with given user context | [optional]

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

