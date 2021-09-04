import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable()
export class StudentService {

  URL_PATH = `https://krishnapythonwhere.pythonanywhere.com`;
  constructor(private http: HttpClient) {
  }

  // Uses http.get() to load data from a single API endpoint
  list() {
    return this.http.get(`${this.URL_PATH}/api/academic/students`);
  }
  createStudent(studentData) {
    return this.http.post(`${this.URL_PATH}/api/academic/students`, studentData);
  }

}