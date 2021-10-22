import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from './../../../environments/environment'

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  URL: string = environment.api_url;
  headers: any = { headers: new HttpHeaders({
    'Content-type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"',
    'Access-Control-Allow-Methods': 'GET,POST,OPTIONS,DELETE,PUT',
  }) };


  constructor(private http: HttpClient) { }

  registrarUsuario(form: any) {
    const link = this.URL + 'users/registrar/';
    const body = {
      nombres: form.nombre,
      apellidos: form.apellidos,
      correo: form.correo,
      contrasenha: form.contrasenha
    }
    return this.http.post(link, body, this.headers);
  }
}
