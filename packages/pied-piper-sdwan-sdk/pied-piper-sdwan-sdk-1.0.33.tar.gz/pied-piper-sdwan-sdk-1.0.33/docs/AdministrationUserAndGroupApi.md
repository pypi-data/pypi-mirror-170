# openapi_client.AdministrationUserAndGroupApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_colo_group**](AdministrationUserAndGroupApi.md#create_colo_group) | **POST** /admin/cologroup | 
[**create_group_grid_columns**](AdministrationUserAndGroupApi.md#create_group_grid_columns) | **GET** /admin/usergroup/definition | 
[**create_user**](AdministrationUserAndGroupApi.md#create_user) | **POST** /admin/user | 
[**create_user_group**](AdministrationUserAndGroupApi.md#create_user_group) | **POST** /admin/usergroup | 
[**create_vpn_group**](AdministrationUserAndGroupApi.md#create_vpn_group) | **POST** /admin/vpngroup | 
[**delete_colo_group**](AdministrationUserAndGroupApi.md#delete_colo_group) | **DELETE** /admin/cologroup/{id} | 
[**delete_user**](AdministrationUserAndGroupApi.md#delete_user) | **DELETE** /admin/user/{userName} | 
[**delete_user_group**](AdministrationUserAndGroupApi.md#delete_user_group) | **DELETE** /admin/usergroup/{userGroupId} | 
[**delete_vpn_group**](AdministrationUserAndGroupApi.md#delete_vpn_group) | **DELETE** /admin/vpngroup/{id} | 
[**edit_colo_group**](AdministrationUserAndGroupApi.md#edit_colo_group) | **PUT** /admin/cologroup/{id} | 
[**edit_vpn_group**](AdministrationUserAndGroupApi.md#edit_vpn_group) | **PUT** /admin/vpngroup/{id} | 
[**find_user_auth_type**](AdministrationUserAndGroupApi.md#find_user_auth_type) | **GET** /admin/user/userAuthType | 
[**find_user_groups**](AdministrationUserAndGroupApi.md#find_user_groups) | **GET** /admin/usergroup | 
[**find_user_groups_as_key_value**](AdministrationUserAndGroupApi.md#find_user_groups_as_key_value) | **GET** /admin/usergroup/keyvalue | 
[**find_user_role**](AdministrationUserAndGroupApi.md#find_user_role) | **GET** /admin/user/role | 
[**find_users**](AdministrationUserAndGroupApi.md#find_users) | **GET** /admin/user | 
[**get_active_sessions**](AdministrationUserAndGroupApi.md#get_active_sessions) | **GET** /admin/user/activeSessions | 
[**get_colo_groups**](AdministrationUserAndGroupApi.md#get_colo_groups) | **GET** /admin/cologroup | 
[**get_vpn_groups**](AdministrationUserAndGroupApi.md#get_vpn_groups) | **GET** /admin/vpngroup | 
[**remove_sessions**](AdministrationUserAndGroupApi.md#remove_sessions) | **DELETE** /admin/user/removeSessions | 
[**reset_user**](AdministrationUserAndGroupApi.md#reset_user) | **POST** /admin/user/reset | 
[**resource_group**](AdministrationUserAndGroupApi.md#resource_group) | **GET** /admin/resourcegroup | 
[**resource_group1**](AdministrationUserAndGroupApi.md#resource_group1) | **POST** /admin/resourcegroup/switch | 
[**resource_group2**](AdministrationUserAndGroupApi.md#resource_group2) | **PUT** /admin/resourcegroup/{groupId} | 
[**resource_group3**](AdministrationUserAndGroupApi.md#resource_group3) | **DELETE** /admin/resourcegroup/{groupId} | 
[**resource_group4**](AdministrationUserAndGroupApi.md#resource_group4) | **POST** /admin/resourcegroup | 
[**resource_group_name**](AdministrationUserAndGroupApi.md#resource_group_name) | **GET** /admin/user/resourceGroupName | 
[**update_admin_password**](AdministrationUserAndGroupApi.md#update_admin_password) | **POST** /admin/user/admin/password | 
[**update_password**](AdministrationUserAndGroupApi.md#update_password) | **PUT** /admin/user/password/{userName} | 
[**update_profile_locale**](AdministrationUserAndGroupApi.md#update_profile_locale) | **PUT** /admin/user/profile/locale | 
[**update_profile_password**](AdministrationUserAndGroupApi.md#update_profile_password) | **PUT** /admin/user/profile/password | 
[**update_user**](AdministrationUserAndGroupApi.md#update_user) | **PUT** /admin/user/{userName} | 
[**update_user_group**](AdministrationUserAndGroupApi.md#update_user_group) | **PUT** /admin/usergroup/{userGroupId} | 
[**validate_password**](AdministrationUserAndGroupApi.md#validate_password) | **POST** /admin/user/password/validate | 


# **create_colo_group**
> create_colo_group()



Add COLO group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Colocation group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_colo_group(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->create_colo_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Colocation group | [optional]

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

# **create_group_grid_columns**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_group_grid_columns()



Get user groups in a grid table

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create_group_grid_columns()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->create_group_grid_columns: %s\n" % e)
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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> create_user()



Create a user

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_user(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User | [optional]

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

# **create_user_group**
> create_user_group()



Create user group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_user_group(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->create_user_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User group | [optional]

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

# **create_vpn_group**
> create_vpn_group()



Add VPN group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | VPN group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_vpn_group(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->create_vpn_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| VPN group | [optional]

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

# **delete_colo_group**
> delete_colo_group(id)



Delete COLO group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    id = "id_example" # str | Colocation group Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_colo_group(id)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->delete_colo_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Colocation group Id |

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

# **delete_user**
> delete_user(user_name)



Delete user

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    user_name = "userName_example" # str | User name

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_user(user_name)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| User name |

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

# **delete_user_group**
> delete_user_group(user_group_id)



Delete user group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    user_group_id = "userGroupId_example" # str | User group Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_user_group(user_group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->delete_user_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| User group Id |

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

# **delete_vpn_group**
> delete_vpn_group(id)



Delete VPN group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    id = "id_example" # str | VPN group Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_vpn_group(id)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->delete_vpn_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VPN group Id |

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

# **edit_colo_group**
> edit_colo_group(id)



Update COLO group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    id = "id_example" # str | Colocation group Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Colocation group (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.edit_colo_group(id)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->edit_colo_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_colo_group(id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->edit_colo_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Colocation group Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Colocation group | [optional]

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

# **edit_vpn_group**
> edit_vpn_group(id)



Update VPN group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    id = "id_example" # str | VPN group Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | VPN group (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.edit_vpn_group(id)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->edit_vpn_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_vpn_group(id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->edit_vpn_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VPN group Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| VPN group | [optional]

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

# **find_user_auth_type**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_user_auth_type()



Find user authentication type, whether it is SAML enabled

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_user_auth_type()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->find_user_auth_type: %s\n" % e)
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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_user_groups**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] find_user_groups()



Get all user groups

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_user_groups()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->find_user_groups: %s\n" % e)
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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_user_groups_as_key_value**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] find_user_groups_as_key_value()



Get user groups as key value map

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_user_groups_as_key_value()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->find_user_groups_as_key_value: %s\n" % e)
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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_user_role**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_user_role()



Check whether a user has admin role

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_user_role()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->find_user_role: %s\n" % e)
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

# **find_users**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] find_users()



Get all users

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_users()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->find_users: %s\n" % e)
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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_sessions**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_active_sessions()



Get active sessions

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_active_sessions()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->get_active_sessions: %s\n" % e)
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

# **get_colo_groups**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_colo_groups()



Get COLO groups

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_colo_groups()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->get_colo_groups: %s\n" % e)
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

# **get_vpn_groups**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vpn_groups()



Get VPN groups

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_vpn_groups()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->get_vpn_groups: %s\n" % e)
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

# **remove_sessions**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} remove_sessions()



Remove sessions

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    request_body = [] # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] | User (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.remove_sessions(request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->remove_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**| User | [optional]

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

# **reset_user**
> reset_user()



Unlock a user

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.reset_user(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->reset_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User | [optional]

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

# **resource_group**
> [ResourceGroup] resource_group()



Get all groups

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from openapi_client.model.resource_group import ResourceGroup
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.resource_group()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->resource_group: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ResourceGroup]**](ResourceGroup.md)

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

# **resource_group1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} resource_group1(body)



Global netadmin switches to a different resource group view

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Global netadmin switches to a different resource group view

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.resource_group1(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->resource_group1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Global netadmin switches to a different resource group view |

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

# **resource_group2**
> resource_group2(group_id)



Update a group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from openapi_client.model.resource_group import ResourceGroup
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    group_id = "groupId_example" # str | 
    resource_group = ResourceGroup(
        desc="desc_example",
        device_ips=[
            "device_ips_example",
        ],
        device_ips=[
            "device_ips_example",
        ],
        id={},
        mgmt_sytem_ips_map={
            "key": "key_example",
        },
        name="name_example",
        site_ids=[
            1,
        ],
        uuid_sytem_ips_map={
            "key": "key_example",
        },
    ) # ResourceGroup | Update group description (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.resource_group2(group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->resource_group2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.resource_group2(group_id, resource_group=resource_group)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->resource_group2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |
 **resource_group** | [**ResourceGroup**](ResourceGroup.md)| Update group description | [optional]

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

# **resource_group3**
> resource_group3(group_id)



Delete a group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    group_id = "groupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.resource_group3(group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->resource_group3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |

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

# **resource_group4**
> resource_group4(resource_group)



Create a group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from openapi_client.model.resource_group import ResourceGroup
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    resource_group = ResourceGroup(
        desc="desc_example",
        device_ips=[
            "device_ips_example",
        ],
        device_ips=[
            "device_ips_example",
        ],
        id={},
        mgmt_sytem_ips_map={
            "key": "key_example",
        },
        name="name_example",
        site_ids=[
            1,
        ],
        uuid_sytem_ips_map={
            "key": "key_example",
        },
    ) # ResourceGroup | Create a group

    # example passing only required values which don't have defaults set
    try:
        api_instance.resource_group4(resource_group)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->resource_group4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_group** | [**ResourceGroup**](ResourceGroup.md)| Create a group |

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

# **resource_group_name**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] resource_group_name()



Get the name of the resource group associated with the current logged in user

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.resource_group_name()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->resource_group_name: %s\n" % e)
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

# **update_admin_password**
> update_admin_password()



Update admin default password

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_admin_password(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->update_admin_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User | [optional]

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

# **update_password**
> update_password(user_name)



Update user password

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    user_name = "userName_example" # str | User name
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_password(user_name)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->update_password: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_password(user_name, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->update_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| User name |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User | [optional]

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

# **update_profile_locale**
> update_profile_locale()



Update profile locale

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_profile_locale(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->update_profile_locale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User | [optional]

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

# **update_profile_password**
> update_profile_password()



Update profile password

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_profile_password(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->update_profile_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User | [optional]

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

# **update_user**
> update_user(user_name)



Update user

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    user_name = "userName_example" # str | User name
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_user(user_name)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_user(user_name, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| User name |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User | [optional]

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

# **update_user_group**
> update_user_group(user_group_id)



Update user group

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    user_group_id = "userGroupId_example" # str | User group Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User group (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_user_group(user_group_id)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->update_user_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_user_group(user_group_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->update_user_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| User group Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User group | [optional]

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

# **validate_password**
> validate_password()



Validate user password

### Example


```python
import time
import openapi_client
from openapi_client.api import administration_user_and_group_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = administration_user_and_group_api.AdministrationUserAndGroupApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User password (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.validate_password(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling AdministrationUserAndGroupApi->validate_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User password | [optional]

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

