# openapi_client.ConfigurationDisasterRecoveryApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](ConfigurationDisasterRecoveryApi.md#activate) | **POST** /disasterrecovery/activate | 
[**delete**](ConfigurationDisasterRecoveryApi.md#delete) | **POST** /disasterrecovery/deregister | 
[**delete_dc**](ConfigurationDisasterRecoveryApi.md#delete_dc) | **POST** /disasterrecovery/deleteRemoteDataCenter | 
[**delete_local_dc**](ConfigurationDisasterRecoveryApi.md#delete_local_dc) | **POST** /disasterrecovery/deleteLocalDataCenter | 
[**disaster_recovery_pause_replication**](ConfigurationDisasterRecoveryApi.md#disaster_recovery_pause_replication) | **POST** /disasterrecovery/pausereplication | 
[**disaster_recovery_replication_request**](ConfigurationDisasterRecoveryApi.md#disaster_recovery_replication_request) | **POST** /disasterrecovery/requestimport | 
[**disaster_recovery_un_pause_replication**](ConfigurationDisasterRecoveryApi.md#disaster_recovery_un_pause_replication) | **POST** /disasterrecovery/unpausereplication | 
[**download**](ConfigurationDisasterRecoveryApi.md#download) | **GET** /disasterrecovery/download/backup/{token}/db_bkp.tar.gz | 
[**download_replication_data**](ConfigurationDisasterRecoveryApi.md#download_replication_data) | **GET** /disasterrecovery/download/{token}/{fileName} | 
[**get**](ConfigurationDisasterRecoveryApi.md#get) | **GET** /disasterrecovery/usernames | 
[**get_cluster_info**](ConfigurationDisasterRecoveryApi.md#get_cluster_info) | **GET** /disasterrecovery/clusterInfo | 
[**get_config_db_restore_status**](ConfigurationDisasterRecoveryApi.md#get_config_db_restore_status) | **GET** /disasterrecovery/dbrestorestatus | 
[**get_details**](ConfigurationDisasterRecoveryApi.md#get_details) | **GET** /disasterrecovery/details | 
[**get_disaster_recovery_local_replication_schedule**](ConfigurationDisasterRecoveryApi.md#get_disaster_recovery_local_replication_schedule) | **GET** /disasterrecovery/schedule | 
[**get_disaster_recovery_status**](ConfigurationDisasterRecoveryApi.md#get_disaster_recovery_status) | **GET** /disasterrecovery/drstatus | 
[**get_history**](ConfigurationDisasterRecoveryApi.md#get_history) | **GET** /disasterrecovery/history | 
[**get_local_data_center_state**](ConfigurationDisasterRecoveryApi.md#get_local_data_center_state) | **GET** /disasterrecovery/localdc | 
[**get_local_history**](ConfigurationDisasterRecoveryApi.md#get_local_history) | **GET** /disasterrecovery/localLatestHistory | 
[**get_reachability_info**](ConfigurationDisasterRecoveryApi.md#get_reachability_info) | **POST** /disasterrecovery/validateNodes | 
[**get_remote_data_center_state**](ConfigurationDisasterRecoveryApi.md#get_remote_data_center_state) | **GET** /disasterrecovery/remotedc | 
[**get_remote_data_center_version**](ConfigurationDisasterRecoveryApi.md#get_remote_data_center_version) | **GET** /disasterrecovery/remotedc/swversion | 
[**get_remote_dc_members_state**](ConfigurationDisasterRecoveryApi.md#get_remote_dc_members_state) | **GET** /disasterrecovery/remoteDcState | 
[**getdr_status**](ConfigurationDisasterRecoveryApi.md#getdr_status) | **GET** /disasterrecovery/status | 
[**pause_dr**](ConfigurationDisasterRecoveryApi.md#pause_dr) | **POST** /disasterrecovery/pause | 
[**pause_local_arbitrator**](ConfigurationDisasterRecoveryApi.md#pause_local_arbitrator) | **POST** /disasterrecovery/pauseLocalArbitrator | 
[**pause_local_dc_for_dr**](ConfigurationDisasterRecoveryApi.md#pause_local_dc_for_dr) | **POST** /disasterrecovery/pauseLocalDC | 
[**pause_local_dc_replication**](ConfigurationDisasterRecoveryApi.md#pause_local_dc_replication) | **POST** /disasterrecovery/pauseLocalReplication | 
[**register**](ConfigurationDisasterRecoveryApi.md#register) | **POST** /disasterrecovery/register | 
[**restart_data_center**](ConfigurationDisasterRecoveryApi.md#restart_data_center) | **POST** /disasterrecovery/restartDataCenter | 
[**restore_config_db**](ConfigurationDisasterRecoveryApi.md#restore_config_db) | **POST** /disasterrecovery/dbrestore | 
[**unpause_dr**](ConfigurationDisasterRecoveryApi.md#unpause_dr) | **POST** /disasterrecovery/unpause | 
[**unpause_local_arbitrator**](ConfigurationDisasterRecoveryApi.md#unpause_local_arbitrator) | **POST** /disasterrecovery/unpauseLocalArbitrator | 
[**unpause_local_dc_for_dr**](ConfigurationDisasterRecoveryApi.md#unpause_local_dc_for_dr) | **POST** /disasterrecovery/unpauseLocalDC | 
[**unpause_local_dc_replication**](ConfigurationDisasterRecoveryApi.md#unpause_local_dc_replication) | **POST** /disasterrecovery/unpauseLocalReplication | 
[**update**](ConfigurationDisasterRecoveryApi.md#update) | **POST** /disasterrecovery/password | 
[**update1**](ConfigurationDisasterRecoveryApi.md#update1) | **PUT** /disasterrecovery/register | 
[**update_disaster_recovery_state**](ConfigurationDisasterRecoveryApi.md#update_disaster_recovery_state) | **POST** /disasterrecovery/remotePassword | 
[**update_disaster_recovery_state1**](ConfigurationDisasterRecoveryApi.md#update_disaster_recovery_state1) | **POST** /disasterrecovery/remotedc | 
[**update_dr_state**](ConfigurationDisasterRecoveryApi.md#update_dr_state) | **POST** /disasterrecovery/updateDRConfigOnArbitrator | 
[**update_replication**](ConfigurationDisasterRecoveryApi.md#update_replication) | **POST** /disasterrecovery/updateReplication | 


# **activate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} activate()



Activate cluster to start working as primary

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.activate()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->activate: %s\n" % e)
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

# **delete**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete()



Delete disaster recovery

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->delete: %s\n" % e)
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

# **delete_dc**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_dc()



Delete data center

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_dc()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->delete_dc: %s\n" % e)
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

# **delete_local_dc**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_local_dc()



Delete local data center

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_local_dc()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->delete_local_dc: %s\n" % e)
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

# **disaster_recovery_pause_replication**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} disaster_recovery_pause_replication()



Pause DR data replication

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.disaster_recovery_pause_replication()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->disaster_recovery_pause_replication: %s\n" % e)
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

# **disaster_recovery_replication_request**
> disaster_recovery_replication_request()



Replication Request message sent from primary

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | DR request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.disaster_recovery_replication_request(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->disaster_recovery_replication_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| DR request | [optional]

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

# **disaster_recovery_un_pause_replication**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} disaster_recovery_un_pause_replication()



Un-Pause DR data replication

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.disaster_recovery_un_pause_replication()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->disaster_recovery_un_pause_replication: %s\n" % e)
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

# **download**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} download(token)



Downloading stats file

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    token = "token_example" # str | Token

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.download(token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token |

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

# **download_replication_data**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] download_replication_data(token, file_name)



Download replication data

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    token = "token_example" # str | Token
    file_name = "fileName_example" # str | File name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.download_replication_data(token, file_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->download_replication_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token |
 **file_name** | **str**| File name |

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

# **get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get()



Fetch data centers and vBonds usernames for disaster recovery

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Datacenter/vBond password update request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Datacenter/vBond password update request | [optional]

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

# **get_cluster_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cluster_info()



Get disaster recovery cluster info

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cluster_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_cluster_info: %s\n" % e)
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

# **get_config_db_restore_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_config_db_restore_status()



Config-db restore status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_config_db_restore_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_config_db_restore_status: %s\n" % e)
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

# **get_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_details()



Get disaster recovery details

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_details()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_details: %s\n" % e)
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

# **get_disaster_recovery_local_replication_schedule**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_disaster_recovery_local_replication_schedule()



Get disaster recovery local replication schedule

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_disaster_recovery_local_replication_schedule()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_disaster_recovery_local_replication_schedule: %s\n" % e)
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

# **get_disaster_recovery_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_disaster_recovery_status()



Disaster recovery status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_disaster_recovery_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_disaster_recovery_status: %s\n" % e)
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

# **get_history**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_history()



Get disaster recovery switchover history

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_history()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_history: %s\n" % e)
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

# **get_local_data_center_state**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_local_data_center_state()



Get local data center details

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_local_data_center_state()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_local_data_center_state: %s\n" % e)
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

# **get_local_history**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_local_history()



Get disaster recovery local switchover history

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_local_history()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_local_history: %s\n" % e)
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

# **get_reachability_info**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_reachability_info()



Validate a list of nodes

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    request_body = [] # [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] | Node list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_reachability_info(request_body=request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_reachability_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**| Node list | [optional]

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

# **get_remote_data_center_state**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_remote_data_center_state()



Get remote data center details

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_remote_data_center_state()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_remote_data_center_state: %s\n" % e)
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

# **get_remote_data_center_version**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_remote_data_center_version()



Get remote data center vManage version

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_remote_data_center_version()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_remote_data_center_version: %s\n" % e)
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

# **get_remote_dc_members_state**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_remote_dc_members_state()



Gets remote data center member state

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_remote_dc_members_state()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->get_remote_dc_members_state: %s\n" % e)
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

# **getdr_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} getdr_status()



Get disaster recovery status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.getdr_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->getdr_status: %s\n" % e)
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

# **pause_dr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} pause_dr()



Pause DR

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.pause_dr()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->pause_dr: %s\n" % e)
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

# **pause_local_arbitrator**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} pause_local_arbitrator()



Pause DR for Local Arbitrator

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.pause_local_arbitrator()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->pause_local_arbitrator: %s\n" % e)
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

# **pause_local_dc_for_dr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} pause_local_dc_for_dr()



Pause DR for Local datacenter

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.pause_local_dc_for_dr()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->pause_local_dc_for_dr: %s\n" % e)
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

# **pause_local_dc_replication**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} pause_local_dc_replication()



Pause DR replication for Local datacenter

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.pause_local_dc_replication()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->pause_local_dc_replication: %s\n" % e)
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

# **register**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} register()



Register data centers for disaster recovery

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Datacenter registration request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.register(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->register: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Datacenter registration request | [optional]

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

# **restart_data_center**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} restart_data_center()



Restart data center

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Datacenter registration (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.restart_data_center(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->restart_data_center: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Datacenter registration | [optional]

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

# **restore_config_db**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} restore_config_db()



Signal vManage to initiate configuration-db restore operation

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Config-db meta payload (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.restore_config_db(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->restore_config_db: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Config-db meta payload | [optional]

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

# **unpause_dr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unpause_dr()



Unpause DR

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.unpause_dr()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->unpause_dr: %s\n" % e)
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

# **unpause_local_arbitrator**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unpause_local_arbitrator()



Unpause DR for Local Arbitrator

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.unpause_local_arbitrator()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->unpause_local_arbitrator: %s\n" % e)
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

# **unpause_local_dc_for_dr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unpause_local_dc_for_dr()



Unpause DR for Local datacenter

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.unpause_local_dc_for_dr()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->unpause_local_dc_for_dr: %s\n" % e)
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

# **unpause_local_dc_replication**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unpause_local_dc_replication()



Unpause DR replication for local datacenter

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.unpause_local_dc_replication()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->unpause_local_dc_replication: %s\n" % e)
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

# **update**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update()



Update data centers and vBonds passwords for disaster recovery

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Datacenter/vBond password update request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Datacenter/vBond password update request | [optional]

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

# **update1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update1()



Update data centers for disaster recovery

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Datacenter registration request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update1(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->update1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Datacenter registration request | [optional]

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

# **update_disaster_recovery_state**
> update_disaster_recovery_state()



Update disaster recovery information with updated password to remote data center

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Datacenter registration (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_disaster_recovery_state(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->update_disaster_recovery_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Datacenter registration | [optional]

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

# **update_disaster_recovery_state1**
> update_disaster_recovery_state1()



Update complete disaster recovery information to remote data center

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Datacenter registration (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_disaster_recovery_state1(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->update_disaster_recovery_state1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Datacenter registration | [optional]

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

# **update_dr_state**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_dr_state()



Update arbitrator with primary and secondary states cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.update_dr_state()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->update_dr_state: %s\n" % e)
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

# **update_replication**
> update_replication()



Update DR replication status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_disaster_recovery_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_disaster_recovery_api.ConfigurationDisasterRecoveryApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Replication status (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_replication(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationDisasterRecoveryApi->update_replication: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Replication status | [optional]

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

