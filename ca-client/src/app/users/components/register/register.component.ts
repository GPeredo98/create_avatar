import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  form: any = {}

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
  }

  registrarUsuario() {
    this.authService.registrarUsuario(this.form).subscribe((res: any) => {
      console.log('res', res);
    });
  }

}
