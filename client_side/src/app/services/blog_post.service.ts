import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {UserService} from './user.service';

@Injectable()
export class BlogPostService {

  constructor(private http: HttpClient, private _userService: UserService) {
  }

  URL_PATH = `http://127.0.0.1:8000/api/discussionforum/post`
  // Uses http.get() to load data from a single API endpoint
  list() {
    return this.http.get(`${this.URL_PATH}`);
  }
//http://krishnapythonwhere.pythonanywhere.com/
  // send a POST request to the API to create a new data object
  create(post, token) {
    return this.http.post(`${this.URL_PATH}`, JSON.stringify(post), this.getHttpOptions());
  }

  // helper function to build the HTTP headers
  getHttpOptions() {
    return {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + this._userService.token
      })
    };
  }

}