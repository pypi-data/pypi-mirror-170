# openapi_client.SmartLicenseApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_accounts**](SmartLicenseApi.md#fetch_accounts) | **GET** /smartLicensing/fetchAccounts | 
[**fetch_reports**](SmartLicenseApi.md#fetch_reports) | **GET** /smartLicensing/fetchReportsForSa | 
[**fetch_reports1**](SmartLicenseApi.md#fetch_reports1) | **GET** /smartLicensing/fetchAllSa | 
[**get_settings**](SmartLicenseApi.md#get_settings) | **GET** /smartLicensing/getUserSettings | 
[**sleauthenticate**](SmartLicenseApi.md#sleauthenticate) | **POST** /smartLicensing/authenticate | 
[**sync_licenses**](SmartLicenseApi.md#sync_licenses) | **POST** /smartLicensing/syncLicenses | 
[**sync_licenses1**](SmartLicenseApi.md#sync_licenses1) | **POST** /smartLicensing/removeSaVaSelection | 
[**upload_ack**](SmartLicenseApi.md#upload_ack) | **POST** /smartLicensing/uploadAck | 


# **fetch_accounts**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} fetch_accounts(mode)



fetch sava for sle

### Example


```python
import time
import openapi_client
from openapi_client.api import smart_license_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = smart_license_api.SmartLicenseApi(api_client)
    mode = "mode_example" # str | mode
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Partner (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_accounts(mode)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->fetch_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetch_accounts(mode, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->fetch_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **str**| mode |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Partner | [optional]

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_reports**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} fetch_reports(sa_domain, sa_id)



fetch reports offline for sle

### Example


```python
import time
import openapi_client
from openapi_client.api import smart_license_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = smart_license_api.SmartLicenseApi(api_client)
    sa_domain = "saDomain_example" # str | saDomain
    sa_id = "saId_example" # str | saId
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Partner (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_reports(sa_domain, sa_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->fetch_reports: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetch_reports(sa_domain, sa_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->fetch_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sa_domain** | **str**| saDomain |
 **sa_id** | **str**| saId |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Partner | [optional]

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

# **fetch_reports1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} fetch_reports1()



fetch reports offline for sle

### Example


```python
import time
import openapi_client
from openapi_client.api import smart_license_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = smart_license_api.SmartLicenseApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Partner (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.fetch_reports1(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->fetch_reports1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Partner | [optional]

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

# **get_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_settings()



get settings

### Example


```python
import time
import openapi_client
from openapi_client.api import smart_license_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = smart_license_api.SmartLicenseApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_settings()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->get_settings: %s\n" % e)
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

# **sleauthenticate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sleauthenticate()



authenticate user for sle

### Example


```python
import time
import openapi_client
from openapi_client.api import smart_license_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = smart_license_api.SmartLicenseApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Partner (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sleauthenticate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->sleauthenticate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Partner | [optional]

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

# **sync_licenses**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sync_licenses()



get all licenses for sa/va

### Example


```python
import time
import openapi_client
from openapi_client.api import smart_license_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = smart_license_api.SmartLicenseApi(api_client)
    data = "data_example" # str |  (optional)
    name = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sync_licenses(data=data, name=name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->sync_licenses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**|  | [optional]
 **name** | **file_type**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_licenses1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sync_licenses1()



get all licenses for sa/va

### Example


```python
import time
import openapi_client
from openapi_client.api import smart_license_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = smart_license_api.SmartLicenseApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Partner (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sync_licenses1(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->sync_licenses1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Partner | [optional]

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

# **upload_ack**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} upload_ack()



upload ack file  for sa/va

### Example


```python
import time
import openapi_client
from openapi_client.api import smart_license_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = smart_license_api.SmartLicenseApi(api_client)
    data = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.upload_ack(data=data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SmartLicenseApi->upload_ack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **file_type**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

