# openapi_client.ConfigurationDeviceSoftwareUpdateApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_package_file**](ConfigurationDeviceSoftwareUpdateApi.md#download_package_file) | **GET** /device/action/software/package/{fileName} | 
[**edit_image_metadata**](ConfigurationDeviceSoftwareUpdateApi.md#edit_image_metadata) | **PUT** /device/action/software/package/{versionId}/metadata | 
[**get_image_metadata**](ConfigurationDeviceSoftwareUpdateApi.md#get_image_metadata) | **GET** /device/action/software/package/{versionId}/metadata | 
[**get_upload_images_count**](ConfigurationDeviceSoftwareUpdateApi.md#get_upload_images_count) | **GET** /device/action/software/package/imageCount | 
[**install_pkg**](ConfigurationDeviceSoftwareUpdateApi.md#install_pkg) | **POST** /device/action/software/package | 
[**process_software_image**](ConfigurationDeviceSoftwareUpdateApi.md#process_software_image) | **POST** /device/action/software/package/{imageType} | 


# **download_package_file**
> download_package_file(file_name, )



Download software package file

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_update_api.ConfigurationDeviceSoftwareUpdateApi(api_client)
    file_name = "fileName_example" # str | Pakcage file name

    # example passing only required values which don't have defaults set
    try:
        api_instance.download_package_file(file_name, )
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwareUpdateApi->download_package_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Pakcage file name |
 **image_type** | **str**| Image type | defaults to "software"

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

# **edit_image_metadata**
> edit_image_metadata(version_id)



Update Package Metadata

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_update_api.ConfigurationDeviceSoftwareUpdateApi(api_client)
    version_id = "versionId_example" # str | Image ID
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.edit_image_metadata(version_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwareUpdateApi->edit_image_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_image_metadata(version_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwareUpdateApi->edit_image_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| Image ID |
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

# **get_image_metadata**
> get_image_metadata(version_id)



Update Package Metadata

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_update_api.ConfigurationDeviceSoftwareUpdateApi(api_client)
    version_id = "versionId_example" # str | Image ID

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_image_metadata(version_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwareUpdateApi->get_image_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| Image ID |

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

# **get_upload_images_count**
> get_upload_images_count(image_type)



Number of software image presented in vManage repository

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_update_api.ConfigurationDeviceSoftwareUpdateApi(api_client)
    image_type = [
        "software",
    ] # [str] | Image type

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_upload_images_count(image_type)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwareUpdateApi->get_upload_images_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_type** | **[str]**| Image type |

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

# **install_pkg**
> install_pkg()



Install software package

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_update_api.ConfigurationDeviceSoftwareUpdateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.install_pkg()
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwareUpdateApi->install_pkg: %s\n" % e)
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

# **process_software_image**
> process_software_image(image_type)



Install software image package

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_update_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_update_api.ConfigurationDeviceSoftwareUpdateApi(api_client)
    image_type = "imageType_example" # str | Image type

    # example passing only required values which don't have defaults set
    try:
        api_instance.process_software_image(image_type)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwareUpdateApi->process_software_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_type** | **str**| Image type |

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

