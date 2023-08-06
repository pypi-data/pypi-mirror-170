# openapi_client.ConfigurationDeviceSoftwarePackageApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vnf_package**](ConfigurationDeviceSoftwarePackageApi.md#create_vnf_package) | **POST** /device/action/software/package/custom/vnfPackage | 
[**edit_config_file**](ConfigurationDeviceSoftwarePackageApi.md#edit_config_file) | **PUT** /device/action/software/package/custom/file/{uuid} | 
[**get_file_contents**](ConfigurationDeviceSoftwarePackageApi.md#get_file_contents) | **GET** /device/action/software/package/custom/file/{uuid} | 
[**upload_image_file**](ConfigurationDeviceSoftwarePackageApi.md#upload_image_file) | **POST** /device/action/software/package/custom/uploads/{type} | 


# **create_vnf_package**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_vnf_package()



Create VNF custom package

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_package_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_package_api.ConfigurationDeviceSoftwarePackageApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Custom package (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_vnf_package(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwarePackageApi->create_vnf_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Custom package | [optional]

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

# **edit_config_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_config_file(uuid)



Edit bootstrap file

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_package_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_package_api.ConfigurationDeviceSoftwarePackageApi(api_client)
    uuid = "uuid_example" # str | File uuid
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Bootstrap file (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_config_file(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwarePackageApi->edit_config_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_config_file(uuid, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwarePackageApi->edit_config_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| File uuid |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Bootstrap file | [optional]

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

# **get_file_contents**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_file_contents(uuid)



Get bootstrap file contents

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_package_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_package_api.ConfigurationDeviceSoftwarePackageApi(api_client)
    uuid = "uuid_example" # str | File uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_file_contents(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwarePackageApi->get_file_contents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| File uuid |

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

# **upload_image_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} upload_image_file(type)



Upload virtual image/bootstrap file

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_device_software_package_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_device_software_package_api.ConfigurationDeviceSoftwarePackageApi(api_client)
    type = "image" # str | Upload file type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.upload_image_file(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDeviceSoftwarePackageApi->upload_image_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Upload file type |

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

