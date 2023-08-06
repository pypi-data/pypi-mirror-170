# openapi_client.ConfigurationTemplateConfigurationApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_cli_mode_devices**](ConfigurationTemplateConfigurationApi.md#generate_cli_mode_devices) | **GET** /template/config/device/mode/cli | 
[**generatev_manage_mode_devices**](ConfigurationTemplateConfigurationApi.md#generatev_manage_mode_devices) | **GET** /template/config/device/mode/vmanage | 
[**get_attached_config**](ConfigurationTemplateConfigurationApi.md#get_attached_config) | **GET** /template/config/attached/{deviceId} | 
[**get_compatible_devices**](ConfigurationTemplateConfigurationApi.md#get_compatible_devices) | **GET** /template/config/rmalist/{oldDeviceId} | 
[**get_device_diff**](ConfigurationTemplateConfigurationApi.md#get_device_diff) | **GET** /template/config/diff/{deviceId} | 
[**get_running_config**](ConfigurationTemplateConfigurationApi.md#get_running_config) | **GET** /template/config/running/{deviceId} | 
[**get_vpn_for_device**](ConfigurationTemplateConfigurationApi.md#get_vpn_for_device) | **GET** /template/config/vpn/{deviceId} | 
[**rma_update**](ConfigurationTemplateConfigurationApi.md#rma_update) | **PUT** /template/config/rmaupdate | 
[**update_device_to_cli_mode**](ConfigurationTemplateConfigurationApi.md#update_device_to_cli_mode) | **POST** /template/config/device/mode/cli | 
[**upload_config**](ConfigurationTemplateConfigurationApi.md#upload_config) | **PUT** /template/config/attach/{deviceId} | 


# **generate_cli_mode_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generate_cli_mode_devices(type)



Generates a JSON object that contains a list of valid devices in CLI mode

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    type = "vedge" # str | Device type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_cli_mode_devices(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->generate_cli_mode_devices: %s\n" % e)
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

# **generatev_manage_mode_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] generatev_manage_mode_devices(type)



Get list of devices that are allowable for vmanage modes

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    type = "vedge" # str | Device type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generatev_manage_mode_devices(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->generatev_manage_mode_devices: %s\n" % e)
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

# **get_attached_config**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_attached_config(device_id)



Get local template attached config for given device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    device_id = "deviceId_example" # str | Device Model ID
    type = "CFS" # str | Config type (optional) if omitted the server will use the default value of "CFS"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_attached_config(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->get_attached_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attached_config(device_id, type=type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->get_attached_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Model ID |
 **type** | **str**| Config type | [optional] if omitted the server will use the default value of "CFS"

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

# **get_compatible_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_compatible_devices(old_device_id)



Get compatible devices of model, chassis number, certificate serial number with the old device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    old_device_id = "oldDeviceId_example" # str | Device Model ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_compatible_devices(old_device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->get_compatible_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_device_id** | **str**| Device Model ID |

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

# **get_device_diff**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_diff(device_id)



Generates a JSON object that contains the diff for a given device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    device_id = "deviceId_example" # str | Device Model ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_diff(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->get_device_diff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Model ID |

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

# **get_running_config**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_running_config(device_id)



Get device running config

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    device_id = "deviceId_example" # str | Device Model ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_running_config(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->get_running_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Model ID |

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

# **get_vpn_for_device**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vpn_for_device(device_id)



Get list of configured VPN (excluding reserved VPN) for a device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    device_id = "deviceId_example" # str | Device Model ID

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vpn_for_device(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->get_vpn_for_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Model ID |

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

# **rma_update**
> rma_update()



Update new device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.rma_update(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->rma_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template config | [optional]

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

# **update_device_to_cli_mode**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_device_to_cli_mode()



Given a JSON list of devices not managed by any third member partners, push to devices from a CLI template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_device_to_cli_mode(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->update_device_to_cli_mode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device list | [optional]

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

# **upload_config**
> upload_config(device_id)



Upload device config

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_template_configuration_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_template_configuration_api.ConfigurationTemplateConfigurationApi(api_client)
    device_id = "deviceId_example" # str | Device Model ID
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template config (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.upload_config(device_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->upload_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.upload_config(device_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationTemplateConfigurationApi->upload_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Model ID |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template config | [optional]

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

