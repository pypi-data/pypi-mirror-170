# openapi_client.CertificateManagementDeviceApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decommission_enterprise_csr_for_vedge**](CertificateManagementDeviceApi.md#decommission_enterprise_csr_for_vedge) | **POST** /certificate/revoke/enterprise/certificate | 
[**delete_configuration**](CertificateManagementDeviceApi.md#delete_configuration) | **DELETE** /certificate/{uuid} | 
[**force_sync_root_cert**](CertificateManagementDeviceApi.md#force_sync_root_cert) | **POST** /certificate/forcesync/rootCert | 
[**generate_csr**](CertificateManagementDeviceApi.md#generate_csr) | **POST** /certificate/generate/csr | 
[**generate_edge_device_csr**](CertificateManagementDeviceApi.md#generate_edge_device_csr) | **POST** /certificate/generate/wanedge/csr | 
[**generate_enterprise_csr**](CertificateManagementDeviceApi.md#generate_enterprise_csr) | **POST** /certificate/generate/enterprise/csr/vedge | 
[**get_cert_details**](CertificateManagementDeviceApi.md#get_cert_details) | **POST** /certificate/certdetails | 
[**get_certificate_data**](CertificateManagementDeviceApi.md#get_certificate_data) | **GET** /certificate/record | 
[**get_certificate_detail**](CertificateManagementDeviceApi.md#get_certificate_detail) | **GET** /certificate/stats/detail | 
[**get_certificate_stats**](CertificateManagementDeviceApi.md#get_certificate_stats) | **GET** /certificate/stats/summary | 
[**get_csr_view_right_menus**](CertificateManagementDeviceApi.md#get_csr_view_right_menus) | **GET** /certificate/csr/details | 
[**get_device_view_right_menus**](CertificateManagementDeviceApi.md#get_device_view_right_menus) | **GET** /certificate/device/details | 
[**get_devices_list**](CertificateManagementDeviceApi.md#get_devices_list) | **GET** /certificate/device/list | 
[**get_installed_cert**](CertificateManagementDeviceApi.md#get_installed_cert) | **GET** /certificate/vedge | 
[**get_list_status**](CertificateManagementDeviceApi.md#get_list_status) | **GET** /certificate/list/status | 
[**get_root_cert_chains**](CertificateManagementDeviceApi.md#get_root_cert_chains) | **GET** /certificate/rootcertchains | 
[**get_root_certificate**](CertificateManagementDeviceApi.md#get_root_certificate) | **GET** /certificate/rootcertificate | 
[**get_view**](CertificateManagementDeviceApi.md#get_view) | **GET** /certificate/view | 
[**getc_edge_list**](CertificateManagementDeviceApi.md#getc_edge_list) | **GET** /certificate/tokengeneratedlist | 
[**getv_edge_csr**](CertificateManagementDeviceApi.md#getv_edge_csr) | **GET** /certificate/vedge/csr | 
[**getv_edge_list**](CertificateManagementDeviceApi.md#getv_edge_list) | **GET** /certificate/vedge/list | 
[**getv_smart_list**](CertificateManagementDeviceApi.md#getv_smart_list) | **GET** /certificate/vsmart/list | 
[**install_certificate**](CertificateManagementDeviceApi.md#install_certificate) | **POST** /certificate/install/signedCert | 
[**reset_rsa**](CertificateManagementDeviceApi.md#reset_rsa) | **POST** /certificate/reset/rsa | 
[**save_root_cert_chain**](CertificateManagementDeviceApi.md#save_root_cert_chain) | **PUT** /certificate/rootcertchains | 
[**save_v_edge_list**](CertificateManagementDeviceApi.md#save_v_edge_list) | **POST** /certificate/save/vedge/list | 
[**setv_edge_list**](CertificateManagementDeviceApi.md#setv_edge_list) | **POST** /certificate/vedge/list | 
[**setv_smart_list**](CertificateManagementDeviceApi.md#setv_smart_list) | **POST** /certificate/vsmart/list | 
[**setv_smart_list1**](CertificateManagementDeviceApi.md#setv_smart_list1) | **GET** /certificate/mthub/list | 
[**syncv_bond**](CertificateManagementDeviceApi.md#syncv_bond) | **GET** /certificate/syncvbond | 
[**update_jks**](CertificateManagementDeviceApi.md#update_jks) | **PUT** /certificate/jks | 


# **decommission_enterprise_csr_for_vedge**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} decommission_enterprise_csr_for_vedge()



Revoking enterprise CSR for hardware vEdge<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Revoking CSR for hardware vEdge (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.decommission_enterprise_csr_for_vedge(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->decommission_enterprise_csr_for_vedge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Revoking CSR for hardware vEdge | [optional]

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

# **delete_configuration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_configuration(uuid)



Invalidate device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    uuid = "uuid_example" # str | Device uuid
    replace_controller = False # bool | Replace a vSmart in Multi-tenant setup with a new vSmart (optional) if omitted the server will use the default value of False
    device_id = "deviceId_example" # str | uuid of new vSmart (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_configuration(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->delete_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_configuration(uuid, replace_controller=replace_controller, device_id=device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->delete_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |
 **replace_controller** | **bool**| Replace a vSmart in Multi-tenant setup with a new vSmart | [optional] if omitted the server will use the default value of False
 **device_id** | **str**| uuid of new vSmart | [optional]

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

# **force_sync_root_cert**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} force_sync_root_cert()



Force sync root certificate<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Singed certificate (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.force_sync_root_cert(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->force_sync_root_cert: %s\n" % e)
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

# **generate_csr**
> str generate_csr()



Generate CSR<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSR request for device (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_csr(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->generate_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSR request for device | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_edge_device_csr**
> str generate_edge_device_csr()



Generate CSR<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSR request for device (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_edge_device_csr(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->generate_edge_device_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSR request for device | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_enterprise_csr**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_enterprise_csr()



Generate CSR<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSR request for hardware device (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.generate_enterprise_csr(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->generate_enterprise_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSR request for hardware device | [optional]

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

# **get_cert_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cert_details()



Get cert details

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | parse cert (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cert_details(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_cert_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| parse cert | [optional]

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

# **get_certificate_data**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_certificate_data()



Get certificate chain

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_certificate_data()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_certificate_data: %s\n" % e)
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

# **get_certificate_detail**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_certificate_detail()



Get certificate detail

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_certificate_detail()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_certificate_detail: %s\n" % e)
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

# **get_certificate_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_certificate_stats()



Get certificate expiration status

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_certificate_stats()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_certificate_stats: %s\n" % e)
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

# **get_csr_view_right_menus**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_csr_view_right_menus()



Get CSR detail view

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_csr_view_right_menus()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_csr_view_right_menus: %s\n" % e)
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

# **get_device_view_right_menus**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_view_right_menus()



Get device detail view

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_device_view_right_menus()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_device_view_right_menus: %s\n" % e)
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

# **get_devices_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_devices_list()



Get vEdge list

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_devices_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_devices_list: %s\n" % e)
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

# **get_installed_cert**
> str get_installed_cert(uuid)



Get Installed Certificate<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_installed_cert(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_installed_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

### Return type

**str**

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

# **get_list_status**
> get_list_status()



get certificate

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_list_status()
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_list_status: %s\n" % e)
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

# **get_root_cert_chains**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_root_cert_chains(action)



Get root cert chain

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    action = "get" # str | Action

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_root_cert_chains(action)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_root_cert_chains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Action |

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

# **get_root_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_root_certificate()



Get device root certificate detail view

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_root_certificate()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_root_certificate: %s\n" % e)
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

# **get_view**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_view()



Get certificate UI view

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_view()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->get_view: %s\n" % e)
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

# **getc_edge_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} getc_edge_list()



Get cEdge list with tokengenerated list

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.getc_edge_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->getc_edge_list: %s\n" % e)
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

# **getv_edge_csr**
> str getv_edge_csr(uuid)



Get vEdge CSR Certificate<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.getv_edge_csr(uuid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->getv_edge_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

### Return type

**str**

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

# **getv_edge_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} getv_edge_list()



Get vEdge list

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    model = "vedge-cloud" # str | Device model (optional)
    state = [
        "state_example",
    ] # [str] | Device state (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.getv_edge_list(model=model, state=state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->getv_edge_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Device model | [optional]
 **state** | **[str]**| Device state | [optional]

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

# **getv_smart_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} getv_smart_list()



Get vSmart list<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.getv_smart_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->getv_smart_list: %s\n" % e)
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

# **install_certificate**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} install_certificate()



Install singed certificate<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Singed certificate (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.install_certificate(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->install_certificate: %s\n" % e)
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

# **reset_rsa**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} reset_rsa()



Register CSR<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | CSR request for vEdge (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.reset_rsa(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->reset_rsa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| CSR request for vEdge | [optional]

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

# **save_root_cert_chain**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} save_root_cert_chain()



Save root cert chain<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Save root cert chain (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.save_root_cert_chain(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->save_root_cert_chain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Save root cert chain | [optional]

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

# **save_v_edge_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} save_v_edge_list()



Save vEdge device list

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vEdge device list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.save_v_edge_list(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->save_v_edge_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vEdge device list | [optional]

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

# **setv_edge_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} setv_edge_list()



Save vEdge list

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vEdge device list (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.setv_edge_list(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->setv_edge_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vEdge device list | [optional]

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

# **setv_smart_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} setv_smart_list()



Save vSmart list

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.setv_smart_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->setv_smart_list: %s\n" % e)
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

# **setv_smart_list1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} setv_smart_list1()



Save vSmart list

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.setv_smart_list1()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->setv_smart_list1: %s\n" % e)
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

# **syncv_bond**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} syncv_bond()



sync vManage UUID to all vBond

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.syncv_bond()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->syncv_bond: %s\n" % e)
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

# **update_jks**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_jks()



update JKS<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

### Example


```python
import time
import openapi_client
from openapi_client.api import certificate_management_device_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certificate_management_device_api.CertificateManagementDeviceApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Update JKS (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_jks(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateManagementDeviceApi->update_jks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Update JKS | [optional]

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

