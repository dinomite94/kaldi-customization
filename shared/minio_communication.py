import minio
from minio import ResponseError

minio_buckets = dict(
    # all resources/file uploads
    RESOURCE_BUCKET='resources',
    TRAINING_RESOURCE_BUCKET='training-resources',

    DECODING_BUCKET='decodings',

    # acoustic models thfilenameat are trained by users
    ACOUSTIC_MODELS_BUCKET='acoustic-models',

    # projects
    TRAINING_BUCKET='trainings'
    )


def does_bucket_exist(minio_client, bucket_name):
    try:
        minio_client.bucket_exists(bucket_name)
    except ResponseError as err:
        print(err)
        return (False, err)
    print("Requested bucket exists.")
    return (True, "")


def download_from_bucket(minio_client, bucket, filename, target_path):
    try:
        minio_client.fget_object(bucket, filename, target_path)

    except ResponseError as err:
        print(err)
        return (False, err)

    print("Download of /" + bucket + "/" + filename + " was successfull.")
    return (True, "")


def upload_to_bucket(minio_client, bucket, filename, file_path):
    try:
        minio_client.fput_object(bucket, filename, file_path)
    except ResponseError as err:
        print(err)
        return (False, err)

    print("Upload of /" + bucket + "/" + filename + " was successfull.")
    return (True, "")

def copy_object_in_bucket(minio_client, old_bucket, old_file, new_bucket, new_file):
    try:
        minio_client.copy_object(new_bucket,new_file,"/{}/{}".format(old_bucket,old_file))
    except ResponseError as err:
        print(err)
        return (False,err)

    print("Copy of {} was successfull.".format(new_file))
    return (True,"")