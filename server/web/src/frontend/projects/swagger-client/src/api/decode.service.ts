/**
 * Kaldi Customization Server
 * Kaldi Customization Server.
 *
 * The version of the OpenAPI document: 1.0.1
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

import { DecodeMessage } from '../model/decodeMessage';
import { InlineResponse202 } from '../model/inlineResponse202';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable({
  providedIn: 'root'
})
export class DecodeService {

    protected basePath = '/api/v1';
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
     * Get the result of a decoding task
     * Returns the result of a decoding task
     * @param projectUuid UUID of the project
     * @param trainingVersion Training version of the project
     * @param decodeUuid UUID of the decoding task
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getDecodeResult(projectUuid: string, trainingVersion: number, decodeUuid: string, observe?: 'body', reportProgress?: boolean): Observable<DecodeMessage>;
    public getDecodeResult(projectUuid: string, trainingVersion: number, decodeUuid: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<DecodeMessage>>;
    public getDecodeResult(projectUuid: string, trainingVersion: number, decodeUuid: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<DecodeMessage>>;
    public getDecodeResult(projectUuid: string, trainingVersion: number, decodeUuid: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (projectUuid === null || projectUuid === undefined) {
            throw new Error('Required parameter projectUuid was null or undefined when calling getDecodeResult.');
        }
        if (trainingVersion === null || trainingVersion === undefined) {
            throw new Error('Required parameter trainingVersion was null or undefined when calling getDecodeResult.');
        }
        if (decodeUuid === null || decodeUuid === undefined) {
            throw new Error('Required parameter decodeUuid was null or undefined when calling getDecodeResult.');
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

        return this.httpClient.get<DecodeMessage>(`${this.configuration.basePath}/project/${encodeURIComponent(String(projectUuid))}/training/${encodeURIComponent(String(trainingVersion))}/decode/${encodeURIComponent(String(decodeUuid))}`,
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
     * Decode audio data to text using the trained project
     * @param projectUuid UUID of the project
     * @param trainingVersion Training version of the project
     * @param audioFile Audio file for decoding
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public startDecode(projectUuid: string, trainingVersion: number, audioFile: Blob, observe?: 'body', reportProgress?: boolean): Observable<InlineResponse202>;
    public startDecode(projectUuid: string, trainingVersion: number, audioFile: Blob, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InlineResponse202>>;
    public startDecode(projectUuid: string, trainingVersion: number, audioFile: Blob, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InlineResponse202>>;
    public startDecode(projectUuid: string, trainingVersion: number, audioFile: Blob, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (projectUuid === null || projectUuid === undefined) {
            throw new Error('Required parameter projectUuid was null or undefined when calling startDecode.');
        }
        if (trainingVersion === null || trainingVersion === undefined) {
            throw new Error('Required parameter trainingVersion was null or undefined when calling startDecode.');
        }
        if (audioFile === null || audioFile === undefined) {
            throw new Error('Required parameter audioFile was null or undefined when calling startDecode.');
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

        if (audioFile !== undefined) {
            formParams = formParams.append('audio_file', <any>audioFile) as any || formParams;
        }

        return this.httpClient.post<InlineResponse202>(`${this.configuration.basePath}/project/${encodeURIComponent(String(projectUuid))}/training/${encodeURIComponent(String(trainingVersion))}/decode`,
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