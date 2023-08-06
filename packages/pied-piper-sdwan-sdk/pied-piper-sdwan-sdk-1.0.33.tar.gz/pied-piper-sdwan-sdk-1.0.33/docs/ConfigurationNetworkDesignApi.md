# openapi_client.ConfigurationNetworkDesignApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquire_attach_lock**](ConfigurationNetworkDesignApi.md#acquire_attach_lock) | **POST** /networkdesign/profile/lock/{profileId} | 
[**acquire_edit_lock**](ConfigurationNetworkDesignApi.md#acquire_edit_lock) | **POST** /networkdesign/lock/edit | 
[**create_network_design**](ConfigurationNetworkDesignApi.md#create_network_design) | **POST** /networkdesign | 
[**edit_network_design**](ConfigurationNetworkDesignApi.md#edit_network_design) | **PUT** /networkdesign | 
[**get_device_profile_config_status**](ConfigurationNetworkDesignApi.md#get_device_profile_config_status) | **GET** /networkdesign/profile/status | 
[**get_device_profile_config_status_by_profile_id**](ConfigurationNetworkDesignApi.md#get_device_profile_config_status_by_profile_id) | **GET** /networkdesign/profile/status/{profileId} | 
[**get_device_profile_task_count**](ConfigurationNetworkDesignApi.md#get_device_profile_task_count) | **GET** /networkdesign/profile/task/count | 
[**get_device_profile_task_status**](ConfigurationNetworkDesignApi.md#get_device_profile_task_status) | **GET** /networkdesign/profile/task/status | 
[**get_device_profile_task_status_by_profile_id**](ConfigurationNetworkDesignApi.md#get_device_profile_task_status_by_profile_id) | **GET** /networkdesign/profile/task/status/{profileId} | 
[**get_global_parameters**](ConfigurationNetworkDesignApi.md#get_global_parameters) | **GET** /networkdesign/global/parameters | 
[**get_network_design**](ConfigurationNetworkDesignApi.md#get_network_design) | **GET** /networkdesign | 
[**get_service_profile_config**](ConfigurationNetworkDesignApi.md#get_service_profile_config) | **GET** /networkdesign/serviceProfileConfig/{profileId} | 
[**push_device_profile_template**](ConfigurationNetworkDesignApi.md#push_device_profile_template) | **POST** /networkdesign/profile/attachment/{profileId} | 
[**push_network_design**](ConfigurationNetworkDesignApi.md#push_network_design) | **POST** /networkdesign/attachment | 
[**run_my_test**](ConfigurationNetworkDesignApi.md#run_my_test) | **GET** /networkdesign/mytest/{name} | 


# **acquire_attach_lock**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} acquire_attach_lock(profile_id)



Get the service profile config for a given device profile id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)
    profile_id = "profileId_example" # str | Device profile Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.acquire_attach_lock(profile_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->acquire_attach_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Device profile Id |

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

# **acquire_edit_lock**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} acquire_edit_lock()



Acquire edit lock

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.acquire_edit_lock()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->acquire_edit_lock: %s\n" % e)
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

# **create_network_design**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_network_design()



Create network design

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Network design payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_network_design(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->create_network_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Network design payload | [optional]

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

# **edit_network_design**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_network_design(id)



Edit network segment

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)
    id = "id_example" # str | Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Network design payload (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_network_design(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->edit_network_design: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_network_design(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->edit_network_design: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Network design payload | [optional]

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

# **get_device_profile_config_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_profile_config_status()



Get device profile configuration status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_profile_config_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->get_device_profile_config_status: %s\n" % e)
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

# **get_device_profile_config_status_by_profile_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_profile_config_status_by_profile_id(profile_id)



Get device profile configuration status by profile Id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)
    profile_id = "profileId_example" # str | Device profile Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_profile_config_status_by_profile_id(profile_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->get_device_profile_config_status_by_profile_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Device profile Id |

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

# **get_device_profile_task_count**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_profile_task_count()



Get device profile configuration task count

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_profile_task_count()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->get_device_profile_task_count: %s\n" % e)
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

# **get_device_profile_task_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_profile_task_status()



Get device profile configuration task status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_profile_task_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->get_device_profile_task_status: %s\n" % e)
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

# **get_device_profile_task_status_by_profile_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_profile_task_status_by_profile_id(profile_id)



Get device profile configuration status by profile Id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)
    profile_id = "profileId_example" # str | Device profile Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_device_profile_task_status_by_profile_id(profile_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->get_device_profile_task_status_by_profile_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Device profile Id |

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

# **get_global_parameters**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_global_parameters()



Get global parameter templates

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_global_parameters()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->get_global_parameters: %s\n" % e)
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

# **get_network_design**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_network_design()



Get existing network design

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_network_design()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->get_network_design: %s\n" % e)
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

# **get_service_profile_config**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_service_profile_config(profile_id, device_model)



Get the service profile config for a given device profile id

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)
    profile_id = "profileId_example" # str | Device profile Id
    device_model = "deviceModel_example" # str | Device model

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_service_profile_config(profile_id, device_model)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->get_service_profile_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Device profile Id |
 **device_model** | **str**| Device model |

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

# **push_device_profile_template**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} push_device_profile_template(profile_id)



Attach to device profile

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)
    profile_id = "profileId_example" # str | Device profile Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device template (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.push_device_profile_template(profile_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->push_device_profile_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.push_device_profile_template(profile_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->push_device_profile_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Device profile Id |
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

# **push_network_design**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} push_network_design()



Attach network design

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Device template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.push_network_design(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->push_network_design: %s\n" % e)
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

# **run_my_test**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} run_my_test(name)



Get all device templates for this feature template

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_network_design_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_network_design_api.ConfigurationNetworkDesignApi(api_client)
    name = "name_example" # str | Test bane

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.run_my_test(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationNetworkDesignApi->run_my_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Test bane |

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

