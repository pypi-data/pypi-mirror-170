# openapi_client.ConfigurationNetworkDesignTemplatesApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_device_profile_template**](ConfigurationNetworkDesignTemplatesApi.md#edit_device_profile_template) | **PUT** /networkdesign/profile/template/{templateId} | 
[**edit_global_template**](ConfigurationNetworkDesignTemplatesApi.md#edit_global_template) | **PUT** /networkdesign/global/template/{templateId} | 
[**generate_profile_template_list**](ConfigurationNetworkDesignTemplatesApi.md#generate_profile_template_list) | **GET** /networkdesign/profile/template | 
[**get_device_profile_feature_template_list**](ConfigurationNetworkDesignTemplatesApi.md#get_device_profile_feature_template_list) | **GET** /networkdesign/profile/feature | 
[**get_device_profile_template**](ConfigurationNetworkDesignTemplatesApi.md#get_device_profile_template) | **GET** /networkdesign/profile/template/{templateId} | 
[**get_global_template**](ConfigurationNetworkDesignTemplatesApi.md#get_global_template) | **GET** /networkdesign/global/template/{templateId} | 


# **edit_device_profile_template**
> edit_device_profile_template(template_id)



Edit device profile template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_templates_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_templates_api.ConfigurationNetworkDesignTemplatesApi(api_client)
    template_id = "templateId_example" # str | Template Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Global template (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.edit_device_profile_template(template_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignTemplatesApi->edit_device_profile_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_device_profile_template(template_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignTemplatesApi->edit_device_profile_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Global template | [optional]

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

# **edit_global_template**
> edit_global_template(template_id)



Edit global template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_templates_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_templates_api.ConfigurationNetworkDesignTemplatesApi(api_client)
    template_id = "templateId_example" # str | Template Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Global template (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.edit_global_template(template_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignTemplatesApi->edit_global_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_global_template(template_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignTemplatesApi->edit_global_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Global template | [optional]

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

# **generate_profile_template_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_profile_template_list()



Generate profile template list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_templates_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_templates_api.ConfigurationNetworkDesignTemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_profile_template_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignTemplatesApi->generate_profile_template_list: %s\n" % e)
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

# **get_device_profile_feature_template_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_device_profile_feature_template_list()



Generate device profile template list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_templates_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_templates_api.ConfigurationNetworkDesignTemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_profile_feature_template_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignTemplatesApi->get_device_profile_feature_template_list: %s\n" % e)
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

# **get_device_profile_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_profile_template(template_id)



Get device profile template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_templates_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_templates_api.ConfigurationNetworkDesignTemplatesApi(api_client)
    template_id = "templateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_profile_template(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignTemplatesApi->get_device_profile_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |

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

# **get_global_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_global_template(template_id)



Get global template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_templates_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_templates_api.ConfigurationNetworkDesignTemplatesApi(api_client)
    template_id = "templateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_global_template(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignTemplatesApi->get_global_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |

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

