# openapi_client.TroubleshootingToolsDeviceConnectivityApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_admin_tech_on_device**](TroubleshootingToolsDeviceConnectivityApi.md#copy_admin_tech_on_device) | **POST** /device/tools/admintech/copy | 
[**create_admin_tech**](TroubleshootingToolsDeviceConnectivityApi.md#create_admin_tech) | **POST** /device/tools/admintech | 
[**delete_admin_tech_file**](TroubleshootingToolsDeviceConnectivityApi.md#delete_admin_tech_file) | **DELETE** /device/tools/admintech/{requestID} | 
[**delete_admin_tech_on_device**](TroubleshootingToolsDeviceConnectivityApi.md#delete_admin_tech_on_device) | **DELETE** /device/tools/admintech/delete | 
[**download_admin_tech_file**](TroubleshootingToolsDeviceConnectivityApi.md#download_admin_tech_file) | **GET** /device/tools/admintech/download/{filename} | 
[**factory_reset**](TroubleshootingToolsDeviceConnectivityApi.md#factory_reset) | **POST** /device/tools/factoryreset | 
[**get_control_connections**](TroubleshootingToolsDeviceConnectivityApi.md#get_control_connections) | **GET** /troubleshooting/control/{uuid} | 
[**get_device_configuration**](TroubleshootingToolsDeviceConnectivityApi.md#get_device_configuration) | **GET** /troubleshooting/devicebringup | 
[**get_in_progress_count**](TroubleshootingToolsDeviceConnectivityApi.md#get_in_progress_count) | **GET** /device/tools/admintechs/inprogress | 
[**invalidate_device**](TroubleshootingToolsDeviceConnectivityApi.md#invalidate_device) | **POST** /certificate/device/invalidate | 
[**list_admin_techs**](TroubleshootingToolsDeviceConnectivityApi.md#list_admin_techs) | **GET** /device/tools/admintechs | 
[**list_admin_techs_on_device**](TroubleshootingToolsDeviceConnectivityApi.md#list_admin_techs_on_device) | **POST** /device/tools/admintechlist | 
[**nping_device**](TroubleshootingToolsDeviceConnectivityApi.md#nping_device) | **POST** /device/tools/nping/{deviceIP} | 
[**ping_device**](TroubleshootingToolsDeviceConnectivityApi.md#ping_device) | **POST** /device/tools/ping/{deviceIP} | 
[**process_interface_reset**](TroubleshootingToolsDeviceConnectivityApi.md#process_interface_reset) | **POST** /device/tools/reset/interface/{deviceIP} | 
[**process_port_hop_color**](TroubleshootingToolsDeviceConnectivityApi.md#process_port_hop_color) | **POST** /device/tools/porthopcolor/{deviceIP} | 
[**process_reset_user**](TroubleshootingToolsDeviceConnectivityApi.md#process_reset_user) | **POST** /device/tools/resetuser/{deviceIP} | 
[**service_path**](TroubleshootingToolsDeviceConnectivityApi.md#service_path) | **POST** /device/tools/servicepath/{deviceIP} | 
[**stage_device**](TroubleshootingToolsDeviceConnectivityApi.md#stage_device) | **POST** /certificate/device/stage | 
[**traceroute_device**](TroubleshootingToolsDeviceConnectivityApi.md#traceroute_device) | **POST** /device/tools/traceroute/{deviceIP} | 
[**tunnel_path**](TroubleshootingToolsDeviceConnectivityApi.md#tunnel_path) | **POST** /device/tools/tunnelpath/{deviceIP} | 
[**upload_admin_tech**](TroubleshootingToolsDeviceConnectivityApi.md#upload_admin_tech) | **POST** /device/tools/admintechs/upload | 


# **copy_admin_tech_on_device**
> copy_admin_tech_on_device()



copy admin tech logs

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Admin tech copy request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.copy_admin_tech_on_device(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->copy_admin_tech_on_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Admin tech copy request | [optional]

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

# **create_admin_tech**
> create_admin_tech()



Generate admin tech logs

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Admin tech generation request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_admin_tech(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->create_admin_tech: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Admin tech generation request | [optional]

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

# **delete_admin_tech_file**
> delete_admin_tech_file(request_id)



Delete admin tech logs

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    request_id = "requestID_example" # str | Request Id of admin tech generation request

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_admin_tech_file(request_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->delete_admin_tech_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request Id of admin tech generation request |

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

# **delete_admin_tech_on_device**
> delete_admin_tech_on_device()



delete admin tech logs

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Admin tech copy request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_admin_tech_on_device(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->delete_admin_tech_on_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Admin tech copy request | [optional]

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

# **download_admin_tech_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} download_admin_tech_file(filename)



Download admin tech logs

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    filename = "filename_example" # str | Admin tech file

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.download_admin_tech_file(filename)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->download_admin_tech_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Admin tech file |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **factory_reset**
> factory_reset()



Device factory reset

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device factory reset (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.factory_reset(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->factory_reset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device factory reset | [optional]

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

# **get_control_connections**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_control_connections(uuid)



Troubleshoot control connections

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_control_connections(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->get_control_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **get_device_configuration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_configuration(uuid)



Debug device bring up

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_configuration(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->get_device_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **get_in_progress_count**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_in_progress_count()



Get device admin-tech InProgressCount

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_in_progress_count()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->get_in_progress_count: %s\n" % e)
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

# **invalidate_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} invalidate_device()



invalidate the device

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vEdge device info (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.invalidate_device(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->invalidate_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vEdge device info | [optional]

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

# **list_admin_techs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_admin_techs()



Get device admin-tech information

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_admin_techs()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->list_admin_techs: %s\n" % e)
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

# **list_admin_techs_on_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_admin_techs_on_device()



List admin tech logs

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Admin tech listing request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_admin_techs_on_device(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->list_admin_techs_on_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Admin tech listing request | [optional]

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

# **nping_device**
> nping_device(device_ip)



NPing device

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | NPing parameter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.nping_device(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->nping_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.nping_device(device_ip, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->nping_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| NPing parameter | [optional]

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

# **ping_device**
> ping_device(device_ip)



Ping device

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Ping parameter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.ping_device(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->ping_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.ping_device(device_ip, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->ping_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Ping parameter | [optional]

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

# **process_interface_reset**
> process_interface_reset(device_ip)



Reset device interface

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device interface (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.process_interface_reset(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->process_interface_reset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.process_interface_reset(device_ip, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->process_interface_reset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device interface | [optional]

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

# **process_port_hop_color**
> process_port_hop_color(device_ip)



Request port hop color

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device port hop color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.process_port_hop_color(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->process_port_hop_color: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.process_port_hop_color(device_ip, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->process_port_hop_color: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device port hop color | [optional]

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

# **process_reset_user**
> process_reset_user(device_ip)



Request reset user

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device user reset (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.process_reset_user(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->process_reset_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.process_reset_user(device_ip, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->process_reset_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device user reset | [optional]

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

# **service_path**
> service_path(device_ip)



Service path

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Service path parameter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.service_path(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->service_path: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.service_path(device_ip, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->service_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Service path parameter | [optional]

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

# **stage_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} stage_device()



Stop data traffic to device

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vEdge device info (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.stage_device(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->stage_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vEdge device info | [optional]

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

# **traceroute_device**
> traceroute_device(device_ip)



Traceroute

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Traceroute parameter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.traceroute_device(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->traceroute_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.traceroute_device(device_ip, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->traceroute_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Traceroute parameter | [optional]

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

# **tunnel_path**
> tunnel_path(device_ip)



TunnelPath

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    device_ip = "deviceIP_example" # str | Device IP
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | TunnelPath parameter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.tunnel_path(device_ip)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->tunnel_path: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.tunnel_path(device_ip, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->tunnel_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ip** | **str**| Device IP |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| TunnelPath parameter | [optional]

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

# **upload_admin_tech**
> upload_admin_tech()



upload admin tech to SR

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_device_connectivity_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_device_connectivity_api.TroubleshootingToolsDeviceConnectivityApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Admin tech upload request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.upload_admin_tech(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDeviceConnectivityApi->upload_admin_tech: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Admin tech upload request | [optional]

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

