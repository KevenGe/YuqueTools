# V2DocVersionDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  版本 ID | [optional] 
**doc_id** | **int** |  文档 ID | [optional] 
**slug** | **str** |  文档路径 | [optional] 
**title** | **str** |  文档标题 | [optional] 
**user_id** | **int** |  发版人 ID | [optional] 
**format** | **str** |  内容格式 (markdown:Markdown 格式, lake:语雀 Lake 格式, html:HTML 标准格式, lakesheet:语雀表格) | [optional] 
**body** | **str** |  正文原始内容 | [optional] 
**body_html** | **str** |  正文 HTML 标准格式内容 | [optional] 
**body_asl** | **str** |  正文语雀 Lake 格式内容 | [optional] 
**diff** | **str** |  版本 DIFF | [optional] 
**created_at** | **datetime** |  创建时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**updated_at** | **datetime** |  更新时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**user** | [**V2User**](V2User.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

