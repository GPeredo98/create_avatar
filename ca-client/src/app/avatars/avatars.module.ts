import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MakerComponent } from './components/maker/maker.component';
import { MyAvatarsComponent } from './components/my-avatars/my-avatars.component';
import { UsersModule } from '../users/users.module';
import { AvatarComponent } from './components/avatar/avatar.component';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    MakerComponent,
    MyAvatarsComponent,
    AvatarComponent
  ],
  exports: [
    AvatarComponent
  ],
  imports: [
    CommonModule,
    FormsModule
  ]
})
export class AvatarsModule { }
