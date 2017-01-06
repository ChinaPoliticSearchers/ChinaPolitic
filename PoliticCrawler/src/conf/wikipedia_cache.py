# coding=utf-8
ITEM_PIPELINES = {"framework.data_pipeline.CachePipeline.FilePipeline": 400}
EXTENSIONS = {"framework.extension.SqliteExtension.SqliteExtension": 600}
SCHEDULER_MIDDLEWARES = ["scrapy_redis.scheduler.Scheduler"]
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
DOWNLOAD_URL_PATH = "/home/friddle/Politics/Temp/"
