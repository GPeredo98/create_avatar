import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { AvatarComponent } from '../avatars/components/avatar/avatar.component';
import { HomeComponent } from './components/home/home.component';
import { AvatarsModule } from '../avatars/avatars.module';




@NgModule({
  declarations: [
    LoginComponent,
    RegisterComponent,
    HomeComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    AvatarsModule
  ]
})
export class UsersModule { }
