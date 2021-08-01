import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

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

  constructor(private http: HttpClient) {}

  // Uses http.post() to get an auth token from djangorestframework-jwt endpoint
  public login(user) {
    this.http
      .post('http://127.0.0.1:8000/api/gettoken/', JSON.stringify(user))
      .subscribe(
        (data) => {
          this.getToken = new Observable((subscriber) => {
            subscriber.next(data['access']);
          });
          console.log('login success', data);
          this.refreshTokenVal = data['refresh'];
          this.updateData(data['access']);
        },
        (err) => {
          console.error('login error', err);
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
        'http://127.0.0.1:8000/api/refreshtoken/',
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
  }

  private updateData(token) {
    this.token = token;
    sessionStorage.setItem('token', this.token);
    this.errors = [];

    // decode the token to read the username and expiration timestamp
    const token_parts = this.token.split('.');
    const token_decoded = JSON.parse(window.atob(token_parts[1]));
    this.token_expires = new Date(token_decoded.exp * 1000);
  }
}
