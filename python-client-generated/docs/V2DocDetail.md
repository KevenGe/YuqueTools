# V2DocDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  文档 ID | [optional] 
**type** | **str** |  文档类型 (Doc:普通文档, Sheet:表格, Thread:话题, Board:图集, Table:数据表) | [optional] 
**slug** | **str** |  路径 | [optional] 
**title** | **str** |  标题 | [optional] 
**description** | **str** |  摘要 | [optional] 
**cover** | **str** |  封面 | [optional] 
**user_id** | **int** |  归属用户/团队 ID | [optional] 
**book_id** | **int** |  归属知识库 ID | [optional] 
**last_editor_id** | **int** |  最后编辑者 ID | [optional] 
**format** | **str** |  内容格式 (markdown:Markdown 格式, lake:语雀 Lake 格式, html:HTML 标准格式, lakesheet:语雀表格) | [optional] 
**body_draft** | **str** |  正文草稿内容 | [optional] 
**body** | **str** |  正文原始内容 | [optional] 
**body_sheet** | **str** |  表格正文内容   语雀表格 (lakesheet) 正文格式示例, JSON 反序列化后的结构: (注意: 所有项的值均为字符串, 公式项为计算后的值, 日期格式: yyyy-mm-dd HH:MM:SS)   &#x60;&#x60;&#x60;json {   \&quot;version\&quot;: \&quot;1.0\&quot;,   \&quot;data\&quot;: [     {       \&quot;name\&quot;: \&quot;Sheet1\&quot;,       \&quot;index\&quot;: 0,       \&quot;rowCount\&quot;: 100,       \&quot;colCount\&quot;: 4,       \&quot;table\&quot;: [         [\&quot;参数名\&quot;, \&quot;类型\&quot;, \&quot;必填\&quot;, \&quot;默认值\&quot;],         [\&quot;name\&quot;, \&quot;string\&quot;, \&quot;1\&quot;, \&quot;\&quot;],         [\&quot;flag\&quot;, \&quot;boolean\&quot;, \&quot;0\&quot;, \&quot;false\&quot;]       ]     },     {       \&quot;name\&quot;: \&quot;Sheet2\&quot;,       \&quot;index\&quot;: 0,       \&quot;rowCount\&quot;: 100,       \&quot;colCount\&quot;: 8,       \&quot;table\&quot;: []     }   ] } &#x60;&#x60;&#x60;   | [optional] 
**body_html** | **str** |  正文 HTML 标准格式内容 | [optional] 
**body_lake** | **str** |  正文语雀 Lake 格式内容 | [optional] 
**public** | **int** |  公开性 (0:私密, 1:公开, 2:企业内公开) | [optional] 
**status** | **str** |  状态 (0:草稿, 1:发布) | [optional] 
**likes_count** | **int** |  点赞数 | [optional] 
**read_count** | **int** |  阅读数   | [optional] 
**hits** | **int** |  阅读数   | [optional] 
**comments_count** | **int** |  评论数 | [optional] 
**word_count** | **int** |  内容字数 | [optional] 
**created_at** | **datetime** |  创建时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**updated_at** | **datetime** |  更新时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**content_updated_at** | **datetime** |  内容更新时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**published_at** | **datetime** |  发布时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**first_published_at** | **datetime** |  首次发布时间 格式: YYYY-MM-DDTHH:mm:ss.sssZ (ISO_8601) | [optional] 
**book** | [**V2Book**](V2Book.md) |  | [optional] 
**user** | [**V2User**](V2User.md) |  | [optional] 
**creator** | [**V2User**](V2User.md) |  | [optional] 
**tags** | [**V2Tag**](V2Tag.md) |  | [optional] 
**latest_version_id** | **int** |  最新已发版本 ID   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

