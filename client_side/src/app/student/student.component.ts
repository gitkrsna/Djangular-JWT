import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { StudentService } from '../services/student.service';
@Component({
  selector: 'app-student',
  templateUrl: './student.component.html',
  styleUrls: ['./student.component.scss']
})
export class StudentComponent implements OnInit {
 
  student = {
    first_name: '',
    last_name: '',
    date_of_birth: '',
    enrollment_date: ''
  }

  studentList : any = [];
  displayedColumns = [];
  constructor(private studentService: StudentService,
              private changeDetectorRef: ChangeDetectorRef
    ) {}

  ngOnInit() {
   this.studentService.list().subscribe(response => {
    this.displayedColumns = ['First Name', 'Last Name', 'Enrollment Date'];
     this.studentList = response;
     console.log(response);
   })
  }
   saveStudentDetails(){
    this.studentService.createStudent(this.student).subscribe(response => {
      this.studentList = response;
      console.log(response);
      this.changeDetectorRef.detectChanges();
    })
   }
}

