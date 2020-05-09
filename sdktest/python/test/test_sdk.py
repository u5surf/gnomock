import gnomock
from gnomock.rest import ApiException

import unittest
import os

class TestSDK(unittest.TestCase):
    def setUp(self):
        with gnomock.ApiClient() as client:
            self.api = gnomock.PresetsApi(client)

    def tearDown(self):
        return super().tearDown()

    def test_mongo(self):
        options = gnomock.Options(tag="3")
        file_name = os.path.abspath("./test/testdata/mongo")
        preset = gnomock.Mongo(data_path=file_name)
        mongo_request = gnomock.MongoRequest(options=options, preset=preset)
        id = ""

        try:
            response = self.api.start_mongo(mongo_request)
            id = response.id
            self.assertEqual("127.0.0.1", response.host)

        finally:
            if id is not "":
                stop_request = gnomock.StopRequest(id=id)
                self.api.stop(stop_request)


    def test_mysql(self):
        options = gnomock.Options(tag="8")
        file_name = os.path.abspath("./test/testdata/mysql/schema.sql")
        preset = gnomock.Mysql(queries_file=file_name)
        mysql_request = gnomock.MysqlRequest(options=options, preset=preset)
        id = ""

        try:
            response = self.api.start_mysql(mysql_request)
            id = response.id
            self.assertEqual("127.0.0.1", response.host)

        finally:
            if id is not "":
                stop_request = gnomock.StopRequest(id=id)
                self.api.stop(stop_request)


    def test_mssql(self):
        options = gnomock.Options(tag="2019-latest")
        file_name = os.path.abspath("./test/testdata/mssql/schema.sql")
        preset = gnomock.Mssql(queries_file=file_name, license=True)
        mssql_request = gnomock.MssqlRequest(options=options, preset=preset)
        id = ""

        try:
            response = self.api.start_mssql(mssql_request)
            id = response.id
            self.assertEqual("127.0.0.1", response.host)

        finally:
            if id is not "":
                stop_request = gnomock.StopRequest(id=id)
                self.api.stop(stop_request)


    def test_postgres(self):
        options = gnomock.Options(tag="12")
        file_name = os.path.abspath("./test/testdata/postgres/schema.sql")
        preset = gnomock.Postgres(queries_file=file_name)
        postgres_request = gnomock.PostgresRequest(options=options, preset=preset)
        id = ""

        try:
            response = self.api.start_postgres(postgres_request)
            id = response.id
            self.assertEqual("127.0.0.1", response.host)

        finally:
            if id is not "":
                stop_request = gnomock.StopRequest(id=id)
                self.api.stop(stop_request)


    def test_redis(self):
        options = gnomock.Options(tag="5")
        preset = gnomock.Redis()
        redis_request = gnomock.RedisRequest(options=options, preset=preset)
        id = ""

        try:
            response = self.api.start_redis(redis_request)
            id = response.id
            self.assertEqual("127.0.0.1", response.host)

        finally:
            if id is not "":
                stop_request = gnomock.StopRequest(id=id)
                self.api.stop(stop_request)


    def test_splunk(self):
        options = gnomock.Options(tag="8.0.2.1")
        file_name = os.path.abspath("./test/testdata/splunk/events.jsonl")
        preset = gnomock.Splunk(values_file=file_name, accept_license=True,
                admin_password="12345678")
        splunk_request = gnomock.SplunkRequest(options=options, preset=preset)
        id = ""

        try:
            response = self.api.start_splunk(splunk_request)
            id = response.id
            self.assertEqual("127.0.0.1", response.host)

        finally:
            if id is not "":
                stop_request = gnomock.StopRequest(id=id)
                self.api.stop(stop_request)


    def test_localstack(self):
        options = gnomock.Options(tag="0.11.0")
        preset = gnomock.Localstack(services=['s3'])
        localstack_request = gnomock.LocalstackRequest(options=options, preset=preset)
        id = ""

        try:
            response = self.api.start_localstack(localstack_request)
            id = response.id
            self.assertEqual("127.0.0.1", response.host)

        finally:
            if id is not "":
                stop_request = gnomock.StopRequest(id=id)
                self.api.stop(stop_request)


if __name__ == "__main__":
    unittest.main()
