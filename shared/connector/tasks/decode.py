from collections import namedtuple
from enum import IntEnum


class DecodeTask(dict):
    """DecodeTask is used for redis communication from API to DecodeWorker

       The dict-type ensures that the class can be handled by the json
       package without special handling.
    """
    def __init__(self, decode_uuid, acoustic_model_id, training_id, decode_file):
        dict.__init__(self,
                      decode_uuid=decode_uuid,
                      acoustic_model_id=acoustic_model_id,
                      training_id=training_id,
                      decode_file=decode_file)

    @property
    def decode_uuid(self):
        return self['decode_uuid']
    
    @property
    def decode_file(self):
        return self['decode_file']

    @property
    def acoustic_model_id(self):
        return self['acoustic_model_id']

    @property
    def training_id(self):
        return self['training_id']


class DecodeStatusCode(IntEnum):
    IN_PROGRESS = 10
    FAILURE = 100
    SUCCESS = 200


class DecodeStatus(dict):
    """KaldiStatus is used for redis communication from DecodeWorker to API"""

    def __init__(self, id, decode_uuid, transcripts, __queue__='decode'):
        assert __queue__ == 'decode'

        dict.__init__(self, __queue__=__queue__,
                      id=id, decode_uuid=decode_uuid, transcripts=transcripts)

    @property
    def id(self):
        return self['id']

    @property
    def decode_uuid(self):
        return self['decode_uuid']

    @property
    def transcripts(self):
        return self['transcripts']
