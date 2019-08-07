import connexion
import six

from openapi_server.models.resource import Resource  # noqa: E501
from openapi_server.models.training import Training  # noqa: E501
from openapi_server import util

from redis_communication import create_kaldi_job

from models import db, AcousticModel as DB_AcousticModel, Project as DB_Project, Training as DB_Training, TrainingStateEnum as DB_TrainingStateEnum


def assign_resource_to_training(project_uuid, training_version, resource_uuid):  # noqa: E501
    """Assign a resource to the training

    Assign the specified resource to the training # noqa: E501

    :param project_uuid: UUID of the project
    :type project_uuid: 
    :param training_version: Training version of the project
    :type training_version: int
    :param resource_uuid: UUID of the resource
    :type resource_uuid: 

    :rtype: Resource
    """
    return 'do some magic!'


def create_training(project_uuid):  # noqa: E501
    """Create a new training

     # noqa: E501

    :param project_uuid: Project object that needs to be trained
    :type project_uuid: 

    :rtype: Training
    """
    return 'do some magic!'


def delete_assigned_resource_from_training(project_uuid, training_version, resource_uuid):  # noqa: E501
    """Remove a resource from the training

    Removes the assigned resource from the training # noqa: E501

    :param project_uuid: UUID of the project
    :type project_uuid: 
    :param training_version: Training version of the project
    :type training_version: int
    :param resource_uuid: UUID of the resource
    :type resource_uuid: 

    :rtype: None
    """
    return 'do some magic!'


def get_corpus_of_training_resource(project_uuid, training_version, resource_uuid):  # noqa: E501
    """Get the corpus of the resource

    Returns the corpus of the specified resource for this training # noqa: E501

    :param project_uuid: UUID of the project
    :type project_uuid: 
    :param training_version: Training version of the project
    :type training_version: int
    :param resource_uuid: UUID of the resource
    :type resource_uuid: 

    :rtype: str
    """
    return 'do some magic!'


def get_training_by_version(project_uuid, training_version):  # noqa: E501
    """Find project training results by UUID

    Returns the training object # noqa: E501

    :param project_uuid: UUID of the project
    :type project_uuid: 
    :param training_version: Training version of the project
    :type training_version: int

    :rtype: Training
    """
    return 'do some magic!'


def get_training_resources(project_uuid, training_version):  # noqa: E501
    """Get a list of assigned resources

    Returns a list of all resources assigned to this training # noqa: E501

    :param project_uuid: UUID of the project
    :type project_uuid: 
    :param training_version: Training version of the project
    :type training_version: int

    :rtype: List[Training]
    """
    return 'do some magic!'


def set_corpus_of_training_resource(project_uuid, training_version, resource_uuid, body):  # noqa: E501
    """Set the corpus of the resource

    Updates the corpus of the specified resource for this training # noqa: E501

    :param project_uuid: UUID of the project
    :type project_uuid: 
    :param training_version: Training version of the project
    :type training_version: int
    :param resource_uuid: UUID of the resource
    :type resource_uuid: 
    :param body: New or updated corpus as plain text
    :type body: str

    :rtype: None
    """
    return 'do somid = db.Column(db.Integer, primary_key=True)
    
    project = db.relationship('Project')
    project_id = db.Column(db.Integer,db.ForeignKey("projects.id"))

    version = db.Column(db.Integer)
    
    create_date = db.Column(db.DateTime(timezone=False))
    status = db.Column(db.Enum(TrainingStateEnum))id = db.Column(db.Integer, primary_key=True)
    
    project = db.relationship('Project')
    project_id = db.Column(db.Integer,db.ForeignKey("projects.id"))

    version = db.Column(db.Integer)
    
    create_date = db.Column(db.DateTime(timezone=False))
    status = db.Column(db.Enum(TrainingStateEnum))id = db.Column(db.Integer, primary_key=True)
    
    project = db.relationship('Project')
    project_id = db.Column(db.Integer,db.ForeignKey("projects.id"))

    version = db.Column(db.Integer)
    
    create_date = db.Column(db.DateTime(timezone=False))
    status = db.Column(db.Enum(TrainingStateEnum))e magic!'


def start_training_by_version(project_uuid, training_version):  # noqa: E501
    """Start the specified training

    Start the training process for the specified training # noqa: E501

    :param project_uuid: UUID of the project
    :type project_uuid: 
    :param training_version: Training version of the project
    :type training_version: int

    :rtype: Training
    """
    db_project = DB_Project.query.filter_by(uuid=project_uuid).first()
    db_training = DB_Training.query.filter_by(version=training_version,project=db_project).first()

    if db_training.status != DB_TrainingStateEnum.Trainable:
        return ("training already done or pending",400)

    db_training.status = DB_TrainingStateEnum.Training_Pending

    db.session.add(db_training)
    db.session.commit()

    create_kaldi_job(training_id=db_training.id, acoustic_model_id=db_project.acoustic_model_id)

    #TODO return Training -> missing mapper
    return 'do some magic!'
