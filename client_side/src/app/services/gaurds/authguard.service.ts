import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class AuthguardService implements CanActivate {
  constructor(public router: Router) {}
  canActivate(): boolean {
    if (!sessionStorage.getItem('token')) {
      this.router.navigate(['login']);
      return false;
    }
    return true;
  }
}
