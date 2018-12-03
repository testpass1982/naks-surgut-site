import json
import urllib.request
from .models import Registry
from django.utils import timezone
from django.shortcuts import get_object_or_404


data_url = 'http://ac.naks.ru/curl/json.php?url=reestr_personal&token=NtdRAUoEtsiwrew73UWyASw0wsYa&type=personal&popov=Y'


class RegistryRecordAdapter:
    """adapter, that converts data to Registry model"""

    def __init__(self, args):
        self.created_date = args['date_created']
        self.title = args['title']
        self.typeof = args['typeof']
        self.params = args['params']
        self.status = args['status']


class RegistryRecordMapper:
    """relation between RegistryRecords objects and database"""
    pass

    def find_by(self, params, record):
        pass

    def check_by_params(self, record):
        try:
            Registry.objects.get(title=record.title)
            print('Found')
            return True
        except Exception as e:
            print('Not found')
            return False

    def find_by_id(self, record):
        return get_object_or_404(Registry, pk=record.pk)

    def insert(self, record):
        try:
            record.save()
        except Exception as e:
            print(e)

    def update(self, id, **params):
        try:
            record = Registry.objects.get(pk=id)
            record.save(params)
        except Exception as e:
            print(e)

    def delete(self, record):
        try:
            rec = Registry.objects.get(pk=record.pk)
            rec.delete()
        except Exception as e:
            print(e)


class Importer:
    """importer, converter to json, and loader to database
        with checking if already loaded"""

    def __init__(self, url):
        self.data = self.get_data_from_url(url)
        self.mapper = RegistryRecordMapper()

    def get_data_from_url(self, url):
        data = urllib.request.urlopen(url)
        read_data = data.read()
        json_data = json.loads(read_data.decode('utf-8'))
        return json_data

    def check_if_already_loaded(self, record):
        pass

    def save_data_to_db(self, record):
        """save every data record to DB through RegistryRecordAdapter"""
        args = {
            'date_created': timezone.now(),
            'title': record['fio']+'-'+record['vid_d']+'-'+record['stamp'],
            'typeof': 'Аттестация персонала',
            'params': record,
            'status': 0
        }
        adapted_record = RegistryRecordAdapter(args)
        print(adapted_record.__dict__)
        record = Registry(**adapted_record.__dict__)
        if self.mapper.check_by_params(record):
            print('Already there', record.title)
        else:
            self.mapper.insert(record)
            print('SAVED NEW RECORD', record.title)


imported = Importer(data_url)
for i in range(10):
    imported.save_data_to_db(imported.data[i])
