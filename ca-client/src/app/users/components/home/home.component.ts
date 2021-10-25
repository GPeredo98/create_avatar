import { Component, OnInit } from '@angular/core';
import { AvatarService } from 'src/app/avatars/services/avatar.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  avatares: any = []

  constructor(private avatarService: AvatarService) { }

  ngOnInit(): void {
    this.obtenerAvatares();
  }

  obtenerAvatares() {
    let user =  JSON.parse(localStorage.getItem('usuario') || '{}')
    this.avatarService.obtenerAvatares().subscribe((res: any) => {
      this.avatares = res.data;
    })
  }

  copiarAvatar(avatar: any) {
    // this.avatar = avatar;
    // this.guardar = true;
    // if (this.openModal) this.openModal.nativeElement.click();
  }

}
