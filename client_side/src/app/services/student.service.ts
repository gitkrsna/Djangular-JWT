import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable()
export class StudentService {

  constructor(private http: HttpClient) {
  }

  // Uses http.get() to load data from a single API endpoint
  list() {
    return this.http.get('http://127.0.0.1:8000/api/academic/students');
  }
  createStudent(studentData) {
    return this.http.post('http://127.0.0.1:8000/api/academic/students', studentData);
  }

}