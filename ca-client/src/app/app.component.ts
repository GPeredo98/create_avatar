import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  title = 'ca-client';
  logged: boolean = false;

  constructor(private router: Router) {

  }
  
  ngOnInit(): void {
    this.logged = (localStorage.getItem('token')) ? true : false;
  }

  logout() {
    localStorage.clear();
    this.router.navigateByUrl('/home').then((res: any) => {
      window.location.reload();
    });
  }

}
