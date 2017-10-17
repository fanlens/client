# swagger_client.TagsetsApi

All URIs are relative to *https://localhost/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tagsets_get**](TagsetsApi.md#tagsets_get) | **GET** /tagsets/ | Get tagsets of current user
[**tagsets_post**](TagsetsApi.md#tagsets_post) | **POST** /tagsets/ | Create new tagset
[**tagsets_tagset_id_delete**](TagsetsApi.md#tagsets_tagset_id_delete) | **DELETE** /tagsets/{tagset_id} | Remove the tagset
[**tagsets_tagset_id_get**](TagsetsApi.md#tagsets_tagset_id_get) | **GET** /tagsets/{tagset_id} | Get tagset
[**tagsets_tagset_id_patch**](TagsetsApi.md#tagsets_tagset_id_patch) | **PATCH** /tagsets/{tagset_id} | Update the tagset
[**tagsets_tagset_id_tag_delete**](TagsetsApi.md#tagsets_tagset_id_tag_delete) | **DELETE** /tagsets/{tagset_id}/{tag} | Remove tag from tagset
[**tagsets_tagset_id_tag_put**](TagsetsApi.md#tagsets_tagset_id_tag_put) | **PUT** /tagsets/{tagset_id}/{tag} | Add tag to the tagset


# **tagsets_get**
> TagSetList tagsets_get()

Get tagsets of current user

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
api_instance = swagger_client.TagsetsApi()

try: 
    # Get tagsets of current user
    api_response = api_instance.tagsets_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsetsApi->tagsets_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TagSetList**](TagSetList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagsets_post**
> tagsets_post(tagset)

Create new tagset

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
api_instance = swagger_client.TagsetsApi()
tagset = swagger_client.TagSet() # TagSet | 

try: 
    # Create new tagset
    api_instance.tagsets_post(tagset)
except ApiException as e:
    print("Exception when calling TagsetsApi->tagsets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagset** | [**TagSet**](TagSet.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagsets_tagset_id_delete**
> Ok tagsets_tagset_id_delete(tagset_id)

Remove the tagset

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
api_instance = swagger_client.TagsetsApi()
tagset_id = 56 # int | 

try: 
    # Remove the tagset
    api_response = api_instance.tagsets_tagset_id_delete(tagset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsetsApi->tagsets_tagset_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagset_id** | **int**|  | 

### Return type

[**Ok**](Ok.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagsets_tagset_id_get**
> TagSet tagsets_tagset_id_get(tagset_id)

Get tagset

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
api_instance = swagger_client.TagsetsApi()
tagset_id = 56 # int | 

try: 
    # Get tagset
    api_response = api_instance.tagsets_tagset_id_get(tagset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsetsApi->tagsets_tagset_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagset_id** | **int**|  | 

### Return type

[**TagSet**](TagSet.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagsets_tagset_id_patch**
> TagSet tagsets_tagset_id_patch(tagset_id, tagset)

Update the tagset

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
api_instance = swagger_client.TagsetsApi()
tagset_id = 56 # int | 
tagset = swagger_client.TagSet() # TagSet | Can be a subset of the TagSet fields. Only the specified fields will be updated.

try: 
    # Update the tagset
    api_response = api_instance.tagsets_tagset_id_patch(tagset_id, tagset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsetsApi->tagsets_tagset_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagset_id** | **int**|  | 
 **tagset** | [**TagSet**](TagSet.md)| Can be a subset of the TagSet fields. Only the specified fields will be updated. | 

### Return type

[**TagSet**](TagSet.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagsets_tagset_id_tag_delete**
> Ok tagsets_tagset_id_tag_delete(tagset_id, tag)

Remove tag from tagset

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
api_instance = swagger_client.TagsetsApi()
tagset_id = 56 # int | 
tag = 'tag_example' # str | 

try: 
    # Remove tag from tagset
    api_response = api_instance.tagsets_tagset_id_tag_delete(tagset_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsetsApi->tagsets_tagset_id_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagset_id** | **int**|  | 
 **tag** | **str**|  | 

### Return type

[**Ok**](Ok.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagsets_tagset_id_tag_put**
> Ok tagsets_tagset_id_tag_put(tagset_id, tag)

Add tag to the tagset

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
api_instance = swagger_client.TagsetsApi()
tagset_id = 56 # int | 
tag = 'tag_example' # str | 

try: 
    # Add tag to the tagset
    api_response = api_instance.tagsets_tagset_id_tag_put(tagset_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsetsApi->tagsets_tagset_id_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagset_id** | **int**|  | 
 **tag** | **str**|  | 

### Return type

[**Ok**](Ok.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

