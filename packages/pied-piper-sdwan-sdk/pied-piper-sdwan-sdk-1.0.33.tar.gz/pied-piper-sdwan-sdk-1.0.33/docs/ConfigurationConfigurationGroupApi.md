# openapi_client.ConfigurationConfigurationGroupApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_config_group**](ConfigurationConfigurationGroupApi.md#create_config_group) | **POST** /v1/config-group | 
[**create_config_group_association**](ConfigurationConfigurationGroupApi.md#create_config_group_association) | **POST** /v1/config-group/{configGroupId}/device/associate | 
[**create_config_group_device_variables**](ConfigurationConfigurationGroupApi.md#create_config_group_device_variables) | **PUT** /v1/config-group/{configGroupId}/device/variables | 
[**create_config_group_device_variables1**](ConfigurationConfigurationGroupApi.md#create_config_group_device_variables1) | **GET** /v1/config-group/{configGroupId}/device/variables/schema | 
[**delete_config_group**](ConfigurationConfigurationGroupApi.md#delete_config_group) | **DELETE** /v1/config-group/{configGroupId} | 
[**delete_config_group_association**](ConfigurationConfigurationGroupApi.md#delete_config_group_association) | **DELETE** /v1/config-group/{configGroupId}/device/associate | 
[**deploy_config_group**](ConfigurationConfigurationGroupApi.md#deploy_config_group) | **POST** /v1/config-group/{configGroupId}/device/deploy | 
[**edit_config_group**](ConfigurationConfigurationGroupApi.md#edit_config_group) | **PUT** /v1/config-group/{configGroupId} | 
[**get_cedge_config_group_schema_by_schema_type**](ConfigurationConfigurationGroupApi.md#get_cedge_config_group_schema_by_schema_type) | **GET** /v1/config-group/schema/sdwan | 
[**get_config_group**](ConfigurationConfigurationGroupApi.md#get_config_group) | **GET** /v1/config-group/{configGroupId} | 
[**get_config_group_association**](ConfigurationConfigurationGroupApi.md#get_config_group_association) | **GET** /v1/config-group/{configGroupId}/device/associate | 
[**get_config_group_by_solution**](ConfigurationConfigurationGroupApi.md#get_config_group_by_solution) | **GET** /v1/config-group | 
[**get_config_group_device_configuration_preview**](ConfigurationConfigurationGroupApi.md#get_config_group_device_configuration_preview) | **POST** /v1/config-group/{configGroupId}/device/{deviceId}/preview | 
[**get_config_group_device_variables**](ConfigurationConfigurationGroupApi.md#get_config_group_device_variables) | **GET** /v1/config-group/{configGroupId}/device/variables | 
[**update_config_group_association**](ConfigurationConfigurationGroupApi.md#update_config_group_association) | **PUT** /v1/config-group/{configGroupId}/device/associate | 


# **create_config_group**
> str create_config_group()



Create a new Configuration Group

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    body = "TODO" # str | Config Group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_config_group(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->create_config_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Config Group | [optional]

### Return type

**str**

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

# **create_config_group_association**
> create_config_group_association(config_group_id)



Create associations with device and a config group

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_config_group_association(config_group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->create_config_group_association: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_config_group_association(config_group_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->create_config_group_association: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **create_config_group_device_variables**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_config_group_device_variables(config_group_id)



assign values to device variables<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request import GetO365PreferredPathFromVAnalyticsRequest
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | Config Group Id
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_config_group_device_variables(config_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->create_config_group_device_variables: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_config_group_device_variables(config_group_id, get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->create_config_group_device_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**| Config Group Id |
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

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

# **create_config_group_device_variables1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_config_group_device_variables1(config_group_id)



assign values to device variables

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | Config Group Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_config_group_device_variables1(config_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->create_config_group_device_variables1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**| Config Group Id |

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

# **delete_config_group**
> delete_config_group(config_group_id)



Delete Config Group

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_config_group(config_group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->delete_config_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**|  |

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

# **delete_config_group_association**
> delete_config_group_association(config_group_id)



Delete Config Group Association from devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_config_group_association(config_group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->delete_config_group_association: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_config_group_association(config_group_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->delete_config_group_association: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **deploy_config_group**
> String deploy_config_group(config_group_id)



deploy config group to devices<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request import GetO365PreferredPathFromVAnalyticsRequest
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | Config Group Id
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.deploy_config_group(config_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->deploy_config_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.deploy_config_group(config_group_id, get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->deploy_config_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**| Config Group Id |
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

### Return type

[**String**](String.md)

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

# **edit_config_group**
> str edit_config_group(config_group_id)



Edit a Configuration Group

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | 
    body = "TODO" # str | Config Group (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_config_group(config_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->edit_config_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_config_group(config_group_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->edit_config_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**|  |
 **body** | **str**| Config Group | [optional]

### Return type

**str**

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

# **get_cedge_config_group_schema_by_schema_type**
> str get_cedge_config_group_schema_by_schema_type()



Get a Cedge famiy Configuration Group Schema by Schema Type

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    schema_type = "post" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cedge_config_group_schema_by_schema_type(schema_type=schema_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->get_cedge_config_group_schema_by_schema_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_type** | **str**|  | [optional]

### Return type

**str**

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

# **get_config_group**
> ConfigGroup get_config_group(config_group_id)



Get a Configuration Group by ID

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from openapi_client.model.config_group import ConfigGroup
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_config_group(config_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->get_config_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**|  |

### Return type

[**ConfigGroup**](ConfigGroup.md)

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

# **get_config_group_association**
> get_config_group_association(config_group_id)



Get devices association with a config group

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_config_group_association(config_group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->get_config_group_association: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**|  |

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

# **get_config_group_by_solution**
> str get_config_group_by_solution()



Get a Configuration Group by Solution

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    solution = "solution_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_config_group_by_solution(solution=solution)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->get_config_group_by_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution** | **str**|  | [optional]

### Return type

**str**

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

# **get_config_group_device_configuration_preview**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_config_group_device_configuration_preview(config_group_id, device_id)



Get a preview of the configuration for a device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request import GetO365PreferredPathFromVAnalyticsRequest
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | Config Group Id
    device_id = "deviceId_example" # str | Device Id
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_config_group_device_configuration_preview(config_group_id, device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->get_config_group_device_configuration_preview: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_config_group_device_configuration_preview(config_group_id, device_id, get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->get_config_group_device_configuration_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**| Config Group Id |
 **device_id** | **str**| Device Id |
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

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

# **get_config_group_device_variables**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_config_group_device_variables(config_group_id)



Get device variables<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | Config Group Id
    device_id = "device-id_example" # str | Comma separated device id's like d1,d2 (optional)
    suggestions = True # bool | Suggestions for possible values (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_config_group_device_variables(config_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->get_config_group_device_variables: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_config_group_device_variables(config_group_id, device_id=device_id, suggestions=suggestions)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->get_config_group_device_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**| Config Group Id |
 **device_id** | **str**| Comma separated device id&#39;s like d1,d2 | [optional]
 **suggestions** | **bool**| Suggestions for possible values | [optional]

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

# **update_config_group_association**
> update_config_group_association(config_group_id)



Move the devices from one config group to another

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_configuration_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_configuration_group_api.ConfigurationConfigurationGroupApi(api_client)
    config_group_id = "configGroupId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_config_group_association(config_group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->update_config_group_association: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_config_group_association(config_group_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationConfigurationGroupApi->update_config_group_association: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_group_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

