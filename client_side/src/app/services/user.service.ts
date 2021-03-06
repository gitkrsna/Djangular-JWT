import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable()
export class UserService {
  // http options used for making API calls
  private httpOptions: any;

  // the actual JWT token
  public token: string;
  public getToken = new Observable();
  // the token expiration date
  public token_expires: Date;

  // the username of the logged in user
  public username: string;

  // error messages received from the login attempt
  public errors: any = [];
  refreshTokenVal: any;
  URL_PATH = `http://localhost:8000/api/discussionforum`;
  constructor(private http: HttpClient,
     private _snackBar: MatSnackBar,
    private router: Router) {}

    public register(user) {
      this.http
        .post(`${this.URL_PATH}/student/signup`, JSON.stringify(user))
        .subscribe(
          (data) => {
            this._snackBar.open('Register Successfully', 'Success', {
              duration: 5000,
            });
            this.router.navigate(['/signin']);
          },
          (err) => {
            this._snackBar.open(err.error.error, 'Error', {
              duration: 5000,
            });
            this.errors = err['error'];
          }
        );
    }

  // Uses http.post() to get an auth token from djangorestframework-jwt endpoint
  public login(user) {
    this.http
      .post(`${this.URL_PATH}/student/login/`, JSON.stringify(user))
      .subscribe(
        (data) => {
          if(data['access']) {
              console.log('login success', data);
              this.refreshTokenVal = data['refresh'];
              this.updateData(data['access']);
              this.router.navigate(['home']);
          }
        },
        (err) => {
          this._snackBar.open(err.error.detail, 'Error', {
            duration: 5000,
          });
          this.errors = err['error'];
        }
      );
  }

  /**
   * Refreshes the JWT token, to extend the time the user is logged in
   */
  public refreshToken() {
    this.http
      .post(
        `${this.URL_PATH}/api/refreshtoken/`,
        JSON.stringify({ refresh: this.refreshTokenVal })
      )
      .subscribe(
        (data) => {
          console.log('refresh success', data);
          this.updateData(data['access']);
        },
        (err) => {
          console.error('refresh error', err);
          this.errors = err['error'];
        }
      );
  }

  public logout() {
    this.token = null;
    this.token_expires = null;
    this.username = null;
    this.refreshTokenVal = null;
  }

  private updateData(token) {
    this.token = token;
    localStorage.setItem('token', this.token);
    this.errors = [];

    // decode the token to read the username and expiration timestamp
    const token_parts = this.token.split('.');
    const token_decoded = JSON.parse(window.atob(token_parts[1]));
    this.token_expires = new Date(token_decoded.exp * 1000);
  }
}
