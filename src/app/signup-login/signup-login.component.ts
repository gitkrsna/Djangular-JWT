import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BlogPostService } from '../services/blog_post.service';
import { UserService } from '../services/user.service';
import { throwError } from 'rxjs'; // Angular 6/RxJS 6
import { FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-signup-login',
  templateUrl: './signup-login.component.html',
  styleUrls: ['./signup-login.component.scss'],
})
export class SignupLoginComponent implements OnInit {
  public user: any;
  email = new FormControl('', [Validators.required, Validators.email]);
  hide = true;

  constructor(private userService: UserService) {}

  ngOnInit() {
    this.user = {
      username: '',
      password: '',
    };
  }

  login() {
    this.userService.login({
      username: this.user.username,
      password: this.user.password,
    });
    this.user.username = '';
    this.user.password = '';
  }

  getErrorMessage() {
    if (this.email.hasError('required')) {
      return 'You must enter a value';
    }
    return this.email.hasError('email') ? 'Not a valid email' : '';
  }
}
