import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  form: any = {}

  constructor(private authService: AuthService, private router: Router, private toastr: ToastrService) { }

  ngOnInit(): void {
  }

  registrarUsuario() {
    this.authService.registrarUsuario(this.form).subscribe((res: any) => {
      if (res.success) {
        localStorage.setItem('usuario', JSON.stringify(res.data.usuario));
        localStorage.setItem('token', res.data.token);
        this.router.navigateByUrl('/home').then((res: any) => {
          window.location.reload();
        });
      } else {
        this.toastr.warning(res.message, '', {
          timeOut: 3000,
          positionClass: 'toast-bottom-right',
        });
      }
    });
  }

}
