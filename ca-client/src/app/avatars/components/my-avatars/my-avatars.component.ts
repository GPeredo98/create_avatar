import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { AvatarService } from '../../services/avatar.service';

@Component({
  selector: 'app-my-avatars',
  templateUrl: './my-avatars.component.html',
  styleUrls: ['./my-avatars.component.css']
})
export class MyAvatarsComponent implements OnInit {

  pieles: any = [];
  rostros: any = [];
  cabellos: any = [];
  atuendos: any = [];
  lentes: any = [];

  avatar: any = {};
  misAvatares: any = [];
  guardar: boolean = true;

  @ViewChild('closeModal') closeModal: ElementRef | undefined;
  @ViewChild('openModal') openModal: ElementRef | undefined;

  constructor(private avatarService: AvatarService, private toastr: ToastrService) { }

  ngOnInit(): void {
    this.obtenerCaracteristicas();
    this.obtenerMisAvatares();
  }

  obtenerCaracteristicas() {
    this.avatarService.obtenerCaracteristicas().subscribe((res: any) => {
      this.pieles = res.data.pieles;
      this.rostros = res.data.rostros;
      this.cabellos = res.data.cabellos;
      this.lentes = res.data.lentes;
      this.atuendos = res.data.atuendos;
    });
  }

  aplicarItem(item: any) {
    switch (item.tipo) {
      case 1:
        this.avatar.piel = 'http://127.0.0.1:5000/avatars/'+item.imagen;
        break;
      case 2:
        this.avatar.rostro = 'http://127.0.0.1:5000/avatars/'+item.imagen;
        break;
      case 3:
        this.avatar.atuendo = 'http://127.0.0.1:5000/avatars/'+item.imagen;
        break;
      case 4:
        this.avatar.cabello = 'http://127.0.0.1:5000/avatars/'+item.imagen;
        break;
      case 5:
        this.avatar.lente = 'http://127.0.0.1:5000/avatars/'+item.imagen;
        break;
    
      default:
        break;
    }
  }

  guardarAvatar() {
    if(this.guardar) {
      this.avatar.nombre = "Sin nombre";
      let user =  JSON.parse(localStorage.getItem('usuario') || '{}')
      this.avatar.fk_user = user.id;
      this.avatarService.guardarAvatar(this.avatar).subscribe((res: any) => {
        if (this.closeModal) this.closeModal.nativeElement.click();
        this.obtenerMisAvatares();
        this.avatar = {};
        this.toastr.success(res.message, '', {
          timeOut: 3000,
          positionClass: 'toast-bottom-right',
        });
      })
    } else {
      this.avatar.nombre = "Sin nombre";
      let user =  JSON.parse(localStorage.getItem('usuario') || '{}')
      this.avatar.fk_user = user.id;
      this.avatarService.editarAvatar(this.avatar).subscribe((res: any) => {
        if (this.closeModal) this.closeModal.nativeElement.click();
        this.obtenerMisAvatares();
        this.avatar = {};
        this.toastr.success(res.message, '', {
          timeOut: 3000,
          positionClass: 'toast-bottom-right',
        });
      })
    }
  }

  editarAvatar(avatar: any) {
    this.avatar = avatar;
    this.guardar = false;
    if (this.openModal) this.openModal.nativeElement.click();
  }

  copiarAvatar(avatar: any) {
    this.avatar = avatar;
    this.guardar = true;
    if (this.openModal) this.openModal.nativeElement.click();
  }

  eliminarAvatar(id: any) {
    this.avatarService.borrarAvatar(id).subscribe((res: any) => {
      if(res.success) {
        this.obtenerMisAvatares();
        this.toastr.success(res.message, '', {
          timeOut: 3000,
          positionClass: 'toast-bottom-right',
        });
      }
    })
  }

  obtenerMisAvatares() {
    let user =  JSON.parse(localStorage.getItem('usuario') || '{}')
    this.avatarService.obtenerMisAvatares(user.id).subscribe((res: any) => {
      this.misAvatares = res.data;
    })
  }
}
