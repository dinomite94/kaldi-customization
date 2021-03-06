/**
 * Kaldi Customization Server
 * Kaldi Customization Server.
 *
 * The version of the OpenAPI document: 1.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { AcousticModelType } from './acousticModelType';
import { Language } from './language';


export interface AcousticModel { 
    name: string;
    language: Language;
    model_type: AcousticModelType;
    uuid: string;
}

