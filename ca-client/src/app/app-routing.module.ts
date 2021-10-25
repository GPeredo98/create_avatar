import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MyAvatarsComponent } from './avatars/components/my-avatars/my-avatars.component';
import { HomeComponent } from './users/components/home/home.component';
import { LoginComponent } from './users/components/login/login.component';
import { RegisterComponent } from './users/components/register/register.component';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full'},
  { path: 'home', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'my-avatars', component: MyAvatarsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { initialNavigation: 'enabled' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
