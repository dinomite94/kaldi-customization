/**
 * Kaldi Customization Server
 * Kaldi Customization Server.
 *
 * The version of the OpenAPI document: 1.0.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
/* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs';

import { Audio } from '../model/audio';
import { AudioReferenceObject } from '../model/audioReferenceObject';
import { AudioReferenceWithCallbackObject } from '../model/audioReferenceWithCallbackObject';
import { DecodeMessage } from '../model/decodeMessage';
import { DecodeTaskReference } from '../model/decodeTaskReference';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable({
  providedIn: 'root'
})
export class DecodeService {

    protected basePath = 'http://localhost:8080/api/v1';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {

        if (configuration) {
            this.configuration = configuration;
            this.configuration.basePath = configuration.basePath || basePath || this.basePath;

        } else {
            this.configuration.basePath = basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Assign Audio to training
     * Assign audio to to be decoded in a specific training
     * @param project_uuid UUID of the project
     * @param training_version Training version of the project
     * @param audio_reference_object Audio that needs to be decoded
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public assignAudioToTraining(project_uuid: string, training_version: number, audio_reference_object: AudioReferenceObject, observe?: 'body', reportProgress?: boolean): Observable<DecodeTaskReference>;
    public assignAudioToTraining(project_uuid: string, training_version: number, audio_reference_object: AudioReferenceObject, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<DecodeTaskReference>>;
    public assignAudioToTraining(project_uuid: string, training_version: number, audio_reference_object: AudioReferenceObject, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<DecodeTaskReference>>;
    public assignAudioToTraining(project_uuid: string, training_version: number, audio_reference_object: AudioReferenceObject, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (project_uuid === null || project_uuid === undefined) {
            throw new Error('Required parameter project_uuid was null or undefined when calling assignAudioToTraining.');
        }
        if (training_version === null || training_version === undefined) {
            throw new Error('Required parameter training_version was null or undefined when calling assignAudioToTraining.');
        }
        if (audio_reference_object === null || audio_reference_object === undefined) {
            throw new Error('Required parameter audio_reference_object was null or undefined when calling assignAudioToTraining.');
        }

        let headers = this.defaultHeaders;

        // authentication (oauth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        const httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected !== undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.post<DecodeTaskReference>(`${this.configuration.basePath}/project/${encodeURIComponent(String(project_uuid))}/training/${encodeURIComponent(String(training_version))}/decode`,
            audio_reference_object,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Delete audio by UUID
     * Delete a single audio resource
     * @param audio_uuid UUID of audio to delete
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public deleteAudioByUuid(audio_uuid: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public deleteAudioByUuid(audio_uuid: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public deleteAudioByUuid(audio_uuid: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public deleteAudioByUuid(audio_uuid: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (audio_uuid === null || audio_uuid === undefined) {
            throw new Error('Required parameter audio_uuid was null or undefined when calling deleteAudioByUuid.');
        }

        let headers = this.defaultHeaders;

        // authentication (oauth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        const httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.delete<any>(`${this.configuration.basePath}/audio/${encodeURIComponent(String(audio_uuid))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Returns a list of available audio
     * 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getAllAudio(observe?: 'body', reportProgress?: boolean): Observable<Array<Audio>>;
    public getAllAudio(observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Array<Audio>>>;
    public getAllAudio(observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Array<Audio>>>;
    public getAllAudio(observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        let headers = this.defaultHeaders;

        // authentication (oauth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        const httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get<Array<Audio>>(`${this.configuration.basePath}/audio`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Find audio by UUID
     * Returns a single audio resource
     * @param audio_uuid UUID of audio to return
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getAudioByUuid(audio_uuid: string, observe?: 'body', reportProgress?: boolean): Observable<Audio>;
    public getAudioByUuid(audio_uuid: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Audio>>;
    public getAudioByUuid(audio_uuid: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Audio>>;
    public getAudioByUuid(audio_uuid: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (audio_uuid === null || audio_uuid === undefined) {
            throw new Error('Required parameter audio_uuid was null or undefined when calling getAudioByUuid.');
        }

        let headers = this.defaultHeaders;

        // authentication (oauth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        const httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get<Audio>(`${this.configuration.basePath}/audio/${encodeURIComponent(String(audio_uuid))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Returns the audio content
     * Returns the audio content
     * @param audio_uuid UUID of resource to return
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getAudioData(audio_uuid: string, observe?: 'body', reportProgress?: boolean): Observable<Blob>;
    public getAudioData(audio_uuid: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Blob>>;
    public getAudioData(audio_uuid: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Blob>>;
    public getAudioData(audio_uuid: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (audio_uuid === null || audio_uuid === undefined) {
            throw new Error('Required parameter audio_uuid was null or undefined when calling getAudioData.');
        }

        let headers = this.defaultHeaders;

        // authentication (oauth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        const httpHeaderAccepts: string[] = [
            'audio/wav'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get(`${this.configuration.basePath}/audio/${encodeURIComponent(String(audio_uuid))}/data`,
            {
                responseType: "blob",
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Get the result of a decoding task
     * Returns the result of a decoding task
     * @param project_uuid UUID of the project
     * @param training_version Training version of the project
     * @param decode_uuid UUID of the decoding task
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getDecodeResult(project_uuid: string, training_version: number, decode_uuid: string, observe?: 'body', reportProgress?: boolean): Observable<DecodeMessage>;
    public getDecodeResult(project_uuid: string, training_version: number, decode_uuid: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<DecodeMessage>>;
    public getDecodeResult(project_uuid: string, training_version: number, decode_uuid: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<DecodeMessage>>;
    public getDecodeResult(project_uuid: string, training_version: number, decode_uuid: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (project_uuid === null || project_uuid === undefined) {
            throw new Error('Required parameter project_uuid was null or undefined when calling getDecodeResult.');
        }
        if (training_version === null || training_version === undefined) {
            throw new Error('Required parameter training_version was null or undefined when calling getDecodeResult.');
        }
        if (decode_uuid === null || decode_uuid === undefined) {
            throw new Error('Required parameter decode_uuid was null or undefined when calling getDecodeResult.');
        }

        let headers = this.defaultHeaders;

        // authentication (oauth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        const httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get<DecodeMessage>(`${this.configuration.basePath}/project/${encodeURIComponent(String(project_uuid))}/training/${encodeURIComponent(String(training_version))}/decode/${encodeURIComponent(String(decode_uuid))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * List of all decodings
     * Returns a list of all decodings for this training version
     * @param project_uuid UUID of the project
     * @param training_version Training version of the project
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getDecodings(project_uuid: string, training_version: number, observe?: 'body', reportProgress?: boolean): Observable<Array<DecodeMessage>>;
    public getDecodings(project_uuid: string, training_version: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Array<DecodeMessage>>>;
    public getDecodings(project_uuid: string, training_version: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Array<DecodeMessage>>>;
    public getDecodings(project_uuid: string, training_version: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (project_uuid === null || project_uuid === undefined) {
            throw new Error('Required parameter project_uuid was null or undefined when calling getDecodings.');
        }
        if (training_version === null || training_version === undefined) {
            throw new Error('Required parameter training_version was null or undefined when calling getDecodings.');
        }

        let headers = this.defaultHeaders;

        // authentication (oauth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        const httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.get<Array<DecodeMessage>>(`${this.configuration.basePath}/project/${encodeURIComponent(String(project_uuid))}/training/${encodeURIComponent(String(training_version))}/decode`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Decode audio to text
     * Decode audio data to text using the trained project and the given audio
     * @param project_uuid UUID of the project
     * @param training_version Training version of the project
     * @param decode_uuid UUID of the decoding task
     * @param audio_reference_with_callback_object Audio that needs to be decoded
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public startDecode(project_uuid: string, training_version: number, decode_uuid: string, audio_reference_with_callback_object: AudioReferenceWithCallbackObject, observe?: 'body', reportProgress?: boolean): Observable<DecodeTaskReference>;
    public startDecode(project_uuid: string, training_version: number, decode_uuid: string, audio_reference_with_callback_object: AudioReferenceWithCallbackObject, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<DecodeTaskReference>>;
    public startDecode(project_uuid: string, training_version: number, decode_uuid: string, audio_reference_with_callback_object: AudioReferenceWithCallbackObject, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<DecodeTaskReference>>;
    public startDecode(project_uuid: string, training_version: number, decode_uuid: string, audio_reference_with_callback_object: AudioReferenceWithCallbackObject, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (project_uuid === null || project_uuid === undefined) {
            throw new Error('Required parameter project_uuid was null or undefined when calling startDecode.');
        }
        if (training_version === null || training_version === undefined) {
            throw new Error('Required parameter training_version was null or undefined when calling startDecode.');
        }
        if (decode_uuid === null || decode_uuid === undefined) {
            throw new Error('Required parameter decode_uuid was null or undefined when calling startDecode.');
        }
        if (audio_reference_with_callback_object === null || audio_reference_with_callback_object === undefined) {
            throw new Error('Required parameter audio_reference_with_callback_object was null or undefined when calling startDecode.');
        }

        let headers = this.defaultHeaders;

        // authentication (oauth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        const httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected !== undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.put<DecodeTaskReference>(`${this.configuration.basePath}/project/${encodeURIComponent(String(project_uuid))}/training/${encodeURIComponent(String(training_version))}/decode/${encodeURIComponent(String(decode_uuid))}/enqueue`,
            audio_reference_with_callback_object,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Uploads audio
     * 
     * @param upfile File object that needs to be uploaded
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public uploadAudio(upfile: Blob, observe?: 'body', reportProgress?: boolean): Observable<Audio>;
    public uploadAudio(upfile: Blob, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Audio>>;
    public uploadAudio(upfile: Blob, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Audio>>;
    public uploadAudio(upfile: Blob, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (upfile === null || upfile === undefined) {
            throw new Error('Required parameter upfile was null or undefined when calling uploadAudio.');
        }

        let headers = this.defaultHeaders;

        // authentication (oauth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        const httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'multipart/form-data'
        ];

        const canConsumeForm = this.canConsumeForm(consumes);

        let formParams: { append(param: string, value: any): any; };
        let useForm = false;
        let convertFormParamsToString = false;
        // use FormData to transmit files using content-type "multipart/form-data"
        // see https://stackoverflow.com/questions/4007969/application-x-www-form-urlencoded-or-multipart-form-data
        useForm = canConsumeForm;
        if (useForm) {
            formParams = new FormData();
        } else {
            formParams = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        }

        if (upfile !== undefined) {
            formParams = formParams.append('upfile', <any>upfile) as any || formParams;
        }

        return this.httpClient.post<Audio>(`${this.configuration.basePath}/audio`,
            convertFormParamsToString ? formParams.toString() : formParams,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
