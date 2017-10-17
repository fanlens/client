# swagger_client.SourcesApi

All URIs are relative to *https://localhost/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sources_get**](SourcesApi.md#sources_get) | **GET** /sources/ | Get sources of current user
[**sources_post**](SourcesApi.md#sources_post) | **POST** /sources/ | Create a new Source
[**sources_source_id_delete**](SourcesApi.md#sources_source_id_delete) | **DELETE** /sources/{source_id} | Remove the source, **WARNING!** This will remove all data associated with the source!
[**sources_source_id_get**](SourcesApi.md#sources_source_id_get) | **GET** /sources/{source_id} | Get source
[**sources_source_id_patch**](SourcesApi.md#sources_source_id_patch) | **PATCH** /sources/{source_id} | Update the source.


# **sources_get**
> SourcesList sources_get()

Get sources of current user

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SourcesApi()

try: 
    # Get sources of current user
    api_response = api_instance.sources_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SourcesList**](SourcesList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_post**
> sources_post(source)

Create a new Source

Currently supported types: facebook, twitter, generic

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SourcesApi()
source = swagger_client.Source() # Source | 

try: 
    # Create a new Source
    api_instance.sources_post(source)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | [**Source**](Source.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_source_id_delete**
> Ok sources_source_id_delete(source_id)

Remove the source, **WARNING!** This will remove all data associated with the source!

**WARNING!** This will remove all data associated with the source!

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SourcesApi()
source_id = 56 # int | 

try: 
    # Remove the source, **WARNING!** This will remove all data associated with the source!
    api_response = api_instance.sources_source_id_delete(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_source_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**|  | 

### Return type

[**Ok**](Ok.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_source_id_get**
> Source sources_source_id_get(source_id)

Get source

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SourcesApi()
source_id = 56 # int | 

try: 
    # Get source
    api_response = api_instance.sources_source_id_get(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_source_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**|  | 

### Return type

[**Source**](Source.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_source_id_patch**
> Source sources_source_id_patch(source_id, source)

Update the source.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SourcesApi()
source_id = 56 # int | 
source = swagger_client.Source() # Source | Fields can be a subset of a full source. Will update only the specified fields.

try: 
    # Update the source.
    api_response = api_instance.sources_source_id_patch(source_id, source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->sources_source_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**|  | 
 **source** | [**Source**](Source.md)| Fields can be a subset of a full source. Will update only the specified fields. | 

### Return type

[**Source**](Source.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

