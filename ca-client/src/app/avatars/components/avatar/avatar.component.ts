import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-avatar',
  templateUrl: './avatar.component.html',
  styleUrls: ['./avatar.component.css']
})
export class AvatarComponent implements OnInit {

  @Input() piel: any;
  @Input() rostro: any;
  @Input() cabello: any;
  @Input() atuendo: any;
  @Input() lente: any;
  @Input() vellofacial: any;
  @Input() sombrero: any;

  constructor() { }

  ngOnInit(): void {
    console.log(this.piel);
  }

}
