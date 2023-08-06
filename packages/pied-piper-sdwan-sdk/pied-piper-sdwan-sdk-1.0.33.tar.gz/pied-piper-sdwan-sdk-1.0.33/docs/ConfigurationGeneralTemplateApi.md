# openapi_client.ConfigurationGeneralTemplateApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_template_resource_group**](ConfigurationGeneralTemplateApi.md#change_template_resource_group) | **POST** /template/feature/resource-group/{resourceGroupName}/{templateId} | 
[**clone_template**](ConfigurationGeneralTemplateApi.md#clone_template) | **POST** /template/feature/clone | 
[**create_feature_template**](ConfigurationGeneralTemplateApi.md#create_feature_template) | **POST** /template/feature | 
[**create_li_template**](ConfigurationGeneralTemplateApi.md#create_li_template) | **POST** /template/feature/li | 
[**delete_general_template**](ConfigurationGeneralTemplateApi.md#delete_general_template) | **DELETE** /template/feature/{templateId} | 
[**edit_feature_template**](ConfigurationGeneralTemplateApi.md#edit_feature_template) | **PUT** /template/feature/{templateId} | 
[**edit_li_template**](ConfigurationGeneralTemplateApi.md#edit_li_template) | **PUT** /template/feature/li/{templateId} | 
[**generate_feature_template_list**](ConfigurationGeneralTemplateApi.md#generate_feature_template_list) | **GET** /template/feature | 
[**generate_master_template_definition**](ConfigurationGeneralTemplateApi.md#generate_master_template_definition) | **GET** /template/feature/master/{type_name} | 
[**generate_template_by_device_type**](ConfigurationGeneralTemplateApi.md#generate_template_by_device_type) | **GET** /template/feature/{deviceType} | 
[**generate_template_type_definition**](ConfigurationGeneralTemplateApi.md#generate_template_type_definition) | **GET** /template/feature/types/definition/{type_name}/{version} | 
[**generate_template_types**](ConfigurationGeneralTemplateApi.md#generate_template_types) | **GET** /template/feature/types | 
[**get_default_networks**](ConfigurationGeneralTemplateApi.md#get_default_networks) | **GET** /template/feature/default/networks | 
[**get_device_templates_attached_to_feature**](ConfigurationGeneralTemplateApi.md#get_device_templates_attached_to_feature) | **GET** /template/feature/devicetemplates/{templateId} | 
[**get_encrypted_string**](ConfigurationGeneralTemplateApi.md#get_encrypted_string) | **POST** /template/security/encryptText/encrypt | 
[**get_general_template**](ConfigurationGeneralTemplateApi.md#get_general_template) | **GET** /template/feature/object/{templateId} | 
[**get_network_interface**](ConfigurationGeneralTemplateApi.md#get_network_interface) | **GET** /template/feature/default/networkinterface | 
[**get_template_definition**](ConfigurationGeneralTemplateApi.md#get_template_definition) | **GET** /template/feature/definition/{templateId} | 
[**get_template_for_migration**](ConfigurationGeneralTemplateApi.md#get_template_for_migration) | **GET** /template/feature/migration | 
[**list_li_template**](ConfigurationGeneralTemplateApi.md#list_li_template) | **GET** /template/feature/li | 


# **change_template_resource_group**
> change_template_resource_group(template_id, resource_group_name)



Change template resource group

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    template_id = "templateId_example" # str | Template Id
    resource_group_name = "resourceGroupName_example" # str | Resrouce group name

    # example passing only required values which don't have defaults set
    try:
        api_instance.change_template_resource_group(template_id, resource_group_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->change_template_resource_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |
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

# **clone_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} clone_template(id, name, desc)



Clone a feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    id = "220a6bd0-28ef-4c88-92e6-ee7539396fd7" # str | Template Id to clone from
    name = "BR2-VPN10-Feature" # str | Name for the cloned template
    desc = "desc_example" # str | Description for the cloned template

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.clone_template(id, name, desc)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->clone_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template Id to clone from |
 **name** | **str**| Name for the cloned template |
 **desc** | **str**| Description for the cloned template |

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

# **create_feature_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_feature_template()



Create feature template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Feature template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_feature_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->create_feature_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Feature template | [optional]

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

# **create_li_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_li_template()



Create LI feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | LI template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_li_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->create_li_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| LI template | [optional]

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

# **delete_general_template**
> delete_general_template(template_id)



Delete feature template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    template_id = "templateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_general_template(template_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->delete_general_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |

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

# **edit_feature_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_feature_template(template_id)



Update feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    template_id = "templateId_example" # str | Template Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_feature_template(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->edit_feature_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_feature_template(template_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->edit_feature_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template | [optional]

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

# **edit_li_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_li_template(template_id)



Update LI feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    template_id = "templateId_example" # str | Template Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | LI template (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_li_template(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->edit_li_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_li_template(template_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->edit_li_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| LI template | [optional]

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

# **generate_feature_template_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_feature_template_list()



Get feature template list<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    summary = False # bool | Flag to include template definition (optional) if omitted the server will use the default value of False
    offset = 1 # int | Pagination offset (optional)
    limit = 0 # int | Pagination limit on templateId (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_feature_template_list(summary=summary, offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->generate_feature_template_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summary** | **bool**| Flag to include template definition | [optional] if omitted the server will use the default value of False
 **offset** | **int**| Pagination offset | [optional]
 **limit** | **int**| Pagination limit on templateId | [optional] if omitted the server will use the default value of 0

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

# **generate_master_template_definition**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_master_template_definition(type_name)



Generate template type definition by device type<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    type_name = "type_name_example" # str | Device type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_master_template_definition(type_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->generate_master_template_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| Device type |

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

# **generate_template_by_device_type**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_template_by_device_type(device_type)



Generate template based on device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    device_type = "deviceType_example" # str | Device type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_template_by_device_type(device_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->generate_template_by_device_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type** | **str**| Device type |

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

# **generate_template_type_definition**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_template_type_definition(type_name, version)



Generate template type definition<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    type_name = "type_name_example" # str | Feature template type
    version = "version_example" # str | Version

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_template_type_definition(type_name, version)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->generate_template_type_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| Feature template type |
 **version** | **str**| Version |

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

# **generate_template_types**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_template_types(type)



Generate template types<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    type = "vedge" # str | Device type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_template_types(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->generate_template_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Device type |

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

# **get_default_networks**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_default_networks(device_model)



Get default networks<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    device_model = "vedge-nfvis-ENCS5400" # str | Device model

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_default_networks(device_model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->get_default_networks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_model** | **str**| Device model |

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

# **get_device_templates_attached_to_feature**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_templates_attached_to_feature(template_id)



Get all device templates for this feature template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    template_id = "templateId_example" # str | Feature template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_templates_attached_to_feature(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->get_device_templates_attached_to_feature: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Feature template Id |

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

# **get_encrypted_string**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_encrypted_string()



Get Type 6 Encryptedd String for a given value

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Type6 Encryption (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_encrypted_string(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->get_encrypted_string: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Type6 Encryption | [optional]

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

# **get_general_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_general_template(template_id)



Get template object definition for given template Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    template_id = "templateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_general_template(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->get_general_template: %s\n" % e)
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

# **get_network_interface**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_network_interface(device_model)



Get default network interface<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    device_model = "ENCS" # str | Device model

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_network_interface(device_model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->get_network_interface: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_model** | **str**| Device model |

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

# **get_template_definition**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_template_definition(template_id)



Get the configured template definition for given template Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)
    template_id = "templateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_template_definition(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->get_template_definition: %s\n" % e)
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

# **get_template_for_migration**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_template_for_migration()



Generate a list of templates which require migration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_template_for_migration()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->get_template_for_migration: %s\n" % e)
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

# **list_li_template**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_li_template()



Get LI feature template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_general_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_general_template_api.ConfigurationGeneralTemplateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_li_template()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationGeneralTemplateApi->list_li_template: %s\n" % e)
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

