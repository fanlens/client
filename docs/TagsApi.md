# swagger_client.TagsApi

All URIs are relative to *https://localhost/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_get**](TagsApi.md#tags_get) | **GET** /tags/ | Get all tags of current user
[**tags_tag_delete**](TagsApi.md#tags_tag_delete) | **DELETE** /tags/{tag} | Remove tag and all it&#39;s associations from the system
[**tags_tag_get**](TagsApi.md#tags_tag_get) | **GET** /tags/{tag} | Get this tag
[**tags_tag_put**](TagsApi.md#tags_tag_put) | **PUT** /tags/{tag} | Add tag to the system


# **tags_get**
> TagInfo tags_get(with_count=with_count)

Get all tags of current user

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
api_instance = swagger_client.TagsApi()
with_count = false # bool | should the tag counts be included (optional) (default to false)

try: 
    # Get all tags of current user
    api_response = api_instance.tags_get(with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_count** | **bool**| should the tag counts be included | [optional] [default to false]

### Return type

[**TagInfo**](TagInfo.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_delete**
> Ok tags_tag_delete(tag)

Remove tag and all it's associations from the system

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
api_instance = swagger_client.TagsApi()
tag = 'tag_example' # str | 

try: 
    # Remove tag and all it's associations from the system
    api_response = api_instance.tags_tag_delete(tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 

### Return type

[**Ok**](Ok.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_get**
> SingleTagInfo tags_tag_get(tag, with_count=with_count)

Get this tag

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
api_instance = swagger_client.TagsApi()
tag = 'tag_example' # str | 
with_count = false # bool | should the tag count be included (optional) (default to false)

try: 
    # Get this tag
    api_response = api_instance.tags_tag_get(tag, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 
 **with_count** | **bool**| should the tag count be included | [optional] [default to false]

### Return type

[**SingleTagInfo**](SingleTagInfo.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_put**
> SingleTagInfo tags_tag_put(tag)

Add tag to the system

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
api_instance = swagger_client.TagsApi()
tag = 'tag_example' # str | 

try: 
    # Add tag to the system
    api_response = api_instance.tags_tag_put(tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | 

### Return type

[**SingleTagInfo**](SingleTagInfo.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

