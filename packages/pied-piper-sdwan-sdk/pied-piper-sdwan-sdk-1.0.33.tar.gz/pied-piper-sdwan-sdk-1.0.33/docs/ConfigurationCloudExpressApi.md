# openapi_client.ConfigurationCloudExpressApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_apps**](ConfigurationCloudExpressApi.md#add_apps) | **POST** /template/cloudx/manage/apps | 
[**add_cloudx_interfaces**](ConfigurationCloudExpressApi.md#add_cloudx_interfaces) | **POST** /template/cloudx/interfaces | 
[**add_cloudx_type**](ConfigurationCloudExpressApi.md#add_cloudx_type) | **POST** /template/cloudx/addcloudx/{type} | 
[**delete_webex_prefix_lists**](ConfigurationCloudExpressApi.md#delete_webex_prefix_lists) | **DELETE** /cloudservices/app/webex | 
[**edit_apps**](ConfigurationCloudExpressApi.md#edit_apps) | **PUT** /template/cloudx/manage/apps | 
[**enable_webex**](ConfigurationCloudExpressApi.md#enable_webex) | **POST** /cloudservices/app/webex | 
[**enable_webex1**](ConfigurationCloudExpressApi.md#enable_webex1) | **PUT** /cloudservices/app/webex | 
[**get_apps**](ConfigurationCloudExpressApi.md#get_apps) | **GET** /template/cloudx/manage/apps | 
[**get_attached_client_list**](ConfigurationCloudExpressApi.md#get_attached_client_list) | **GET** /template/cloudx/attachedclient | 
[**get_attached_dia_list**](ConfigurationCloudExpressApi.md#get_attached_dia_list) | **GET** /template/cloudx/attacheddia | 
[**get_attached_gateway_list**](ConfigurationCloudExpressApi.md#get_attached_gateway_list) | **GET** /template/cloudx/attachedgateway | 
[**get_cloud_x_available_apps**](ConfigurationCloudExpressApi.md#get_cloud_x_available_apps) | **GET** /template/cloudx/availableapps | 
[**get_cloud_x_status**](ConfigurationCloudExpressApi.md#get_cloud_x_status) | **GET** /template/cloudx | 
[**get_dia_list**](ConfigurationCloudExpressApi.md#get_dia_list) | **GET** /template/cloudx/dialist | 
[**get_gateway_list**](ConfigurationCloudExpressApi.md#get_gateway_list) | **GET** /template/cloudx/gatewaylist | 
[**get_site_list**](ConfigurationCloudExpressApi.md#get_site_list) | **GET** /template/cloudx/clientlist | 
[**site_per_app**](ConfigurationCloudExpressApi.md#site_per_app) | **GET** /template/cloudx/status | 


# **add_apps**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] add_apps()



Add apps and vpns

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloudx apps and vpns (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_apps(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->add_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloudx apps and vpns | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **add_cloudx_interfaces**
> add_cloudx_interfaces()



Enable cloudx gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloudx (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_cloudx_interfaces(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->add_cloudx_interfaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloudx | [optional]

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

# **add_cloudx_type**
> add_cloudx_type(type)



Add cloudx gateway

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)
    type = "type_example" # str | Cloudx type
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloudx (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_cloudx_type(type)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->add_cloudx_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_cloudx_type(type, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->add_cloudx_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Cloudx type |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloudx | [optional]

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

# **delete_webex_prefix_lists**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] delete_webex_prefix_lists()



deleteWebexPrefixLists

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | TMP-Cloudx apps and vpns (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_webex_prefix_lists(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->delete_webex_prefix_lists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| TMP-Cloudx apps and vpns | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **edit_apps**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_apps()



Edit apps and vpns

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloudx apps and vpns (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_apps(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->edit_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloudx apps and vpns | [optional]

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

# **enable_webex**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] enable_webex()



Add Webex App

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloudx apps and vpns (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.enable_webex(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->enable_webex: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloudx apps and vpns | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **enable_webex1**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] enable_webex1()



Day N- Update Webex App

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloudx apps and vpns (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.enable_webex1(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->enable_webex1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloudx apps and vpns | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_apps**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_apps()



Get apps and vpns

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_apps()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->get_apps: %s\n" % e)
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

# **get_attached_client_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_attached_client_list()



Get attached client site list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_attached_client_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->get_attached_client_list: %s\n" % e)
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

# **get_attached_dia_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_attached_dia_list()



Get attached Dia site list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_attached_dia_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->get_attached_dia_list: %s\n" % e)
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

# **get_attached_gateway_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_attached_gateway_list()



Get attached gateway list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_attached_gateway_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->get_attached_gateway_list: %s\n" % e)
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

# **get_cloud_x_available_apps**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cloud_x_available_apps()



Get CloudX available apps list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_x_available_apps()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->get_cloud_x_available_apps: %s\n" % e)
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

# **get_cloud_x_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cloud_x_status()



Get CloudX feature list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_x_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->get_cloud_x_status: %s\n" % e)
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

# **get_dia_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_dia_list()



Get Dia site list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_dia_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->get_dia_list: %s\n" % e)
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

# **get_gateway_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_gateway_list()



Get gateway list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_gateway_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->get_gateway_list: %s\n" % e)
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

# **get_site_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_site_list()



Get site list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_site_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->get_site_list: %s\n" % e)
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

# **site_per_app**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] site_per_app(app_name)



Get sites per application per vpn

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_express_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_express_api.ConfigurationCloudExpressApi(api_client)
    app_name = "appName_example" # str | App name
    vpn_id = 1 # int | VPN Id (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.site_per_app(app_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->site_per_app: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.site_per_app(app_name, vpn_id=vpn_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudExpressApi->site_per_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| App name |
 **vpn_id** | **int**| VPN Id | [optional]

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

