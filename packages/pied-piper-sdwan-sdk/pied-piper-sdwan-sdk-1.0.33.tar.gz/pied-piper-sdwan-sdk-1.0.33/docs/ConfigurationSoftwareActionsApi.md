# openapi_client.ConfigurationSoftwareActionsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remote_server**](ConfigurationSoftwareActionsApi.md#add_remote_server) | **POST** /device/action/remote-server | 
[**create_image_url**](ConfigurationSoftwareActionsApi.md#create_image_url) | **POST** /device/action/software | 
[**delete_image_url**](ConfigurationSoftwareActionsApi.md#delete_image_url) | **DELETE** /device/action/software/{versionId} | 
[**delete_remote_server**](ConfigurationSoftwareActionsApi.md#delete_remote_server) | **DELETE** /device/action/remote-server/{id} | 
[**find_software_images**](ConfigurationSoftwareActionsApi.md#find_software_images) | **GET** /device/action/software | 
[**find_software_images_with_filters**](ConfigurationSoftwareActionsApi.md#find_software_images_with_filters) | **GET** /device/action/software/images | 
[**find_software_version**](ConfigurationSoftwareActionsApi.md#find_software_version) | **GET** /device/action/software/version | 
[**find_v_edge_software_version**](ConfigurationSoftwareActionsApi.md#find_v_edge_software_version) | **GET** /device/action/software/vedge/version | 
[**find_ztp_software_version**](ConfigurationSoftwareActionsApi.md#find_ztp_software_version) | **GET** /device/action/software/ztp/version | 
[**get_image_properties**](ConfigurationSoftwareActionsApi.md#get_image_properties) | **GET** /device/action/software/imageProperties/{versionId} | 
[**get_pnf_properties**](ConfigurationSoftwareActionsApi.md#get_pnf_properties) | **GET** /device/action/software/pnfproperties/{pnfType} | 
[**get_remote_server_by_id**](ConfigurationSoftwareActionsApi.md#get_remote_server_by_id) | **GET** /device/action/remote-server/{id} | 
[**get_remote_server_list**](ConfigurationSoftwareActionsApi.md#get_remote_server_list) | **GET** /device/action/remote-server | 
[**get_vnf_properties**](ConfigurationSoftwareActionsApi.md#get_vnf_properties) | **GET** /device/action/software/vnfproperties/{versionId} | 
[**update_image_url**](ConfigurationSoftwareActionsApi.md#update_image_url) | **PUT** /device/action/software/{versionId} | 
[**update_remote_server**](ConfigurationSoftwareActionsApi.md#update_remote_server) | **PUT** /device/action/remote-server/{id} | 


# **add_remote_server**
> add_remote_server()



Add a new remote server entry.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Request payload for a new remote server entry. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_remote_server(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->add_remote_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Request payload for a new remote server entry. | [optional]

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

# **create_image_url**
> create_image_url()



Create software image URL

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Create software image request payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_image_url(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->create_image_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Create software image request payload | [optional]

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

# **delete_image_url**
> delete_image_url(version_id)



Delete software image URL

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    version_id = "versionId_example" # str | Version

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_image_url(version_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->delete_image_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| Version |

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

# **delete_remote_server**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] delete_remote_server(id)



Delete remote server for the specified ID

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    id = "id_example" # str | Remote Server ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_remote_server(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->delete_remote_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Remote Server ID |

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

# **find_software_images**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] find_software_images()



Get software images

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_software_images()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->find_software_images: %s\n" % e)
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

# **find_software_images_with_filters**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] find_software_images_with_filters(image_type)



Get software images

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    image_type = "imageType_example" # str | Image type
    vnf_type = "vnfType_example" # str | VNF type (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.find_software_images_with_filters(image_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->find_software_images_with_filters: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.find_software_images_with_filters(image_type, vnf_type=vnf_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->find_software_images_with_filters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_type** | **str**| Image type |
 **vnf_type** | **str**| VNF type | [optional]

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

# **find_software_version**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_software_version()



Get software version

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_software_version()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->find_software_version: %s\n" % e)
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

# **find_v_edge_software_version**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_v_edge_software_version()



Get vEdge software version

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_v_edge_software_version()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->find_v_edge_software_version: %s\n" % e)
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

# **find_ztp_software_version**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_ztp_software_version()



Get ZTP software version

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_ztp_software_version()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->find_ztp_software_version: %s\n" % e)
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

# **get_image_properties**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_image_properties(version_id)



Get Image Properties

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    version_id = "versionId_example" # str | Version

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_image_properties(version_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->get_image_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| Version |

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

# **get_pnf_properties**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_pnf_properties(pnf_type)



Get PNF Properties

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    pnf_type = "pnfType_example" # str | PNF type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_pnf_properties(pnf_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->get_pnf_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pnf_type** | **str**| PNF type |

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

# **get_remote_server_by_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_remote_server_by_id(id)



Get remote server for the specified ID

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    id = "id_example" # str | Remote Server ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_remote_server_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->get_remote_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Remote Server ID |

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

# **get_remote_server_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_remote_server_list()



Get list of remote servers

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_remote_server_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->get_remote_server_list: %s\n" % e)
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

# **get_vnf_properties**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_vnf_properties(version_id)



Get VNF Properties

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    version_id = "versionId_example" # str | Version

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vnf_properties(version_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->get_vnf_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| Version |

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

# **update_image_url**
> update_image_url(version_id)



Update software image URL

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    version_id = "versionId_example" # str | Version
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Update software image request payload (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_image_url(version_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->update_image_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_image_url(version_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->update_image_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| Version |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Update software image request payload | [optional]

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

# **update_remote_server**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] update_remote_server(id)



Update remote server for the specified ID

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_software_actions_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_software_actions_api.ConfigurationSoftwareActionsApi(api_client)
    id = "id_example" # str | Remote Server ID
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_remote_server(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->update_remote_server: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_remote_server(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSoftwareActionsApi->update_remote_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Remote Server ID |
 **body** | **str**|  | [optional]

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

