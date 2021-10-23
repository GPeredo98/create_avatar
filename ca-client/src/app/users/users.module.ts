import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { AvatarComponent } from './components/avatar/avatar.component';
import { HomeComponent } from './components/home/home.component';



@NgModule({
  declarations: [
    LoginComponent,
    RegisterComponent,
    AvatarComponent,
    HomeComponent
  ],
  exports: [
    AvatarComponent
  ],
  imports: [
    CommonModule,
    FormsModule
  ],
  entryComponents: []
})
export class UsersModule { }
