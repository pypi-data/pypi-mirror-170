# openapi_client.ConfigurationTemplateMasterApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_template_resource_group1**](ConfigurationTemplateMasterApi.md#change_template_resource_group1) | **POST** /template/device/resource-group/{resourceGroupName}/{templateId} | 
[**create_cli_template**](ConfigurationTemplateMasterApi.md#create_cli_template) | **POST** /template/device/cli | 
[**create_master_template**](ConfigurationTemplateMasterApi.md#create_master_template) | **POST** /template/device/feature | 
[**delete_master_template**](ConfigurationTemplateMasterApi.md#delete_master_template) | **DELETE** /template/device/{templateId} | 
[**edit_master_template**](ConfigurationTemplateMasterApi.md#edit_master_template) | **PUT** /template/device/{templateId} | 
[**generate_master_template_list**](ConfigurationTemplateMasterApi.md#generate_master_template_list) | **GET** /template/device | 
[**generate_template_for_migration**](ConfigurationTemplateMasterApi.md#generate_template_for_migration) | **GET** /template/device/migration | 
[**get_master_template_definition**](ConfigurationTemplateMasterApi.md#get_master_template_definition) | **GET** /template/device/object/{templateId} | 
[**get_out_of_sync_devices**](ConfigurationTemplateMasterApi.md#get_out_of_sync_devices) | **GET** /template/device/syncstatus/{templateId} | 
[**get_out_of_sync_templates**](ConfigurationTemplateMasterApi.md#get_out_of_sync_templates) | **GET** /template/device/syncstatus | 
[**is_migration_required**](ConfigurationTemplateMasterApi.md#is_migration_required) | **GET** /template/device/is_migration_required | 
[**migrate_templates**](ConfigurationTemplateMasterApi.md#migrate_templates) | **POST** /template/device/migration | 
[**migration_info**](ConfigurationTemplateMasterApi.md#migration_info) | **GET** /template/device/migration_info | 


# **change_template_resource_group1**
> change_template_resource_group1(template_id, resource_group_name)



Change template resource group

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    template_id = "templateId_example" # str | Template Id
    resource_group_name = "resourceGroupName_example" # str | Resource group name

    # example passing only required values which don't have defaults set
    try:
        api_instance.change_template_resource_group1(template_id, resource_group_name)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->change_template_resource_group1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |
 **resource_group_name** | **str**| Resource group name |

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

# **create_cli_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_cli_template()



Create CLI template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Create template request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_cli_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->create_cli_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Create template request | [optional]

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

# **create_master_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_master_template()



Create a device template from feature templates and sub templates<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Create template request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_master_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->create_master_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Create template request | [optional]

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

# **delete_master_template**
> delete_master_template(template_id)



Delete template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    template_id = "templateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_master_template(template_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->delete_master_template: %s\n" % e)
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

# **edit_master_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_master_template(template_id)



Edit template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    template_id = "templateId_example" # str | Template Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_master_template(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->edit_master_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_master_template(template_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->edit_master_template: %s\n" % e)
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

# **generate_master_template_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_master_template_list(feature)



Generate template list<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    feature = "lawful-interception" # str | Feature

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_master_template_list(feature)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->generate_master_template_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **str**| Feature |

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

# **generate_template_for_migration**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_template_for_migration()



Generate a list of templates which require migration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    has_aaa = True # bool | Return only those uses AAA (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_template_for_migration(has_aaa=has_aaa)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->generate_template_for_migration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **has_aaa** | **bool**| Return only those uses AAA | [optional]

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

# **get_master_template_definition**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_master_template_definition(template_id)



Generate template by Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    template_id = "templateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_master_template_definition(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->get_master_template_definition: %s\n" % e)
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

# **get_out_of_sync_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_out_of_sync_devices(template_id)



Get out of sync devices<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    template_id = "templateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_out_of_sync_devices(template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->get_out_of_sync_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template Id |

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

# **get_out_of_sync_templates**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_out_of_sync_templates()



Get template sync status<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_out_of_sync_templates()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->get_out_of_sync_templates: %s\n" % e)
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

# **is_migration_required**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} is_migration_required()



Check if any device templates need migration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.is_migration_required()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->is_migration_required: %s\n" % e)
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

# **migrate_templates**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} migrate_templates(id)



Migrate the device templates given the template Ids

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)
    id = [
        "id_example",
    ] # [str] | Template Id
    prefix = "cisco" # str | Prefix (optional) if omitted the server will use the default value of "cisco"
    include_all = True # bool | Include all flag (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.migrate_templates(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->migrate_templates: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.migrate_templates(id, prefix=prefix, include_all=include_all)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->migrate_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **[str]**| Template Id |
 **prefix** | **str**| Prefix | [optional] if omitted the server will use the default value of "cisco"
 **include_all** | **bool**| Include all flag | [optional] if omitted the server will use the default value of True

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

# **migration_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} migration_info()



Returns the mapping between old and migrated templates<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_master_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_master_api.ConfigurationTemplateMasterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.migration_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateMasterApi->migration_info: %s\n" % e)
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

