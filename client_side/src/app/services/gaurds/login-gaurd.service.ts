import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class LoginGaurdService {
  constructor(public router: Router) {}
  canActivate(): boolean {
    if (localStorage.getItem('token')) {
      this.router.navigate(['']);
      return false;
    }
    return true;
  }
}
