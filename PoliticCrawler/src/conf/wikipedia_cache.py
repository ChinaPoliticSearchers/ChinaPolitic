# coding=utf-8
ITEM_PIPELINES = {"framework.data_pipeline.CachePipeline.FilePipeline": 400}
EXTENSIONS = {"framework.extension.SqliteExtension.SqliteExtension": 600}
SCHEDULER = {"framework.scheduler.PeeweeScheduler.Scheduler":400}
SQLITE_DB_NAME = "history.db"
DOWNLOAD_URL_PATH = "/home/friddle/Politics/Temp/"
