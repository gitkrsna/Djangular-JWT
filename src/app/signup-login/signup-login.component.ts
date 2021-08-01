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
  weakPasswordMessage = ''
  passwordStrength = 0
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
    if (this.email.hasError('email') || this.email.hasError('required')) {
      return
    }  
    if (this.passwordStrength < 40) {
      return;
    } 
    this.userService.login({
      username: this.user.username,
      password: this.user.password,
    });
    this.user.username = '';
    this.user.password = '';
  }

getPasswordErrorMessage() {
  if(this.user.password.length < 6) {
    this.weakPasswordMessage = "Password should has atleast 6 charecters"
  } else  if(this.user.password.length > 12) {
    this.weakPasswordMessage = "Password can't have more than 12 charecters"
  }
  this.passwordStrength = this.checkStrength(this.user.password);
  if (this.passwordStrength < 40) {
    this.weakPasswordMessage = "Week Password";
  } else {
    this.weakPasswordMessage = '';
  }
}

  getErrorMessage() {
    if (this.email.hasError('required')) {
      return 'You must enter a value';
    }
    return this.email.hasError('email') ? 'Not a valid email' : '';
  }

  checkStrength(p) {
    // 1
    let force = 0;
  
    // 2
    const regex = /[$-/:-?{-~!"^_@`\[\]]/g;
    const lowerLetters = /[a-z]+/.test(p);
    const upperLetters = /[A-Z]+/.test(p);
    const numbers = /[0-9]+/.test(p);
    const symbols = regex.test(p);
  
    // 3
    const flags = [lowerLetters, upperLetters, numbers, symbols];
  
    // 4
    let passedMatches = 0;
    for (const flag of flags) {
      passedMatches += flag === true ? 1 : 0;
    }
  
    // 5
    force += 2 * p.length + ((p.length >= 10) ? 1 : 0);
    force += passedMatches * 10;
  
    // 6
    force = (p.length <= 6) ? Math.min(force, 10) : force;
  
    // 7
    force = (passedMatches === 1) ? Math.min(force, 10) : force;
    force = (passedMatches === 2) ? Math.min(force, 20) : force;
    force = (passedMatches === 3) ? Math.min(force, 30) : force;
    force = (passedMatches === 4) ? Math.min(force, 40) : force;
  
    return force;
  }
}
