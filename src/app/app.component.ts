import {Component, OnInit} from '@angular/core';
import { Router } from '@angular/router';
import {BlogPostService} from './services/blog_post.service';
import {UserService} from './services/user.service';
import {throwError} from 'rxjs';  // Angular 6/RxJS 6

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent  {


}