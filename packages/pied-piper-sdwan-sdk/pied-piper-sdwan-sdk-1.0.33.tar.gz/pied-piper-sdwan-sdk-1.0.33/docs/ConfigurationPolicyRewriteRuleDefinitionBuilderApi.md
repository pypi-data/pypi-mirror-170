# openapi_client.ConfigurationPolicyRewriteRuleDefinitionBuilderApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_definition19**](ConfigurationPolicyRewriteRuleDefinitionBuilderApi.md#create_policy_definition19) | **POST** /template/policy/definition/rewriterule | 
[**delete_policy_definition19**](ConfigurationPolicyRewriteRuleDefinitionBuilderApi.md#delete_policy_definition19) | **DELETE** /template/policy/definition/rewriterule/{id} | 
[**edit_multiple_policy_definition19**](ConfigurationPolicyRewriteRuleDefinitionBuilderApi.md#edit_multiple_policy_definition19) | **PUT** /template/policy/definition/rewriterule/multiple/{id} | 
[**edit_policy_definition19**](ConfigurationPolicyRewriteRuleDefinitionBuilderApi.md#edit_policy_definition19) | **PUT** /template/policy/definition/rewriterule/{id} | 
[**get_definitions19**](ConfigurationPolicyRewriteRuleDefinitionBuilderApi.md#get_definitions19) | **GET** /template/policy/definition/rewriterule | 
[**get_policy_definition19**](ConfigurationPolicyRewriteRuleDefinitionBuilderApi.md#get_policy_definition19) | **GET** /template/policy/definition/rewriterule/{id} | 
[**preview_policy_definition19**](ConfigurationPolicyRewriteRuleDefinitionBuilderApi.md#preview_policy_definition19) | **POST** /template/policy/definition/rewriterule/preview | 
[**preview_policy_definition_by_id19**](ConfigurationPolicyRewriteRuleDefinitionBuilderApi.md#preview_policy_definition_by_id19) | **GET** /template/policy/definition/rewriterule/preview/{id} | 
[**save_policy_definition_in_bulk19**](ConfigurationPolicyRewriteRuleDefinitionBuilderApi.md#save_policy_definition_in_bulk19) | **PUT** /template/policy/definition/rewriterule/bulk | 


# **create_policy_definition19**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_policy_definition19()



Create policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_rewrite_rule_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_rewrite_rule_definition_builder_api.ConfigurationPolicyRewriteRuleDefinitionBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_policy_definition19(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->create_policy_definition19: %s\n" % e)
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

# **delete_policy_definition19**
> delete_policy_definition19(id)



Delete policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_rewrite_rule_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_rewrite_rule_definition_builder_api.ConfigurationPolicyRewriteRuleDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_policy_definition19(id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->delete_policy_definition19: %s\n" % e)
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

# **edit_multiple_policy_definition19**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_multiple_policy_definition19(id)



Edit multiple policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_rewrite_rule_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_rewrite_rule_definition_builder_api.ConfigurationPolicyRewriteRuleDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_multiple_policy_definition19(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->edit_multiple_policy_definition19: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_multiple_policy_definition19(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->edit_multiple_policy_definition19: %s\n" % e)
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

# **edit_policy_definition19**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_policy_definition19(id)



Edit a policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_rewrite_rule_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_rewrite_rule_definition_builder_api.ConfigurationPolicyRewriteRuleDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_policy_definition19(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->edit_policy_definition19: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_policy_definition19(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->edit_policy_definition19: %s\n" % e)
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

# **get_definitions19**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_definitions19()



Get policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_rewrite_rule_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_rewrite_rule_definition_builder_api.ConfigurationPolicyRewriteRuleDefinitionBuilderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_definitions19()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->get_definitions19: %s\n" % e)
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

# **get_policy_definition19**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_policy_definition19(id)



Get a specific policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_rewrite_rule_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_rewrite_rule_definition_builder_api.ConfigurationPolicyRewriteRuleDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_policy_definition19(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->get_policy_definition19: %s\n" % e)
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

# **preview_policy_definition19**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_definition19()



Preview policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_rewrite_rule_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_rewrite_rule_definition_builder_api.ConfigurationPolicyRewriteRuleDefinitionBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_policy_definition19(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->preview_policy_definition19: %s\n" % e)
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

# **preview_policy_definition_by_id19**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_definition_by_id19(id)



Preview policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_rewrite_rule_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_rewrite_rule_definition_builder_api.ConfigurationPolicyRewriteRuleDefinitionBuilderApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_policy_definition_by_id19(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->preview_policy_definition_by_id19: %s\n" % e)
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

# **save_policy_definition_in_bulk19**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} save_policy_definition_in_bulk19()



Create/Edit policy definitions in bulk

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_rewrite_rule_definition_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_rewrite_rule_definition_builder_api.ConfigurationPolicyRewriteRuleDefinitionBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.save_policy_definition_in_bulk19(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyRewriteRuleDefinitionBuilderApi->save_policy_definition_in_bulk19: %s\n" % e)
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

