import { Observable } from 'rxjs';
import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MatSnackBar } from '@angular/material';
import {
  Audio,
  TrainingStatus,
  TrainingService,
  DecodeService,
  DecodeAudio,
  DecodeSession,
  DecodeSessionStatus,
  Project,
  ProjectService,
  AudioStatus}
from 'swagger-client';
import AppConstants from  '../app.component';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-project',
  templateUrl: './project.component.html',
  styleUrls: ['./project.component.less']
})
export class ProjectComponent implements OnInit {

  graphUrl;
  projectUuid: string;
  project$: Observable<Project>;

  decodings: Map<number, Array<DecodeSession>>;
  currentDecodeSessionOfTraining: Map<number, DecodeSession>;

  currentlyPlayingAudio? : {
    audio: Audio,
    data: string
  } = null;
  @ViewChild('audioPlayer') audioPlayer;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private sanitizer:DomSanitizer,
    public trainingService: TrainingService,
    public decodeService: DecodeService,
    public projectService: ProjectService,
    private snackBar: MatSnackBar
    ) {}

  ngOnInit() {
    this.currentDecodeSessionOfTraining = new Map();
    this.decodings = new Map();
    this.decodings.set(0, [
      {
        session_uuid: "",
        status: DecodeSessionStatus.Decoding_InProgress,
        decodings: [
          {
            audio: {
              uuid: "",
              name: "test1.wav",
              status: AudioStatus.AudioPrep_Success
            }
          },
          {
            audio: {
              uuid: "",
              name: "test2.wav",
              status: AudioStatus.AudioPrep_Success
            }
          },
        ]
      },
      {
        session_uuid: "",
        status: DecodeSessionStatus.Decoding_InProgress,
        decodings: [
          {
            audio: {
              uuid: "",
              name: "test3.wav",
              status: AudioStatus.AudioPrep_Success
            }
          },
          {
            audio: {
              uuid: "",
              name: "test4.wav",
              status: AudioStatus.AudioPrep_Success
            }
          },
        ]
      }
    ]);
    this.decodings.set(1, [
      {
        session_uuid: "",
        status: DecodeSessionStatus.Decoding_Success,
        decodings: [
          {
            audio: {
              uuid: "",
              name: "test5.wav",
              status: AudioStatus.AudioPrep_Success
            }
          },
          {
            audio: {
              uuid: "",
              name: "test6.wav",
              status: AudioStatus.AudioPrep_Success
            }
          },
        ]
      }
    ]);

    this.projectUuid = this.route.snapshot.paramMap.get('uuid');
    this.project$ = this.projectService.getProjectByUuid(this.projectUuid);

    this.project$.subscribe(project => {
      if (project.trainings.length) {
        project.trainings.forEach(training => {
          this.decodeService.getAllDecodeSessions(
            this.projectUuid,
            training.version)
            .subscribe(decodeSessions => {
              decodeSessions.forEach(session => {
                //this.decodings[training.version].push(session.decodings);
              })
          });

          this.decodeService.getCurrentDecodeSession(
            this.projectUuid,
            training.version
          ).subscribe(session => {
            if(session != null) {
              this.currentDecodeSessionOfTraining.set(training.version, session);
            }
          })
        });
      }
    });
  }

  audioData() {
    if (!this.currentlyPlayingAudio)
      return null;

    return this.sanitizer.bypassSecurityTrustResourceUrl(this.currentlyPlayingAudio.data);
  }

  triggerAudio(event, audio) {
    event.stopPropagation();

    if (this.isPlaying(audio)) {
      this.currentlyPlayingAudio = null;
    } else {
      this.decodeService.getAudioData(audio.uuid)
        .subscribe(data => {
          const audioData = URL.createObjectURL(data);
          if (this.currentlyPlayingAudio) {
            URL.revokeObjectURL(this.currentlyPlayingAudio.data);
          }

          this.currentlyPlayingAudio = {
            audio: audio,
            data: audioData
          };

          setTimeout(() => this.audioPlayer.nativeElement.play(), 0);
        });
      }
  }

  stopAudio() {
    this.currentlyPlayingAudio = null;
  }

  isPlaying(audio: Audio) {
    return (this.currentlyPlayingAudio && this.currentlyPlayingAudio.audio.uuid == audio.uuid);
  }

  // creates a new training and opens the training page
  createTraining() {
    this.trainingService.createTraining(this.projectUuid)
      .subscribe(training => {
        // opens training dialog
        this.snackBar.open("Erstelle neues Training...", "", AppConstants.snackBarConfig);
        this.router.navigate(['/upload/training/' + this.projectUuid + "/" + training.version]);
      });
  }

  openTraining(trainingVersion:number, trainingStatus:TrainingStatus) {
    if(trainingStatus == TrainingStatus.Training_Success)
    {
      this.snackBar.open("Öffne Trainingsübersicht...", "", AppConstants.snackBarConfig);
      this.router.navigate(['/upload/training/overview/' + this.projectUuid + "/" + trainingVersion]);
    }else if (trainingStatus == TrainingStatus.Training_Failure) {
      this.trainingService.createTraining(this.projectUuid)
      .subscribe(training => {
        // opens training dialog
        this.snackBar.open("Erstelle neues Training...", "", AppConstants.snackBarConfig);
        this.router.navigate(['/upload/training/' + this.projectUuid + "/" + training.version]);
      });
    }else {
      this.snackBar.open("Öffne Training...", "", AppConstants.snackBarConfig);
      this.router.navigate(['/upload/training/' + this.projectUuid + "/" + trainingVersion]);
    }
  }

  wasTrainingSuccessful(trainingStatus:TrainingStatus) {
    return trainingStatus != TrainingStatus.Training_Success;
  }

  downloadTraining(trainingVersion:number) {
    this.snackBar.open("Lade Training herunter...", "", AppConstants.snackBarConfig);
    this.trainingService.downloadModelForTraining(
      this.projectUuid,
      trainingVersion,
    ).subscribe(blob => {
      this.graphUrl = URL.createObjectURL(blob);

      // calls download dialog
      let a = document.createElement('a');
      a.href = this.graphUrl;
      a.download = 'graphs.zip';
      document.body.appendChild(a);
      a.click();
      setTimeout(() => {
        // cleans up download dialog
        URL.revokeObjectURL(this.graphUrl);
        a.parentNode.removeChild(a);
      }, 5000);
    });
  }

  createDecode(trainingVersion:number): void {
    let currentSession = this.currentDecodeSessionOfTraining.get(trainingVersion);

    if(currentSession != null && currentSession.status == DecodeSessionStatus.Decoding_Success) {
      this.snackBar.open("Öffne laufende Spracherkennung...", "", AppConstants.snackBarConfig);
      this.router.navigate(['/upload/decoding/overview/' + this.projectUuid + "/" + trainingVersion + "/" + currentSession.session_uuid]);
    } else {

      this.decodeService.createDecodeSession(
        this.projectUuid,
        trainingVersion
      ).subscribe(session => {
        this.snackBar.open("Erstelle neue Spracherkennung...", "", AppConstants.snackBarConfig);
        this.router.navigate(['/upload/decoding/' + this.projectUuid + "/" + trainingVersion + "/" + session.session_uuid]);
      });
    }
  }

  wasDecodingSessionSuccessful(sessionStatus:DecodeSessionStatus) {
    return sessionStatus != DecodeSessionStatus.Decoding_Success;
  }

  downloadTranscript(data, name:string) {
    let fileName = name.split('.').slice(0, -1).join('.');
    this.snackBar.open("Lade" + fileName + " Transkript herunter...", "", AppConstants.snackBarConfig);

    if(!data) {
      console.error("No data!");
      return;
    }

    let blob = new Blob([data], {type: 'text/plain'});
    let event = document.createEvent('MouseEvent');
    let a = document.createElement('a');

    a.href = URL.createObjectURL(blob);
    a.download = fileName + '.txt';
    a.dataset.downloadurl = ['text/plain', a.download, a.href].join(':');
    event.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    a.dispatchEvent(event);
  }

  copyToClipboard(text) {
    let tempTextArea = document.createElement('textarea');
    tempTextArea.style.position = 'fixed';
    tempTextArea.style.left = '0';
    tempTextArea.style.top = '0';
    tempTextArea.style.opacity = '0';
    tempTextArea.value = text;

    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    tempTextArea.focus();
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);
  }
}
