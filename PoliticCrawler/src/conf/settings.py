# coding=utf-8

ITEM_PIPELINES={'framework.data_pipeline.DataManagePipeline.DataManagePipeline': 1}
DOWNLOADER_MIDDLEWARES={'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100}
SCHEDULER_MIDDLEWARES=["scrapy_redis.scheduler.Scheduler"]
REDIS_HOST='localhost'
REDIS_PORT= '6379'
