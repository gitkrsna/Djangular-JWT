import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable()
export class StudentService {

  // URL_PATH = `https://krishnapythonwhere.pythonanywhere.com`;
  URL_PATH = `http://127.0.0.1:8000`;
  constructor(private http: HttpClient) {
  }

  // Uses http.get() to load data from a single API endpoint
  list() {
    return this.http.get(`${this.URL_PATH}/api/academic/students`);
  }
  createStudent(studentData) {
    return this.http.post(`${this.URL_PATH}/api/academic/students`, studentData);
  }

  submitFees(feesData) {
    return this.http.post(`${this.URL_PATH}/api/academic/feessubmit`, feesData);
  }

  listFees() {
    return this.http.get(`${this.URL_PATH}/api/academic/feeslist`);
  }
}