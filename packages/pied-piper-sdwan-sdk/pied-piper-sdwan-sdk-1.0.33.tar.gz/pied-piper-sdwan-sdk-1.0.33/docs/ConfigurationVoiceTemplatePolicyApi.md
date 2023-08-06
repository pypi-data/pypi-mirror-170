# openapi_client.ConfigurationVoiceTemplatePolicyApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_voice_template**](ConfigurationVoiceTemplatePolicyApi.md#create_voice_template) | **POST** /template/policy/voice | 
[**delete_voice_template**](ConfigurationVoiceTemplatePolicyApi.md#delete_voice_template) | **DELETE** /template/policy/voice/{policyId} | 
[**edit_voice_template**](ConfigurationVoiceTemplatePolicyApi.md#edit_voice_template) | **PUT** /template/policy/voice/{policyId} | 
[**generate_voice_policy_summary**](ConfigurationVoiceTemplatePolicyApi.md#generate_voice_policy_summary) | **GET** /template/policy/voice/summary | 
[**generate_voice_template_list**](ConfigurationVoiceTemplatePolicyApi.md#generate_voice_template_list) | **GET** /template/policy/voice | 
[**get_device_list_by_policy_id**](ConfigurationVoiceTemplatePolicyApi.md#get_device_list_by_policy_id) | **GET** /template/policy/voice/devices/{policyId} | 
[**get_template_by_id**](ConfigurationVoiceTemplatePolicyApi.md#get_template_by_id) | **GET** /template/policy/voice/definition/{policyId} | 
[**get_voice_policy_device_list**](ConfigurationVoiceTemplatePolicyApi.md#get_voice_policy_device_list) | **GET** /template/policy/voice/devices | 
[**get_voice_templates_for_device**](ConfigurationVoiceTemplatePolicyApi.md#get_voice_templates_for_device) | **GET** /template/policy/voice/{deviceModel} | 


# **create_voice_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_voice_template()



Create Template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_voice_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_voice_template_policy_api.ConfigurationVoiceTemplatePolicyApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_voice_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->create_voice_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy template | [optional]

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

# **delete_voice_template**
> delete_voice_template(policy_id)



Delete Template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_voice_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_voice_template_policy_api.ConfigurationVoiceTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_voice_template(policy_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->delete_voice_template: %s\n" % e)
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

# **edit_voice_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_voice_template(policy_id)



Edit Template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_voice_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_voice_template_policy_api.ConfigurationVoiceTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy template (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_voice_template(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->edit_voice_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_voice_template(policy_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->edit_voice_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy template | [optional]

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

# **generate_voice_policy_summary**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_voice_policy_summary()



Get templates that map a device model

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_voice_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_voice_template_policy_api.ConfigurationVoiceTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_voice_policy_summary()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->generate_voice_policy_summary: %s\n" % e)
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

# **generate_voice_template_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_voice_template_list()



Generate template list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_voice_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_voice_template_policy_api.ConfigurationVoiceTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_voice_template_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->generate_voice_template_list: %s\n" % e)
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

# **get_device_list_by_policy_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_device_list_by_policy_id(policy_id)



Get device list by policy Id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_voice_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_voice_template_policy_api.ConfigurationVoiceTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_list_by_policy_id(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->get_device_list_by_policy_id: %s\n" % e)
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

# **get_template_by_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_template_by_id(policy_id)



Get templates by policy Id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_voice_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_voice_template_policy_api.ConfigurationVoiceTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_template_by_id(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->get_template_by_id: %s\n" % e)
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

# **get_voice_policy_device_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_voice_policy_device_list()



Get all device list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_voice_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_voice_template_policy_api.ConfigurationVoiceTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_voice_policy_device_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->get_voice_policy_device_list: %s\n" % e)
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

# **get_voice_templates_for_device**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_voice_templates_for_device(device_model)



Get templates that map a device model

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_voice_template_policy_api
from openapi_client.model.device_model import DeviceModel
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_voice_template_policy_api.ConfigurationVoiceTemplatePolicyApi(api_client)
    device_model = DeviceModel(
        device_model="device_model_example",
    ) # DeviceModel | Device model

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_voice_templates_for_device(device_model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationVoiceTemplatePolicyApi->get_voice_templates_for_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_model** | **DeviceModel**| Device model |

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

