# job-service

#####Post Body

```	
{
    "coname" : "coname",            // 名字
    "cosize" : "cosize",            // 规模
    "cotype" : "cotype",            // 性质
    "vocation" : "vocation",        // 行业
    "location" : "location",        // 位置
    "description" : "description",  // 描述
    "source" : "source",            // 来源
    "coid" : "coid"                 // 编号
}
```

######上传工作任务结果

```
{
    "id": 1000,		// 任务id
    "ok": 0			// 完成是1，失败是0
}

```

获取一个爬取列表
```
{
	"1" : "xx网",
	"2" : "xxxx"
}
```

上传一个表单
```
{
	"tasks": [
		"a",
		"b",
		"c"
	]
}
```

        