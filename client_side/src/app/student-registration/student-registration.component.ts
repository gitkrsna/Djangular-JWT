import {ChangeDetectorRef, Component, Inject} from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { StudentService } from '../services/student.service';
import { Router } from '@angular/router';

export interface DialogData {
  animal: string;
  name: string;
}

/**
 * @title Dialog Overview
 */
@Component({
  selector: 'create-student-registration',
  templateUrl: './create-student-registration.html',
  styleUrls: ['./student-registration.component.scss']
})
export class CreateStudentRegistration {

  animal: string;
  name: string;

  constructor(public dialog: MatDialog) {}

  openDialog(): void {
    const dialogRef = this.dialog.open(StudentRegistrationForm, {
      width: '30rem',
      data: {name: this.name, animal: this.animal}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      this.animal = result;
    });
  }

}

// modal form
@Component({
  selector: 'student-registration-modal-form',
  templateUrl: './student-registration.component.html',
  styleUrls: ['./student-registration.component.scss']
})
export class StudentRegistrationForm {

  student = {
    first_name: '',
    last_name: '',
    date_of_birth: '',
    enrollment_date: ''
  }
  studentList : any = [];
  constructor(
    public dialogRef: MatDialogRef<StudentRegistrationForm>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData,
    private studentService: StudentService,
    private changeDetectorRef: ChangeDetectorRef,
    private router: Router) {}

  onCancelClick(): void {
    this.dialogRef.close();
  }

  saveStudentDetails(){
    this.studentService.createStudent(this.student).subscribe(response => {
      this.studentList = response;
      this.dialogRef.close();
      this.router.navigate(['/students']);
    })
   }
}
