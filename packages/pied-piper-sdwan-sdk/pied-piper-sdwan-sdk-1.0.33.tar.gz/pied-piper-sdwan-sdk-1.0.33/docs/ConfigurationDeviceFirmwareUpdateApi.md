# openapi_client.ConfigurationDeviceFirmwareUpdateApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_firmware_image**](ConfigurationDeviceFirmwareUpdateApi.md#activate_firmware_image) | **POST** /device/action/firmware/activate | 
[**delete_firmware_image**](ConfigurationDeviceFirmwareUpdateApi.md#delete_firmware_image) | **DELETE** /device/action/firmware/{versionId} | 
[**get_devices_fw_upgrade**](ConfigurationDeviceFirmwareUpdateApi.md#get_devices_fw_upgrade) | **GET** /device/action/firmware/devices | 
[**get_firmware_image_details**](ConfigurationDeviceFirmwareUpdateApi.md#get_firmware_image_details) | **GET** /device/action/firmware/{versionId} | 
[**get_firmware_images**](ConfigurationDeviceFirmwareUpdateApi.md#get_firmware_images) | **GET** /device/action/firmware | 
[**install_firmware_image**](ConfigurationDeviceFirmwareUpdateApi.md#install_firmware_image) | **POST** /device/action/firmware/install | 
[**process_firmware_image**](ConfigurationDeviceFirmwareUpdateApi.md#process_firmware_image) | **POST** /device/action/firmware | 
[**remove_firmware_image**](ConfigurationDeviceFirmwareUpdateApi.md#remove_firmware_image) | **POST** /device/action/firmware/remove | 


# **activate_firmware_image**
> activate_firmware_image()



Activate firmware on device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_firmware_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_firmware_update_api.ConfigurationDeviceFirmwareUpdateApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.activate_firmware_image(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceFirmwareUpdateApi->activate_firmware_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **delete_firmware_image**
> delete_firmware_image(version_id)



Delete firmware image package

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_firmware_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_firmware_update_api.ConfigurationDeviceFirmwareUpdateApi(api_client)
    version_id = "versionId_example" # str | Firmware image version

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_firmware_image(version_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceFirmwareUpdateApi->delete_firmware_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| Firmware image version |

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

# **get_devices_fw_upgrade**
> get_devices_fw_upgrade()



Get list of devices that support firmware upgrade

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_firmware_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_firmware_update_api.ConfigurationDeviceFirmwareUpdateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_devices_fw_upgrade()
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceFirmwareUpdateApi->get_devices_fw_upgrade: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_firmware_image_details**
> get_firmware_image_details(version_id)



Get firmware image details for a given version

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_firmware_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_firmware_update_api.ConfigurationDeviceFirmwareUpdateApi(api_client)
    version_id = "versionId_example" # str | Firmware image version

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_firmware_image_details(version_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceFirmwareUpdateApi->get_firmware_image_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| Firmware image version |

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

# **get_firmware_images**
> get_firmware_images()



Get list of firmware images in the repository

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_firmware_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_firmware_update_api.ConfigurationDeviceFirmwareUpdateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_firmware_images()
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceFirmwareUpdateApi->get_firmware_images: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **install_firmware_image**
> install_firmware_image()



Install firmware on device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_firmware_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_firmware_update_api.ConfigurationDeviceFirmwareUpdateApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.install_firmware_image(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceFirmwareUpdateApi->install_firmware_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **process_firmware_image**
> process_firmware_image()



Upload firmware image package

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_firmware_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_firmware_update_api.ConfigurationDeviceFirmwareUpdateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.process_firmware_image()
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceFirmwareUpdateApi->process_firmware_image: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **remove_firmware_image**
> remove_firmware_image()



Remove firmware on device

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_firmware_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_firmware_update_api.ConfigurationDeviceFirmwareUpdateApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.remove_firmware_image(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceFirmwareUpdateApi->remove_firmware_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

