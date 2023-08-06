# openapi_client.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_definition16**](ConfigurationPolicyDeviceAccessListDefinitionBuilderApi.md#create_policy_definition16) | **POST** /template/policy/definition/deviceaccesspolicy | 
[**delete_policy_definition16**](ConfigurationPolicyDeviceAccessListDefinitionBuilderApi.md#delete_policy_definition16) | **DELETE** /template/policy/definition/deviceaccesspolicy/{id} | 
[**edit_multiple_policy_definition16**](ConfigurationPolicyDeviceAccessListDefinitionBuilderApi.md#edit_multiple_policy_definition16) | **PUT** /template/policy/definition/deviceaccesspolicy/multiple/{id} | 
[**edit_policy_definition16**](ConfigurationPolicyDeviceAccessListDefinitionBuilderApi.md#edit_policy_definition16) | **PUT** /template/policy/definition/deviceaccesspolicy/{id} | 
[**get_definitions16**](ConfigurationPolicyDeviceAccessListDefinitionBuilderApi.md#get_definitions16) | **GET** /template/policy/definition/deviceaccesspolicy | 
[**get_policy_definition16**](ConfigurationPolicyDeviceAccessListDefinitionBuilderApi.md#get_policy_definition16) | **GET** /template/policy/definition/deviceaccesspolicy/{id} | 
[**preview_policy_definition16**](ConfigurationPolicyDeviceAccessListDefinitionBuilderApi.md#preview_policy_definition16) | **POST** /template/policy/definition/deviceaccesspolicy/preview | 
[**preview_policy_definition_by_id16**](ConfigurationPolicyDeviceAccessListDefinitionBuilderApi.md#preview_policy_definition_by_id16) | **GET** /template/policy/definition/deviceaccesspolicy/preview/{id} | 
[**save_policy_definition_in_bulk16**](ConfigurationPolicyDeviceAccessListDefinitionBuilderApi.md#save_policy_definition_in_bulk16) | **PUT** /template/policy/definition/deviceaccesspolicy/bulk | 


# **create_policy_definition16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_policy_definition16()



Create policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_device_access_list_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_device_access_list_definition_builder_api.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_policy_definition16(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->create_policy_definition16: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

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

# **delete_policy_definition16**
> delete_policy_definition16(id)



Delete policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_device_access_list_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_device_access_list_definition_builder_api.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_policy_definition16(id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->delete_policy_definition16: %s\n" % e)
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

# **edit_multiple_policy_definition16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_multiple_policy_definition16(id)



Edit multiple policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_device_access_list_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_device_access_list_definition_builder_api.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_multiple_policy_definition16(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->edit_multiple_policy_definition16: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_multiple_policy_definition16(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->edit_multiple_policy_definition16: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

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

# **edit_policy_definition16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_policy_definition16(id)



Edit a policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_device_access_list_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_device_access_list_definition_builder_api.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_policy_definition16(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->edit_policy_definition16: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_policy_definition16(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->edit_policy_definition16: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

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

# **get_definitions16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_definitions16()



Get policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_device_access_list_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_device_access_list_definition_builder_api.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_definitions16()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->get_definitions16: %s\n" % e)
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

# **get_policy_definition16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_policy_definition16(id)



Get a specific policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_device_access_list_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_device_access_list_definition_builder_api.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_policy_definition16(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->get_policy_definition16: %s\n" % e)
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

# **preview_policy_definition16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_definition16()



Preview policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_device_access_list_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_device_access_list_definition_builder_api.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_policy_definition16(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->preview_policy_definition16: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

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

# **preview_policy_definition_by_id16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_definition_by_id16(id)



Preview policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_device_access_list_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_device_access_list_definition_builder_api.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_policy_definition_by_id16(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->preview_policy_definition_by_id16: %s\n" % e)
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

# **save_policy_definition_in_bulk16**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} save_policy_definition_in_bulk16()



Create/Edit policy definitions in bulk

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_device_access_list_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_device_access_list_definition_builder_api.ConfigurationPolicyDeviceAccessListDefinitionBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.save_policy_definition_in_bulk16(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyDeviceAccessListDefinitionBuilderApi->save_policy_definition_in_bulk16: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

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

