# openapi_client.ConfigurationMultidomainPolicyApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_internal_policy**](ConfigurationMultidomainPolicyApi.md#add_internal_policy) | **PUT** /mdp/policies/mdpconfig | 
[**attach_devices**](ConfigurationMultidomainPolicyApi.md#attach_devices) | **POST** /mdp/attachDevices/{nmsId} | 
[**detach_devices**](ConfigurationMultidomainPolicyApi.md#detach_devices) | **POST** /mdp/detachDevices/{nmsId} | 
[**disconnect_from_mdp**](ConfigurationMultidomainPolicyApi.md#disconnect_from_mdp) | **GET** /mdp/disconnect/{nmsId} | 
[**edit_attached_devices**](ConfigurationMultidomainPolicyApi.md#edit_attached_devices) | **PUT** /mdp/attachDevices/{nmsId} | 
[**get_mdp_onboarding_status**](ConfigurationMultidomainPolicyApi.md#get_mdp_onboarding_status) | **GET** /mdp/onboard/status | 
[**offboard**](ConfigurationMultidomainPolicyApi.md#offboard) | **DELETE** /mdp/onboard/{nmsId} | 
[**onboard_mdp**](ConfigurationMultidomainPolicyApi.md#onboard_mdp) | **POST** /mdp/onboard | 
[**retrieve_mdp_attached_devices**](ConfigurationMultidomainPolicyApi.md#retrieve_mdp_attached_devices) | **GET** /mdp/attachDevices/{nmsId} | 
[**retrieve_mdp_config_object**](ConfigurationMultidomainPolicyApi.md#retrieve_mdp_config_object) | **GET** /mdp/policies/mdpconfig/{deviceId} | 
[**retrieve_mdp_policies**](ConfigurationMultidomainPolicyApi.md#retrieve_mdp_policies) | **GET** /mdp/policies/{nmsId} | 
[**retrieve_mdp_supported_devices_**](ConfigurationMultidomainPolicyApi.md#retrieve_mdp_supported_devices_) | **GET** /mdp/devices/{nmsId} | 
[**update_onboarding_payload**](ConfigurationMultidomainPolicyApi.md#update_onboarding_payload) | **PUT** /mdp/onboard/{nmsId} | 
[**update_policy_status**](ConfigurationMultidomainPolicyApi.md#update_policy_status) | **PUT** /mdp/policies/{nmsId} | 


# **add_internal_policy**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} add_internal_policy()



Add internal policy from vmanage

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | addInternalPolicy (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_internal_policy(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->add_internal_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| addInternalPolicy | [optional]

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

# **attach_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} attach_devices(nms_id)



Share devices with MDP

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | deviceList (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.attach_devices(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->attach_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attach_devices(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->attach_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| deviceList | [optional]

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

# **detach_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} detach_devices(nms_id)



Disconnect devices from mpd controller

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | deviceList (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.detach_devices(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->detach_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.detach_devices(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->detach_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| deviceList | [optional]

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

# **disconnect_from_mdp**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] disconnect_from_mdp(nms_id)



disconnect from mpd controller

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.disconnect_from_mdp(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->disconnect_from_mdp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |

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

# **edit_attached_devices**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_attached_devices(nms_id)



Edit attached devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | deviceList (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_attached_devices(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->edit_attached_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_attached_devices(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->edit_attached_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| deviceList | [optional]

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

# **get_mdp_onboarding_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_mdp_onboarding_status()



Get MDP onboarding status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_mdp_onboarding_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->get_mdp_onboarding_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **offboard**
> offboard(nms_id)



offboard the mdp application

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.offboard(nms_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->offboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |

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

# **onboard_mdp**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} onboard_mdp()



Start MDP onboarding operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Onboard (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.onboard_mdp(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->onboard_mdp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Onboard | [optional]

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

# **retrieve_mdp_attached_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] retrieve_mdp_attached_devices(nms_id)



Retrieve MDP attached devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_mdp_attached_devices(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->retrieve_mdp_attached_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |

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

# **retrieve_mdp_config_object**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] retrieve_mdp_config_object(device_id)



Retrieve MDP ConfigObject

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    device_id = "deviceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_mdp_config_object(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->retrieve_mdp_config_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  |

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

# **retrieve_mdp_policies**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] retrieve_mdp_policies(nms_id)



Retrieve MDP policies

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_mdp_policies(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->retrieve_mdp_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |

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

# **retrieve_mdp_supported_devices_**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] retrieve_mdp_supported_devices_(nms_id)



Retrieve MDP supported devices

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_mdp_supported_devices_(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->retrieve_mdp_supported_devices_: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |

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

# **update_onboarding_payload**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_onboarding_payload(nms_id)



update MDP onboarding document

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Onboard (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_onboarding_payload(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->update_onboarding_payload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_onboarding_payload(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->update_onboarding_payload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Onboard | [optional]

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

# **update_policy_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_policy_status(nms_id)



update policy status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_multidomain_policy_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_multidomain_policy_api.ConfigurationMultidomainPolicyApi(api_client)
    nms_id = "nmsId_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | policyList (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_policy_status(nms_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->update_policy_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_policy_status(nms_id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationMultidomainPolicyApi->update_policy_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nms_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| policyList | [optional]

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

