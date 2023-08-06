# openapi_client.ConfigurationAzureConnectApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_azure_connect_cred_and_add**](ConfigurationAzureConnectApi.md#authenticate_azure_connect_cred_and_add) | **POST** /template/cortex/cloud/authenticate | 
[**delete_wan_resource_groups**](ConfigurationAzureConnectApi.md#delete_wan_resource_groups) | **DELETE** /template/cortex/wanrg | 
[**edit_wan_resource_groups**](ConfigurationAzureConnectApi.md#edit_wan_resource_groups) | **PUT** /template/cortex/wanrg | 
[**get_cortex_status**](ConfigurationAzureConnectApi.md#get_cortex_status) | **GET** /template/cortex | 
[**get_mapped_wan_resource_groups**](ConfigurationAzureConnectApi.md#get_mapped_wan_resource_groups) | **GET** /template/cortex/map | 
[**get_wan_resource_groups**](ConfigurationAzureConnectApi.md#get_wan_resource_groups) | **GET** /template/cortex/wanrg | 
[**save_wan_resource_groups**](ConfigurationAzureConnectApi.md#save_wan_resource_groups) | **POST** /template/cortex/wanrg | 
[**sync_wan_resource_groups**](ConfigurationAzureConnectApi.md#sync_wan_resource_groups) | **POST** /template/cortex/sync | 


# **authenticate_azure_connect_cred_and_add**
> authenticate_azure_connect_cred_and_add()



Authenticate Cloud Account Credentials

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_azure_connect_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_azure_connect_api.ConfigurationAzureConnectApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Credential (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.authenticate_azure_connect_cred_and_add(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAzureConnectApi->authenticate_azure_connect_cred_and_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Credential | [optional]

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

# **delete_wan_resource_groups**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_wan_resource_groups()



Delete WAN Resource Groups

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_azure_connect_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_azure_connect_api.ConfigurationAzureConnectApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | WAN resource group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_wan_resource_groups(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAzureConnectApi->delete_wan_resource_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| WAN resource group | [optional]

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

# **edit_wan_resource_groups**
> edit_wan_resource_groups()



Edit WAN Resource Groups

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_azure_connect_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_azure_connect_api.ConfigurationAzureConnectApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | WAN resource group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_wan_resource_groups(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAzureConnectApi->edit_wan_resource_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| WAN resource group | [optional]

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

# **get_cortex_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cortex_status()



Get Cortex List

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_azure_connect_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_azure_connect_api.ConfigurationAzureConnectApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cortex_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAzureConnectApi->get_cortex_status: %s\n" % e)
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

# **get_mapped_wan_resource_groups**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mapped_wan_resource_groups(accountid, cloudregion)



Get Mapped WAN Resource Groups

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_azure_connect_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_azure_connect_api.ConfigurationAzureConnectApi(api_client)
    accountid = "accountid_example" # str | Account Id
    cloudregion = "cloudregion_example" # str | Cloud region

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_mapped_wan_resource_groups(accountid, cloudregion)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAzureConnectApi->get_mapped_wan_resource_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |
 **cloudregion** | **str**| Cloud region |

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

# **get_wan_resource_groups**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_wan_resource_groups(accountid)



Get WAN Resource Groups

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_azure_connect_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_azure_connect_api.ConfigurationAzureConnectApi(api_client)
    accountid = "accountid_example" # str | Account Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_wan_resource_groups(accountid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAzureConnectApi->get_wan_resource_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |

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

# **save_wan_resource_groups**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} save_wan_resource_groups()



Create WAN Resource Groups

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_azure_connect_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_azure_connect_api.ConfigurationAzureConnectApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | WAN resource group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.save_wan_resource_groups(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAzureConnectApi->save_wan_resource_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| WAN resource group | [optional]

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

# **sync_wan_resource_groups**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sync_wan_resource_groups()



Sync WAN Resource Groups

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_azure_connect_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_azure_connect_api.ConfigurationAzureConnectApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | WAN resource group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sync_wan_resource_groups(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAzureConnectApi->sync_wan_resource_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| WAN resource group | [optional]

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

