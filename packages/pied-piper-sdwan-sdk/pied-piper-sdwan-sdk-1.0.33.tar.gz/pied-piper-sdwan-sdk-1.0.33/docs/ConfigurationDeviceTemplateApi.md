# openapi_client.ConfigurationDeviceTemplateApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_device_template**](ConfigurationDeviceTemplateApi.md#attach_device_template) | **POST** /template/device/config/attachment | 
[**check_vbond**](ConfigurationDeviceTemplateApi.md#check_vbond) | **GET** /template/device/config/vbond | 
[**create_device_input**](ConfigurationDeviceTemplateApi.md#create_device_input) | **POST** /template/device/config/input | 
[**create_input_without_device**](ConfigurationDeviceTemplateApi.md#create_input_without_device) | **POST** /template/device/config/exportcsv | 
[**detach_device_template**](ConfigurationDeviceTemplateApi.md#detach_device_template) | **POST** /template/device/config/detach | 
[**detach_sites**](ConfigurationDeviceTemplateApi.md#detach_sites) | **POST** /template/device/config/detachcloudx | 
[**edit_cloudx_config**](ConfigurationDeviceTemplateApi.md#edit_cloudx_config) | **PUT** /template/device/config/attachcloudx | 
[**get_attached_config_to_device**](ConfigurationDeviceTemplateApi.md#get_attached_config_to_device) | **GET** /template/device/config/attachedconfig | 
[**get_attached_device_list**](ConfigurationDeviceTemplateApi.md#get_attached_device_list) | **GET** /template/device/config/attached/{masterTemplateId} | 
[**get_device_configuration_preview**](ConfigurationDeviceTemplateApi.md#get_device_configuration_preview) | **POST** /template/device/config/config | 
[**get_device_list_by_master_template_id**](ConfigurationDeviceTemplateApi.md#get_device_list_by_master_template_id) | **GET** /template/device/config/available/{masterTemplateId} | 
[**get_devices_with_duplicate_ip**](ConfigurationDeviceTemplateApi.md#get_devices_with_duplicate_ip) | **POST** /template/device/config/duplicateip | 
[**get_quick_connect_variables**](ConfigurationDeviceTemplateApi.md#get_quick_connect_variables) | **POST** /template/device/config/quickconnectvariable | 
[**process_input_comma_sep_file**](ConfigurationDeviceTemplateApi.md#process_input_comma_sep_file) | **POST** /template/device/config/process/input/file | 
[**push_cli_template**](ConfigurationDeviceTemplateApi.md#push_cli_template) | **POST** /template/device/config/attachcli | 
[**push_cloudx_config**](ConfigurationDeviceTemplateApi.md#push_cloudx_config) | **POST** /template/device/config/attachcloudx | 
[**push_master_template**](ConfigurationDeviceTemplateApi.md#push_master_template) | **POST** /template/device/config/attachfeature | 
[**push_master_template1**](ConfigurationDeviceTemplateApi.md#push_master_template1) | **POST** /template/device/config/attachBootStrap | 
[**validate_template**](ConfigurationDeviceTemplateApi.md#validate_template) | **POST** /template/device/config/verify | 


# **attach_device_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} attach_device_template()



Attach device template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attach_device_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->attach_device_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device template | [optional]

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

# **check_vbond**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} check_vbond()



Check if vBond is configured<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.check_vbond()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->check_vbond: %s\n" % e)
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

# **create_device_input**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_device_input()



Create device input<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Template device input (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_device_input(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->create_device_input: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Template device input | [optional]

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

# **create_input_without_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_input_without_device()



Export the device template to CSV format for given template id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_input_without_device(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->create_input_without_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device template | [optional]

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

# **detach_device_template**
> detach_device_template()



Detach device template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.detach_device_template(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->detach_device_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device template | [optional]

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

# **detach_sites**
> str detach_sites()



Disable enabled gateways, clients, dias<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CloudX config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.detach_sites(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->detach_sites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CloudX config | [optional]

### Return type

**str**

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

# **edit_cloudx_config**
> str edit_cloudx_config()



Edit already enabled gateways, clients, dias<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CloudX config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_cloudx_config(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->edit_cloudx_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CloudX config | [optional]

### Return type

**str**

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

# **get_attached_config_to_device**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_attached_config_to_device(device_id)



Get attached config to device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    device_id = "deviceId_example" # str | Device Model ID
    policy_id = "policyId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_attached_config_to_device(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->get_attached_config_to_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_attached_config_to_device(device_id, policy_id=policy_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->get_attached_config_to_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Model ID |
 **policy_id** | **str**|  | [optional]

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

# **get_attached_device_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_attached_device_list(master_template_id)



Get attached device list by master template Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    master_template_id = "masterTemplateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_attached_device_list(master_template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->get_attached_device_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_template_id** | **str**| Template Id |

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

# **get_device_configuration_preview**
> str get_device_configuration_preview()



Get device configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_configuration_preview(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->get_device_configuration_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device template | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_list_by_master_template_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_device_list_by_master_template_id(master_template_id)



Get possible device list by master template Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    master_template_id = "masterTemplateId_example" # str | Template Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_list_by_master_template_id(master_template_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->get_device_list_by_master_template_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_template_id** | **str**| Template Id |

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

# **get_devices_with_duplicate_ip**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_devices_with_duplicate_ip()



Detects duplicate system IP from a list of devices<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_devices_with_duplicate_ip(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->get_devices_with_duplicate_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device list | [optional]

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

# **get_quick_connect_variables**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_quick_connect_variables()



Get connection variables to be configured

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device List (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_quick_connect_variables(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->get_quick_connect_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device List | [optional]

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

# **process_input_comma_sep_file**
> str process_input_comma_sep_file()



Process input comma separated file<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.process_input_comma_sep_file()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->process_input_comma_sep_file: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_cli_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} push_cli_template()



Attach CLI device template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.push_cli_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->push_cli_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device template | [optional]

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

# **push_cloudx_config**
> str push_cloudx_config()



Enable gateways, clients, dias

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CloudX config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.push_cloudx_config(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->push_cloudx_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CloudX config | [optional]

### Return type

**str**

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

# **push_master_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} push_master_template()



Attach feature device template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.push_master_template(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->push_master_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device template | [optional]

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

# **push_master_template1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} push_master_template1()



Attach feature device template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.push_master_template1(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->push_master_template1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Device template | [optional]

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

# **validate_template**
> validate_template()



Validate full template\" <br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_template_api
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request import GetO365PreferredPathFromVAnalyticsRequest
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_template_api.ConfigurationDeviceTemplateApi(api_client)
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.validate_template(get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceTemplateApi->validate_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

