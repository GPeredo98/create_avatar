import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from './../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AvatarService {

  URL: string = environment.api_url;

  constructor(private http: HttpClient) { }

  obtenerCaracteristicas() {
    const link = this.URL + 'avatars/traits_by_types';
    return this.http.get(link);
  }

  guardarAvatar(avatar: any) {
    const link = this.URL + 'avatars/create_avatar';
    return this.http.post(link, avatar);
  }

  editarAvatar(avatar: any) {
    const link = this.URL + 'avatars/edit_avatar';
    return this.http.post(link, avatar);
  }

  borrarAvatar(avatarID: any) {
    const link = this.URL + 'avatars/delete_avatar/' + avatarID;
    return this.http.delete(link)
  }

  obtenerMisAvatares(usuarioID: any) {
    const link = this.URL + 'avatars/my_avatars/' + usuarioID;
    return this.http.get(link);
  }

  obtenerAvatares() {
    const link = this.URL + 'avatars/all_avatars';
    return this.http.get(link);
  }
}
