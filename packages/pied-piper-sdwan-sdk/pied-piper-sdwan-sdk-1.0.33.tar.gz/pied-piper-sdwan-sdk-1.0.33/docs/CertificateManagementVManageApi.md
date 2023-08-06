# openapi_client.CertificateManagementVManageApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dump_certificate**](CertificateManagementVManageApi.md#dump_certificate) | **GET** /setting/configuration/webserver/certificate/certificate | 
[**get_certificate**](CertificateManagementVManageApi.md#get_certificate) | **GET** /setting/configuration/webserver/certificate/getcertificate | 
[**get_csr**](CertificateManagementVManageApi.md#get_csr) | **POST** /setting/configuration/webserver/certificate | 
[**import_certificate**](CertificateManagementVManageApi.md#import_certificate) | **PUT** /setting/configuration/webserver/certificate | 
[**rollback**](CertificateManagementVManageApi.md#rollback) | **GET** /setting/configuration/webserver/certificate/rollback | 
[**show_info**](CertificateManagementVManageApi.md#show_info) | **GET** /setting/configuration/webserver/certificate | 


# **dump_certificate**
> str dump_certificate(type)



Get certificate with alias name

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_v_manage_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_v_manage_api.CertificateManagementVManageApi(api_client)
    type = "type_example" # str | Key alias

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dump_certificate(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementVManageApi->dump_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Key alias |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate**
> str get_certificate()



Get certificate for alias server

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_v_manage_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_v_manage_api.CertificateManagementVManageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_certificate()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementVManageApi->get_certificate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_csr()



Generate Certificate Signing Request

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_v_manage_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_v_manage_api.CertificateManagementVManageApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSR signing request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_csr(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementVManageApi->get_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSR signing request | [optional]

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

# **import_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} import_certificate()



Import a signed web server certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_v_manage_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_v_manage_api.CertificateManagementVManageApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Singed certificate (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.import_certificate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementVManageApi->import_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Singed certificate | [optional]

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

# **rollback**
> str rollback(type)



Rollback certificate with alias name

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_v_manage_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_v_manage_api.CertificateManagementVManageApi(api_client)
    type = "type_example" # str | Key alias

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rollback(type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementVManageApi->rollback: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Key alias |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} show_info()



Retrieves Certificate Signing Request information

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_v_manage_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_v_manage_api.CertificateManagementVManageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.show_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementVManageApi->show_info: %s\n" % e)
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

