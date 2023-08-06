# openapi_client.ConfigurationVEdgeTemplatePolicyApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_policy_resource_group**](ConfigurationVEdgeTemplatePolicyApi.md#change_policy_resource_group) | **POST** /template/policy/vedge/{resourceGroupName}/{policyId} | 
[**create_v_edge_template**](ConfigurationVEdgeTemplatePolicyApi.md#create_v_edge_template) | **POST** /template/policy/vedge | 
[**delete_v_edge_template**](ConfigurationVEdgeTemplatePolicyApi.md#delete_v_edge_template) | **DELETE** /template/policy/vedge/{policyId} | 
[**edit_v_edge_template**](ConfigurationVEdgeTemplatePolicyApi.md#edit_v_edge_template) | **PUT** /template/policy/vedge/{policyId} | 
[**generate_policy_template_list**](ConfigurationVEdgeTemplatePolicyApi.md#generate_policy_template_list) | **GET** /template/policy/vedge | 
[**get_device_list_by_policy**](ConfigurationVEdgeTemplatePolicyApi.md#get_device_list_by_policy) | **GET** /template/policy/vedge/devices/{policyId} | 
[**get_v_edge_policy_device_list**](ConfigurationVEdgeTemplatePolicyApi.md#get_v_edge_policy_device_list) | **GET** /template/policy/vedge/devices | 
[**get_v_edge_template**](ConfigurationVEdgeTemplatePolicyApi.md#get_v_edge_template) | **GET** /template/policy/vedge/definition/{policyId} | 


# **change_policy_resource_group**
> change_policy_resource_group(policy_id, resource_group_name)



Change policy resource group

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_edge_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_edge_template_policy_api.ConfigurationVEdgeTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id
    resource_group_name = "resourceGroupName_example" # str | Resrouce group name

    # example passing only required values which don't have defaults set
    try:
        api_instance.change_policy_resource_group(policy_id, resource_group_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVEdgeTemplatePolicyApi->change_policy_resource_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |
 **resource_group_name** | **str**| Resrouce group name |

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

# **create_v_edge_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_v_edge_template()



Create template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_edge_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_edge_template_policy_api.ConfigurationVEdgeTemplatePolicyApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template policy (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_v_edge_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVEdgeTemplatePolicyApi->create_v_edge_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template policy | [optional]

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

# **delete_v_edge_template**
> delete_v_edge_template(policy_id)



Delete template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_edge_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_edge_template_policy_api.ConfigurationVEdgeTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_v_edge_template(policy_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVEdgeTemplatePolicyApi->delete_v_edge_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |

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

# **edit_v_edge_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_v_edge_template(policy_id)



Edit template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_edge_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_edge_template_policy_api.ConfigurationVEdgeTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template policy (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_v_edge_template(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVEdgeTemplatePolicyApi->edit_v_edge_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_v_edge_template(policy_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVEdgeTemplatePolicyApi->edit_v_edge_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template policy | [optional]

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

# **generate_policy_template_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_policy_template_list()



Get policy details

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_edge_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_edge_template_policy_api.ConfigurationVEdgeTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_policy_template_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVEdgeTemplatePolicyApi->generate_policy_template_list: %s\n" % e)
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

# **get_device_list_by_policy**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_device_list_by_policy(policy_id)



Get device list by policy

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_edge_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_edge_template_policy_api.ConfigurationVEdgeTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_list_by_policy(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVEdgeTemplatePolicyApi->get_device_list_by_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |

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

# **get_v_edge_policy_device_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_v_edge_policy_device_list()



Get device list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_edge_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_edge_template_policy_api.ConfigurationVEdgeTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_v_edge_policy_device_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVEdgeTemplatePolicyApi->get_v_edge_policy_device_list: %s\n" % e)
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

# **get_v_edge_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_v_edge_template(policy_id)



Get template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_v_edge_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_v_edge_template_policy_api.ConfigurationVEdgeTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_v_edge_template(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVEdgeTemplatePolicyApi->get_v_edge_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |

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

