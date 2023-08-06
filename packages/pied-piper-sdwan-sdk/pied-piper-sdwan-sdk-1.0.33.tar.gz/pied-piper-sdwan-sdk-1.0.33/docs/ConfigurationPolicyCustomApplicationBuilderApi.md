# openapi_client.ConfigurationPolicyCustomApplicationBuilderApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_app**](ConfigurationPolicyCustomApplicationBuilderApi.md#create_custom_app) | **POST** /template/policy/customapp | 
[**delete_custom_app**](ConfigurationPolicyCustomApplicationBuilderApi.md#delete_custom_app) | **DELETE** /template/policy/customapp/{id} | 
[**edit_custom_app**](ConfigurationPolicyCustomApplicationBuilderApi.md#edit_custom_app) | **PUT** /template/policy/customapp/{id} | 
[**get_custom_app_by_id**](ConfigurationPolicyCustomApplicationBuilderApi.md#get_custom_app_by_id) | **GET** /template/policy/customapp/{id} | 
[**get_custom_apps**](ConfigurationPolicyCustomApplicationBuilderApi.md#get_custom_apps) | **GET** /template/policy/customapp | 
[**map_traffic_profiles**](ConfigurationPolicyCustomApplicationBuilderApi.md#map_traffic_profiles) | **POST** /template/policy/clouddiscoveredapp | 


# **create_custom_app**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_custom_app()



Create a policy custom applications

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_custom_application_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_custom_application_builder_api.ConfigurationPolicyCustomApplicationBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | App payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_custom_app(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyCustomApplicationBuilderApi->create_custom_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| App payload | [optional]

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

# **delete_custom_app**
> delete_custom_app(id)



Delete a policy custom applications

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_custom_application_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_custom_application_builder_api.ConfigurationPolicyCustomApplicationBuilderApi(api_client)
    id = "id_example" # str | Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_custom_app(id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyCustomApplicationBuilderApi->delete_custom_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id |

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

# **edit_custom_app**
> edit_custom_app(id)



Edit a policy custom applications

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_custom_application_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_custom_application_builder_api.ConfigurationPolicyCustomApplicationBuilderApi(api_client)
    id = "id_example" # str | Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | App payload (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.edit_custom_app(id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyCustomApplicationBuilderApi->edit_custom_app: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_custom_app(id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyCustomApplicationBuilderApi->edit_custom_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| App payload | [optional]

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

# **get_custom_app_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_custom_app_by_id(id)



Get a policy custom applications

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_custom_application_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_custom_application_builder_api.ConfigurationPolicyCustomApplicationBuilderApi(api_client)
    id = "id_example" # str | Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_custom_app_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyCustomApplicationBuilderApi->get_custom_app_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id |

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

# **get_custom_apps**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_custom_apps()



Get all policy custom applications

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_custom_application_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_custom_application_builder_api.ConfigurationPolicyCustomApplicationBuilderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_custom_apps()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyCustomApplicationBuilderApi->get_custom_apps: %s\n" % e)
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

# **map_traffic_profiles**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} map_traffic_profiles()



Set SLA class for policy cloud discovered applications

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_policy_custom_application_builder_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_policy_custom_application_builder_api.ConfigurationPolicyCustomApplicationBuilderApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | App payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.map_traffic_profiles(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationPolicyCustomApplicationBuilderApi->map_traffic_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| App payload | [optional]

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

