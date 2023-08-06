# openapi_client.ConfigurationSecurityTemplatePolicyApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_security_template**](ConfigurationSecurityTemplatePolicyApi.md#create_security_template) | **POST** /template/policy/security | 
[**delete_security_template**](ConfigurationSecurityTemplatePolicyApi.md#delete_security_template) | **DELETE** /template/policy/security/{policyId} | 
[**edit_security_template**](ConfigurationSecurityTemplatePolicyApi.md#edit_security_template) | **PUT** /template/policy/security/{policyId} | 
[**edit_template_with_lenient_lock**](ConfigurationSecurityTemplatePolicyApi.md#edit_template_with_lenient_lock) | **PUT** /template/policy/security/staging/{policyId} | 
[**generate_security_policy_summary**](ConfigurationSecurityTemplatePolicyApi.md#generate_security_policy_summary) | **GET** /template/policy/security/summary | 
[**generate_security_template_list**](ConfigurationSecurityTemplatePolicyApi.md#generate_security_template_list) | **GET** /template/policy/security | 
[**get_device_list_by_id**](ConfigurationSecurityTemplatePolicyApi.md#get_device_list_by_id) | **GET** /template/policy/security/devices/{policyId} | 
[**get_security_policy_device_list**](ConfigurationSecurityTemplatePolicyApi.md#get_security_policy_device_list) | **GET** /template/policy/security/devices | 
[**get_security_template**](ConfigurationSecurityTemplatePolicyApi.md#get_security_template) | **GET** /template/policy/security/definition/{policyId} | 
[**get_security_templates_for_device**](ConfigurationSecurityTemplatePolicyApi.md#get_security_templates_for_device) | **GET** /template/policy/security/{deviceModel} | 


# **create_security_template**
> create_security_template()



Create Template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_security_template(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->create_security_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy template | [optional]

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

# **delete_security_template**
> delete_security_template(policy_id)



Delete Template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_security_template(policy_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->delete_security_template: %s\n" % e)
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

# **edit_security_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_security_template(policy_id)



Edit Template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy template (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_security_template(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->edit_security_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_security_template(policy_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->edit_security_template: %s\n" % e)
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

# **edit_template_with_lenient_lock**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_template_with_lenient_lock(policy_id)



Edit Template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy template (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_template_with_lenient_lock(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->edit_template_with_lenient_lock: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_template_with_lenient_lock(policy_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->edit_template_with_lenient_lock: %s\n" % e)
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

# **generate_security_policy_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_security_policy_summary()



Generate security policy summary

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.generate_security_policy_summary()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->generate_security_policy_summary: %s\n" % e)
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

# **generate_security_template_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_security_template_list()



Generate template list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)
    mode = "mode_example" # str | Mode (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_security_template_list(mode=mode)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->generate_security_template_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **str**| Mode | [optional]

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

# **get_device_list_by_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_device_list_by_id(policy_id)



Get device list by Id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_list_by_id(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->get_device_list_by_id: %s\n" % e)
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

# **get_security_policy_device_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_security_policy_device_list()



Get device list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_security_policy_device_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->get_security_policy_device_list: %s\n" % e)
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

# **get_security_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_security_template(policy_id)



Get Template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_security_template(policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->get_security_template: %s\n" % e)
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

# **get_security_templates_for_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_security_templates_for_device(device_model)



Get templates that map a device model

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_security_template_policy_api
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
    api_instance = configuration_security_template_policy_api.ConfigurationSecurityTemplatePolicyApi(api_client)
    device_model = DeviceModel(
        device_model="device_model_example",
    ) # DeviceModel | Device model

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_security_templates_for_device(device_model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecurityTemplatePolicyApi->get_security_templates_for_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_model** | **DeviceModel**| Device model |

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

