import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { UserService } from './user.service';
import { Observable } from 'rxjs';
@Injectable()
export class TokenInterceptor implements HttpInterceptor {
  constructor(public auth: UserService) {}
  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    let token = localStorage.getItem("token");
    if (!request.headers.has('Content-Type')) {
      request = request.clone({headers: request.headers.set('Content-Type', 'application/json')});
  }
    if (token) {
      request = request.clone({
        setHeaders: {
          Authorization: `Bearer ${token}`,
        }
      });
      return next.handle(request);
    } else {
      return next.handle(request);
    }
  }
}