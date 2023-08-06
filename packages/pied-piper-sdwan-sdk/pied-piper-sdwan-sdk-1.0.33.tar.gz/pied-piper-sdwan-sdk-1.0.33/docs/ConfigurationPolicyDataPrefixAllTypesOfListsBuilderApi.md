# openapi_client.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_list9**](ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi.md#create_policy_list9) | **POST** /template/policy/list/dataprefixall | 
[**delete_policy_list9**](ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi.md#delete_policy_list9) | **DELETE** /template/policy/list/dataprefixall/{id} | 
[**delete_policy_lists_with_info_tag9**](ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi.md#delete_policy_lists_with_info_tag9) | **DELETE** /template/policy/list/dataprefixall | 
[**edit_policy_list9**](ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi.md#edit_policy_list9) | **PUT** /template/policy/list/dataprefixall/{id} | 
[**get_lists_by_id9**](ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi.md#get_lists_by_id9) | **GET** /template/policy/list/dataprefixall/{id} | 
[**get_lists_for_all_data_prefixes**](ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi.md#get_lists_for_all_data_prefixes) | **GET** /template/policy/list/dataprefixall | 
[**get_policy_lists_with_info_tag9**](ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi.md#get_policy_lists_with_info_tag9) | **GET** /template/policy/list/dataprefixall/filtered | 
[**preview_policy_list9**](ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi.md#preview_policy_list9) | **POST** /template/policy/list/dataprefixall/preview | 
[**preview_policy_list_by_id9**](ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi.md#preview_policy_list_by_id9) | **GET** /template/policy/list/dataprefixall/preview/{id} | 


# **create_policy_list9**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_policy_list9()



Create policy list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_data_prefix_all_types_of_lists_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_data_prefix_all_types_of_lists_builder_api.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_policy_list9(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->create_policy_list9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy list | [optional]

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

# **delete_policy_list9**
> delete_policy_list9(id)



Delete policy list entry for a specific type of policy list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_data_prefix_all_types_of_lists_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_data_prefix_all_types_of_lists_builder_api.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_policy_list9(id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->delete_policy_list9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |

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

# **delete_policy_lists_with_info_tag9**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] delete_policy_lists_with_info_tag9()



Delete policy lists with specific info tag

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_data_prefix_all_types_of_lists_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_data_prefix_all_types_of_lists_builder_api.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi(api_client)
    info_tag = "infoTag_example" # str | InfoTag (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_policy_lists_with_info_tag9(info_tag=info_tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->delete_policy_lists_with_info_tag9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info_tag** | **str**| InfoTag | [optional]

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

# **edit_policy_list9**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_policy_list9(id)



Edit policy list entries for a specific type of policy list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_data_prefix_all_types_of_lists_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_data_prefix_all_types_of_lists_builder_api.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi(api_client)
    id = "id_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy list (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_policy_list9(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->edit_policy_list9: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_policy_list9(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->edit_policy_list9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy list | [optional]

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

# **get_lists_by_id9**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_lists_by_id9(id)



Get a specific policy list based on the id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_data_prefix_all_types_of_lists_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_data_prefix_all_types_of_lists_builder_api.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_lists_by_id9(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->get_lists_by_id9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |

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

# **get_lists_for_all_data_prefixes**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_lists_for_all_data_prefixes()



Get policy lists for all data prefixes

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_data_prefix_all_types_of_lists_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_data_prefix_all_types_of_lists_builder_api.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_lists_for_all_data_prefixes()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->get_lists_for_all_data_prefixes: %s\n" % e)
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

# **get_policy_lists_with_info_tag9**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_policy_lists_with_info_tag9()



Get policy lists with specific info tag

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_data_prefix_all_types_of_lists_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_data_prefix_all_types_of_lists_builder_api.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi(api_client)
    info_tag = "infoTag_example" # str | InfoTag (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_policy_lists_with_info_tag9(info_tag=info_tag)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->get_policy_lists_with_info_tag9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **info_tag** | **str**| InfoTag | [optional]

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

# **preview_policy_list9**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_list9()



Preview a policy list based on the policy list type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_data_prefix_all_types_of_lists_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_data_prefix_all_types_of_lists_builder_api.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_policy_list9(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->preview_policy_list9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy list | [optional]

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

# **preview_policy_list_by_id9**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_list_by_id9(id)



Preview a specific policy list entry based on id provided

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_data_prefix_all_types_of_lists_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_data_prefix_all_types_of_lists_builder_api.ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_policy_list_by_id9(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDataPrefixAllTypesOfListsBuilderApi->preview_policy_list_by_id9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |

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

