## 说明

### 应用场景

发现大部分下载视频都是从主页中抓取。这个是从抖音短视频通过搜索得到的视频及其评论的下载，方便特定种类的视频的下载。  

### 使用方法

模拟器安装好证书和xposed框架后，通过手动点击或者录制好的下滑页面的脚本，通过mitm中douyin_search_dump的解析存取url至mongo，最后通过download_video_mongo.py下载视频。  
注意视频下载链接有效时间不超过12个小时。   
mitmdump.exe -s .\douyin_search_dump.py   
python download_video_mongo.py 

### 文件说明

search_item.json是下载到本地的https://aweme.snssdk.com/aweme/v1/search/item/开头的文件的response记录



## 依赖

1. python库 jsonpath,pymongo,icecream,mitmproxy 
2. 夜神模拟器 
3. mongo community

