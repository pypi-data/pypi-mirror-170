# openapi_client.SystemCloudServiceApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cloud_credentials**](SystemCloudServiceApi.md#add_cloud_credentials) | **POST** /cloudservices/credentials | 
[**connect**](SystemCloudServiceApi.md#connect) | **GET** /cloudservices/connect | 
[**entity_ownership_info**](SystemCloudServiceApi.md#entity_ownership_info) | **GET** /entityownership/tree | 
[**get_access_tokenfor_device**](SystemCloudServiceApi.md#get_access_tokenfor_device) | **GET** /cloudservices/accesstoken | 
[**get_azure_token**](SystemCloudServiceApi.md#get_azure_token) | **POST** /cloudservices/authtoken | 
[**get_cloud_credentials**](SystemCloudServiceApi.md#get_cloud_credentials) | **GET** /cloudservices/credentials | 
[**get_cloud_settings**](SystemCloudServiceApi.md#get_cloud_settings) | **GET** /dca/cloudservices | 
[**get_device_code**](SystemCloudServiceApi.md#get_device_code) | **POST** /cloudservices/devicecode | 
[**get_otp**](SystemCloudServiceApi.md#get_otp) | **GET** /dca/cloudservices/otp | 
[**get_telemetry_state**](SystemCloudServiceApi.md#get_telemetry_state) | **GET** /cloudservices/telemetry | 
[**is_staging**](SystemCloudServiceApi.md#is_staging) | **GET** /cloudservices/staging | 
[**list_entity_ownership_info**](SystemCloudServiceApi.md#list_entity_ownership_info) | **GET** /entityownership/list | 
[**opt_in**](SystemCloudServiceApi.md#opt_in) | **PUT** /cloudservices/telemetry/optin | 
[**opt_out**](SystemCloudServiceApi.md#opt_out) | **DELETE** /cloudservices/telemetry/optout | 
[**updatet_otp**](SystemCloudServiceApi.md#updatet_otp) | **PUT** /dca/cloudservices/otp | 


# **add_cloud_credentials**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} add_cloud_credentials()



Get cloud service settings

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_cloud_credentials(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->add_cloud_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **connect**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} connect()



Telemetry Opt In

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.connect()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->connect: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **entity_ownership_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} entity_ownership_info()



Entity ownership info grouped by buckets

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.entity_ownership_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->entity_ownership_info: %s\n" % e)
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

# **get_access_tokenfor_device**
> get_access_tokenfor_device()



### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_access_tokenfor_device()
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->get_access_tokenfor_device: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_token**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_azure_token()



Get Azure token

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_azure_token(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->get_azure_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **get_cloud_credentials**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_credentials()



Get cloud service credentials

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_credentials()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->get_cloud_credentials: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_cloud_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_settings()



Get cloud service settings

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_settings()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->get_cloud_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_device_code**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_code()



Get Azure device code

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_code()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->get_device_code: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_otp**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_otp()



Get cloud service OTP value

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_otp()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->get_otp: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_telemetry_state**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_telemetry_state()



Get Telemetry state

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_telemetry_state()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->get_telemetry_state: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **is_staging**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} is_staging()



Check if testbed or production

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.is_staging()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->is_staging: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **list_entity_ownership_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_entity_ownership_info()



List all entity ownership info

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_entity_ownership_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->list_entity_ownership_info: %s\n" % e)
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

# **opt_in**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} opt_in()



Telemetry Opt In

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.opt_in(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->opt_in: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **opt_out**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} opt_out()



Telemetry Opt Out

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.opt_out(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->opt_out: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

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

# **updatet_otp**
> updatet_otp()



Update cloud service OTP value

### Example


```python
import time
import openapi_client
from openapi_client.api import system_cloud_service_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_cloud_service_api.SystemCloudServiceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloud service OTP value (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.updatet_otp(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling SystemCloudServiceApi->updatet_otp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloud service OTP value | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

