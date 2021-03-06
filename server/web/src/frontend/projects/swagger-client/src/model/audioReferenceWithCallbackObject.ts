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
import { CallbackObject } from './callbackObject';


export interface AudioReferenceWithCallbackObject { 
    /**
     * UUID of the audio file
     */
    audio_uuid: string;
    callback?: CallbackObject;
}

